import csv
def read_csv_file(HumptyDumpty):
    f=open(HumptyDumpty)
    for row in csv.reader(f):
        print(row)

with open("HumptyDumpty.txt",'w',encoding = 'utf-8') as f:
    f.write("Humpty Dumpty sat on a wall, \n")
    f.write("Humpty Dumpty had a great fall. \n")
    f.write("All the king's horses and all the king's men \n")
    f.write("couldn't put Humpty together again.")


    