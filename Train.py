from collections import Counter, defaultdict

def split_lable(samples, labels):
        stick_samples_lable = defaultdict(list)
    
        for sample, label in zip(samples, labels):
            stick_samples_lable[label].append(sample)
            
        return stick_samples_lable


class Train:
    HAM = 0
    SPAM = 1
    
    def __init__(self, samples, labels):
        self.D_train = split_lable(samples, labels)
        self.D_HAM = self.D_train[Train.HAM]
        self.D_SPAM = self.D_train[Train.SPAM]
        self.train()
        
    def word_freq(self, mails_list):
        word_freq = Counter()
        for mail in mails_list:
            words = mail.split()
            word_freq.update(words)
    
        return word_freq
        
    def train(self):
        #tan so xuat hien tu trong ham
        self.ham_fw = self.word_freq(self.D_HAM)
        #tan so xuat hien tu trong spam
        self.spam_fw = self.word_freq(self.D_SPAM)
        
        total_words_in_ham = sum(self.ham_fw.values())
        total_words_in_spam = sum(self.spam_fw.values())
        
        words_in_ham = set(self.ham_fw.keys())
        words_in_spam = set(self.spam_fw.keys())
        
        self.T = words_in_ham.union(words_in_spam)
        n_T = len(self.T)
        
        self.P_ti_HAM = Counter()
        self.P_ti_SPAM = Counter()
        
        for t in self.T:
            self.P_ti_HAM[t] = (self.ham_fw[t] + 1)/(total_words_in_ham + n_T)
            self.P_ti_SPAM[t] = (self.spam_fw[t] + 1)/(total_words_in_spam + n_T)
        
        self.P = defaultdict(list)
        self.P_ti = defaultdict(list)
            
        self.P[Train.HAM] = len(self.D_HAM)/len(self.D_HAM + self.D_SPAM)
        self.P[Train.SPAM] = len(self.D_SPAM)/len(self.D_HAM + self.D_SPAM)
        
        self.P_ti[Train.HAM] = self.P_ti_HAM
        self.P_ti[Train.SPAM] = self.P_ti_SPAM
        
    
    


    