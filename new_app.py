from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask(__name__)

if __name__=='__main__':
    app.run(debug=True)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("postgresql://postgres:password@8003:5432/database1")
db = SQLAlchemy(app)


class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), unique=True, nullable=False)
  content = db.Column(db.String(120), unique=True, nullable=False)

  def __init__(self, title, content):
    self.title = title
    self.content = content
db.create_all()

@app.route('/post/<id>', methods=['GET'])
def get_post(id):
  post = Post.query.get(id)
  del item.__dict__['_sa_instance_state']
  return jsonify(item.__dict__)

@app.route('/posts', methods=['GET'])
def get_posts():
  items = []
  for post in db.session.query(Post).all():
    del Post.__dict__['_sa_instance_state']
    posts.append(Post.__dict__)
  return jsonify(posts)

@app.route('/posts', methods=['POST'])
def create_post():
  body = request.get_json()
  db.session.add(Post(body['title'], body['content']))
  db.session.commit()
  return "Post created", 201

@app.route('/posts/<id>', methods=['PUT'])
def update_Post(id):
  body = request.get_json()
  db.session.query(Post).filter_by(id=id).update(
    dict(Post=body['title'], content=body['content']))
  db.session.commit()
  return "Post updated", 201

@app.route('/posts/<id>', methods=['DELETE'])
def delete_Post(id):
  db.session.query(Post).filter_by(id=id).delete()
  db.session.commit()
  return "Post deleted"



    

