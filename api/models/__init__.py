""" Module for handling all database models.
Notes:
    The models created with the inherited `Base` constant
    must be imported below the declaration for `Alembic`
    autogenerate to work.
"""
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from broker.models.schema.parents.parents import Parents
from broker.models.schema.children.quotes import QuoteChildren
from broker.models.schema.contacts.contacts import Contacts
from broker.models.schema.renewals.renewals import Renewals
