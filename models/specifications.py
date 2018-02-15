from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel


class Specifications(EndpointsModel):
    _message_fields_schema = ('id', 'color', 'size', 'frame', 'fork',
                              'headset', 'cranks', 'chain', 'front_hub',
                              'rear_hub', 'spokes', 'rims', 'tires', 'brakes',
                              'pedals', 'handlebar', 'stem', 'seat', 'extras')
    color = ndb.StringProperty()
    size = ndb.StringProperty()
    frame = ndb.StringProperty()
    fork = ndb.StringProperty()
    headset = ndb.StringProperty()
    cranks = ndb.StringProperty()
    chain = ndb.StringProperty()
    front_hub = ndb.StringProperty()
    rear_hub = ndb.StringProperty()
    spokes = ndb.StringProperty()
    rims = ndb.StringProperty()
    tires = ndb.StringProperty()
    brakes = ndb.StringProperty()
    pedals = ndb.StringProperty()
    handlebar = ndb.StringProperty()
    stem = ndb.StringProperty()
    seat = ndb.StringProperty()
    extras = ndb.StringProperty(repeated=True)

    def IdSet(self, value):
        if not isinstance(value, basestring):
            raise TypeError('ID must be a string.')
        self.UpdateFromKey(ndb.Key(Specifications, value))
