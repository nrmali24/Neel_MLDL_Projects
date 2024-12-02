import numpy as np
import pickle
import config
import json 

class LoanSanction():
    def __init__(self,LoanAmount,Credit_History,Property_Area):
        
        self.LoanAmount=LoanAmount
        self.Credit_History=Credit_History
        self.Property_Area=Property_Area     
        
    def get_loadModel(self):
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model = pickle.load(f) #to load the ml model

        with open(config.JSON_FILE_PATH,"r") as file:
            self.json_data = json.load(file) 
                
    def get_decision(self):
        
        self.get_loadModel()
        test_array = np.zeros(3) #initialized default values
        test_array[0] = self.LoanAmount
        test_array[1] = self.Credit_History
        test_array[2] = self.json_data["Property_Area_values"][self.Property_Area]          

        decision = self.model.predict(test_array) #prediction  [price]
        print('##############################',decision)
        return decision

        

    