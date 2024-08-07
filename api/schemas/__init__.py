from fastapi.openapi.models import Schema
from pydantic import fields


class Sandwich:
    pass
class Customer:
    pass

class CustomerSchema(Schema):
    id = fields.Integer(dump_only=True)

