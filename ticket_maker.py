import datetime
import csv
import random


def get_cust_name():
  """Get name from user"""
  cust_name = None
  while cust_name is None:
      try:
        cust_name = str(input('Please enter your name.\n'))
      except ValueError:
        print ("Invalid entry; please enter a valid name.")
  return cust_name

customername = get_cust_name()


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

  get_ticket_amount()

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
  csvData = ['Name', 'Classification', 'Price']

  with open('ticket.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(csvData)

  csvFile.close()

def enter_csv():
  """Populate CSV file with information"""
  with open('ticket.csv', 'a') as csvAdd:
    writer = csv.writer(csvAdd)
    writer.writerow(row)

  csvFile.close()

def samp_num():
  """Generate random ticket numer"""
  ranum = random.randint(1,1001)*7
  return ranum

date = str(datetime.date.today())


def make_tix():
  """Print ticket details"""
  print("KINETIC EXPRESSIONS")
  print("____________________________________")
  print(" ")
  print("             Date: ",time.strftime("%d/%m/%Y"))
  print("             Time: ",time.strftime("%I:%M:%S"))
  print("             Venue: Jelkyl Drama Center")
  print(" Name            : ", name)
  print(" Ticket ID       : ", ranum)
  print(" ")
  print("_____________________________________")
  print(" ")

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

  options()


def options():
  """Give user ticket options"""
  opt = input("Enter your option : ")
  if (opt == "B" or "CH"):
    num_tickets = 1
  else:
    num_tickets = 0
  return num_tickets, opt

  get_number_of_tickets()
    

def main():
  """Starts the ticketing program"""
  mainmenu()

if __name__ == '__main__':
  main()