from mongoengine import Document, ObjectIdField, StringField, DateTimeField
from datetime import datetime

class GithubActionShema(Document):
    id = ObjectIdField(primary_key=True)
    request_id = StringField(required=True, unique=True)
    author = StringField(required=True)
    action = StringField(required=True)
    from_branch = StringField(required=True)
    to_branch = StringField(required=True)
    timestamp = DateTimeField(default=datetime.now("utc"))
    