#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      eduar
#
# Created:     13/05/2019
# Copyright:   (c) eduar 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from urllib.request import urlopen

def main():
    pass

if __name__ == '__main__':
    main()

_urls = open(r"C:\Users\eduar\Dropbox\Documents\Python\13052019\links.txt","r")
for _url in _urls.readlines():
    outfile = open(_url.rstrip()+".htm", "wb")
    outurl=urlopen("http://"+_url.rstrip())
    for line in outurl.readlines():
        outfile.write(line)
    outurl.close()
    outfile.close()
