import json
import urllib2
import base64
import os
import time

DoALL = False
DoINDIV = True

limit = 50000
total = 50000
start_key=''

dir_out = '/home/jacob/data/couch_dump'
if not os.path.exists(dir_out):
    os.makedirs(dir_out)

if DoALL:
    print "Beginning..."
    url = 'http://ga1.cloudant.com/movie/_all_docs?include_docs=true&skip=1&limit=%s' % (limit1)
    request = urllib2.Request(url)

    #encode the desired password in base 64 encoding     
    encoded_string = base64.encodestring('%s:%s' % ("ga1", "ga1"))[:-1]
    request.add_header("Authorization", "Basic %s" % encoded_string)
    print "Requesting %s" % url
    document  = []
    document = urllib2.urlopen(request).read()
    print "Loading %s" % url
    data = {}
    data = json.loads(document)

    startkey = data['rows'][-1]['key']
    print "Saving"
    f = open('%s/movie_data_all.json'% (dir_out), 'w+')
    f.write(document)
    f.close()

if DoINDIV:
    data = json.loads(open('data/movie_dict.json').read())
    for d in data:
        try:
            start = time.time()
            url = 'https://ga1.cloudant.com/movie/movie_%s?&format=json' % d
            request = urllib2.Request(url)

            #encode the desired password in base 64 encoding
            encoded_string = base64.encodestring('%s:%s' % ("ga1", "ga1"))[:-1]
            request.add_header("Authorization", "Basic %s" % encoded_string)
            print "Requesting %s" % url
            document  = []
            document = urllib2.urlopen(request).read()
            end = time.time()
            total = end-start
            print 'retrieved document in %s seconds' % total

            data = json.loads(document)
            print data
            print "Saving"
            f = open('%s/movie_data_%s.json'% (dir_out,d), 'w+')
            f.write(document)
            f.close()

        except:
            print 'could not find document for movie %s' % d
