==================
INSTALLATION GUIDE
==================

(1) set up and launch a WAMP or MAMP server

(2) execute the contents of 'is212_example.sql' in phpMyAdmin, i.e. at:

       http://localhost/phpmyadmin  OR
	   http://localhost/phpMyAdmin

(3) find your web server's root directory (e.g. C:\wamp\www) and create a
    folder called 'is212'. Copy the contents of 'htdocs' into 'is212'.

(4) in the 'flask' directory, run "python app.py" in a terminal.

(5) go to http://localhost/is212 where the application should be working!

=============
RUNNING TESTS
=============

To run unit and integration tests, go into the 'flask' folder on your
command line and do:

  python unit_tests.py
  python integration_tests.py

If you get an error message, it may be due to missing packages. Resolve
this by doing:

  python -m pip install flask_testing

for each missing package (in this case, 'flask_testing').
