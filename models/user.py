import hashlib
import os

from enum import Enum
from . import MongoModel
from . import timestamp
from . import safe_list_get
from decimal import Decimal
from .order import Order
from .product import Product
from flask import current_app as app


class Role(Enum):
    root = 1
    admin = 2
    client = 3


class User(MongoModel):
    @classmethod
    def _fields(cls):
        fields = [
            ('username', str, ''),
            ('nickname', str, ''),
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
        valid_username = cls.find_one(username=username) is None
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
        status = valid_username and valid_username_len and valid_password_len
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
                p = Product.get(k)
                p.count = v
                p.sum = str(Decimal(p.price) * int(p.count))
                ps.append(p)
        except AttributeError:
            self.cart_clear()
        return ps

    def buy(self, kwargs):
        ps = self.get_cart_detail()
        print('obj-ps:', ps)
        amount = sum([Decimal(p.sum) for p in ps])
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
        self.add = safe_list_get(self.add_list, self.add_default, None)

