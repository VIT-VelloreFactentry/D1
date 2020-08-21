import PyPDF2 
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

filename = 'Documents/US17275RBD35.pdf' 
#open allows you to read the file
pdfFileObj = open(filename,'rb')
#The pdfReader variable is a readable object that will be parsed
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#discerning the number of pages will allow us to parse through all #the pages
num_pages = pdfReader.numPages
count = 0
text = ""
#The while loop will read each page
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
#This if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.
if text != "":
   text = text
#If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text
else:
   text = textract.process(fileurl, method='tesseract', language='eng')
text=text.lower()
# Now we have a text variable which contains all the text derived #from our PDF file. Type print(text) to see what it contains. It #likely contains a lot of spaces, possibly junk such as '\n' etc.
# Now, we will clean our text variable, and return it as a list of keywords.

#The word_tokenize() function will break our text phrases into #individual words
tokens = word_tokenize(text)
# print(tokens)
# print(tokens)
#we'll create a new list which contains punctuation we wish to clean
punctuations = ['(',')',';','[',']',',',':']
#We initialize the stopwords variable which is a list of words like #"The", "I", "and", etc. that don't hold much value as keywords
stop_words = stopwords.words('english')
#print(stop_words)
#We create a list comprehension which only returns a list of words #that are NOT IN stop_words and NOT IN punctuations.
keywords = [word for word in tokens if not word in stop_words and not word in punctuations]
# print(keywords)
count=0
index=[]
ind_count=0
words=['principal','amount']
last_index=0
for i in range(len(keywords)):
      if(keywords[i] in words):
         index.append(i)
         # last_index
         # ind_count=ind_count+1
         # print(index)
         # for i in range(index-5,index+5):
               # print(word[i])
# print(index)
print(index)
amount=[]
for ind in index:
   for i in range(ind-10,ind+10):
      pattern = '^-?(?:\d+|\d{1,3}(?:,\d{3})+)(?:(\.|,)\d+)?$'
      # print(keywords[i])
      if(keywords[i+1]=='amount'):
         for j in range(i+2,i+10):
            test_string = keywords[j]
            result = re.match(pattern, test_string)
            if result:
               amount.append(keywords[j])
   # print("-------------------------------------------------------")

print(amount)
# pattern = '^-?(?:\d+|\d{1,3}(?:,\d{3})+)(?:(\.|,)\d+)?$'
# result=re.match(pattern,'1,000')
# if result:
#        print("Success")
   
# for i in range(584,604):
#    print(keywords[i])
# print(len(keywords))
# print(keywords[125])