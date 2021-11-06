import os
from typing import Text
from flask.json import jsonify
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy


database_path = os.environ.get('DATABASE_URL')
if database_path and database_path.startswith("postgres://"):
    database_path = database_path.replace("postgres://", "postgresql://", 1)

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Leopard(db.Model):
    __tablename__ = 'leopard'

    id = Column(Integer, primary_key=True)
    count = Column(Integer)

    def __init__(self, count):
        self.count = count


    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
        'id': self.id,
        'count': self.count
        }


class Picture(db.Model):
    __tablename__ = 'picture'


    id = Column(Integer, primary_key=True)
    date= Column(String)
    location=Column(String)
    image=Column(String)

 
    def __init__(self, date, location, image):
        self.date = date
        self.location = location
        self.image = image


    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
  

    def format(self):
      return {
          'id': self.id,
          'date': self.date,
          'location': self.location,
          'image': self.image
      }

class Reservation(db.Model):
    __tablename__ = 'Reservation'


    id = Column(Integer, primary_key=True)
    name=Column(String)
    date= Column(String)
    location=Column(String)

 
    def __init__(self, name, date, location):
        self.name= name
        self.date = date
        self.location = location

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
  

    def format(self):
      return {
          'id': self.id,
          'name': self.name,
          'date': self.date,
          'image': self.image
      }