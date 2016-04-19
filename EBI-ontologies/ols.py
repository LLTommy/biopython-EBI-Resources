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
    searchurl="http://www.ebi.ac.uk/ols/beta/api/ontologies/"
    anwser = callOLSsearch(searchurl,ontology)
    parseOntoloyData(anwser)

def parseOntoloyData(data):
    try:
        title=data["config"]["title"]
        description=data["config"]["description"]
        homepage=data["config"]["homepage"]
        additional=[data["numberOfTerms"], data["numberOfProperties"], data["numberOfIndividuals"]]
        return ontology(title, description,homepage,additional)
    except:
        raise TypeError('Input Argument has wrong structure')



###########Search for a certain label in all ontologies
def searchforlabel(term):
#Missing: PAGING FOR ALL RESULTS (Right now only results of first page are shown)
    searchurl="http://www.ebi.ac.uk/ols/beta/api/search?q="
    anwser = callOLSsearch(searchurl,term)
    parseLabelRequest(anwser)

#parse the result for a term request
def parseLabelRequest(anwser):
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
    searchurl="http://www.ebi.ac.uk/ols/beta/api/ontologies/"+ontology+"/terms/"
    encodediri=urllib.quote(iri, safe='')
    encodediri=urllib.quote(encodediri, safe='') # double encoded
    request=searchurl+encodediri
    reply = urllib.urlopen(request)
    anwser = json.load(reply)
    return parseIriandOntologyRequest(anwser)

#parse the result
def parseIriandOntologyRequest(anwser):
    try:
        tmpterm=term(anwser["label"], anwser["ontology_name"], anwser["iri"], anwser["description"])
        return tmpterm
    except:
        raise TypeError('Input Argument has wrong structure')
#############################################





###Show Functions, these print the results to the screen

#Print an term instance to the screen
def showTerm(term):
    print("Label: "+term.label)
    print("Ontology: "+term.ontology)
    print("Iri: "+term.iri)
    print(term.description)


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
        return True


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
    return True #In case the the term was found



searchForOntology("efo")

#Excuting of functions during development. Obviously this will go away one day
#This is mostly done by the test class now
#searchforlabel("lactose")
#showTermList()
#showTermByIndex(3)
#showTermByIri("http://purl.obolibrary.org/obo/HP_0004789")
#http://www.ebi.ac.uk/ols/beta/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0005576
#x=searchForIriInOntology("http://purl.obolibrary.org/obo/GO_0005576", "go")
#showTerm(x)
#showTermByIndex(-5) - see test, covered there
#showTermByIndex(100) - see test, covered there
#showTermByIri("http://purl.obolibrary.org/obo/HP_000478239") - see test, covered there
