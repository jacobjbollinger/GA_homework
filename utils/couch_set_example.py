import json
import urllib2
import base64
import os
import couchdbkit

# connect to cloudant
server = couchdbkit.Server('https://ga1:ga1@ga1.cloudant.com')
db = server.get_or_create_db('movie')

# save a document
db.save_doc({
    'author': 'Mike Broberg',
    'content': "In my younger and more vulnerable years, my father told me, 'Son, turn that racket down.'"
})

data = json.loads(open('data/movie_dict.json').read())
for d in data:
    print 'saving %s, %s...' % (d,data[d])
    key = 'movie_'+d
    #db.save_doc({'movie_index':d,'movie_title':data[d]})
    db[key]={'movie_index':d,'movie_title':data[d]}
print 'done!'
