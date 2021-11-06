import os
from flask import Flask, request, abort, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db
from flask_migrate import Migrate
from models import db, Leopard, Picture
from vision import animal_type
from models import Reservation
import cv2

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app) 
  CORS(app)

  migrate = Migrate(app, db)

  @app.route("/Reserve", methods=["POST"], strict_slashes=False)
  def make_Reservation():
      Reserv = Reservation(
        name=request.json['name'],
        date=request.json['date'],
        location=request.json['location']
        )
      
      db.session.add(Reserv)
      db.session.commit()

      return jsonify({
      'success': True
      })

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

  @app.route('/video', method=['GET'])
  def video():
    return Response(gen_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')


#Here add to this list of IP cameras' url, for later usages
  CamerasURL=[0]

  def gen_frames(url=0):
    cap=cv2.VideoCapture(url)
    while True:
        success,frame=cap.read()
        if not success:
            break
        else:
            ret, buffer=cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cap.release()
    cv2.destroyAllWindows()

  return app


app = create_app()

if __name__ == '__main__':
    app.run()

