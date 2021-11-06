import os
from flask import Flask, request, abort, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db
from flask_migrate import Migrate
from models import db, Leopard, Picture
from vision import animal_type, animal_count
from werkzeug.utils import secure_filename
from datetime import datetime
import base64

now = datetime.now()

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app) 
  CORS(app)

  migrate = Migrate(app, db)

  

  @app.route('/leopard')
  def leopard_detail():
    count = Leopard.query.count()
    animal_info = animal_type()
    count = animal_count()
    return jsonify({
    'success': True,
    'count': count,
    'percentage': animal_info[1]*100,
    'animal_type': animal_info[0],
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

  @app.route('/upload', methods=['POST'])
  def upload():
    picture =request.files['pic']

    if not picture:
        return "no image was uploaded", 400

    
    picture.save(secure_filename(picture.name))
    filename=picture.filename
    mimetype = picture.mimetype
    encodedimage=base64.b64encode(picture.read()) 
    print(encodedimage)
    img = Picture(date=now,location="",Image=encodedimage, mimetype=mimetype, name=filename)

    db.session.add(img)
    db.session.commit()

    return "img has been uploaded", 200

  @app.route('/<int:id>')
  def get_img(id):
    picture = Picture.query.filter_by(id=id).first()
    
    if not picture:
        return 'Img Not Found!', 404

    return Response(picture.Image, mimetype=picture.mimetype)  






  return app


app = create_app()

if __name__ == '__main__':
    app.run()

