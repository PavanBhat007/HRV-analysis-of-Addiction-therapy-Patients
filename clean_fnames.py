import os
import encrypter

BASE_PATH_CONTROL = "D:\dev\PROJECTS\ECG-Analysis-SP2\Dataset\data\control"
BASE_PATH_ALCOHOLIC = "D:\dev\PROJECTS\ECG-Analysis-SP2\Dataset\data\\alcoholic"

def clean_file_names(dir):
    for _, filename in enumerate(os.listdir(dir)):
        # src = f"{dir}/{filename}"
        # dst = f"{dir}/{filename.replace('M', 'M.adicht')}"
        
        # name_ind = 0
        # while True:
        #     if filename[name_ind].isdigit():
        #         break
        #     else:
        #         name_ind += 1
        
            
        # age_ind = name_ind+1
        # gender_ind = age_ind
        
        # while True:
        #     if filename[gender_ind] in ['M', 'F', 'm', 'f']:
        #         break
        #     elif filename[gender_ind].lower() == 'female':
        #         gender_ind += 6
        #     else:
        #         gender_ind += 1
        
        
        # name = filename[:name_ind].replace("_", " ").strip()
        # age = filename[name_ind:age_ind+1]
        # gender = filename[gender_ind]
        
        # src = f"{dir}\{filename}"
        # dst = f"{dir}\{name.replace(' ', '_')}-{age}-{gender}"
        
        src = f"{dir}/{filename}"
        dst = f"{dir}/{encrypter.encrypt(filename)}"
        
        tmp = encrypter.encrypt(filename)
        
        print(tmp, encrypter.decrypt(tmp), sep = "  |  ")
        
        # try:
        #     os.rename(src, dst)
        # except FileExistsError:
        #     continue
        
# originally filename had many spaces which are now replaced by '_'        
clean_file_names(BASE_PATH_CONTROL)
clean_file_names(BASE_PATH_ALCOHOLIC)

