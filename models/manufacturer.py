from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel


class Manufacturer(EndpointsModel):
    _message_fields_schema = ('id', 'name', 'description', 'contact')
    name = ndb.StringProperty()
    description = ndb.StringProperty()
    contact = ndb.StringProperty()

    def IdSet(self, value):
        if not isinstance(value, basestring):
            raise TypeError('ID must be a string.')
        self.UpdateFromKey(ndb.Key(Manufacturer, value))
