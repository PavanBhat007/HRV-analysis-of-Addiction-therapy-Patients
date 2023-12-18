import pandas as pd
import joblib
import os
import sys
import json
from analysis_script import analyze_ecg

BASE_PATH = "../results/"
BASE_PATH_CONTROL = "../Dataset/data/control"
BASE_PATH_ALCOHOLIC = "../Dataset/data/alcoholic"
FILEPATH = ""


def get_predictions(filepath):
    RR_PARAMS = analyze_ecg(filepath)
    
    rr_stats = pd.DataFrame(columns=["Mean_RR", "STD_RR", "RMS_RR", "Mean_HR", "STD_HR", "RMSSD"])
    params = {
        "Mean_RR":RR_PARAMS[3],
        "STD_RR":RR_PARAMS[4],
        "RMS_RR":RR_PARAMS[5],
        "Mean_HR":RR_PARAMS[6],
        "STD_HR":RR_PARAMS[7],
        "RMSSD":RR_PARAMS[8]
    }
    rr_stats.loc[len(rr_stats)] = params

    model = joblib.load(f'{BASE_PATH}model-79.joblib')
    y_pred = model.predict(rr_stats)
    
    return tuple([y_pred, params])


def start(patient_name):
    global FILEPATH
    
    patient_name = patient_name.strip().replace(' ', '_')
    print(patient_name)
    alc_dir = os.listdir(BASE_PATH_ALCOHOLIC)
    ctrl_dir = os.listdir(BASE_PATH_CONTROL)
    
    try:
        for filename in alc_dir:
            if patient_name in filename:
                FILEPATH = f"{BASE_PATH_ALCOHOLIC}/{filename}"
        if not FILEPATH:
            for filename in ctrl_dir:
                if patient_name in filename:
                    FILEPATH = f"{BASE_PATH_CONTROL}/{filename}"
                    
    except FileNotFoundError:
        print("File not found !!")
        
    if not FILEPATH:
        print("File not found !!")
        sys.exit(1)
        
    status = None            
    prediction, rr_params = get_predictions(FILEPATH)
    if prediction == 0:
        status = "Non-Alcoholic"
    else:
        status = "Alcoholic"
    
    record = {
        'status': status,
        'params': rr_params
    }
    final_oputput = json.dumps(record)
    return final_oputput


if __name__ == "__main__":
    op = start("Velayudham")
    print(op)
