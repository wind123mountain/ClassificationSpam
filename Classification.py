from math import log
from Preprocessing import data_preprocessing


class SpamClassification:
    HAM = 0
    SPAM = 1
    
    def __init__(self, p, p_ti, t, e = 3):
        self.P_HAM = p[self.HAM]
        self.P_SPAM = p[self.SPAM]
        self.P_ti_ham = p_ti[self.HAM]
        self.P_ti_spam = p_ti[self.SPAM]
        self.T = t
        self.epsilon = e
        
    def classify(self, mail, preprocessed=False):
        if preprocessed == False:
            mail = data_preprocessing(mail)
        
        log_likelihood_ham = self.P_HAM
        log_likelihood_spam = self.P_SPAM
        
        mail_words = set(mail.split())
        T_d = mail_words.intersection(self.T)
        
        for word in T_d:
            log_likelihood_ham += log(self.P_ti_ham[word])
            log_likelihood_spam += log(self.P_ti_spam[word])
            
        if (log_likelihood_spam >= log_likelihood_ham 
            and log_likelihood_spam-log_likelihood_ham > self.epsilon):
            return self.SPAM
        
        return self.HAM
    
    def classify_D_test(self, D_test, data_preprocessed=True):
        result = []
        
        for mail in D_test:
            result.append(self.classify(mail, data_preprocessed))
        return result
    