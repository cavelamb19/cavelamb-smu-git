import unittest
import flask_testing
import json
from app import app, db, Trainer, Learner, Administrator, Course, Classes, Lesson, Quiz, Quizscore, QuestionTrueFalse


class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        
        
class Testgetcourses(TestApp):
    
      def test_get_all_courses(self):
          
          course1 = Course(
          courseID=1, courseName="IS212 Software Project Management G2", courseDesc="agile methods", preRequisites="NULL", classesID=1)

          classes1 = Classes(classesID=1, startDate="August 18 2021", startTime="8am",
                          endDate="November 5 2021", endTime="12pm", classesSize=40, trainerAssigned="Roger Ng", currentEnrolled=0)
          
          course2 = Course(
              courseID=2, courseName="IS115 Computational Thinking G1", courseDesc="Math and coding", preRequisites="IS112 Business applications", classesID=2)

          classes2 = Classes(classesID=2, startDate="August 18 2021", startTime="8am",
                             endDate="November 5 2021", endTime="12pm", classesSize=40, trainerAssigned="John Tan", currentEnrolled=0)

          
          db.session.add(course1)
          db.session.add(course2)
          db.session.add(classes1)
          db.session.add(classes2)
          db.session.commit()
          
          response = self.client.get("/course/")
          
          self.assertEqual.__self__.maxDiff = None
          self.assertEqual(response.status_code, 200)
          self.assertEqual(response.json, {'code': 200, 'data': {"course": [
              
                {
                    "classesID": 1, 
                    "courseDesc": "agile methods", 
                    "courseID": 1, 
                    "courseName": "IS212 Software Project Management G2", 
                    "preRequisites": "NULL"
                }, 
                {
                    "classesID": 2, 
                    "courseDesc": "Math and coding", 
                    "courseID": 2, 
                    "courseName": "IS115 Computational Thinking G1", 
                    "preRequisites": "IS112 Business applications"
                }
            
          ] }})

        

class TestgetLearners(TestApp):
    
      def test_get_all_learners(self):
          
          learner1= Learner(
              CompletedCourses="IS214 System Design", ContactNo="92130843", CoursesAssigned="",
              CoursesEnrolled="", CurrentDesignation="Engineer", Department="Learning",
              Email="constan@gmail.com", Name="Constance TAN", Role="learner",
              StaffID=1, Username="cons", id=1)
          
          learner2 = Learner(
              CompletedCourses="IS115 Computational Thinking", ContactNo="90247788", CoursesAssigned="",
              CoursesEnrolled="", CurrentDesignation="Engineer", Department="Learning",
              Email="johnson@gmail.com", Name="Johnson sim", Role="learner",
              StaffID=2, Username="john", id=2)
      
          db.session.add(learner1)
          db.session.add(learner2)
          db.session.commit()
          
          response = self.client.get("/learner/")
          
          self.assertEqual.__self__.maxDiff = None
          self.assertEqual(response.status_code, 200)
          self.assertEqual(response.json, {'code': 200, 'data': {"course": [
            {
                "CompletedCourses": "IS214 System Design",
                "ContactNo": "92130843",
                "CoursesAssigned": "",
                "CoursesEnrolled": "",
                "CurrentDesignation": "Engineer",
                "Department": "Learning",
                "Email": "constan@gmail.com",
                "Name": "Constance TAN",
                "Role": "learner",
                "StaffID": 1,
                "Username": "cons",
                "id": 1
            },
            {
                "CompletedCourses": "IS115 Computational Thinking",
                "ContactNo": "90247788",
                "CoursesAssigned": "",
                "CoursesEnrolled": "",
                "CurrentDesignation": "Engineer",
                "Department": "Learning",
                "Email": "johnson@gmail.com",
                "Name": "Johnson sim",
                "Role": "learner",
                "StaffID": 2,
                "Username": "john",
                "id": 2
            }
            
          ] }})




