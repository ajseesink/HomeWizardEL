# This Python Script uses Python 3.7
# Author: Andre Seesink
# Version 1.0 - date 15-02-2019 initial release
# Version 1.1 - date 16-02-2019 time format changed
#                               date format changed
#
# http:// <Homewizard-ip-adres>/<Homewizard-password>
# Read Meter: "/el/get/0/readings"
#
# fill in the url and Password variable. 

import json
import http.client
import datetime

ExportString = ""
url = "<fill in your ip>"
Password = "<fill in your password>"
command = "/el/get/0/readings"
TijdStip = datetime.datetime.now()
tijd = TijdStip.strftime("%H:%M")
datum = TijdStip.strftime("%d-%m-%y")

connection = http.client.HTTPConnection(url)
connection.request("GET", "/" + Password  + command)
response = connection.getresponse()
connection.close()

#print("Status pagina oproepen Energie Link: ", response.status, response.reason, "\n")
#print(data)
data = json.loads(response.read())
AantalRecords = len(data['response'])


def Electricity():
    #print("Electriciteit")
    ELtariff = data["response"] [a] ['tariff']
    ELconsumed = data["response"] [a] ["consumed"]
    ELproduced = data["response"] [a] ['produced']

    if ELtariff == 1:
        #print("Laag tarief: ",ELtariff)
        #print("Verbruikt: ", ELconsumed) 
        #print("Geproduceerd: ",ELproduced)
        return ELconsumed
    if ELtariff == 2:
        #print("Hoog tarief: ",ELtariff)
        #print("Verbruikt: ", ELconsumed) 
        #print("Geproduceerd: ",ELproduced)
        return ELconsumed

def Gas():
    #print("Gas")
    ELconsumed = data["response"] [a] ["consumed"]
    ELtimestamp = data["response"] [a] ['timestamp']
    #print("Verbruikt: ", ELconsumed) 
    #print("Tijd: ",ELtimestamp)
    return ELconsumed

a=0
while a < AantalRecords:
    ELtype = data["response"] [a] ["type"]
    
    if ELtype == 'electricity':
        ExportString = ExportString + str(Electricity()) + ","
    if ELtype == 'gas':
        ExportString = ExportString + str(Gas())
    a=a+1

ExportString = datum + "," + tijd + "," + ExportString
print(ExportString)
    
    

    
    

