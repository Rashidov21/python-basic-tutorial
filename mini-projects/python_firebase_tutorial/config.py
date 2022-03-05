import pyrebase

firebase_config = {
    # YOUR API DATA
}
firebase = pyrebase.initialize_app(firebase_config)
# auth = firebase.auth()
db = firebase.database()

# storage = firebase.storage()