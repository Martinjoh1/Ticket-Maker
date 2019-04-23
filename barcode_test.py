import barcode
import random
from barcode.writer import ImageWriter

def generate_barcode(i):
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
    ean.save('ean13_barcode'+str(i))

for i in range(5):
    generate_barcode(i)
