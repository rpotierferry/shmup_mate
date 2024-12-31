import csv

def load_csv(path):
    with open(path, "r") as f:
        content = csv.reader(f, delimiter=';')
        return list(content)

def save_csv(path, content):
    with open(path, "w") as f:
        writer = csv.writer(f, delimiter=";", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        for row in content:
            writer.writerow(row)
