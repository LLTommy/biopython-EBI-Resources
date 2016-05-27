import urllib
import json
import variables


def callService(searchurl, query):
    try:
        request=searchurl+query+"&format=JSON&limit=25&offset=0&inference=false"
        reply = urllib.urlopen(request)
        print(reply)
        anwser = json.load(reply)
        return anwser
    except:
        raise LookupError('Failed to reach the Endpoint, Service is down or wrong url!')


# work in progress
#def parseResult(reply):
#    head=reply["head"]
#    body=reply["bindings"]
#    return head, body



#print(callService(variables.atlas, variables.query))
#print(callService(variables.chembl, variables.chemblQuery))

# Failed to load resource: the server responded with a status of 500 (Internal Server Error)
#print(callService(variables.chembl,"empty&format=JSON&limit=25&offset=0&inference=false"))
