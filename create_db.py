from app import db

db.drop_all()
db.create_all()

from app import URLs

allURLs = URLs.query.all()
print(allURLs)
