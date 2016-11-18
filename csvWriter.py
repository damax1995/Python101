#Let's write a CSV file

import csv

def csvWriter(data, path):
    with open(path, "w", newline = '') as csvFile:
        writer = csv.writer(csvFile, delimiter=",")
        for line in data:
            writer.writerow(line)

if __name__ == "__main__":
    data = ["first_name,last_name,city".split(","),
            "Tyrese, Hirthe, Strackeport".split(","),
            "Jules,Dicki,Lake Nickolasville".split(","),
            "Dedric, Medhurst,Stiedemannberg".split(",")]
    path = "output.csv"
    csvWriter(data, path)
    
