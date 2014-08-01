from ferris import BasicModel
from google.appengine.ext import ndb


class Playlist(BasicModel):
    Title = ndb.StringProperty(required=True)
	Songs = ndb.StructuredProperty(Song, repeated=True)
    