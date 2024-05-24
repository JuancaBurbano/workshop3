from kafka import KafkaProducer
from json import dumps
from json import loads
import json
import pandas as pd
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

csv_file_path = '../Data/test.csv'
my_dataframe = pd.read_csv(csv_file_path)


producer = KafkaProducer(
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    bootstrap_servers=['localhost:9092']
)

for index, row in my_dataframe.iterrows():
    dict_row = row.to_dict()
    json_row = json.dumps(dict_row)  
    producer.send('w', value=dict_row)  
    time.sleep(0.2)
    logging.info(f'Message sent: {dict_row}')

