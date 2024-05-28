import pickle
import json
import config
import numpy as np

class MakePrediction():
    def __init__(self, age, gender, height, weight, bmi):
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.bmi = bmi
    
    def load_model(self):
        with open(config.MODEL_PATH, 'rb') as f:
            self.model = pickle.load(f)
            
        with open(config.PROJECT_DATA_PATH, 'r') as f:
            self.project_data = json.load(f)
            
    def get_prediction(self):
        self.load_model()
        
        test_array = np.zeros(len(self.project_data["columns"]))
        test_array[0]= self.age
        test_array[1]= self.project_data["gender"][self.gender]
        test_array[2]= self.height
        test_array[3]= self.weight
        test_array[4]= self.bmi
        print(f'Test array is :{test_array}' )
        
        given_prediction = self.model.predict([test_array])[0]
        if given_prediction == 0:
            print('You are not Obese')
        else:
            print('You are Obese')
        return given_prediction
    
if __name__ == '__main__':
    age = 25.0
    gender ='Male'
    height = 149.0
    weight = 78.0
    bmi = 541.0
    
    mk_pred = MakePrediction(age, gender, height, weight, bmi)
    mk_pred.get_prediction()