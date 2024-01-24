from extensions import ma
from models.users import User
from marshmallow.fields import String
from marshmallow import validate


class UserSchema(ma.SQLAlchemyAutoSchema):
    name = String(required=True,validate=[validate.Length(min=3)])
    email = String(required=True,validate=[validate.Email()])
    class Meta:
        model = User
        exclude = ["id"]

    