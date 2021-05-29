from random import shuffle
from Train import split_lable

def datas_split(samples, labels, train_ratio, val_ratio):
    
    stick_samples_lable = split_lable(samples, labels)
    
    train, test, val = [], [], []
    
    for lable in set(labels):
        temp = stick_samples_lable[lable]
        shuffle(temp)
        n_train = int(len(temp) * train_ratio)
        n_val = int(len(temp) * val_ratio)
        x_train = temp[:n_train]
        x_val = temp[n_train:(n_train + n_val)]
        x_test = temp[(n_train + n_val):]
        
        y_train = [lable] * len(x_train)
        y_val = [lable] * len(x_val)
        y_test = [lable] * len(x_test)
        
        train.extend(zip(x_train, y_train))
        val.extend(zip(x_val, y_val))
        test.extend(zip(x_test, y_test))
    
    shuffle(train)
    shuffle(val)
    shuffle(test)

    x_train = [item[0] for item in train]
    y_train = [item[1] for item in train]
    
    x_val = [item[0] for item in val]
    y_val = [item[1] for item in val]

    x_test = [item[0] for item in test]
    y_test = [item[1] for item in test]

    return x_train, x_val, x_test, y_train, y_val, y_test

def accuracy(expected_labels, predicted_labels):
    correct = sum([1 if expected_label == predicted_label else 0
                   for expected_label, predicted_label in zip(expected_labels, predicted_labels)])
    return correct / len(expected_labels)


def evaluate(expected_labels, predicted_labels, label):
    num_labels = len(expected_labels)
    true_positive = 0
    false_positive = 0
    true_negative = 0
    false_negative = 0

    for expected_label, predicted_label in zip(expected_labels, predicted_labels):
        if expected_label == label and predicted_label == label:
            true_positive += 1
        elif expected_label != label and predicted_label != label:
            true_negative += 1
        elif expected_label == label and predicted_label != label:
            false_negative += 1
        else:
            false_positive += 1

    #true_positive = 100*true_positive/num_labels
    #false_positive = 100*false_positive/num_labels
    #true_negative = 100*true_negative/num_labels
    #false_negative = 100*false_negative/num_labels
    
    return (true_negative, true_positive, false_positive, false_negative)
    
def confusion_matrix(expected_labels, predicted_labels, label):
    
    TN, TP, FP, FN = evaluate(expected_labels, predicted_labels, label)
    
    if label == 1:
        print('Confusion_matrix: Spam class - Total mails: ' + str(len(expected_labels)))
    else:
        print('Confusion_matrix: Ham class - Total mails: ' + str(len(expected_labels)))
    
    #print('TP: {:.15}'.format(TP) + '     FN: {:.15}'.format(FN))
    #print('FP: {:.15}'.format(FP) + '     TN: {:.15}'.format(TN))
    #print('TP: ' + str(TP) + '     FN: ' + str(FN))
    #print('FP: ' + str(FP) + '     TN: ' + str(TN))
    print('TP: {:5}'.format(TP) + '     FN: {:5}'.format(FN))
    print('FP: {:5}'.format(FP) + '     TN: {:5}'.format(TN))
    
def precision(expected_labels, predicted_labels, label):
    
    TN, TP, FP, FN = evaluate(expected_labels, predicted_labels, label)
    
    precision_lable = TP/(TP + FP)
    
    return precision_lable

def recall(expected_labels, predicted_labels, label):
    TN, TP, FP, FN = evaluate(expected_labels, predicted_labels, label)
    
    precision_lable = TP/(TP + FN)
    
    return precision_lable

def Macro_averaging(expected_labels, predicted_labels):
    
    precision_ham = precision(expected_labels, predicted_labels, 0)
    precision_spam = precision(expected_labels, predicted_labels, 1)
    
    return (precision_ham + precision_spam)/2




    




