import urllib2
for url in ["/qcbin/rest/domains/Middleware/projects/SIO_SI_OSR_PORTAL/Defects?Action=FindDefect&DefectID=2"]:
    try:
        connection = urllib2.urlopen(url)
        print connection.getcode()
        connection.close()
    except urllib2.HTTPError, e:
        print e.getcode()