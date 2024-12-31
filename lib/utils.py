import csv
import json

def load_csv(path):
    with open(path, "r") as f:
        content = csv.reader(f, delimiter=';')
        return list(content)

def save_csv(path, content):
    with open(path, "w") as f:
        writer = csv.writer(f, delimiter=";", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        for row in content:
            writer.writerow(row)

def save_json(path, content):
    with open(path, "w") as f:
        json.dump(content, f)

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)
