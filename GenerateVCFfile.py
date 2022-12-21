import xlrd
import pandas as pd
import os

#file=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop','Vcard','Contacts.xlsx') #If your excel file not in same directory with python file u can use it 
file= 'FlatsDataset.xlsx' #If your excel file in same directory with python file u can use it 
excelfile= pd.ExcelFile(file)
# print(excelfile)

column = excelfile.parse('Bangalore ')
s = ""
begin = "BEGIN:VCARD\nVERSION:2.1"

# print(column["Phone"])
cnt = 0
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

        #s+=begin+"\nN:;"+str(column["Name"][i]).split(".")[0]+";;;\nFN:"+str(column["Surname"][i]).split(".")[0]+"\nTEL;CELL:+"+str(column["Phone"][i]).split(".")[0]+"\nEND:VCARD\n"
        fNumber = str(int(float(fNumber)))
        secN="\nN:"+ "Broker " + fNumber + " " +  fName
        secFN="\nFN:" + "Broker " + fNumber + " " +  fName
        secPhone="\nTEL;CELL:"+str(column["Phone"][i]).split(".")[0]
        # if("Mail" in column.columns.values):
        #     secMail=""
        #     if(str(column["Mail"][i]) != "nan"):
        #         secMail="\nEMAIL;HOME:"+str(column["Mail"][i])
        s+=begin+secN + secFN +secPhone + secMail +"\nEND:VCARD\n"
        cnt = cnt+1
        # print(fNumber)
print(cnt)
# text_file = open("Exported.vcf", "w")
# text_file.write(s)
# text_file.close()
# print("Completed!")
