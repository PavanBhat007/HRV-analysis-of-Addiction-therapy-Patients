from flask import Flask, request, jsonify
from model import start


app = Flask(__name__)

@app.route('/api', methods = ['GET'])
def return_pred():
    d = {}
    
    patient_name = request.args['query']
    preds = start(patient_name=patient_name)
    
    print(preds)
    d['output'] = preds
    return d


if __name__ == "__main__" :
    app.run(debug=True)