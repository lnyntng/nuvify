from ferris import BasicModel
from google.appengine.ext import ndb


class Song(BasicModel):
    Title = ndb.StringProperty(required=True)
	Tags = ndb.StructuredProperty(Tag, repeated=True)
    