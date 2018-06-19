# Naive-Bayes-Classifiers
Implemented Naive Bayes Classification

We will be using a subset of 2005 TREC Public Spam Corpus [1] containing 5000 training examples and 1000 test examples. This dataset is available in github folder (nbctrain and nbctest).

Each line in the train/test files represents a single email in the following format.
email-id class-label word count word count ...

The email-id is of the format /xxx/yyy. The class-label is either spam or ham (non-spam). Word count
pair indicate the number of occurrences of the word in the email. The data has been preprocessed to
remove non-word characters such as punctuation marks.

To learn a naive bayes classifier we do the following:

1. Compute the prior probabilities P(spam) and P(ham) using the training data
2. Determine the vocabulary and compute the conditional probabilities P (x /spam) and P (x /ham)  using the m-estimate, where m = vocabulary and p = 	1/ vocabulary . We found out the 5 most frequently words indicative of a spam and a ham email?
3. Use these probabilities to classify the test data and report the accuracy. We discuss the difficulty we face when computing the posterior probabilities and propose a solution to overcome this problem.
4. We vary the m parameter and study the changes in the accuracies as a function of m.

### Running the implementation:

python naive.py

For more details, refer to the pdf in the repository.

### Reference:
[1] http://plg.uwaterloo.ca/~gvcormac/treccorpus/about.html
