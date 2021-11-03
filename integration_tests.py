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
        

class TestSelfEnrolled(TestApp):

    def test_self_enrolled(self):

        learner = Learner(
            CompletedCourses="IS214 System Design", ContactNo="92130843", CoursesAssigned="",
            CoursesEnrolled="", CurrentDesignation="Engineer", Department="Learning",
            Email="constan@gmail.com", Name="Constance TAN", Role="learner",
            StaffID=1, Username="cons", id=1)


        db.session.add(learner)
        db.session.commit()
       
        request_body = {
            'learnerid': learner.StaffID,
            'enrolledCourses': "IS212 Software Project Management G2"
            
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

        db.session.add(learner)
        db.session.commit()

        request_body = {
            'learnerid': learner.StaffID,
            'enrolledCourses': "IS212 Software Project Management G2"

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

        learner = Learner(
            CompletedCourses="IS214 System Design", ContactNo="92130843", CoursesAssigned="",
            CoursesEnrolled="", CurrentDesignation="Engineer", Department="Learning",
            Email="constan@gmail.com", Name="Constance TAN", Role="learner",
            StaffID=1, Username="cons", id=1)

        db.session.add(learner)
        db.session.commit()

        request_body = {
            'learnerid': learner.StaffID,
            'AssignedCourses': "IS212 Software Project Management G2"

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
          
          classes = Classes(classesID=1, startDate="August 18 2021", startTime="8am",
                            endDate="November 5 2021", endTime="12pm", classesSize=40, trainerAssigned="Roger Ng", currentEnrolled=0)
          lesson = Lesson(lessonID=1, courseMaterial="week1a introduction",classesID=1)
          
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
        
          
          request_body = {
              'question': "Software Project Management module will teach you about agile process",
              'answer': "True",
              'lessonID': 1,
              
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
              
              
