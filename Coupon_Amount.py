import PyPDF2 
import re

pdfFileObj = open('documents/CA136375CR16.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

#print(pdfReader.numPages)
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i) 
    pageDetails=pageObj.extractText()
    # if "amount" in pageDetails:
    #     count=count+1
    # if "Coupon" in pageDetails:
    #     print(2)
    pageDetails.replace(" ","").strip()
    #print(pageDetails.strip())
# print(count)
#txt = "The rain in Spain"
    reSearchCoupon = re.search("Coupon.*", pageDetails)
    if(reSearchCoupon):
        startPos = reSearchCoupon.span()[1]
        #print("hello")
        # print(t)
        couponStr = pageDetails[reSearchCoupon.span()[1]:reSearchCoupon.span()[1] + 10].strip()
        print(couponStr)
        # couponPos = couponStr.find(":")
        # print(couponPos)
        # print(couponPos.start())
        # print(pageDetails[couponPos + startPos:startPos +10].strip())
        # couponStr = pageDetails[reSearchCoupon.span()[1]:reSearchCoupon.span()[1] + 15].strip()
        #print(x.span()[1])
        #print(couponStr)
    reSearchAmount = re.search("Amount.*", pageDetails)
    #print(x)
    if (reSearchAmount):
        startPos=reSearchAmount.span()[1]
        # print(t)
        amountStr=pageDetails[reSearchAmount.span()[1]:reSearchAmount.span()[1] + 20].strip()
        amountPos=amountStr.find("$")
        print(pageDetails[amountPos+startPos:startPos + 20])
pdfFileObj.close() 
