from Preprocessing import load_dataset
from Train import Train
from Classification import SpamClassification
from Evaluation import*


# load data
easy_ham, spam = load_dataset(data_preprocessed=True)

# chuan bi du lieu va nhan
samples = easy_ham + spam
labels = [SpamClassification.HAM] * (len(easy_ham)) + [SpamClassification.SPAM] * len(spam)

# ti le tap train
train_ratio = 0.66

# ti le tap val
val_ratio = 0

# Tron du lieu va chia tap du lieu thanh cac tap train, val, test
x_train, x_val, x_test, y_train, y_val, y_test = datas_split(samples, labels, train_ratio, val_ratio)

# Train
train = Train(x_train, y_train)

#%%
# epsilon
e = 3

# Classify
classifier = SpamClassification(train.P, train.P_ti, train.T, e)

# predict test data
predicted_y_test = classifier.classify_D_test(x_test)

# Evaluation
print("accuracy: {:.5f}\n".format(accuracy(y_test, predicted_y_test)))

confusion_matrix(y_test, predicted_y_test, Train.SPAM)

print("\nprecision_spam: {:.5f}\n".format(precision(y_test, predicted_y_test, Train.SPAM)))

print("Macro_averaging: {:.5f}".format(Macro_averaging(y_test, predicted_y_test)))


