# Stack Overflow Natural Language Query Challege

Googling-StackOverflow is humorous name for a development technique that
consists in Googling every programming task to find StackOverflow snippets of
code for it. Google queries are usually written in Natural Language, therefore it
should be interesting to explore how much we can program in Natural Language,
given a large database that links Natural Language titles with code snippets such
as StackOverflow.
Another advantage of the database is that answers are voted, meaning that
is possible to evaluate what are the best snippets. This can be used to the
advantage of the recommendation system.

The full data dump for StackOverflow can be found at:
https://archive.org/details/stackexchange
Kaggle Provides an older version that includes only Python answers here:
https://www.kaggle.com/stackoverflow/pythonquestions/data
Examples of Queries to this dataset can be found here:
http://data.stackexchange.com/stackoverflow/queries

Specifically, this final project requires you and your team to develop
a recommendation system that given a list Natural Language statements,
return a list of python snippets.


# How to run the program:

1. Make sure you have python installed on your computer.
2. Download Answers.csv, Questions.csv, and Tags.csv from the Kaggle site.  Also download glove.840B.300d.txt.  These three files need to be placed in the BigData_StackOverflowQuery/website/codesearch directory.
3. Open BigData_StackOverflowQuery/website/codesearch/word_vector_model.py.  Change the 2 paths in this file to the correct paths on your computer.  Also open BigData_StackOverflowQuery/website/website/settings.py and under 'TEMPLATES', change the 'DIRS' to the correct path to the 'templates' directory.
4. Open a terminal and navigate to the BigData_StackOverflowQuery/website/ directory.  Run the command 'python manage.py runserver'.  If the file is not found, put in the full path to manage.py.  This will run the code on localhost on port 8000.  If you want to use a different port, specify the port number in the command.  For example, 'python manage.py runserver 8080'.
5. Open localhost:8000/codesearch (or whatever port you used) in your browser.

Note: this program currently takes a long time to run.  The first time is the longest, since the system needs to set up on your computer.  Also, currently, every time you search there is preparation that happens in the system.


# Most important files:

BigData_StackOverflowQuery/website/codesearch/word_vector_model.py:

 This file contains the model for selecting the answers.
 
BigData_StackOverflowQuery/website/codesearch/views.py:

 This file contains the code to handle the request made by the user.
 
BigData_StackOverflowQuery/website/templates/result.html

 This file contains the html code for the site.
