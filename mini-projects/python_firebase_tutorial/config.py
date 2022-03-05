import pyrebase

firebase_config = {
    'apiKey': "AIzaSyBfePZU1LMCmrwxFqLYXiQF_n132SdZhC4",
    'authDomain': "fruitsbase.firebaseapp.com",
    'projectId': "fruitsbase",
    'storageBucket': "fruitsbase.appspot.com",
    'messagingSenderId': "445383361070",
    'appId': "1:445383361070:web:4210d09aabe8622619d5bf",
    'measurementId': "G-QCV1XJRVHR",
    # Add this line
    'databaseURL':'https://fruitsbase-default-rtdb.firebaseio.com/'
}
firebase = pyrebase.initialize_app(firebase_config)
# auth = firebase.auth()
db = firebase.database()

# storage = firebase.storage()