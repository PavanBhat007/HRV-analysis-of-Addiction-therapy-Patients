import numpy as np
import math


def get_rr_intervals(r_peak_locations):
    rr_intervals = []
    for i in range(1, len(r_peak_locations)):
        rr_interval = float(r_peak_locations[i]) - float(r_peak_locations[i-1])
        rr_intervals.append(rr_interval)
        
    return rr_intervals



def calc_mean_RR(rr_ints):
    return sum(rr_ints)/len(rr_ints)



def calc_std_dev_RR(rr_ints):
    return np.std(rr_ints)



def calc_rms_RR(rr_ints):
    mean_squares = 0
    for interval in rr_ints:
        mean_squares += abs(interval ** 2)
        
    mean_squares /= len(rr_ints)
    
    return math.sqrt(mean_squares)



def calc_mean_HR(rr_ints):
    return 60000 / calc_mean_RR(rr_ints)



def calc_std_dev_HR(rr_ints):
    instantaneous_hr = [60000 / rr_interval for rr_interval in rr_ints]
    return np.std(instantaneous_hr)  



def calc_rmssd(rr_ints):
    differences = [rr_ints[i] - rr_ints[i - 1] for i in range(1, len(rr_ints))]
    squared_differences = [diff ** 2 for diff in differences]
    mean_squared_differences = np.mean(squared_differences)
    return np.sqrt(mean_squared_differences) 