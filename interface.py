from flask import Flask, jsonify, request, render_template
import config
from smruti_flask.utils import MakePrediction

app = Flask(__name__)

###################################################################################################################
######################################## Homepage API #############################################################
###################################################################################################################

@app.route('/')
def obese_model():
    print('Welcome to the obese Model')
    return render_template('index.html')

###################################################################################################################
########################################## Model API ##############################################################
###################################################################################################################

@app.route('/predict_obesity', methods = ["POST"])
def get_obesity():
    print('We are in POST Method')
    data = request.form
    age = eval(data['age'])
    gender = data['gender']
    height = eval(data['height'])
    weight =  eval(data['weight'])
    bmi = eval(data['bmi'])
    
    mk_pred = MakePrediction(age, gender, height, weight, bmi)
    final = mk_pred.get_prediction()
    if final == 0:
        return jsonify({'Result': f'Test for obesity is Negative'})
    else:
        return jsonify({'Result': f'Test for obesity is Positive'})
        
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = config.PORT_NUMBER, debug=False)
    
