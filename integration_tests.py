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
            StaffID=3, Username="cons", id=3)


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
                                            'StaffID': 3,
                                            'Username': 'cons',
                                            'id': 3 }})
    
    
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
              StaffID=3, Username="cons", id=3)

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
          self.assertEqual(response.json, {'code':200, 'data':{ 'CompletedCourses': 'IS214 System Design',
                                            'ContactNo': '92130843',
                                            'CoursesAssigned': '',
                                            'CoursesEnrolled': '',
                                            'CurrentDesignation': 'Engineer',
                                            'Department': 'Learning',
                                            'Email': 'constan@gmail.com',
                                                'Name': 'Constance TAN',
                                                'Role': 'learner',
                                                'StaffID': 3,
                                                'Username': 'cons',
                                                'id': 3 }})
    
         
 

        
        


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
         
         
