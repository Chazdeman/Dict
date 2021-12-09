from module1 import*
from keyboard import *

coun=loe_failist_listisse("country.txt")
linn=loe_failist_listisse("linnad.txt")
Sonastik={} #Создал словарь с помощью литерала

while 1:

    if read_key()=="3":
        vastus=otsing_nimi_jargi(coun,linn)
        print(vastus)