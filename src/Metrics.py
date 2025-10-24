from abc import ABC, abstractmethod
from sklearn.metrics import confusion_matrix
class Metrics:
    def __init__(self,predicted_values,ground_truth,dict_encode_labels):
        self.predicted_values=predicted_values
        self.ground_truth=ground_truth
        self.dict_encode_labels=dict_encode_labels
        self.label_encoded=list(self.dict_encode_labels.values())

    def calculate_metrics(self):
        cm=confusion_matrix(self.ground_truth,self.predicted_values,labels=self.label_encoded)
        main_metrics={}
        for label,label_encoded in self.dict_encode_labels.items():
            tp = cm[label_encoded, label_encoded]
            fp = sum(cm[:, label_encoded]) - tp
            fn = sum(cm[label_encoded, :]) - tp
            tn= cm.sum() - (tp+ fp + fn)
            precision = tp / (tp + fp)  # 10 / 13 ≈ 0.769
            recall = tp / (tp + fn)     # 10 / 12 ≈ 0.833
            f1 = 2 * (precision * recall) / (precision + recall)  # ≈ 0.8

            main_metrics[label]={"tp":tp,"fp":fp,"fn":fn,"tn":tn,"precision":precision,"recall":recall,"f1-score":f1}
        return main_metrics

pred = [0, 1, 1, 2, 2, 2]
true = [0, 0, 1, 2, 2, 1]
encode = {"class0": 0, "class1": 1, "class2": 2}

m = Metrics(pred, true, encode)
results = m.calculate_metrics()
print(results)