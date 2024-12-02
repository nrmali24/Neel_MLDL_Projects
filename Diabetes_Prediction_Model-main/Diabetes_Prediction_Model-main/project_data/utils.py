import os
import pickle
import json
import config
import numpy as np

class diabetics():
    def __init__(self,Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):

        self.Pregnancies = Pregnancies
        self.Glucose     = Glucose
        self.BloodPressure = BloodPressure
        self.SkinThickness = SkinThickness
        self.Insulin       = Insulin
        self.BMI           = BMI
        self.DiabetesPedigreeFunction = DiabetesPedigreeFunction
        self.Age          = Age

    def load_path(self):
        with open(config.model_path,'rb')as file:
            self.model = pickle.load(file)

        with open(config.json_path,'r')as file:
            self.json = json.load(file)


    def diabetics_prediction(self):
        self.load_path()

        test_arr = np.zeros(len(self.json['columns']))

        test_arr[0] = self.Pregnancies
        test_arr[1] = self.Glucose
        test_arr[2] = self.BloodPressure
        test_arr[3] = self.SkinThickness
        test_arr[4] = self.Insulin
        test_arr[5] = self.BMI
        test_arr[6] = self.DiabetesPedigreeFunction
        test_arr[7] = self.Age

        print('test_array :',test_arr)

        prediction =  self.model.predict([test_arr])
        return prediction


          








        