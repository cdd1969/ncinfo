import urllib2
import json

url = 'http://api.twitter.com/1/trends/44418.json'

# download the json string
json_string = '{"errors":[{"message":"SSL is required","code":92}]}'


# de-serialize the string so that we can work with it
the_data = json.loads(json_string)

# get the list of trends
print the_data
for k, v in the_data.iteritems():
    print k, v