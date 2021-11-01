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
    Role = db.Column(db.String(50))

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

    id = db.Column(db.Integer, db.ForeignKey(
        'employee.StaffID'), primary_key=True)
    CoursesAssigned = db.Column(db.String(50))
    CompletedCourses = db.Column(db.String(50))
    CoursesEnrolled = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'learner'
    }


class Trainer(Employee):
    __tablename__ = 'trainer'

    id = db.Column(db.Integer, db.ForeignKey(
        'employee.StaffID'), primary_key=True)
    coursesTeaching = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'trainer'
    }


class Administrator(Employee):
    __tablename__ = 'administrator'

    id = db.Column(db.Integer, db.ForeignKey(
        'employee.StaffID'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'administrator'
    }


class Course(db.Model):

    __tablename__ = 'course'

    courseID = db.Column(db.Integer, primary_key=True)
    courseName = db.Column(db.String(50))
    courseDesc = db.Column(db.String(50))
    preRequisites = db.Column(db.String(50))
    classesID = db.Column(db.Integer, db.ForeignKey('classes.classesID'))

    def __init__(self, courseID, courseName, courseDesc, preRequisites, classesID):
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
    startDate = db.Column(db.String(50))
    startTime = db.Column(db.String(50))
    endDate = db.Column(db.String(50))
    endTime = db.Column(db.String(50))
    classesSize = db.Column(db.Integer)
    trainerAssigned = db.Column(db.String(50))
    currentEnrolled = db.Column(db.Integer)

    def __init__(self, classesID, startDate, startTime, endDate, endTime, classesSize, trainerAssigned, currentEnrolled):
        self.classesID = classesID
        self.startDate = startDate
        self.startTime = startTime
        self.endDate = endDate
        self.endTime = endTime
        self.classesSize = classesSize
        self.trainerAssigned = trainerAssigned
        self.currentEnrolled = currentEnrolled

    def json(self):
        return {"classesID": self.classesID, "startDate": self.startDate,
                "startTime": self.startTime, "endDate": self.endDate,
                "endTime": self.endTime, "classesSize": self.classesSize, "trainerAssigned": self.trainerAssigned, "currentEnrolled": self.currentEnrolled}

    def increaseclasssize(self, num_people, currentEnrolled, classesSize):
        if (currentEnrolled + num_people) < classesSize:
            currentEnrolled = currentEnrolled + num_people
        else:
            raise Exception("Class is full.")


class Lesson(db.Model):

    __tablename__ = 'lesson'

    lessonID = db.Column(db.Integer, primary_key=True)
    courseMaterial = db.Column(db.String(50))
    classesID = db.Column(db.Integer, db.ForeignKey('classes.classesID'))

    def __init__(self, lessonID, courseMaterial, classesID):
        self.lessonID = lessonID
        self.courseMaterial = courseMaterial
        self.classesID = classesID

    def json(self):
        return {"lessonID": self.lessonID, "courseMaterial": self.courseMaterial,
                "classesID": self.classesID}


class Quiz(db.Model):

    __tablename__ = 'quiz'

    quizID = db.Column(db.Integer, primary_key=True)
    quizDuration = db.Column(db.String(50))
    attemptNo = db.Column(db.String(50))
    quizTitle = db.Column(db.String(50))
    quizDesc = db.Column(db.String(50))
    lessonID = db.Column(db.Integer, db.ForeignKey('Lesson.lessonID'))

    def __init__(self, quizID, quizDuration, attemptNo, quizTitle, quizDesc, lessonID):
        self.quizID = quizID
        self.quizDuration = quizDuration
        self.attemptNo = attemptNo
        self.quizTitle = quizTitle
        self.quizDesc = quizDesc
        self.lessonID = lessonID

    def json(self):
        return {"quizID": self.quizID, "quizDuration": self.quizDuration,
                "attemptNo": self.attemptNo, "quizTitle": self.quizTitle, "quizDesc": self.quizDesc,
                "lessonID": self.lessonID}


class Quizscore(db.Model):

    __tablename__ = 'quizscore'

    qsID = db.Column(db.Integer, primary_key=True)
    quizscore = db.Column(db.Integer)
    quizID = db.Column(db.Integer)
    learnerID = db.Column(db.Integer)

    def __init__(self, qsID, quizscore, quizID, learnerID):
        self.qsID = qsID
        self.quizscore = quizscore
        self.quizID = quizID
        self.learnerID = learnerID

    def json(self):
        return {"qsID": self.qsID, "quizscore": self.quizscore,
                "quizID": self.quizID, "learnerID": self.learnerID}


class QuestionTrueFalse(db.Model):

    __tablename__ = 'questiontruefalse'

    qnID = db.Column(db.Integer, primary_key=True)
    qn = db.Column(db.String(10000))
    ans = db.Column(db.String(10000))
    quizID = db.Column(db.Integer, db.ForeignKey('Quiz.quizID'))

    def __init__(self, qnID, qn, ans, quizID):
        self.qnID = qnID
        self.qn = qn
        self.ans = ans
        self.quizID = quizID

    def json(self):
        return {"qnID": self.qnID, "qn": self.qn,
                "ans": self.ans, "quizID": self.quizID}


db.create_all()

###########################################################

# For Employee


@app.route("/employee/")
def getallemployee():

    employeelist = Employee.query.all()
    if len(employeelist):
        return jsonify({
            "code": 200,
            "data": {
                "course": [employee.to_dict() for employee in employeelist]
            }
        }), 200

    else:
        return jsonify({
            "message": "All courses not found."
        }), 404


@app.route("/employee/<int:staffid>")
def staffid(staffid):
    employee = Employee.query.filter_by(StaffID=staffid).first()
    if employee:
        return jsonify({
            "code": 200,
            "data": employee.to_dict()
        }), 200
    else:
        return jsonify({
            "code": 404,
            "message": "employee not found."
        }), 404


###########################################################

# trainer
@app.route("/trainer/<int:trainerid>")
def trainerid(trainerid):
    trainer = Trainer.query.filter_by(id=trainerid).first()
    if trainer:
        return jsonify({
            "code": 200,
            "data": trainer.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "trainer not found."
        }), 404


###########################################################

# Learner
@app.route("/learner/")
def getalllearner():

    learnerlist = Learner.query.all()
    if len(learnerlist):
        return jsonify({
            "code": 200,
            "data": {
                "course": [learner.to_dict() for learner in learnerlist]
            }
        }), 200

    else:
        return jsonify({
            "message": "All courses not found."
        }), 404


@app.route("/learner/<int:learnerid>")
def learnerid(learnerid):
    learner = Learner.query.filter_by(id=learnerid).first()
    if learner:
        return jsonify({
            "code": 200,
            "data": learner.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "learner not found."
        }), 404


###########################################################

# course
@app.route("/course/")
def getallCourse():

    courselist = Course.query.all()
    if len(courselist):
        return jsonify({
            "code": 200,
            "data": {
                "course": [course.json() for course in courselist]
            }
        }), 200

    else:
        return jsonify({
            "message": "All courses not found."
        }), 404


@app.route("/course/classesID/<int:classesID>")
def find_course_by_classesid(classesID):

    course = Course.query.filter_by(classesID=classesID).first()
    if course:
        return jsonify(
            {
                "code": 200,
                "data": course.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "No Course found."
        }
    ), 404


@app.route("/course/courseName/<string:courseName>")
def find_course(courseName):
    courselist = Course.query.filter(
        Course.courseName.like('%' + courseName + '%')).first()

    if courselist:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "course": courselist.json()
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "No Courses found."
        }
    ), 404


