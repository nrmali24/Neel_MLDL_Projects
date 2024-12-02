import os
import pickle
import json
import numpy as np
import config

class Heart():
    def __init__(self,age,creatinine_phosphokinase,diabetes,ejection_fraction,platelets,serum_creatinine,serum_sodium,sex,time):
        self.age = age
        self.creatinine_phosphokinase=creatinine_phosphokinase
        self.diabetes=diabetes
        self.ejection_fraction=ejection_fraction
        self.platelets=platelets
        self.serum_creatinine=serum_creatinine
        self.serum_sodium=serum_sodium
        self.sex=sex
        self.time=time

    def load_path(self):
        with open (config.model_path,"rb") as file:
            self.model = pickle.load(file)
        with open (config.project_data,"r") as file:
            self.columns = json.load(file)

    def get_medic(self):
        self.load_path()
        
        test_array = np.zeros(len(self.columns["columns"]))
        test_array[0]=self.age
        test_array[1]=self.creatinine_phosphokinase
        test_array[2]=self.diabetes
        test_array[3]=self.ejection_fraction
        test_array[4]=self.platelets
        test_array[5]=self.serum_creatinine
        test_array[6]=self.serum_sodium
        test_array[7]=self.sex
        test_array[8]=self.time
        
        print(test_array)

        result = self.model.predict([test_array])
        return result

