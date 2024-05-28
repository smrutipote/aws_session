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

@app.route('/predict_obesity', methods = ['POST','GET'])
def get_obesity():
    if request.method == 'POST':
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

    else:
        print('We are in GET Method')
        data1 = request.args
        age = eval(data1.get('age'))
        gender = data1.get('gender')
        height = eval(data1.get('height'))
        weight = eval(data1.get('weight'))
        bmi = eval(data1.get('bmi'))

        mk_pred1 = MakePrediction(age, gender, height, weight, bmi)
        final1 = mk_pred1.get_prediction()
        if final1 == 0:
            return jsonify({'Result': f'Test for obesity is Negative'})
        else:
            return jsonify({'Result': f'Test for obesity is Positive'})
        
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = config.PORT_NUMBER, debug=False)