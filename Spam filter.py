import numpy as np

class SpamClassifier:
    def __init__(self):
        self.pGiven = np.zeros([2, 0], float) #stores the probability of a word appearing given its spam or ham (first index)
        self.totalSpam = np.zeros(2, int)
        
    def train(self):
        
        training_spam = np.loadtxt(open("data/training_spam.csv"), delimiter=",").astype(int) #used to be np.int
        self.pGiven = np.zeros([2, len(training_spam[0])], float)
        
        #counts total spam and ham
        for i in range(0, len(training_spam)):
            if(training_spam[i, 0] == 1):
                self.totalSpam[1] += 1
            else:
                self.totalSpam[0] += 1
        
        #stores how many time words appear in spam / ham emails seperately
        for y in range(0, len(self.pGiven)):
            for i in range(0, len(self.pGiven[y])):
                self.pGiven[y, i] = self.pTrueGivenSpam(training_spam[:,0], training_spam[:,i], y)
        
        
    def predict(self, data):
        """makes a prediction for a list of emails given"""
        predictions = np.zeros(len(data), int)
        
        for i in range(0, len(predictions)):
            predictions[i] = self.singlePrediction(data[i])
        
        return predictions
    
    
        
    def singlePrediction(self, data):
        """makes a prediction for a single email"""
        yesNoValue = np.array([1.0, 1.0])
        for y in range(0, 2):
            
            #for every word measured, 
            #if it appears in email, multiply probability by chance of email being spam given it appears
            #if not, multiply probability by chance of email being spam given it doesnt appear
            for i in range(0, len(self.pGiven[0]) -1):
                if(data[i] == 1):
                    yesNoValue[y] *= self.pGiven[y, i +1]
                else:
                    yesNoValue[y] *= 1 - self.pGiven[y, i +1]
        
        #find which probability is bigger and return prediction for spam or ham
        if(abs(yesNoValue[0]) > abs(yesNoValue[1])):
            return 0
        return 1
            
    
        
    def pTrueGivenSpam(self, spamArray, varArray, givenValue):
        """takes in an array of the spam values and an array of the values being tested
        returns the probability of that value being true given that the email is spam"""
        intersect = 0
        for i in range(0, len(spamArray)):
            if(spamArray[i] == givenValue and varArray[i] == 1):
                intersect += 1
                    
        #laplace smoothing
        #if word is never included in any spam emails in training and that word appears in testing email
        #email will always be assinged ham no matter other factors
        #laplce smoothing makes weighting of this factor less extreme
        if intersect == 0:
            intersect = 1
            
        return intersect / self.totalSpam[givenValue]
    

def create_classifier():
    classifier = SpamClassifier()
    classifier.train()
    return classifier

classifier = create_classifier()
testing_spam = np.loadtxt(open("data/testing_spam.csv"), delimiter=",").astype(int)
results = classifier.predict(testing_spam[:, 1:])

correctSpam = 0
correctHam = 0
for i in range(0, len(results)):
    if(results[i] == 1 and testing_spam[i, 0] == 1):
        correctSpam += 1
    if(results[i] == 0 and testing_spam[i, 0] == 0):
        correctHam += 1
        
print("accuracy: ",(correctSpam + correctHam) / len(results))