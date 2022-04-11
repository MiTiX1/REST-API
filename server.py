from flask import Flask, jsonify, request, Response
from db import MySQLConnection

app = Flask(__name__)

db = MySQLConnection(host="host", user="user", password="password", database="database")

@app.route('/')
def home():
    return '<h1>hi</h1>'

@app.route('/articles', methods=['GET'])
def get_all():
    if request.method == 'GET':
        return jsonify(db.get_all())

@app.route('/articles/<id>', methods=['GET'])
def get_by_id(id):
    if request.method == 'GET':
        return jsonify(db.get_by_id(id))

@app.route('/add-article', methods=['POST'])
def add_article():  
    if request.method == 'POST':
        article = {
            'title': request.form.get('title'),
            'content': request.form.get('content')
        }
        db.add_article(article)
        return Response(status=200)

@app.route('/update-article', methods=['PUT'])
def update_article():
    if request.method == 'PUT':
        article = {
            'id': request.form.get('id'),
            'title': request.form.get('title'),
            'content': request.form.get('content')
        }
        db.update(article)
        return Response(status=200)

@app.route('/delete-article', methods=['DELETE'])
def delete_article():
    if request.method == 'DELETE':
        id = request.form.get('id')
        db.delete(id)
        return Response(status=200)

if __name__ == "__main__":
    app.run()