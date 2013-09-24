import json
import urllib
import os
import time

dir_out = 'yahoo_data_in_class'

if not os.path.exists(dir_out):
    os.mkdir(dir_out)
    print 'created directory %s' % dir_out

symbols = ['FB']
tmp =[]

for symbol in symbols:
    time.sleep(.5)
    data_out = {}
    try:
        if 'less than 15' not in data_out:
            data_out['less than 15']=0
        if 'more than 15' not in data_out:
            data_out['more than 15']=0
        url = 'http://ichart.finance.yahoo.com/table.csv?s=%s&d=6&e=24&f=2013&g=d&a=4&b=18&c=2012&ignore=.csv' % (symbol)
        data = urllib.urlopen(url).read()
        print data
        file = '%s/%s_data.csv' % (dir_out, symbol)
        print 'savingfile %s' % file
        f = open(file,'w')
        f.write('%s' % str(data))
        f.close()
        data = data.split('\n')
        for d in data[1:-1]:
            try:
                d = d.split(',')
                close = d[6]
                tmp.append(close)
                if float(close)>=float(15):
                    data_out['more than 15']+=1
                elif float(close)<float(15):
                    data_out['less than 15']+=1
            except:pass
    except:pass
    print json.dumps(data_out)

