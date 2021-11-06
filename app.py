import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db
from flask_migrate import Migrate
from models import db, Leopard, Picture
from vision import animal_type
def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app) 
  CORS(app)

  migrate = Migrate(app, db)

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

  @app.route('/leopard')
  def leopard_detail():
    count = Leopard.query.count()
    animal_t = animal_type()
    return jsonify({
    'success': True,
    'count': count,
    'animal_type': animal_t
    })  


  @app.route('/picture')
  def leopard_picture():
    id = Picture.query.id()
    date= Picture.query.date()
    location= Picture.query.location()
    image= Picture.query.image()
    return jsonify({
    'success': True,
    'count': ""
    })  





  return app

  


app = create_app()

if __name__ == '__main__':
    app.run()