###########################################################

# class

@app.route("/classes/<int:classesID>")
def classes(classesID):

    classes = Classes.query.filter_by(classesID=classesID).first()
    if classes:
        return jsonify({
            "code": 200,
            "data": classes.json()


        }), 200

    else:
        return jsonify({
            "message": "class not found."
        }), 404

###########################################################

# lesson


@app.route("/lesson/classesID/<int:classesID>")
def lesson(classesID):

    lessonlist = Lesson.query.filter_by(classesID=classesID).all()
    if lessonlist:
        return jsonify({
            "code": 200,
            "data": [lesson.json() for lesson in lessonlist]


        }), 200

    else:
        return jsonify({
            "message": "class not found."
        }), 404


###########################################################

# quiz


# 29102021 added Post quiz info to Quiz table
@app.route("/addquizInfo", methods=['POST'])
def quiz_info():

    quizInfo = request.get_json()

    # print(enrollcourse)
    if not all(key in quizInfo.keys() for
               key in ('lessonID', 'title', 'time', 'instruction', 'attempt')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    lessonid = quizInfo['lessonID']
    title = quizInfo['title']
    time = quizInfo['time']
    instruction = quizInfo['instruction']
    attempt = quizInfo['attempt']

    quiz = Quiz(quizID=lessonid, quizDuration=time, attemptNo=attempt,
                quizTitle=title, quizDesc=instruction, lessonID=lessonid)

    try:
        db.session.add(quiz)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": quiz.json()
            }
        ), 200

    except Exception as e:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500


# find quiz by lessonid
@app.route("/quiz/lessonID/<int:lessonID>")
def get_quiz_by_lessonid(lessonID):

    quiz = Quiz.query.filter_by(lessonID=lessonID).first()
    if quiz:
        return jsonify({
            "code": 200,
            "data": quiz.json()


        }), 200

    else:
        return jsonify({
            "message": "quiz not found."
        }), 404

# find quiz


@app.route("/quiz/<int:quizID>")
def get_quiz(quizID):

    quiz = Quiz.query.filter_by(quizID=quizID).first()
    if quiz:
        return jsonify({
            "code": 200,
            "data": quiz.json()


        }), 200

    else:
        return jsonify({
            "message": "quiz not found."
        }), 404


