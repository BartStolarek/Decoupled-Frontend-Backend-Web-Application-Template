from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    first_name = fields.String(required=True, validate=validate.Length(min=1))
    last_name = fields.String(required=True, validate=validate.Length(min=1))
    date_of_birth = fields.Date(required=True)
    height_cm = fields.Float(required=True)
    weight_kg = fields.Float(required=True)
    gender = fields.String(required=True, validate=validate.Length(min=4))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6))
    new_email = fields.Email(required=False)
    
    