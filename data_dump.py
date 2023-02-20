import json
import pandas as pd

from scania.connection import mongo_client

DATA_FILE_PATH="https://raw.githubusercontent.com/Bhupendra1770/SCANIA/main/aps_failure_training_set.csv"
DATABASE_NAME="SCANIA"
COLLECTION_NAME="STFD"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    df = df.iloc[:34000,:]
    print(f"Rows and columns: {df.shape}")

    #Convert dataframe to json so that we can dump these record in mongo db
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    #insert converted json record to mongo db
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)