import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("./firebase_api/key.json")

default_app = firebase_admin.initialize_app(cred, {
	  'databaseURL': 'https://firechatt-e9ee4-default-rtdb.firebaseio.com',
      'storageBucket' : 'firechatt-e9ee4.appspot.com'
	})

bucket = storage.bucket()

# users_database = {
# 	"1274981264" : {
# 		"username" : "user_1",
# 		"last_activity" : 1619212557
# 		},
# 	"4254785764" : {
# 		"username" : "user_2",
# 		"last_activity" : 1603212638
# 		}
# }

# db.reference("/users_database/").set(users_database)
# users_db = db.reference("/users_database/").get(users_database)
# print(type(users_db))
# print(users_db)

def db_set(table_name,values):
	data = {
		f"{table_name}":values
	}
	db.reference("/users_database/").set(data)
	print("OK")

def db_get(table_name):
	data = db.reference("/users_database/").get(table_name)
	return data