As deliverable for this Final Project, each team should produce a short report of no less than five pages explaining:
 • A small introduction to the given problem
. • A description of the data used. Good examples of how to describe data can be found on the website where the data is obtained and the papers studied in class. As a guidance, answer the following: How was the data collected? How is the data composed (i.e. columns, json file, etc) What does the data describes?. 
• Answers to the questions asked in the Assignment Section of this document. Most importantly, this part of the report should include a detailed description of the process used to arrive to conclusions.
 • A conclusions section in which you will resume all your findings.



 
Introduction
Googling-StackOverflow is humorous name for a development technique that consists in Googling every programming task to find StackOverflow snippets of code for it. Google queries are usually written in Natural Language, therefore it should be interesting to explore how much we can program in Natural Language, given a large database that links Natural Language titles with code snippets such as StackOverflow. 
For this project we developed a recommendation system that given a list of Natural Language statements, returns a list of Python snippets.  
Data Description 
Stack Exchange provides an anonymized dump of all user-contributed content on its network sites, including StackOverflow. Each site is formatted as a separate archive consisting of XML files zipped via 7-zip using bzip2 compression. Each site archive includes Posts, Users, Votes, Comments, PostHistory and PostLinks. A key feature of the database that facilitated our recommendation system is that answers are voted, meaning that is possible to evaluate what are the best snippets. 
Since this project focused on recommendations of Python snippets, we utilized a convenient subset of the StackOverflow dump provided by Kaggle which focusses on questions and answers regarding Pyhon, as identified by the Python tag. The dataset contains the full text of all questions and answers from Stack Overflow tagged with the python tag posted between August 2, 2008 and Ocotober 19, 2016. It is organized into three tables:
1.	Questions contains the title, body, creation date, score, and owner ID for each Python question.
2.	Answers contains the body, creation date, score, and owner ID for each of the answers to these questions. The ParentId column links back to the Questions table.
3.	Tags contains the tags on each question besides the Python tag. Schema *I don’t understand what the columns here represent*
Each table was downloaded as a csv file from https://www.kaggle.com/stackoverflow/pythonquestions/data, a total of 1.62 GB of data.

Data processing
*talk about how the first method we tried and why the second method is better, provide graphs a processing times to corroborate. Get into details of second method. I have drafted the main talking points for the second method. I’ll talk to Jiachen and fill in details*
Clean
Before any analysis is done, stop words such as ‘the’ and ‘that’ are removed from phrases such that only key words remain. Further, these keywords are lemmatized so that different inflections or variants of a word do not hinder the systems ability to produce accurate suggestions.
*insert example*
NLTK, Natural Language Toolkit, lexical resources were utilized in this preprocessing, specifically Wordnet and Corpus
Vectorize
GloVe is an unsupervised learning algorithm for obtaining vector representations for words. Training is performed on aggregated global word-word co-occurrence statistics from a corpus, and the resulting representations showcase interesting linear substructures of the word vector space.  glove.840B.300d.txt, an aggregation of words and their GloVe vector representation was obtained from Kaggle and used as a template to convert words in our system to vectors. Each word in a query, and hence the entire query, was made into a vector. Post titles were treated similarly. 
The Data
Before processing is carried out, the individual tables, answers, questions and tags, are aggregated into one csv file using Pandas, a Python package providing expressive data structures for working with “relational” or “labeled” data.

The dataset 
Answers


