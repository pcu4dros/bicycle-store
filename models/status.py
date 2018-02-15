from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel


class Status(EndpointsModel):
    _message_fields_schema = ('id', 'name', 'description')
    name = ndb.StringProperty()
    description = ndb.StringProperty()

    def IdSet(self, value):
        if not isinstance(value, basestring):
            raise TypeError('ID must be a string.')
        self.UpdateFromKey(ndb.Key(Status, value))
