from Preprocessing import load_dataset
from Train import Train
from Classification import SpamClassification
from Evaluation import datas_split

def create_modul(train_ratio = 0.66, e = 3):
    # load data
    easy_ham, spam = load_dataset(data_preprocessed=True)
    
    # chuan bi du lieu va nhan
    samples = easy_ham + spam
    labels = [SpamClassification.HAM] * (len(easy_ham)) + [SpamClassification.SPAM] * len(spam)
    
    # Tron du lieu va chia tap du lieu thanh cac tap train, val, test
    x_train, x_val, x_test, y_train, y_val, y_test = datas_split(samples, labels, train_ratio)
    
    # Train
    train = Train(x_train, y_train)
    
    # Classify
    classifier = SpamClassification(train.P, train.P_ti, train.T, e)
    
    return classifier
