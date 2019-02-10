import codecs
#open it with utf-8 encoding 
f=codecs.open("soapUI.key","r",encoding='utf-8',errors='ignore')
#read the file to unicode string
sfile=f.read()

#check the encoding type
print type(file) #it's unicode

#unicode should be encoded to standard string to display it properly
print sfile.encode('utf-8')
#check the type of encoded string

print type(sfile.encode('utf-8'))