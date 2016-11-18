#This one (I dont know why) is not working yet
import csv

def csvDictReader(fileObj):
    reader = csv.DictReader(fileObj, delimiter = ",")
    for line in reader:
        print(line["first_name"]),
        print(line["last_name"])

if __name__ == "__main__":
    with open("TB_data_dictionary_2016-11-17.csv") as fObj:
        csvDictReader(fObj)
