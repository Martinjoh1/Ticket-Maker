import csv
import os
import os.path
import pandas as pd


def create_scanned_csv():
    csvData = ['ID']

    with open('scanned_tickets.csv', 'a') as csvFile:
      writer = csv.writer(csvFile)
      writer.writerow(csvData)

    csvFile.close()

def add_to_csv(id):
    with open('scanned_tickets.csv', 'a') as csvAdd:
      writer = csv.writer(csvAdd)
      row = [id]
      writer.writerow(row)
    csvAdd.close()

def check_valid():
    id = str(input("Ready to scan."+"\n"))
    new_id = ""
    for i in range(len(id)-1):
        new_id += id[i]
    new_id += ".0"
    new_id = float(new_id)
    data = pd.read_csv("scanned_tickets.csv")
    scanned_list = list(data["ID"])
    if new_id not in scanned_list:
        pass
    else:
        print("Ticket already scanned.")
        return False
    # data = pd.read_csv("scanned_tickets.csv")
    # scanned_list = list(data["ID"])
    data = pd.read_csv("ticket.csv")
    bar_list = list(data["ID"])
    if new_id not in bar_list:
        print("Invalid Ticket")
    else:
        print("Thanks, enjoy the show.")
        return new_id


def main():

    if not os.path.isfile('scanned_tickets.csv'):
        create_scanned_csv()
    id = check_valid()
    if id:
        add_to_csv(id)


main()
