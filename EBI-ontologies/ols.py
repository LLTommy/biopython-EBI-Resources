import urllib
import json

#The termlist contains terms - for example if a search returns multiple terms they go into the termlist
termlist=[]

#This class represents a term, it contains all (relevant?) term information in OLS
class term:

    def __init__(self, label, ontology, iri, description):
        self.label=label
        self.ontology=ontology
        self.iri=iri
        self.description=description

#Class to save the ontology data
class ontology:
    def __init__(self, title, description, homepage, additional):
        self.title=title
        self.description=description
        self.homepage=homepage
        self.additional=additional


#clean up termlist
def clearTermlist():
    termlist=[]

#generic call to the OLS search API
def callOLSsearch(searchurl, query):
    try:
        request=searchurl+query
        reply = urllib.urlopen(request)
        anwser = json.load(reply)
        return anwser
    except:
        raise LookupError('Failed to reach the Endpoint, Service is down or wrong url!')


def searchForOntology(ontology):
    searchurl="http://www.ebi.ac.uk/ols/api/ontologies/"
    anwser = callOLSsearch(searchurl,ontology)
    return parseOntologyData(anwser)

def parseOntologyData(data):
    try:
        title=data["config"]["title"]
        description=data["config"]["description"]
        homepage=data["config"]["homepage"]
        additional=[data["numberOfTerms"], data["numberOfProperties"], data["numberOfIndividuals"]]
        return ontology(title, description,homepage,additional)
    except:
        raise TypeError('Input Argument has wrong structure')


def showOntology(ontology):
    try:
        print("-----OntologyInformation-----------")
        print("Title: "+ontology.title)
        print("Description: "+ontology.description)
        print("Homepage: "+ontology.homepage)
        #print("# of terms:"+ontology.additional["numberOfTerms"])
        #print("# of properties:"+ontology.additional["numberOfProperties"])
        #print("# of individuals:"+ontology.additional["numberOfIndividuals"])
        print("-----------------------------------")
    except:
        raise TypeError('Could not parse Input argument!')

###########Search for a certain label in all ontologies
def searchForLabel(term):
#Missing: PAGING FOR ALL RESULTS (Right now only results of first page are shown)
    searchurl="http://www.ebi.ac.uk/ols/api/search?q="
    anwser = callOLSsearch(searchurl,term)
    parseLabelRequest(anwser)

#parse the result for a term request
def parseLabelRequest(anwser):
    clearTermlist()
    for counter in anwser["response"]["docs"]:
        if "description" in counter:
            print("{}".join(counter["description"]))
            tmpdescription=counter["description"]
        else:
            print("No description available")
            tmpdescription="No description available"

        print("\n")
        tmpterm=term(counter["label"], counter["ontology_name"],counter["iri"], tmpdescription)
        termlist.append(tmpterm)
#####################



############### Search for a certain IRI/URI in a certain ontology
def searchForIriInOntology(iri, ontology):
    searchurl="http://www.ebi.ac.uk/ols/api/ontologies/"+ontology+"/terms/"
    encodediri=urllib.quote(iri, safe='')
    encodediri=urllib.quote(encodediri, safe='') # double encoded
    request=searchurl+encodediri
    reply = urllib.urlopen(request)
    anwser = json.load(reply)
    if (anwser["status"]==404):
        print("Resource not found!")
        raise LookupError('Resource not found! 404 Error, iri or ontology is wrong!')
    else:
        return parseIriandOntologyRequest(anwser)

#parse the result
def parseIriandOntologyRequest(anwser):
    try:
        tmpterm=term(anwser["label"], anwser["ontology_name"], anwser["iri"], anwser["description"])
        return tmpterm
    except:
        raise TypeError('Input Argument has wrong structure')
#############################################



#Retrieve a term
#/api/ontologies/{ontology}/terms/{iri}

#Retrieve a property
# /api/ontologies/{ontology}/properties/{iri}

#Retrieve a individual
# GET /api/ontologies/{ontology}/individuals/{iri}

# suggest endpoint
# /api/suggest?q={query}



###Show Functions, these print the results to the screen
#Print an term instance to the screen
def showTerm(term):
    try:
        print("Label: "+term.label)
        print("Ontology: "+term.ontology)
        print("Iri: "+term.iri)
        print(term.description)
    except:
        raise AttributeError("Input Argument has wrong structure!")

#Print termlist, better table formats can be found here http://stackoverflow.com/questions/9535954/python-printing-lists-as-tabular-data
def showTermList():
    if (len(termlist) == 0):
        raise ValueError("Termlist is empty")
    else:
        print("Index - Label - "+"Ontology - "+"iri")
        index=0
        for element in termlist:
            print(str(index)+" - "+element.label+" - "+element.ontology+" - "+element.iri)
            index=index+1

#Show a certain term from the termlist by index (of the termlist)
def showTermByIndex(index):
    if (index>len(termlist)):
        raise ValueError('Index is larger than the termlist!')
    if (index<0):
        raise ValueError('Index is below 0, this is not allowed!')
    if (index>0 and index<len(termlist)):
        showTerm(termlist[index])

#Show a certain term from the termlist, select by iri
def showTermByIri(iri):
    index=0
    foundFlag=False
    for term in termlist:
        if (term.iri==iri):
            showTermByIndex(index)
            foundFlag=True
            break
        index=index+1

    if (foundFlag==False):
        raise NameError('iri not found it termlist')



#Only for development I call functions here sometimes
