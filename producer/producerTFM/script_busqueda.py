#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# import the Elasticsearch low-level client library
from elasticsearch import Elasticsearch

# domain name, or server's IP address, goes in the 'hosts' list
elastic_client = Elasticsearch(hosts=["localhost"])

# User makes a request on client side
#request = "378520ca-228182532853"
request = "3782f2b2-007248212921"
# Take the user's parameters and put them into a Python
# dictionary structured like an Elasticsearch query:
query_body = {
  "query": {
    "regexp": {
      "message": {
        "value": ".*" + request + ".*",
      }
    }
  }
}

print(query_body)

# call the client's search() method, and have it return results
result = elastic_client.search(index="registered_user", body=query_body, http_auth=('elastic','changeme'))

# see how many "hits" it returned using the len() function
print ("total hits:", len(result["hits"]["hits"]))


'''
MAKE ANOTHER CALL THAT RETURNS
MORE THAN 10 HITS BY USING THE 'size' PARAM
'''
result = elastic_client.search(index="registered_user", body=query_body, size=999, http_auth=('elastic','changeme'))
all_hits = result['hits']['hits']

# see how many "hits" it returned using the len() function
print ("total hits using 'size' param:", len(result["hits"]["hits"]))

# iterate the nested dictionaries inside the ["hits"]["hits"] list
for num, doc in enumerate(all_hits):
    print ("DOC ID:", doc["_id"], "--->", doc, type(doc), "\n")

    # Use 'iteritems()` instead of 'items()' if using Python 2
    for key, value in doc.items():
        print (key, "-->", value)

    # print a few spaces between each doc for readability
    print ("\n\n")