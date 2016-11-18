import csv

def csvDictWriter(path, fieldnames, data):
    with open(path, "w", newline= '') as outFile:
        writer = csv.DictWriter(outFile, delimiter=',')
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    data = ["first_name,last_name,city".split(","),
            "Tyrese, Hirthe, Strackeport".split(","),
            "Jules,Dicki,Lake Nickolasville".split(","),
            "Dedric, Medhurst,Stiedemannberg".split(",")]
    myList = []
    fieldnames = data[0]
    for values in data[1:]:
        innerDict = dict(zip(fieldnames, values))
        myList.append(innerDict)

    path = "dicOutput.csv"
    csvDictWriter(path, fieldnames, myList)
