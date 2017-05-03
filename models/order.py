from . import MongoModel
from uuid import uuid1
from enum import Enum


class Status(Enum):
    pending = 1
    payed = 2
    delivery = 3
    finish = 4


class Order(MongoModel):
    @classmethod
    def _fields(cls):
        fields = [
            ('orderNo', str, ''),
            ('items', dict, ''),
            ('amount', str, ''),
            ('user_id', int, -1),
            ('comment', str, ''),
            ('status', str, ''),
        ]
        fields.extend(super()._fields())
        return fields

    @classmethod
    def new(cls, form):
        m = super().new(form)
        m.set_uuid('orderNo')
        m.status = 'pending'
        m.save()
        return m

    def payed(self):
        self.status = 'payed'
        self.save()
        return self

    def finish(self):
        self.status = 'finish'
        self.save()
        return self
