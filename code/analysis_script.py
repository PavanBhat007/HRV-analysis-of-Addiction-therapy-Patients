import adi
import pandas as pd
import neurokit2 as nk

from get_metrics import get_rr_intervals, calc_mean_RR, calc_std_dev_RR, calc_rms_RR, calc_mean_HR, calc_std_dev_HR, calc_rmssd

pd.set_option('display.max_columns', None) #display all columns
pd.set_option('display.max_rows', None) #display all rows

CHANNELS = 2
BASE_PATH_CONTROL = "D:\dev\PROJECTS\ECG-Analysis-SP2\Dataset\data\control"
BASE_PATH_ALCOHOLIC = "D:\dev\PROJECTS\ECG-Analysis-SP2\Dataset\data\\alcoholic"
COLUMNS = ['Name', 'Age', 'Gender', 'Mean_RR', 'STD_RR', 'RMS_RR', 'Mean_HR', 'STD_HR', 'RMSSD', 'Status']

def extract_data(filepath):
    f = adi.read_file(filepath)
    individual_ecg = []
    for channel in range(CHANNELS):
        # for record in range(1, f.channels[channel].n_records+1):           
        record = 1
        if f.channels[channel].name == "ECG":
            data = f.channels[channel].get_data(record)
            # data = remove_artifacts(data, size=len(data))
            data = data[600:]                    
            for ele in data:
                individual_ecg.append(ele)
                        
    return individual_ecg


def analyze_ecg(filepath):
    params = {}
    ecg = extract_data(filepath)
        
    # finding R peaks
    _, rpeaks = nk.ecg_peaks(ecg, sampling_rate=1000)
    peaks = list(rpeaks['ECG_R_Peaks'])
    # peaks = remove_artifacts(peaks, size=len(peaks))
            
    # finding R-R Intervals
    rr_intervals = get_rr_intervals(peaks)
            
    # calculating parameters based on R-R Intervals
    params['Mean_RR'] = calc_mean_RR(rr_intervals)
    params['STD_RR'] = calc_std_dev_RR(rr_intervals)
    params['RMS_RR'] = calc_rms_RR(rr_intervals)
    params['Mean_HR'] = calc_mean_HR(rr_intervals)
    params['STD_HR'] = calc_std_dev_HR(rr_intervals)
    params['RMSSD'] = calc_rmssd(rr_intervals)

    # get patient details
    tmp = filepath.split("\\")
    patient_details = tmp[-1].split('-')
    name = patient_details[0].replace("_", " ")
    age = patient_details[1]
    gender = patient_details[2][0]
        
    record = [
        name, age, gender,
        str(params['Mean_RR']),
        str(params['STD_RR']),
        str(params['RMS_RR']),
        str(params['Mean_HR']),
        str(params['STD_HR']),
        str(params['RMSSD'])
    ]
        
    return record

print(analyze_ecg(f"{BASE_PATH_ALCOHOLIC}\\Pintu-31-M.adicht"))