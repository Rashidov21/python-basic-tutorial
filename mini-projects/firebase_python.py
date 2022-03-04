import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("/path/to/secret/key.json")

default_app = firebase_admin.initialize_app(cred, {
	  'databaseURL': 'https://realtime-db-name',
    'storageBucket' : 'storage-bucket-local-name'
	})

bucket = storage.bucket()