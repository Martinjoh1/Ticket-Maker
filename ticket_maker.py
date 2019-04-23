import datetime
import csv
import random
import barcode
import random
from fpdf import FPDF
from barcode.writer import ImageWriter


def get_cust_name():
  """Get name from user"""
  cust_name = None
  while cust_name is None:
      try:
        cust_name = str(input('Please enter your name.\n'))
      except ValueError:
        print ("Invalid entry; please enter a valid name.")
  return cust_name

#customername = get_cust_name()


def get_number_of_tickets(num_tickets):
  """Get number of tickets to enter from user"""
  if num_tickets == 1:
    price = 0
  while num_tickets == 0:
      try:
        price = int(input('How many tickets do you want to get?\n'))
      except:
        print ("Invalid entry for number of tickets.")
  return price

  #get_ticket_amount()

# num_tickets = get_number_of_tickets()


def get_ticket_amount(price, opt):
  """Get the ticket amounts from user"""
  if (opt == "B" or "CH"):
    ticket_amt = price
  else:
    ticket_amt = 10 * price
  return ticket_amt


def gather(ticket_amt, price):
  for ticket in range(0, price):
    user_tickets = []
    ticket_amount = ticket_amt
    # add to list once we know we have valid inputs
    user_tickets.append(ticket_amount)
    print ("Ticket {0} added with amount {1}".format(ticket+1, ticket_amount))
    print (user_tickets)


def create_csv():
  """Make CSV file with appropriate headers"""
  csvData = ['Name', 'Classification', 'Price', 'ID']

  with open('ticket.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(csvData)

  csvFile.close()

def enter_csv():
  """Populate CSV file with information"""
  with open('ticket.csv', 'a') as csvAdd:
    writer = csv.writer(csvAdd)
    #writer.writerow(row)

  csvAdd.close()

def samp_num():
  """Generate random ticket numer"""
  ranum = random.randint(1,1001)*7
  return ranum

date = datetime.date.today()


def make_tix(customername, bar_num, barcode):
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
  pdf.set_font("Arial", size=12)
  pdf.cell(200, 10, txt="KINETIC EXPRESSIONS", ln=1, align="C")
  pdf.cell(200, 10, txt="____________________________________", ln=2, align="C")
  pdf.cell(200, 10, txt=" ", ln=3, align="C")
  pdf.cell(200, 10, txt=" Date: " + str(date.strftime("%d/%m/%Y")), ln=4, align="C")
  pdf.cell(200, 10, txt=" Time: " + str(date.strftime("%I:%M:%S")), ln=5, align="C")
  pdf.cell(200, 10, txt=" Venue: Jelkyl Drama Center", ln=6, align="C")
  pdf.cell(200, 10, txt=" Name: " + str(customername), ln=7, align="C")
  pdf.cell(200, 10, txt=" Ticket ID: " + str(bar_num), ln=8, align="C")
  pdf.cell(200, 10, txt=" ", ln=9, align="C")
  pdf.image("ean13_barcode.png", x=85, y=90, w=50)
  pdf.cell(200, 10, txt=" ", ln=10, align="C")
  pdf.cell(200, 10, txt=" ", ln=10, align="C")
  pdf.cell(200, 10, txt="_____________________________________", ln=11, align="C")
  pdf.cell(200, 10, txt=" ", ln=12, align="C")
  pdf.output("ticket.pdf")

  print_tix()


def print_tix():
  """Print ticket from connected printer"""
  afta = input("Kindly hit 'P' to print your show ticket or press 'M' to go back to the Main Menu...")
  if (afta == "P"):
    # code to send ticket to printer
    pass
  elif (afta == "M"):
    mainmenu()
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
  print("M - to return to Main Menu")
  print(" ")

  #options()


def options():
  """Give user ticket options"""
  opt = input("Enter your option : ")
  if (opt == "B" or "CH"):
    num_tickets = 1
  else:
    num_tickets = 0
  return num_tickets, opt

  get_number_of_tickets()

def generate_barcode():
  bar_list= []
  if not bar_list:
      bar_num = random.randint(100000000000,999999999999)
      bar_list.append(bar_num)
  else:
      while bar_num in bar_list:
          bar_num = random.randint(100000000000,999999999999)
      bar_list.append(bar_num)
  EAN = barcode.get_barcode_class('ean13')
  ean = EAN(str(bar_num), writer=ImageWriter())
  bar_code = ean.save('ean13_barcode')
  return bar_num, bar_code


def main():
  """Starts the ticketing program"""
  customername = get_cust_name()
  mainmenu()
  num_tickets, opt = options()
  price = get_number_of_tickets(num_tickets)
  ticket_amt = get_ticket_amount(price, opt)
  gather(ticket_amt, price)
  create_csv()
  enter_csv()
  ranum = samp_num()
  bar_num, barcode = generate_barcode()
  make_tix(customername, bar_num, barcode)




if __name__ == '__main__':
  main()
