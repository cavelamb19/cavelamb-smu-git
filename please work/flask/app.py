from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:' + \
                                        '@localhost:3306/lms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)


class Employee(db.Model):
    __tablename__ = 'employee'

    StaffID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(200))
    Username = db.Column(db.String(50))
    Email = db.Column(db.String(50))
    CurrentDesignation = db.Column(db.String(50))
    Department = db.Column(db.String(50))
    ContactNo = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'employee'
    }

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Learner(Employee):
    __tablename__ = 'learner'

    id= db.Column(db.Integer, db.ForeignKey('employee.StaffID'),primary_key=True)
    CoursesTaking = db.Column(db.String(50))
    CompletedCourses = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'learner'
    }

db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
