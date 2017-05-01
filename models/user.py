import hashlib
import os

from enum import Enum
from . import MongoModel
from . import timestamp
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
        ]
        fields.extend(super()._fields())
        return fields

    @classmethod
    def new(cls, form):
        m = super().new(form)
        m.password = m.salted_password(form.get('password', ''))
        m.save()
        return m

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
