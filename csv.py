import csv

def remove_quotes(file_path):
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        lines = [l for l in reader]

    with open(file_path, "w") as file:
        writer = csv.writer(file)
        for line in lines:
            writer.writerow([e.replace('"', '') for e in line])

file_path = "<file_path>.csv" # specify the file path here
remove_quotes(file_path)
