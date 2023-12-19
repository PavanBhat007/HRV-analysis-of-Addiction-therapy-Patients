from flask import Flask, request
from model import start
import json

app = Flask(__name__)

@app.route('/api', methods = ['GET'])
def return_pred():
    d = {}
    
    patient_name = request.args['query']
    preds = start(patient_name=patient_name)

    d['output'] = json.loads(preds)
    return d


if __name__ == "__main__" :
    app.run(debug=True, host='0.0.0.0')