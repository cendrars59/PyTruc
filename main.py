
#-*-coding:Latin-1 -*

""" Training for Dico """

MY_CALENDAR = {
    "2019" : {
        "beg_date" : "toto",
        "end_date" : ""
    },
    "2018" : {
        "beg_date" : "2017-07-21 16:20:00.0000",
        "end_date" : ""
    }, 
    "2017" : {
        "beg_date" : "toto",
        "end_date" : ""
    }
}


import webbrowser
import time
import datetime

def open_link():
    webbrowser.open("http://www.youtube.com")

def main():
    print('Hello world')
    # Creation dico 
    mondic = {}
    # Creation clé et assignation valeur 
    mondic["cle1"] = "key1"
    print(mondic["cle1"])
    # suppression clé
    del mondic["cle1"]
    print(mondic)

    dic2 = {
        "cle1" : "value1",
        "cle2" : "value2"
    }

    for cle, value in dic2.items():
        print(cle,value)

    print(dic2)


    dic3 = {
        "cle1" : ["l1","l2"],
        "cle2" : "value2"
    }

    for cle, value in dic3.items():
        print(cle,value)

    for value in dic3["cle1"]:
        print("this is the value {0}".format(value[:1]))

    print(dic2)
    count = 3 
    i = 0 
    print(MY_CALENDAR)
    current_date = datetime.datetime.now()
    print(type(current_date))
    #conv1 = datetime.datetime.strptime(current_date, "%Y-%m-%d %H:%M:%S.%f")
    next_year = current_date.year + 1
    print(next_year)
    beg_periode = MY_CALENDAR[str(next_year)]["beg_date"]
    converted = datetime.datetime.strptime(beg_periode, "%Y-%m-%d %H:%M:%S.%f")
    print(type(converted))
    difference = (converted - current_date).total_seconds()
    time.sleep(difference)
    print(difference)
    

    

main()