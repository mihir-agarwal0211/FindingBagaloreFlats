import pandas as pd
import pywhatkit
import time


Number = ["+91123456789","+91123456789"]
file= 'FlatsDataset.xlsx'
excelfile= pd.ExcelFile(file)
column = excelfile.parse('Bangalore ')
s = ""
for i in range(len(column)):
    fNumber = 0
    fName=""
    sName=""
    secMail=""

    if(str(column["Phone"][i])!="nan"):
        if(str(column["S.no."][i])!="nan"):
            fNumber=str(column["S.no."][i])
        if(str(column["Name"][i])!="nan"):
            fName=str(column["Name"][i])

        
        secPhone=str(column["Phone"][i]).split(".")[0]
        # print(secPhone)
        phn = "+91" + secPhone
        # print(phn)
        Number.append(phn)

print(len(Number))
s = "Hi, Mihir here\nI got your number from a friend\nI am looking for 2/3 bhk in bellandur/kadubesanhalli/kasavanahalli/marathalli\nIf you get any flats for rent for bachelors, please call or message me  \nBudget: 40k for 2bhk \n60k for 3bhk"

for i in Number:
    pywhatkit.sendwhatmsg_instantly(i,s)
    time.sleep(3)
