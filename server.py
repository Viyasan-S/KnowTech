from flask import Flask, request, jsonify
import pyrebase

app = Flask(__name__)

# Initialize Firebase configuration
firebase_config = {
  "apiKey" : "AIzaSyB3yxLFzmBXCLpmsGNpNH_yAOP6W3D_kw0",
  "authDomain" : "source-code-server.firebaseapp.com",
  "projectId" : "source-code-server",
  "databaseURL" : "https://source-code-server-default-rtdb.asia-southeast1.firebasedatabase.app/",
  "storageBucket" : "source-code-server.appspot.com",
  "messagingSenderId" : "216240307167",
  "appId" : "1:216240307167:web:e5e30125f9a76f235b226a",
  "measurementId" : "G-M84SK9Y6EK"
}


firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

# API endpoint to send a message
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    user = data.get('user')
    message = data.get('message')
    if message:
        db.child("messages").push({"user":user ,"text": message})
        return jsonify({"message": "Message sent successfully"}), 200
    else:
        return jsonify({"message": "Invalid message"}), 400

# API endpoint to fetch messages
@app.route('/get_messages', methods=['GET'])
def get_messages():
    messages = db.child("messages").get().val()
    messages_list = []
    if messages:
        for key, value in messages.items():
            messages_list.append({"text": value['text']})
    return jsonify(messages_list)

if __name__ == '__main__':
    app.run(debug=True)
