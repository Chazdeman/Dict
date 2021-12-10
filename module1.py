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

12
21
32
45




























65
45
1
23
123
1

123
312
312
132
3
12
123
132
123
3
12
3
3
12
321
312
