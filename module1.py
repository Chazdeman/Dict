from random import *
def loe_failist_listisse(file:str)->list:
    """Loeme tekst failist ja salvesta järjendisse
    :rtype: list:
    """
    file=open(file,"r")
    list_=[]
    for stroka in file:
        list_.append(stroka.strip())
    file.close()
    return list_

def otsing_nimi_jargi(coun,linn)->list:
    """
    """
    a=input("Keda otsime?")
    if a in country or linnad:
       