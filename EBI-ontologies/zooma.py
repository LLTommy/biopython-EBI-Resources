#Just an idea how to structure the code - here we could add the zooma webservice call stuff
import urllib
import json

baseURL="http://www.ebi.ac.uk/spot/zooma/v2/api"

class annotation:
    def __init__(self,confidence, uri, propertyValue, weblink, semanticTags, annotatedBiologicalEntities, provenance):
        self.confidence=confidence
        self.uri=uri
        self.propertyValue=propertyValue
        self.weblink=weblink
        self.semanticTags=semanticTags
        self.annotatedBiologicalEntities=annotatedBiologicalEntities
        self.provenance=provenance

def callZooma(searchurl):
    try:
        request=searchurl
        reply = urllib.urlopen(request)
        anwser = json.load(reply)
        return anwser
    except:
        raise LookupError('Failed to reach the Endpoint, Service is down or wrong url!')

def searchForValue(value):
    if (type(value) is str):
        url=baseURL+"/services/annotate?propertyValue="
        url=url+value
        return callZooma(url)
    else:
        raise TypeError('Parameter must be of type string')

def searchForValueAndType(value, propertyType):
    if ((type(value) is str) and (type(propertyType) is str)):
        url=baseURL+"/services/annotate?propertyValue="
        url=url+value+"&propertyType="+propertyType
        return callZooma(url)
    else:
        raise TypeError('Parameters must be of type string')

def searchForValueAndTypeInDatasource(value, propertyType, datasource):
    if ((type(value) is str) and (type(propertyType) is str) and (type(datasource) is list)):
        url=baseURL+"/services/annotate?propertyValue="
        url=url+value+"&propertyType="+propertyType+"&filter=required:["

        for source in datasource:
            url=url+source+","

        url =url[:-1]
        url=url+"]"
        return callZooma(url)
    else:
        raise TypeError('Parameters must be of type: string, string, list')

def parseAnnotation(annotationTerm):
    if (type(annotationTerm) is list):
        confidence=annotationTerm[0]["confidence"]

        if (annotationTerm[0]["annotatedProperty"]["uri"]!=None):
            uri=annotationTerm[0]["annotatedProperty"]["uri"]
        else:
            uri="Not available"

        propertyValue=annotationTerm[0]["annotatedProperty"]["propertyValue"]
        weblink=baseURL+"/services/annotate?propertyValue="+propertyValue
        annotatedProperty=annotationTerm[0]["derivedFrom"]["annotatedProperty"]
        semanticTags=annotationTerm[0]["derivedFrom"]["semanticTags"]
        annotatedBiologicalEntities=annotationTerm[0]["derivedFrom"]["annotatedBiologicalEntities"]
        provenance=annotationTerm[0]["derivedFrom"]["provenance"]
        return annotation(confidence, uri, propertyValue, weblink, semanticTags, annotatedBiologicalEntities, provenance)
    else:
        raise TypeError('Input value is not of type list!')

def showAnnotation(annotationTerm):
    if (isinstance(annotationTerm, annotation)):
        print("------------------------------------------")
        print("confidence: "+annotationTerm.confidence)
        print("uri: "+annotationTerm.uri)
        print("propertyValue: "+annotationTerm.propertyValue)
        print("weblink: "+annotationTerm.weblink)
        print("-")
        print("semanticTags:")
        print(annotationTerm.semanticTags)
        print("-")
        print("annotatedBiologicalEntities: ")
        print(annotationTerm.annotatedBiologicalEntities)
        print("-")
        print("provenance: ")
        print(annotationTerm.provenance)
        print("------------------------------------------")
    else:
        raise TypeError('Input value is not of type annotation!')


#showAnnotation(parseAnnotation(predictAnnotation("mus+musculus")))
#showAnnotation(parseAnnotation(searchForValue("homo+sapiens")))
searchForValueAndTypeInDatasource("homo+sapiens", "organism", ["efo"])
searchForValueAndTypeInDatasource("homo+sapiens", "organism", ["efo,atlas"])
