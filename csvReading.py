import csv

def csvReader(fileObj):
    reader = csv.reader(fileObj)
    for row in reader:
        print(" ".join(row))

if __name__ == "__main__":
    csvPath = "TB_data_dictionary_2016-11-17.csv"
    with open(csvPath, "r") as fObj:
        csvReader(fObj)

        
