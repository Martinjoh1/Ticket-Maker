import datetime
import csv
import random
import barcode
import random
import time
import os
import os.path
from fpdf import FPDF
import tempfile
# from pdf2image import convert_from_path
from barcode.writer import ImageWriter
import pandas as pd

def get_cust_name():
  """Get name from user"""
  cust_name = None
  event = None
  while cust_name is None:
      try:
        cust_name = str(input('Please enter your name.\n'))
      except ValueError:
        print ("Invalid entry; please enter a valid customer name.")
  while event is None:
      try:
        event = str(input('Please enter the name of the show.\n'))
      except ValueError:
        print ("Invalid entry; please enter a valid show name.")
  return cust_name, event


def get_number_of_tickets():
  """Get number of tickets to enter from user"""
  num_tickets = 0
  while num_tickets == 0:
      try:
        num_tickets = int(input('How many tickets do you want to get?\n'))
      except:
        print ("Invalid entry for number of tickets.")
  return num_tickets


def get_ticket_amount(opt):
  """Get the ticket amounts from user"""
  if (opt == "B" or "CH" or "C"):
      ticket_amt = 0
  if (opt == "S"):
      ticket_amt = 30
  if (opt == "G"):
      ticket_amt = 12
  if (opt == "SN"):
      ticket_amt = 10
  if (opt == "ST"):
      ticket_amt = 8
  if (opt == "M"):
      mainmenu()

  return ticket_amt


def gather(ticket_amt, amount_list):
  for i,amount in enumerate(amount_list):
    user_tickets = []
    ticket_amount = amount
    # add to list once we know we have valid inputs
    user_tickets.append(ticket_amount)
    print ("Ticket {0} added with amount {1}".format(i+1, amount))
    # print (user_tickets)


def create_csv():
  """Make CSV file with appropriate headers"""
  csvData = ['Name', 'Classification', 'Price', 'ID']

  with open('ticket.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(csvData)

  csvFile.close()

def enter_csv(customername, opt, price, ID):
  """Populate CSV file with information"""
  with open('ticket.csv', 'a') as csvAdd:
    writer = csv.writer(csvAdd)
    row = [customername, opt, price, ID]
    writer.writerow(row)
  csvAdd.close()

def samp_num():
  """Generate random ticket numer"""
  ranum = random.randint(1,1001)*7
  return ranum

date = datetime.date.today()


def make_tix(customername, bar_num, barcode, event,i):
  """Print ticket details"""
  # print("KINETIC EXPRESSIONS")
  # print("____________________________________")
  # print(" ")
  # print("             Date: ",date.strftime("%d/%m/%Y"))
  # print("             Time: ",date.strftime("%I:%M:%S"))
  # print("             Venue: Jelkyl Drama Center")
  # print(" Name            : ", customername)
  # print(" Ticket ID       : ", bar_num)
  # print(" ")
  #
  # print("_____________________________________")
  # print(" ")

  pdf = FPDF()
  pdf.add_page()
  pdf.set_font("Courier", size = 12)
  pdf.cell(200, 10, txt = str(event), ln = 1, align = "C")
  pdf.cell(200, 10, txt = "____________________________________", ln = 2, align = "C")
  pdf.cell(200, 10, txt = " ", ln = 3, align = "C")
  pdf.cell(200, 10, txt = " Date: " + str(date.strftime("%m/%d/%Y")), ln = 4, align = "C")
  pdf.cell(200, 10, txt = " Show Time: " + '20' + ':' + '00' + ':' + '00', ln = 5, align = "C")
  pdf.cell(200, 10, txt = " Venue: Jelkyl Drama Center", ln = 6, align = "C")
  pdf.cell(200, 10, txt = " Name: " + str(customername), ln = 7, align = "C")
  pdf.cell(200, 10, txt = " Ticket ID: " + str(bar_num), ln = 8, align = "C")
  pdf.cell(200, 10, txt = " ", ln = 9, align = "C")
  pdf.image("ean13_barcode.png", x = 85, y = 90, w = 50)
  pdf.cell(200, 10, txt = " ", ln = 10, align = "C")
  pdf.cell(200, 10, txt = " ", ln = 10, align = "C")
  pdf.cell(200, 10, txt = "_____________________________________", ln = 11, align = "C")
  pdf.cell(200, 10, txt = " ", ln = 12, align = "C")
  tic = pdf.output("ticket" + str(i) + ".pdf")

  # file_pdf = tic
  #
  # images = convert_from_path('ticket.pdf')
  # for image in images:
  #   image.save('ticket.jpg', 'JPEG')


def print_tix():
  """Print ticket from connected printer"""
  afta = input("Kindly hit 'P' to print your show ticket or press 'M' to go back to the Main Menu...")
  print("M - to return to Main Menu")

  if (afta == "P"):
    # code to send ticket to printer
    pass
  else:
    mainmenu()


def mainmenu():
  """Give user ticket menu"""
  print(" ")
  print(" ")
  print("TICKET PURCHASING MODULE")
  print("B - to purchase ticket for Berea Student")
  print("S - to purchase ticket for Season")
  print("G - to purchase ticket for General")
  print("SN - to purchase ticket for Senior")
  print("ST - to purchase ticket for Other Student")
  print("CH - to purchase ticket for Child")
  print("C - to purchase ticket for Complimentary")
  print("GR - to purchase ticket for Group")
  print(" ")


def options():
  """Give user ticket options"""
  opt = input("Please enter your classification code to continue : ")

  return opt

  get_number_of_tickets()


def generate_barcode():
  try:
      data = pd.read_csv("ticket.csv")
      bar_list = list(data["ID"])
      # print(bar_list)
  except:
      print("didnt work")
      bar_list = []
  # print(bar_list)
  if not bar_list:
      bar_num = str(random.randint(100000000000,999999999999))
      bar_list.append(bar_num)
  else:
      bar_num = str(random.randint(100000000000,999999999999))
      while bar_num in bar_list:
          bar_num = str(random.randint(100000000000,999999999999))
      bar_list.append(bar_num)
  print(bar_num)
  EAN = barcode.get_barcode_class('ean13')
  ean = EAN(str(bar_num), writer=ImageWriter())
  bar_code = ean.save('ean13_barcode')
  return bar_num, bar_code


def main():
  """Starts the ticketing program"""
  customername, event = get_cust_name()
  num_tickets = get_number_of_tickets()
  for i in range(num_tickets):
      mainmenu()
      opt = options()
      amount_lis = []
      ticket_amt = get_ticket_amount(opt)
      amount_list.append(ticket_amt)
      # gather(ticket_amt, amount_list)
      if not os.path.isfile('ticket.csv'):
          create_csv()
      ranum = samp_num()
      bar_num, barcode = generate_barcode()
      make_tix(customername, bar_num, barcode, event, i)
      enter_csv(customername, opt, ticket_amt, bar_num)
  print("Your ticket(s) are printing now.")

if __name__ == '__main__':
  main()