class TestSelfEnrolled(TestApp):

    def test_self_enrolled(self):

        learner = Learner(
            CompletedCourses="IS214 System Design", ContactNo="92130843", CoursesAssigned="",
            CoursesEnrolled="", CurrentDesignation="Engineer", Department="Learning",
            Email="constan@gmail.com", Name="Constance TAN", Role="learner",
            StaffID=1, Username="cons", id=1)

        course = Course(
            courseID=1, courseName="IS212 Software Project Management G2", courseDesc="agile methods", preRequisites="NULL",classesID=1)
        
        classes = Classes(classesID=1, startDate="August 18 2021", startTime="8am",
                          endDate="November 5 2021", endTime="12pm", classesSize=40, trainerAssigned="Roger Ng", currentEnrolled=0)

        db.session.add(learner)
        db.session.add(course)
        db.session.add(classes)
        db.session.commit()
       
        request_body = {
            'learnerid': learner.StaffID,
            'enrolledCourses': course.courseName
            
         }

        response = self.client.post("/enrolledCourses",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        self.assertEqual.__self__.maxDiff = None
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'code':200, 'data':{ 'CompletedCourses': 'IS214 System Design',
                                          'ContactNo': '92130843',
                                          'CoursesAssigned': '',
                                          'CoursesEnrolled': 'IS212 Software Project Management G2',
                                          'CurrentDesignation': 'Engineer',
                                           'Department': 'Learning',
                                           'Email': 'constan@gmail.com',
                                            'Name': 'Constance TAN',
                                            'Role': 'learner',
                                            'StaffID': 1,
                                            'Username': 'cons',
                                            'id': 1 }})
    
    
    def test_self_enrolled_invalid_learner(self):
        
       
        request_body = {
            'learnerid': 10,
            'enrolledCourses': "IS212 Software Project Management G2"

        }

        response = self.client.post("/enrolledCourses",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {
            'message': 'learner not valid.'
        })
        
        
    
         
class TestWithdrawSelfEnrolled(TestApp):

    def test_withdraw_self_enrolled_courses(self):

        learner = Learner(
            CompletedCourses="IS214 System Design", ContactNo="92130843", CoursesAssigned="",
            CoursesEnrolled="", CurrentDesignation="Engineer", Department="Learning",
            Email="constan@gmail.com", Name="Constance TAN", Role="learner",
            StaffID=1, Username="cons", id=1)
        
        course = Course(
            courseID=1, courseName="IS212 Software Project Management G2", courseDesc="agile methods", preRequisites="NULL", classesID=1)

        classes = Classes(classesID=1, startDate="August 18 2021", startTime="8am",
                          endDate="November 5 2021", endTime="12pm", classesSize=40, trainerAssigned="Roger Ng", currentEnrolled=0)


        db.session.add(learner)
        db.session.add(course)
        db.session.add(classes)
        db.session.commit()

        request_body = {
            'learnerid': learner.StaffID,
            'enrolledCourses': course.courseName

        }

        response = self.client.post("/withdrawCourses",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        self.assertEqual.__self__.maxDiff = None
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'code': 200, 'data': {'CompletedCourses': 'IS214 System Design',
                                                               'ContactNo': '92130843',
                                                               'CoursesAssigned': '',
                                                               'CoursesEnrolled': '',
                                                               'CurrentDesignation': 'Engineer',
                                                               'Department': 'Learning',
                                                               'Email': 'constan@gmail.com',
                                                               'Name': 'Constance TAN',
                                                               'Role': 'learner',
                                                               'StaffID': 1,
                                                               'Username': 'cons',
                                                               'id': 1}})


class TestAssignLearner(TestApp):

    def test_assign_learner(self):
        
        course = Course(
            courseID=1, courseName="IS212 Software Project Management G2", courseDesc="agile methods", preRequisites="NULL", classesID=1)

        classes = Classes(classesID=1, startDate="August 18 2021", startTime="8am",
                          endDate="November 5 2021", endTime="12pm", classesSize=40, trainerAssigned="Roger Ng", currentEnrolled=0)
        
        learner = Learner(
            CompletedCourses="IS214 System Design", ContactNo="92130843", CoursesAssigned="",
            CoursesEnrolled="", CurrentDesignation="Engineer", Department="Learning",
            Email="constan@gmail.com", Name="Constance TAN", Role="learner",
            StaffID=1, Username="cons", id=1)

        db.session.add(learner)
        db.session.add(classes)
        db.session.add(course)
        db.session.commit()

        request_body = {
            'learnerid': learner.StaffID,
            'AssignedCourses': course.courseName

        }

        response = self.client.post("/assigncourses",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'code': 200, 'data': {'CompletedCourses': 'IS214 System Design',
                                                               'ContactNo': '92130843',
                                                               'CoursesAssigned': 'IS212 Software Project Management G2',
                                                               'CoursesEnrolled': '',
                                                               'CurrentDesignation': 'Engineer',
                                                               'Department': 'Learning',
                                                               'Email': 'constan@gmail.com',
                                                               'Name': 'Constance TAN',
                                                               'Role': 'learner',
                                                               'StaffID': 1,
                                                               'Username': 'cons',
                                                               'id': 1}})
