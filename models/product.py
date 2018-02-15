from models.category import Category
from models.manufacturer import Manufacturer
from models.status import Status
from models.specifications import Specifications

from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel


class Product(EndpointsModel):
    _message_fields_schema = ('id', 'model', 'description', 'created_at',
                              'manufacturer', 'category',
                              'status', 'description', 'specifications',
                              'price', 'photo', 'features')
    model = ndb.StringProperty(required=True)
    manufacturer = ndb.StructuredProperty(Manufacturer)
    category = ndb.StructuredProperty(Category)
    status = ndb.StructuredProperty(Status)
    specifications = ndb.StructuredProperty(Specifications)
    description = ndb.StringProperty()
    price = ndb.FloatProperty()
    photo = ndb.StringProperty()
    features = ndb.StringProperty(repeated=True)
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    updated_at = ndb.DateTimeProperty(auto_now_add=True)

    def IdSet(self, value):
        if not isinstance(value, basestring):
            raise TypeError('ID must be a string.')
        self.UpdateFromKey(ndb.Key(Product, value))
