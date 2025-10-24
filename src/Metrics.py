from abc import ABC, abstractmethod
from sklearn.metrics import confusion_matrix
import numpy as np
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

    def calculate_metrics_regression(self):
        """
        Calculates the main metrics for regression
        """
        y_true = self.ground_truth
        y_pred = self.predicted_values

        # Mean Absolute Error
        mae = np.mean(np.abs(y_true - y_pred))

        # Mean Squared Error
        mse = np.mean((y_true - y_pred) ** 2)

        # Root Mean Squared Error
        rmse = np.sqrt(mse)

        # R² score (Coefficient of Determination)
        ss_total = np.sum((y_true - np.mean(y_true)) ** 2)
        ss_res = np.sum((y_true - y_pred) ** 2)
        r2 = 1 - (ss_res / ss_total) if ss_total != 0 else 0

        # Mean Absolute Percentage Error (optional)
        mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100 if np.all(y_true != 0) else None

        return {
            "MAE": mae,
            "MSE": mse,
            "RMSE": rmse,
            "R2": r2,
            "MAPE": mape
        }