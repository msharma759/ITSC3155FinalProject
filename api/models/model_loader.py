from . import orders, order_details, recipes, sandwiches, resources, ingredients, customers

from ..dependencies.database import engine
from ..schemas import reviews, payments, menu, promotions


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    ingredients.Base.metadata.create_all(engine)
    customers.Base.metadata.create_all(engine)
    payments.Base.metadata.create_all(engine)
    menu.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)