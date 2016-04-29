import glob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
import pandas as pd
import numpy as np
from scipy import sparse
from sklearn import svm
from sklearn.svm import SVC
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn import preprocessing
from sklearn.multiclass import OneVsOneClassifier
from sklearn.tree import DecisionTreeClassifier



def read_code(directory, ftype):
    files = glob.glob('{}/**/*.{}'.format(directory, ftype), recursive=True)
    for fiyl in files:
        y_file_type.append(ftype)
        with open(fiyl) as f:
            x_texts.append(f.read())


x_texts = []
y_file_type = []



file_types = ['gcc', 'c', 'csharp', 'sbcl', 'clojure', 'java', 'javascript', 'ocaml', 'perl', 'hack', 'php', 'python3', 'jruby', 'yarv', 'scala', 'racket', 'ghc']

for ft in file_types:
    read_code('/Users/David/documents/tiy/programming-language-classifier/benchmarksgame-2014-08-31/benchmarksgame/bench/', ft)




# ***
pipeline_map = [
                ('hashin', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('lin', svm.LinearSVC()),
                ]



# pipeline_map = [('hashin', CountVectorizer()),
#                 ('feature_selection', SelectFromModel(svm.LinearSVC())),
#                 ('tfidf', TfidfTransformer()),
#                 ('bayes', MultinomialNB()),
#                 ]


pipeline = Pipeline(pipeline_map)
#


X_train, X_test, y_train, y_test = train_test_split(
    x_texts, y_file_type, test_size=0.4, random_state=1965)



pipeline.fit(X_train, y_train)

print(pipeline.score(X_train, y_train))
print(pipeline.score(X_test, y_test))


bryce_tests = ['clojure', 'clojure', 'clojure', 'clojure','python3', 'python3',
               'python3',  'python3',  'javascript', 'javascript', 'javascript',
               'javascript', 'jruby', 'jruby', 'jruby', 'ghc', 'ghc',
                'ghc', 'racket', 'racket', 'racket', 'java', 'java',
                'scala', 'scala', 'php', 'php', 'php', 'ocaml',
                'ocaml']


predictions = []
count = 0
num_correct = 0
for n in list(range(1,25)) + list(range(28,32)):
    type_count = {}
    with open('test/{}'.format(n)) as f:
        f = f.read()
        predicter = pipeline.predict([f])
        predictions.append(predicter)
        if predicter == bryce_tests[count]:
            num_correct += 1
        count += 1
        # print(predicter[0])
print(num_correct/len(bryce_tests))