class TestCreateQuizInfo(TestApp):
    
      def test_create_quiz_info(self):
          
          course = Course(
              courseID=1, courseName="IS212 Software Project Management G2", courseDesc="agile methods", preRequisites="NULL", classesID=1)

          classes = Classes(classesID=1, startDate="August 18 2021", startTime="8am",
                            endDate="November 5 2021", endTime="12pm", classesSize=40, trainerAssigned="Roger Ng", currentEnrolled=0)
          lesson = Lesson(lessonID=1, courseMaterial="week1a introduction",classesID=classes.classesID)
         
          db.session.add(course)
          db.session.add(classes)
          db.session.add(lesson)
          db.session.commit()
          

          request_body = {
              'lessonID': lesson.lessonID,
              'title': "Week1 Quiz",
              'time':"15 minutes",
              'instruction':"No calculator",
              'attempt':"1"
             

          }
          
          response = self.client.post("/addquizInfo",
                                      data=json.dumps(request_body),
                                      content_type='application/json')

          self.assertEqual(response.status_code, 200)
          self.assertEqual(response.json, {"code": 200,"data": {
                                                "attemptNo": "1",
                                                "lessonID": 1,
                                                "quizDesc": "No calculator",
                                                "quizDuration": "15 minutes",
                                                "quizID": 1,
                                                "quizTitle": "Week1 Quiz"
                                                     }})
          
          

class TestCreateTrueFalseQuestion(TestApp):
      
      def test_create_True_False_question(self):
          
          course = Course(
              courseID=1, courseName="IS212 Software Project Management G2", courseDesc="agile methods", preRequisites="NULL", classesID=1)

        
          classes = Classes(classesID=1, startDate="August 18 2021", startTime="8am",
                            endDate="November 5 2021", endTime="12pm", classesSize=40, trainerAssigned="Roger Ng", currentEnrolled=0)
          lesson = Lesson(lessonID=1, courseMaterial="week1a introduction",classesID=1)
          
          quiz= Quiz(quizID=1,quizDuration="15 minutes", attemptNo="Unlimited", quizTitle="Week1 Quiz", quizDesc="No Calculator", lessonID=lesson.lessonID)
         
         
          db.session.add(course)
          db.session.add(classes)
          db.session.add(lesson)
          db.session.add(quiz)
          db.session.commit()

          request_body = {
              'question': "Software Project Management module will teach you about agile process",
              'answer': "True",
              'lessonID': quiz.lessonID,
              
          }
          
          response = self.client.post("/addquestiontruefalse",
                                      data=json.dumps(request_body),
                                    content_type='application/json')
          
          self.assertEqual(response.status_code, 200)
          self.assertEqual(response.json, {'code': 200, 'data': {'ans' : "True",
                                                                 'qn': "Software Project Management module will teach you about agile process",
                                                                 'qnID':1,
                                                                 'quizID': 1}})
          
        
      def test_find_True_False_question_by_quizID(self):
              
              quiz = Quiz(quizID= 1, quizDuration="15 mins", attemptNo= "Unlimited", quizTitle="Week 1", quizDesc="No Calculator", lessonID="1")
              
              question = QuestionTrueFalse(
                  qnID=1, qn="Software Project Management module will teach you about agile process", ans="True",
                  quizID=1)
                  

              db.session.add(quiz)
              db.session.add(question)
              db.session.commit()


              response = self.client.get("/questiontruefalse/quizID/1")
              self.assertEqual(response.status_code, 200)
              self.assertEqual(response.json, {'code': 200, 'data': [{'ans': "True",
                                                                     'qn': "Software Project Management module will teach you about agile process",
                                                                     'qnID': 1,
                                                                     'quizID': 1}]})
              

class TestAddlearnerscore(TestApp):
    
      def test_add_learner_score(self):
          
          course = Course(
              courseID=1, courseName="IS212 Software Project Management G2", courseDesc="agile methods", preRequisites="NULL", classesID=1)

          classes = Classes(classesID=1, startDate="August 18 2021", startTime="8am",
                            endDate="November 5 2021", endTime="12pm", classesSize=40, trainerAssigned="Roger Ng", currentEnrolled=0)
          lesson = Lesson(
              lessonID=1, courseMaterial="week1a introduction", classesID=1)

          quiz = Quiz(quizID=1, quizDuration="15 minutes", attemptNo="Unlimited",
                      quizTitle="Week1 Quiz", quizDesc="No Calculator", lessonID=lesson.lessonID)
          
          learner = Learner(
              CompletedCourses="IS214 System Design", ContactNo="92130843", CoursesAssigned="",
              CoursesEnrolled="", CurrentDesignation="Engineer", Department="Learning",
              Email="constan@gmail.com", Name="Constance TAN", Role="learner",
              StaffID=1, Username="cons", id=1)


          db.session.add(course)
          db.session.add(classes)
          db.session.add(lesson)
          db.session.add(quiz)
          db.session.add(learner)
          db.session.commit()  
          
          request_body = {
              'score': 2,
              'quizID': quiz.quizID,
              'learnerID': learner.StaffID,

          }
          
          response = self.client.post("/addscore",
                                      data=json.dumps(request_body),
                                      content_type='application/json')

          self.assertEqual(response.status_code, 200)
          self.assertEqual(response.json, {"code": 200,"data": {
                                                "qsID": 1,
                                                "quizscore": 2,
                                                "quizID": 1,
                                                "learnerID": 1
                                               
                                                     }})

              
