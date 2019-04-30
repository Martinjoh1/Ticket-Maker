# P02: Ticket Tracker 


**Author(s)**: John Martin, Aaron Christson, Lakshiya Indreswaran, and Rofy Ray

*Google Document*: https://docs.google.com/document/d/1V5N-4NouEUfvDezkXH5lArIH8y42cbMOIZle4GVud_w/edit?usp=sharing
---
## Purpose

The Theater department has been keeping track of their tickets by hand for a very long time. We know that this is mostly inefficient, and and can lead to a lot of inaccuracy. This was confirmed by the department chair when she asked if something could be done about the situation currently at hand. As a result, we are seeking to build an embedded system that will help them record ticket trends, as well as create tickets electronically, which they can then print physically. 

## Initial Design Plan

The initial plan is to be able to write a python script that the Raspberry Pi can execute. The script will provide the user with a menu that will allow them to purchase a ticket based on their status as well as the number of total tickets they need. The status of the customer or user determines the price of the ticket and also allows the theater department to keep records of the ticket classification and trends. After the necessary information is collected through the options provided in the script, they are then put together to make an electronic ticket. The electronic ticket is then saved and printed into an actual ticket.


### Hardware Design
- List the hardware components you'll be using, and how they interact. 

* Inateck Barcode Scanner: scans the unique barcode generated on the physical ticket to check if ticket is valid
* Brother QL-700 Label Printer: prints the physical ticket when ready
* Raspberry Pi: acts as the central sytem to which the scanner and printer will be hooked. this also executes the ticket program

![Ticket_Program_Diagram](images/The (1).png "A sample image. This is the text that appears.")
![Ticket_Program_Diagram](images/The (2).jpg "A sample image. This is the text that appears.")
![Ticket_Program_Diagram](images/The (3).jpg "A sample image. This is the text that appears.")
![Ticket_Program_Diagram](images/The (4).jpg "A sample image. This is the text that appears.")

### Software Design
- List all of the classes and functions you'll be creating.
  - Your program must follow good coding standards. 
  Primarily, I mean your code should include meaningful functions 
  and appropriate variables, and be formatted and commented well. 
  - If your programming language supports classes use them. *Classes are expected* to be well-designed and used throughout, if possible.
  - Sloppy code with no structure will be penalized. 

This is an excellent place for a CRC card or two.

### Data Design  

  The device will save data that are being input by the users. This data will then be used to generate the ticket. Name of the customer who is buying the ticket and  the classification they belong to are the inputs that we get from the user. We also have Identification number that is generated by the system for each ticket. These ID numbers are used to generate a bar code when the ticket is scanned. The Ticket ID will be saved in an excel file. The data is saved whenever a customer buys a ticket and the whenever the ticket is being scanned.
   

### Additional Requirement
- Project 3 requires an additional requirement. Describe what additional component you will take on here. 
Thoroughness is encouraged! Explain how your addition moves the project closer to "final product". 
Pictures always help, too.

## Delegation of Tasks

- John Martin: Will work on getting card scanner to create ticket 

- Rofy Ray: Will work on making card scanner to send the ticket 

- Aaron Christson: will work on finding trends in ticket collection based on needs of the department

- Lakshiya Indreswaran: Will work on infrared implementation for counting tickets

## Files

ticket_maker.py : It contains the main code for creating the ticket with bar code

Barcode_test.py :  Initial code for creating barcode

Qrcode_test.py : Code for creating a QR code


## Instructions
- user will need to install VNC on their computer 
- user will need a mouse, keyboard, ethernet cord and a screen, and follow the instructions on this website https://www.raspberrypi.org/documentation/remote-access/vnc/
- user then needs to run the program 
- Scan ticket 

## Errors and Constraints
- Printing: 
  
  - Printing the ticket using a printer was the difficult part.  We have had problem in using the rapberry pi to print the documents. We were able to intsall CUPS library but for the Lexmark printer it gave an error message "Printer is not responding" and for brother QL700, it showed the printing job is completed but it did not print anything. We tried to use brother QL ppd directly to print the ticket and we were able to print via brother QL printer using raspberry Pi but the only problem was the library allows us to only print images in png format. The ticket we have created is in PDF. Thus it does not allow us to print the ticket. We tried different ways to convert pdf to image but it was harder than we thought. The libraries were complicated and we still have issues in converting pdf to image. Our solution to this problem is to print through VNC server installed in the laptop. 

- We could not make the GUI for the user to easily input the ticket information



## References

- https://www.youtube.com/watch?v=9FxlQXuXxFU : how to get card scanner to work with actual cards 

- https://www.raspberrypi.org/forums/viewtopic.php?t=69286 : how to send txt sms on Raspberry pi

- https://raspberry-projects.com/pi/software_utilities/email/ssmtp-to-send-emails : how to send email with Raspberry pi 

- https://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup/finding-your-pis-ip-address : helps us to find the pi's IP 

- https://www.raspberrypi.org/forums/viewtopic.php?t=180370 : shows how to print using CUPS

## Summary and Reflection
  I think we have done a good job in creating a tiket for the theatre department. We created a unique ticket and are able to print it. This project showed us all that we should be prepared for anything. It takes a lot of asking the department what they were looking for in the embedded system, and narrowing our idea down to something manageable. It also took discussing what each individual had learned, and how to apply it to the project. 
  We had gotten the Ql-700 printer to work at one point, but then, the SD card with of the pi it was working on gained a problem. In order to fix this we decided to print from the vnc using CUPS. The great thing is that we are able to make a ticket that can then 

We have created a ticket with bar code. Ticket will have th name of the person who bought the ticket and the bar code. once the bar code is scanned, the program will check whether or not the ticket is valid. everytime a ticket is scanned, it will be saved in a csv file and it will help them to find out how many people have attended the event. 


Write 3 - 5 paragraphs on your reactions to the final project. 
Your reflection should be thoughtful and reflective. 
First, report on what you did. Then, reflect on those actions. 
It's a look back at what you learned by doing this project, but good and bad. 
You should be critical of shortcomings (yours, as well as the instructors/assignments) 
as well as celebratory of what was achieved.

## Final Self-Evaluations

### Ideation, Brainstorming, Design:

*Aaron Christson: 0-10*

*Raymond Okyere-Forson: 0-10*

*Lakshiya Indreswaran: 0-10*

*John Martin: 0-10*

### Physical wiring/construction: 

*Aaron Christson: 0-10*

*Raymond Okyere-Forson: 0-10*

*Lakshiya Indreswaran: 0-10*

*John Martin: 0-10*

### Code creation/debugging/integration: 

*Aaron Christson: 0-10*

*Raymond Okyere-Forson: 0-10*

*Lakshiya Indreswaran: 0-10*

*John Martin: 0-10*

### Documentation:



### Leadership, Teamwork, & Participation:

*Aaron Christson: 0-10*

*Raymond Okyere-Forson: 0-10*

*Lakshiya Indreswaran: 0-10*

*John Martin: 0-10*

---

