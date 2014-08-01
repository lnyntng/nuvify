from ferris import BasicModel
from google.appengine.ext import ndb


class Tag(BasicModel):
    Name = ndb.StringProperty(required=True)
	