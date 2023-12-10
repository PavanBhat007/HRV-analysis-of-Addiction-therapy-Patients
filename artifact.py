# def remove_artifacts(data, size, start=500):
#     # end = size
    
#     # range_beg = start
#     # range_end = end
#     # try:
#     #     while start<end:
#     #         if data[start] < 0:
#     #             range_beg = start
#     #         start+=1
#     # except IndexError:
#     #     pass
        
#     # return tuple([range_beg, range_end])
    
#     print(data[size-1])

# f'{BASE_PATH_CONTROL}\{os.listdir(f"{BASE_PATH_CONTROL}")[0]}'

# def extract_data(filepath):
#     f = adi.read_file(filepath)
    
#     individual_ecg = []
#     for channel in range(CHANNELS):
#         # print(f.channels[channel])
#         for record in range(1, f.channels[channel].n_records+1):            
#             if f.channels[channel].name == "ECG":
#                 data = f.channels[channel].get_data(record)
#                 data = data[600:50000]                    
#                 for ele in data:
#                     individual_ecg.append(ele)
                        
#     return individual_ecg

# ecg = extract_data(f"{BASE_PATH_CONTROL}\Althaf_Pasha-35-M.adicht")
    
# # finding R peaks
# _, rpeaks = nk.ecg_peaks(ecg, sampling_rate=1000)
# peaks = list(rpeaks['ECG_R_Peaks'])
# print(len(peaks))
# peaks = remove_artifacts(peaks, size=len(peaks))