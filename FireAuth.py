import pyrebase as pb
config={
    "apiKey": "AIzaSyDdeZS49wcZ2B4dmsQ9Kdl5HUTjmZwthkA",
    "authDomain": "sona-cse.firebaseapp.com",
    "databaseURL": "https://sona-cse.firebaseio.com",
    "projectId": "sona-cse",
    "storageBucket": "sona-cse.appspot.com",
    "messagingSenderId": "800827897149",
    "appId": "1:800827897149:web:319f8e5e358aecd6390154",
    "measurementId": "G-9C4H8EEFYL"
}

firebase=pb.initialize_app(config)
auth=firebase.auth()

try:
    auth.sign_in_with_email_and_password("viruchith.19cse@sonatech.ac.in", "dg3sCV")
    print("Signed in")
except:
    print("Invalid cred")
