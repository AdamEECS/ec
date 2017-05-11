import hashlib
import base64
from enum import Enum
from . import MongoModel
from . import timestamp
from . import safe_list_get
from . import short_uuid
from decimal import Decimal
from .order import Order
from .product import Product
from .mail import send_verify_email
from .mail import send_password_email
from flask import current_app as app


class Role(Enum):
    root = 1
    admin = 2
    client = 3


bool_dict = {
    'true': True,
    'false': False,
}


class User(MongoModel):
    @classmethod
    def _fields(cls):
        fields = [
            ('username', str, ''),
            ('nickname', str, ''),
            ('email', str, ''),
            ('email_verify', bool, False),
            ('email_token', str, ''),
            ('email_token_exp', int, 0),
            ('password', str, ''),
            ('avatar', str, 'default.png'),
            ('role', str, 'client'),
            ('salt', str, 'q43129dhs*3'),
            ('cart', dict, {}),
            ('add_list', list, []),
            ('add_default', int, 0),
        ]
        fields.extend(super()._fields())
        return fields

    @classmethod
    def new(cls, form):
        m = super().new(form)
        m.password = m.salted_password(form.get('password', ''))
        m.save()
        return m

    def update_user(self, form):
        form = form.to_dict()
        form.pop('role', '')
        password = form.pop('password', '')
        re_password = form.pop('re_password', '')
        email_verify = form.pop('email_verify', 'true')
        form['email_verify'] = bool_dict.get(email_verify, False)
        if(self.email_exist(form.get('email'))):
            form.pop('email')
        self.update(form)
        if len(password) > 0 and password == re_password:
            self.password = self.salted_password(password)
        self.save()
        return self

    def safe_update_user(self, form):
        username = form.get('username', '')
        password = form.get('password', '')
        re_password = form.get('re_password', '')
        if len(username) > 0:
            self.username = username
        if len(password) > 0 and password == re_password:
            self.password = self.salted_password(password)
        self.save()
        return self

    def validate_login(self, form):
        password = form.get('password', '')
        password = self.salted_password(password)
        return password == self.password

    @classmethod
    def valid(cls, form):
        username = form.get('username', '')
        password = form.get('password', '')
        email = form.get('email', '')
        valid_username = cls.find_one(username=username) is None
        valid_email = cls.find_one(email=email) is None
        valid_username_len = len(username) >= 3
        valid_password_len = len(password) >= 3
        # valid_captcha = self.captcha == '3'
        msgs = []
        if not valid_username:
            message = '用户名已经存在'
            msgs.append(message)
        if not valid_username_len:
            message = '用户名长度必须大于等于 3'
            msgs.append(message)
        if not valid_password_len:
            message = '密码长度必须大于等于 3'
            msgs.append(message)
        if not valid_email:
            message = '邮箱已经存在'
            msgs.append(message)
        status = valid_username and valid_username_len and valid_password_len and valid_email
        return status, msgs

    def update_avatar(self, avatar):
        allowed_type = ['jpg', 'jpeg', 'gif', 'png']
        oldname = avatar.filename
        if oldname != '' and oldname.split('.')[-1] in allowed_type:
            path = app.config['USER_AVATARS_DIR']
            filename = '{}_{}.png'.format(str(self.id), timestamp())
            avatar.save(path + filename)
            self.avatar = filename
        else:
            self.avatar = 'default.png'
        self.save()
        return self

    def update_dict(self, **kwargs):
        for k, v in kwargs.items():
            self.__dict__[k] = v
        self.save()
        return self

    def is_admin(self):
        return self.role == 'admin'

    def salted_password(self, password):
        salt = self.salt
        hash1 = hashlib.sha1(password.encode('ascii')).hexdigest()
        hash2 = hashlib.sha1((hash1 + salt).encode('ascii')).hexdigest()
        return hash2

    def get_cart_detail(self):
        cart = self.cart
        ps = []
        try:
            for k, v in cart.items():
                p = Product.find_one(uuid=k)
                p.count = v
                p.sum = '{0:.2f}'.format(Decimal(p.price) * int(p.count))
                print(p.sum)
                ps.append(p)
        except AttributeError:
            self.cart_clear()
        return ps

    def get_cart_count(self):
        cart = self.cart
        return sum([v for k, v in cart.items()])

    def buy(self, kwargs):
        ps = self.get_cart_detail()
        print('obj-ps:', ps)
        amount = str(sum([Decimal(p.sum) for p in ps]))
        add_id = int(kwargs.get('add', 0))
        address = safe_list_get(self.add_list, add_id, '')
        ps = [p.__dict__ for p in ps]
        print('dic-ps:', ps)
        form = dict(
            user_id=self.id,
            user_uuid=self.uuid,
            username=self.username,
            address=address,
            payment=kwargs.get('pay'),
            items=ps,
            amount=amount,
        )
        order = Order.new(form)
        self.cart_clear()
        return order

    def cart_clear(self):
        self.cart = {}
        self.save()
        return self

    def cart_not_empty(self):
        if len(self.cart) > 0:
            return True
        else:
            return False

    def orders(self):
        ms = Order.find(user_id=self.id)
        ms.reverse()
        return ms

    def get_default_add(self):
        return safe_list_get(self.add_list, self.add_default, None)

    def cart_add(self, product_uuid):
        if Product.has(uuid=product_uuid):
            count = self.cart.get(product_uuid, 0)
            count += 1
            self.cart[product_uuid] = count
            self.save()

    def cart_sub(self, product_uuid):
        count = self.cart.get(product_uuid, 0)
        count -= 1
        self.cart[product_uuid] = count
        if count <= 0:
            self.cart.pop(product_uuid)
        self.save()

    def send_email_verify(self, email):
        tb64 = self.set_token(email)
        send_verify_email(email, tb64)

    def set_token(self, email):
        token = '{}-{}'.format(short_uuid(), email)
        self.email_token = token
        self.email_token_exp = timestamp() + 3600
        self.save()
        tb64 = self.encode_email_token(token)
        return tb64

    @staticmethod
    def sha1_email_token(token):
        return hashlib.sha1(token.encode('ascii')).hexdigest()

    def encode_email_token(self, token):
        token_sha1 = self.sha1_email_token(token)
        s = '{}-{}'.format(self.uuid, token_sha1)
        tb64 = base64.b64encode(s.encode('ascii'))
        return tb64

    @classmethod
    def email_verify(cls, tb64):
        s = cls.safe_decode_b64(tb64)
        if s is None:
            return False
        uuid, token_sha1 = s.split('-', 1)
        u = cls.get_uuid(uuid)
        if u.email_token_valid(token_sha1):
            u.email = u.email_token.split('-')[1]
            u.email_verify = True
            u.save()
            u.clear_token()
            return True
        else:
            return False

    def email_token_valid(self, token_sha1):
        now = timestamp()
        if now > self.email_token_exp:
            return False
        return token_sha1 == self.sha1_email_token(self.email_token)

    def email_exist(self, email):
        if self.has(email=email) and self.find_one(email=email).uuid != self.uuid:
            return True
        else:
            return False

    def email_verified(self):
        if len(self.email) <= 0:
            return False
        return self.email_verify

    @classmethod
    def forget_password(cls, form):
        username = form.get('username')
        email = form.get('email')
        u = cls.find_one(username=username)
        if u is not None and u.email_verified() and u.email == email:
            tb64 = u.set_token(email)
            send_password_email(email, tb64)
            return True
        return False

    @classmethod
    def forget_password_verify(cls, tb64):
        s = cls.safe_decode_b64(tb64)
        if s is None:
            return False
        uuid, token_sha1 = s.split('-', 1)
        u = cls.get_uuid(uuid)
        if u.email_token_valid(token_sha1):
            return True
        else:
            return False

    @classmethod
    def get_user_by_tb64(cls, tb64):
        s = cls.safe_decode_b64(tb64)
        if s is None:
            return None
        uuid, token_sha1 = s.split('-', 1)
        u = cls.get_uuid(uuid)
        if u.email_token_valid(token_sha1):
            return u
        else:
            return None

    def reset_password(self, password):
        self.password = self.salted_password(password)
        self.save()
        self.clear_token()
        return self

    def clear_token(self):
        self.email_token = ''
        self.email_token_exp = 0
        self.save()

    @staticmethod
    def safe_decode_b64(tb64):
        try:
            return base64.b64decode(tb64).decode('ascii')
        except:
            return None

