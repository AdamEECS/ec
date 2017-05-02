from . import MongoModel
from . import timestamp
from flask import current_app as app


class Product(MongoModel):
    @classmethod
    def _fields(cls):
        fields = [
            ('name', str, ''),
            ('price', str, ''),
        ]
        fields.extend(super()._fields())
        return fields

    @classmethod
    def valid(cls, form):
        name = form.get('name', '')
        valid_name = cls.find_one(name=name) is None
        msgs = []
        if not valid_name:
            message = '商品已经存在'
            msgs.append(message)

        status = valid_name
        return status, msgs

    def update_pic(self, pic):
        allowed_type = ['jpg', 'jpeg', 'gif', 'png']
        oldname = pic.filename
        if oldname != '' and oldname.split('.')[-1] in allowed_type:
            path = app.config['PRODUCT_PIC_DIR']
            ext = app.config['PRODUCT_PIC_EXT']
            filename = '{}.{}'.format(str(self.id), ext)
            pic.save(path + filename)
