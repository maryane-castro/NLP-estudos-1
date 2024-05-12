import csv
import json
import pandas as pd
from transformers import pipeline

class DataProcessor:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.data = None

    def read_csv_to_json(self):
        with open(self.csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            self.data = [row for row in reader]

    def write_json(self, json_file):
        with open(json_file, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4)

    def read_json(self, json_file):
        with open(json_file, 'r') as file:
            self.data = json.load(file)

    def query_data(self, query):
        table = pd.DataFrame.from_dict(self.data)
        tqa = pipeline(task="table-question-answering", model="google/tapas-large-finetuned-wtq")
        results = tqa(table=table, query=query)
        return results

