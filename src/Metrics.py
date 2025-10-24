from abc import ABC, abstractmethod
from sklearn.metrics import confusion_matrix
class Metrics:
    def __init__(self,predicted_values,ground_truth,dict_encode_labels):
        self.predicted_values=predicted_values
        self.ground_truth=ground_truth
        self.dict_encode_labels=dict_encode_labels
        self.label_encoded=list(self.dict_encode_labels.values())

    def calculate_metrics_classification(self):
        '''
        This method calculates the main important metrics for classification

        '''
        #Calculates the confussion matrix. Labels allows to order the label in the order of the array
        cm=confusion_matrix(self.ground_truth,self.predicted_values,labels=self.label_encoded)
        main_metrics={}  #Stores each label with all the metrics
        for label,label_encoded in self.dict_encode_labels.items(): #Iterate through each label
            tp = cm[label_encoded, label_encoded]  #Calculate true positives
            fp = sum(cm[:, label_encoded]) - tp    #Calculate false positives
            fn = sum(cm[label_encoded, :]) - tp    #Calculate false negatives
            tn= cm.sum() - (tp+ fp + fn)           #Calculate true negatives
            precision = tp / (tp + fp)    #Precision
            recall = tp / (tp + fn)       #Recall
            f1 = 2 * (precision * recall) / (precision + recall)  #F1-score

            main_metrics[label]={"tp":tp,"fp":fp,"fn":fn,"tn":tn,"precision":precision,"recall":recall,"f1-score":f1}
        return main_metrics
