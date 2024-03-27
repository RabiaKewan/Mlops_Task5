from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("database", 27017)
db = client.web_app_db
collection = db.users

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    collection.insert_one({'name': name, 'email': email})
    return 'Data stored successfully!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
