
import time
import os
import pandas as pd
from sqlalchemy import create_engine
import logging

engine = create_engine('sqlite:///ecommerce-sales.db')


logging.basicConfig(
    filename = r'D:\project_pandas\project_01\log\ingest_db.logs',
    filemode = 'a',
    format = '%(asctime)s - %(levelname)s - %(message)s',
    level = logging.DEBUG
    )




def ingest_db(df,tbl,engine):
    df.to_sql(tbl, engine, if_exists = 'replace', index = False)



def load_raw_data():
    
    FOLDER_PATH = 'D:\project_pandas\project_01\data'
    start = time.time()
    for file in os.listdir(FOLDER_PATH):
        if not file.lower().endswith('.csv'):
            continue
        file_path = os.path.join(FOLDER_PATH,file)
        table_name = os.path.splitext(file)[0]
        df = pd.read_csv(file_path)
        ingest_db(df, table_name, engine)
        logging.info(f"Ingesting {file} into table {table_name} in DB.")
        print(f"Ingesting {file} in table {table_name} in DB.")
    end = time.time()
    total_time = end - start
    logging.info((f"Total Time Taken In Data Ingestion Is : {total_time} Seconds"))
    print(f"Total Time Taken In Data Ingestion Is : {total_time} Seconds")

if __name__ == '__main__':
    load_raw_data()