from flask import Flask, request, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms_is212'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)

class Employee(db.Model):
    __tablename__ = 'Employee'

    staffID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50))
    Username = db.Column(db.String(10))
    Email = db.Column(db.String(50))
    CurrentDesignation = db.Column(db.String(50))
    Department = db.Column(db.String(50))
    ContactNo = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'Employee'
    }

    def __init__(self, staffID, Name, Username, Email, CurrentDesignation,Department,ContactNo):
        self.staffID = staffID
        self.Name = Name
        self.Username = Username
        self.Email = Email
        self.CurrentDesignation = CurrentDesignation
        self.Department = Department
        self.ContactNo = ContactNo

    def json(self):
        return {"staffID": self.staffID, "Name": self.Name,
        "Username": self.Username, "Email": self.Email, "CurrentDesignation": self.CurrentDesignation,
        "Department": self.Department, "ContactNo": self.ContactNo}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