###########################################################

# Question

# 29102021 Post Question truefalse to question table
@app.route("/addquestiontruefalse", methods=['POST'])
def add_question():

    questionlist = request.get_json()

    # print(enrollcourse)
    if not all(key in questionlist.keys() for
               key in ('question', 'answer',  'lessonID')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # print(questionlist)

    questiondetails = questionlist['question']
    answer = questionlist['answer']
    lessonid = questionlist['lessonID']

    question = QuestionTrueFalse(
        qnID=None, qn=questiondetails, ans=answer, quizID=lessonid)

    try:
        db.session.add(question)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": question.json()
            }
        ), 200

    except Exception as e:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500


# Find question for true false
@app.route("/questiontruefalse/quizID/<int:quizID>")
def get_question_by_quizID(quizID):

    questionlist = QuestionTrueFalse.query.filter_by(quizID=quizID).all()
    if questionlist:
        return jsonify({
            "code": 200,
            "data": [question.json() for question in questionlist]


        }), 200

    else:
        return jsonify({
            "message": "quiz not found."
        }), 404


###########################################################

# quizscore

# get quiz score for learner
@app.route("/viewscore/<int:learnerID>")
def viewscore(learnerID):

    Quizscorelist = Quizscore.query.filter_by(learnerID=learnerID).all()
    if Quizscorelist:
        return jsonify({
            "code": 200,
            "data": [Quizscore.json() for Quizscore in Quizscorelist]

        }), 200

    else:
        return jsonify({
            "message": "Quizscore not found."
        }), 404


@app.route("/addscore", methods=['POST'])
def add_score():

    scorelist = request.get_json()

    if not all(key in scorelist.keys() for
               key in ('score', 'quizID', 'learnerID')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    quizscore = scorelist['score']
    quizID = scorelist['quizID']
    learnerID = scorelist['learnerID']

    score = Quizscore(qsID=None, quizscore=quizscore,
                      quizID=quizID, learnerID=learnerID)

    try:
        db.session.add(score)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": score.json()
            }
        ), 200

    except Exception as e:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500


###########################################################

# The following is  for self enrolling to courses for learner (1 course) - POST
@app.route("/enrolledCourses", methods=['POST'])
def self_enrolled():

    try:

        enrollcourse = request.get_json()

        # print(enrollcourse)
        if not all(key in enrollcourse.keys() for
                   key in ('learnerid', 'enrolledCourses')):
            return jsonify({
                "message": "Incorrect JSON object provided."
            }), 500

        learnerid = enrollcourse['learnerid']
        learner = Learner.query.filter_by(id=learnerid).first()
        if not learner:
            return jsonify({
                "message": "learner not valid."
            }), 500

        learner.CoursesEnrolled = enrollcourse['enrolledCourses']
        # print(learner.enrolledCourses)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": learner.to_dict()
            }
        ), 200

    except Exception as e:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

# +1


@app.route("/currentEnrolled", methods=['POST'])
def currentEnrolled():

    try:

        currentenroll = request.get_json()

        # print(currentenroll)
        if not all(key in currentenroll.keys() for
                   key in ('classesID', 'currentEnrolled')):
            return jsonify({
                "message": "Incorrect JSON object provided."
            }), 500

        classid = currentenroll['classesID']
        classes = Classes.query.filter_by(classesID=classid).first()
        if not classes:
            return jsonify({
                "message": "class not valid."
            }), 500

        classes.currentEnrolled = currentenroll['currentEnrolled']
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": classes.json()
            }
        ), 200

    except Exception as e:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

# The following withdraw learner from course  (1 course)  - POST


@app.route("/withdrawCourses", methods=['POST'])
def withdraw_course():

    try:

        enrollcourse = request.get_json()

        # print(enrollcourse)
        if not all(key in enrollcourse.keys() for
                   key in ('learnerid', 'enrolledCourses')):
            return jsonify({
                "message": "Incorrect JSON object provided."
            }), 500

        learnerid = enrollcourse['learnerid']
        learner = Learner.query.filter_by(id=learnerid).first()
        if not learner:
            return jsonify({
                "message": "learner not valid."
            }), 500

        learner.CoursesEnrolled = ""
        # print(learner.enrolledCourses)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": learner.to_dict()
            }
        ), 200

    except Exception as e:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500


# The following is to assign learner to course (1 course) - POST
@app.route("/assigncourses", methods=['POST'])
def assign_course():

    assign = request.get_json()

    # print(enrollcourse)
    if not all(key in assign.keys() for
               key in ('learnerid', 'enrolledCourses')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    try:
        learnerid = assign['learnerid']
        learner = Learner.query.filter_by(id=learnerid).first()
        if not learner:
            return jsonify({
                "message": "learner not valid."
            }), 500

        learner.CoursesAssigned = assign['enrolledCourses']
        # print(learner.enrolledCourses)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": learner.to_dict()
            }
        ), 200

    except Exception as e:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
