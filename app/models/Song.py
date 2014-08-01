from ferris import BasicModel
from google.appengine.ext import ndb
from app.models.tag import Tag

class Song(BasicModel):
    Title = ndb.StringProperty(required=True)
    Tags = ndb.StructuredProperty(Tag, repeated=True)