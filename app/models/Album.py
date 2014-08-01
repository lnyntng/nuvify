from ferris import BasicModel
from google.appengine.ext import ndb
from app.models.song import Song


class Album(BasicModel):
    Title = ndb.StringProperty(required=True)
	Songs = ndb.StructuredProperty(Song, repeated=True)
    Artist = ndb.StringProperty(required=True)