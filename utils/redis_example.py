import json
import time
import redis

data = json.loads(open('data/movie_dict.json').read())
#time_out = 60*1000
r = redis.StrictRedis()

for d in data:
    key  = 'movie_test'+d
    r.set(key,data[d])
    start = time.time()
    tmp=r.get(key)
    print tmp
    end = time.time()
    total = end-start
    print 'retrieved document %s in %s seconds' % (d,total)
    


