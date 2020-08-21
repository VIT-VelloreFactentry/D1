import PyPDF2 
import re

pdfFileObj = open('Documents/CA136375CR16.pdf', 'rb') 

pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

#print(pdfReader.numPages) 
count=0
count1=0
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i) 
    pageDetails=pageObj.extractText()
    reSearchAmount = re.findall("\$\d+(?:\.\d+)?", pageDetails)
    #print(x)
    if (reSearchAmount):
        # startPos=reSearchAmount.span()[1]
        # print(t)
        print(reSearchAmount)
        # amountStr=pageDetails[reSearchAmount.span()[1]:reSearchAmount.span()[1] + 20].strip()
        # amountPos=amountStr.find("$")
        # print(pageDetails[amountPos+startPos:startPos + 20])
    reSearchCoupon = re.search("fixed.*", pageDetails)
    if(reSearchCoupon):
       print("Coupon Type:Fixed")
pdfFileObj.close() 
