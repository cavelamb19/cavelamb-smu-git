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
    
class Trainer(Employee):
    __tablename__ = 'trainer'

    id= db.Column(db.Integer, db.ForeignKey('employee.StaffID'),primary_key=True)
    coursesTeaching = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'trainer'
    }



class Administrator(Employee):
    __tablename__ = 'administrator'

    id= db.Column(db.Integer, db.ForeignKey('employee.StaffID'),primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'administrator'
    }
    
class Course(db.Model):

    __tablename__ = 'course'

    courseID = db.Column(db.Integer, primary_key=True)
    courseName = db.Column(db.String(50))
    courseDesc = db.Column(db.String(50))
    preRequisites = db.Column(db.String(50))
    classesID= db.Column(db.Integer, db.ForeignKey('classes.classesID'))

    def __init__(self, courseID,courseName,courseDesc,preRequisites,classesID):
        self.courseID = courseID
        self.courseName = courseName
        self.courseDesc = courseDesc
        self.preRequisites = preRequisites
        self.classesID = classesID

       

    def json(self):
        return {"courseID": self.courseID, "courseName": self.courseName,
        "courseDesc": self.courseDesc, "preRequisites": self.preRequisites, "classesID": self.classesID}

class Classes(db.Model):

    __tablename__ = 'classes'

    classesID = db.Column(db.Integer, primary_key=True)
    startDate = db.Column(db.DATE)
    startTime = db.Column(db.TIMESTAMP)
    endDate = db.Column(db.DATE)
    endTime= db.Column(db.TIMESTAMP)
    classesSize = db.Column(db.Integer)
    trainerAssigned = db.Column(db.String(50))
    

    def __init__(self, classesID,startDate,startTime,endDate,endTime,classesSize,trainerAssigned):
        self.classesID = classesID
        self.startDate = startDate
        self.startTime = startTime
        self.endDate = endDate
        self.endTime = endTime
        self.classesSize = classesSize
        self.trainerAssigned = trainerAssigned
             

    def json(self):
        return {"classesID": self.classesID, "startDate": self.startDate,
        "startTime": self.startTime, "endDate": self.endDate,
        "endTime": self.endTime,"classesSize": self.classesSize,"trainerAssigned": self.trainerAssigned}


class Lesson(db.Model):

    __tablename__ = 'Lesson'

    lessonID = db.Column(db.Integer, primary_key=True)
    courseMaterial = db.Column(db.String(50))
    quizID = db.Column(db.Integer)
    classesID = db.Column(db.Integer)
    
    

    def __init__(self, lessonID,courseMaterial,quizID,classesID):
        self.lessonID = lessonID
        self.courseMaterial = courseMaterial
        self.quizID = quizID
        self.classesID = classesID
    
             

    def json(self):
        return {"lessonID": self.lessonID, "courseMaterial": self.courseMaterial,
        "quizID": self.quizID, "classesID": self.classesID}

class Quiz(db.Model):

    __tablename__ = 'Quiz'

    quizID = db.Column(db.Integer, primary_key=True)
    qn = db.Column(db.String(50))
    qnID = db.Column(db.Integer)
    ansID = db.Column(db.Integer)
    qnType = db.Column(db.String(50))
    StartTime = db.Column(db.TIMESTAMP)
    EndTime = db.Column(db.TIMESTAMP)
    qnDuration = db.Column(db.TIMESTAMP)
    attemptNo = db.Column(db.Integer)
    quizScore = db.Column(db.Integer)

    
    

    def __init__(self, quizID,qn,qnID,ansID,qnType,StartTime,EndTime,qnDuration,attemptNo,quizScore):
        self.quizID = quizID
        self.qn = qn
        self.qnID = qnID
        self.ansID = ansID
        self.qnType = qnType
        self.StartTime = StartTime
        self.EndTime = EndTime
        self.qnDuration = qnDuration
        self.attemptNo = attemptNo
        self.quizScore = quizScore
    
             

    def json(self):
        return {"quizID": self.quizID, "qn": self.qn,
        "qnID": self.qnID, "ansID": self.ansID, "qnType": self.qnType, "StartTime": self.StartTime,
        "EndTime": self.EndTime, "qnDuration": self.qnDuration, "attemptNo": self.attemptNo, "quizScore": self.quizScore}

#For login
@app.route("/employee/<int:staffid>")
def staffid(staffid):
    employee = Employee.query.filter_by(StaffID=staffid).first()
    if employee:
        return jsonify({
            "code":200,
            "data": employee.to_dict()
        }), 200
    else:
        return jsonify({
            "code" : 404,
            "message": "employee not found."
        }), 404
        
         

#
@app.route("/trainer/<int:trainerid>")
def trainerid(trainerid):
    trainer = Trainer.query.filter_by(id=trainerid).first()
    if trainer:
        return jsonify({
            "data": trainer.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "trainer not found."
        }), 404

#
@app.route("/learner/<int:learnerid>")
def learnerid(learnerid):
    learner = Learner.query.filter_by(id=learnerid).first()
    if learner:
        return jsonify({
            "data": learner.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "learner not found."
        }), 404


if __name__ == '__main__':
    app.run(debug = True)
