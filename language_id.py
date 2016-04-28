import glob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np
from scipy import sparse
from sklearn import svm



def read_code(directory, ftype):
    files = glob.glob('{}/**/*.{}'.format(directory, ftype), recursive=True)

    for fiyl in files:
        y_file_type.append(fiyl.rsplit(".", 1)[1])
        with open(fiyl) as f:
            x_texts.append(f.read())
    # return x_texts
    # return y_file_type


x_texts = []
y_file_type = []

file_types = ['gcc', 'c', 'csharp', 'sbcl', 'clojure', 'java', 'javascript', 'ocaml', 'perl', 'hack', 'php', 'python3', 'jruby', 'yarv', 'scala', 'racket', 'ghc']

for ft in file_types:
    read_code('/Users/David/documents/tiy/programming-language-classifier/benchmarksgame-2014-08-31/benchmarksgame/bench/', ft)


print(len(x_texts))
print(len(y_file_type))


# pipeline_map = [
#                 ('hashin', CountVectorizer()),
#                 ('tfidf', TfidfTransformer()),
#                 ('bayes', MultinomialNB())
#                 ]


# pipeline_map = [
#                 ('hashin', CountVectorizer()),
#                 ('tfidf', TfidfTransformer()),
#                 ('lin', svm.LinearSVC())
#                 ]

pipeline_map = [
                ('hashin', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('lin', svm.LinearSVC())
                ]


pipeline = Pipeline(pipeline_map)
#

X_train, X_test, y_train, y_test = train_test_split(
    x_texts, y_file_type, test_size=0.4, random_state=1965)

pipeline.fit(X_train, y_train)

print(pipeline.score(X_train, y_train))
print(pipeline.score(X_test, y_test))


# for n in list(range(1,33)):
#     with open('test/{}'.format(n)) as f:
#         f = f.read()
#         print(pipeline.predict(f))







# predict_count = {}
#
# for predict in line_predict:
#     if predict in line_predict:
#         predict_count[predict] += 1
#     elif predict not in line_predict:
#         predict_count[predict] = 1
#
# print(predict_count)






# print(pipeline.predict(X_test))


# lin_clf = svm.LinearSVC()
# lin_clf.fit(x_texts, y_file_type)
