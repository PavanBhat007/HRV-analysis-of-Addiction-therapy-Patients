import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from datetime import datetime

from analysis_script import analyze_ecg

BASE_PATH = "../results/"
BASE_PATH_CONTROL = "Dataset/data/control"
BASE_PATH_ALCOHOLIC = "Dataset/data/alcoholic"
FILEPATH = ""

clf = None

def model_tuning(X, y, params):
    rfc = RandomForestClassifier()
    rfcCV = GridSearchCV(
        estimator=rfc,
        param_grid=params,
        scoring="neg_mean_absolute_error",
        cv=3,
        return_train_score=True,
        verbose=1,
        n_jobs=-1,
    )
    rfcCV.fit(X, y)
    opt_alpha_random_forest = rfcCV.best_params_["ccp_alpha"]
    return opt_alpha_random_forest


def model_training():
    global clf

    df = pd.read_csv(f"{BASE_PATH}ecg.csv")
    df = df.sample(frac=1)

    le = LabelEncoder()
    df["Gender"] = le.fit_transform(df["Gender"])

    df = df.sample(frac=1)
    X = df.drop(["Name", "Age", "Gender", "Status"], axis=1).copy()
    y = df["Status"].copy()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=66
    )

    params = {
        "ccp_alpha": [ 0.01, 0.05, 0.1, 0.5, 0.9, 1, 5, 9, 10, 50, 100],
        'max_depth': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,20, 50, 100],
        'n_estimators': [50, 80, 100, 200, 300]
    }

    clf = RandomForestClassifier(
        max_depth=6, random_state=1, ccp_alpha=model_tuning(X_train, y_train, params)
    )
    clf.fit(X_train, y_train)

    y_pred_test = clf.predict(X_test)
    return tuple([accuracy_score(y_test, y_pred_test), y_pred_test])


def model_test(X_test):
    global clf
    print(X_test)
    if not clf:
        clf = RandomForestClassifier(max_depth=6, random_state=1, ccp_alpha=0.8)
    return clf.predict(X_test)


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
    y_pred = model_test(rr_stats)
    return y_pred


def take_inp(filepath):
    global FILEPATH
    FILEPATH = filepath


if __name__ == "__main__":
    take_inp(f"{BASE_PATH_ALCOHOLIC}/Pintu-31-M.adicht")

    accuracy, y_pred = model_training()
    # while accuracy <= 0.8:
    #     accuracy, y_pred = model_training()

    t1 = datetime.utcnow()
    prediction = get_predictions(FILEPATH)
    t2 = datetime.utcnow()
    
    print(f"Completed in {t2-t1}\t\t Accuracy: {accuracy}")
    
    if prediction == 0:
        print("Non-Alcoholic")
    else:
        print("Alcoholic")
