# programming-language-classifier
[Link to Jupyter Notebook](https://github.com/conleydg/programming-language-classifier/blob/master/programming-language-classifier.ipynb)

## Programming-language-classifier attempts to use machine learning to identify different programming languages

### Processing the Training Data

 The first part of the pipeline is the CountVectorizer.  The CountVectorizer works by turning 'words' of at least two characters into a numeric representation that can be passed into a classifier. 
 
 The second part of the pipeline is the TfiftTransformer.  This takes the vectorized data and weighs each feature based on how unique it is.  
 
 The final part of the pipeline is the estimator method, which in this case is LinearSVC.  LinearSVC works by creating a vector based on the training data features.  When using predict, LinearSVC will decide if the feature is close enough to that vector to be considered the same class.
 
 ## Results
 
 Using a portion of the original data as a test, the classifier was able to return a score of .829.  Using files that were sourced from the internet the classifier returned scores between .70 and .79.  The model works okay, it might be better if it was fed more data to train with.



