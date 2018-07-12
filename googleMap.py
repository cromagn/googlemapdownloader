import csv
import urllib2
import urllib
from lxml import etree

ofile  = open('c://tmp/out.csv', "wb")
writer = csv.writer(ofile, delimiter='|', quotechar='"', quoting=csv.QUOTE_ALL)

with open('c://tmp/comuni_3.csv', 'rb') as csvfile:
    comunireader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in comunireader:
        url = 'https://maps.googleapis.com/maps/api/place/textsearch/xml'
        values = {'key' : 'xxxxxxxxxx','query' : 'restaurant '+ row[5].decode('utf-8', 'ignore')}
        print row[5].decode('utf-8', 'ignore')
        data = urllib.urlencode(values)
        full_url = url + '?' + data
        #print full_url
        res = urllib2.urlopen(full_url)
        xxxml = res.read()
        tree = etree.fromstring(xxxml)
        #reviews = tree.findall(".//name")
        reviews = tree.findall(".//place_id")
        for b in reviews:
            urlDet = 'https://maps.googleapis.com/maps/api/place/details/xml'
            valuesDet = {'key' : 'xxxxxxxxx','fields': 'name,formatted_address,formatted_phone_number','placeid' : b.text}
            dataDet = urllib.urlencode(valuesDet)
            full_url_Det = urlDet + '?' + dataDet
            resDet = urllib2.urlopen(full_url_Det)
            
            xxxmlDet = resDet.read()
            try:
                treeDet = etree.fromstring(xxxmlDet)
                detName = treeDet.find(".//name")
                detAddress = treeDet.find(".//formatted_address")
                detPhone = treeDet.find(".//formatted_phone_number")
                writer.writerow([detName.text.encode('utf-8'), detAddress.text.encode('utf-8'), detPhone.text.encode('utf-8')])
                
            except:
                print "Not Found"
writer.close()
ofile.close()         
