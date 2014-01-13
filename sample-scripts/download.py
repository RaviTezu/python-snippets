#!/usr/bin/python
import re
import urllib2

url = 'http://www.it-ebooks.info/book/'
initial = int(raw_input("Enter the initial number: "))
end = int(raw_input("Enter the ending number: "))
choice = str(raw_input("Would you like to see the book titles along with the urls?[y/N]: "))
for i in xrange(initial,end):
    dyn_url = url + str(i) + '/'
    response = urllib2.urlopen(dyn_url)
    html = response.read()
    id_tmp = re.search('go\.php\?id\=[\d]*\-[\d]*\-.[a-z|0-9]*', html)
    comp_url = 'http://www.it-ebooks.info/' + id_tmp.group(0)
    format = "%-50s %s"
    if choice == "y":
        book_title = re.search('\.text\(\".*\"\)\<\/script\>', html)
        bookurl_tmp = book_title.group(0).strip(".text").strip("<\/script>")
        print format % (bookurl_tmp.strip('()"'), comp_url)
    else:
        print comp_url
    
