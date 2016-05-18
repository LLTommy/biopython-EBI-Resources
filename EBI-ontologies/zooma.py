#Just an idea how to structure the code - here we could add the zooma webservice call stuff
import urllib
import json

baseURL="http://www.ebi.ac.uk/spot/zooma/v2/api"

class annotation:
    def __init__(self,confidence, uri, propertyValue, weblink):
        self.confidence=confidence
        self.uri=uri
        self.propertyValue=propertyValue
        self.weblink=weblink

def callZooma(searchurl):
    try:
        request=searchurl
        reply = urllib.urlopen(request)
        anwser = json.load(reply)
        return anwser
    except:
        raise LookupError('Failed to reach the Endpoint, Service is down or wrong url!')


def predictAnnotation(value):
    url=baseURL+"/services/annotate?propertyValue="
    url=url+value
    anwser=callZooma(url)
    return anwser

def parseAnnotation(annotationTerm):
    confidence=annotationTerm[0]["confidence"]
    if (annotationTerm[0]["annotatedProperty"]["uri"]!=None):
        uri=annotationTerm[0]["annotatedProperty"]["uri"]
    else:
        uri="Not available"
    propertyValue=annotationTerm[0]["annotatedProperty"]["propertyValue"]
    weblink=baseURL+"/services/annotate?propertyValue="+propertyValue
    return annotation(confidence, uri, propertyValue, weblink)

def showAnnotation(annotationTerm):
    print("------------------------------------------")
    print("confidence: "+annotationTerm.confidence)
    print("uri: "+annotationTerm.uri)
    print("propertyValue: "+annotationTerm.propertyValue)
    print("weblink: "+annotationTerm.weblink)
    print("------------------------------------------")

showAnnotation(parseAnnotation(predictAnnotation("mus+musculus")))
