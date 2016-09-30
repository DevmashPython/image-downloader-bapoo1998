import urllib2
import re

# Input the URL
print "Enter the website whose image links you want to store:\n\n"
userUrl = "http://"+ raw_input("http://")

# URL & Pattern I/O
a = urllib2.urlopen(userUrl)
htmlContent = a.read()
pattern = re.compile('<img [^>]*src="([^"]*)"[^>]*>')
result = re.findall(pattern, htmlContent)

# Storing in a file
file1 = open("URL List.txt", "w")
file1.write(str(result))
