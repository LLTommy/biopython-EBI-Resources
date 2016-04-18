import urllib
import json

#The termlist contains terms - for example if a search returns multiple terms they go into the termlist
termlist=[]

#This class represents a term, it contains all (relevant?) term information in OLS
class term:
    # These are variables shared by all terms (like static variables)?
    # https://docs.python.org/2/tutorial/classes.html#class-and-instance-variables
    # label=""
    # ontology=""
    # iri=""
    # description=""

    def __init__(self, label, ontology, iri, description):
        self.label=label
        self.ontology=ontology
        self.iri=iri
        self.description=description

#Gonna delete the ontology class I think
#class ontology:
#    def __init__(self, name, description):
#        self.name=name
#        self.description=description


#    def __init__(self, inputterm):
#        self.term=inputterm
#        self.searchurl="http://www.ebi.ac.uk/ols/beta/api/search?q="
    #    self.request=self.searchurl+self.term
    #    print(self.request)

#   def callOls(self):
#        reply = urllib.urlopen(self.request)
#        self.anwser = json.load(reply)
#        self.parse()



#generic call to the OLS search API
def callOLSsearch(query):
    searchurl="http://www.ebi.ac.uk/ols/beta/api/search?q="
    request=searchurl+query
    reply = urllib.urlopen(request)
    anwser = json.load(reply)
    return anwser


###########Search for a certain label in all ontologies
def searchforlabel(term):
#Missing: PAGING FOR ALL RESULTS (Right now only results of first page are shown) 
  anwser = callOLSsearch(term)
  parseLabelRequest(anwser)

#parse the result
def parseLabelRequest(anwser):
    #print(anwser)
    #print("\n")
    #print(anwser["response"])
    #print("\n")
    #print(anwser["response"]["numFound"])
    #print("\n")
    #print(anwser["response"]["docs"])
    #print(self.anwser["response"]["docs"][0]["iri"])
    #print(len(anwser["response"]["docs"]))
    for counter in anwser["response"]["docs"]:
        #print(counter)
        #print(counter["label"])
        #print(counter["id"])
        tmpdescription=""
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
    #print(anwser)
    #print(anwser["label"])
    #print(anwser["iri"])
    #print(anwser["ontology_name"])
    #print(anwser["is_defining_ontology"])
    tmpterm=term(anwser["label"], anwser["ontology_name"], anwser["iri"], anwser["description"])
    return tmpterm
#############################################


# search for Ontology information - work in progress
#def searchForOntology(ontology):
#    searchurl="http://www.ebi.ac.uk/ols/beta/api/ontologies/"
#    request=searchurl+query
#    reply = urllib.urlopen(request)
#    anwser = json.load(reply)
#    parseOntoloyData(anwser)

#def parseOntologyData():
#    print(anwser)


###Show Functions, these print the results to the screen

#Print an term instance to the screen
def showTerm(term):
    print("Label: "+term.label)
    print("Ontology: "+term.ontology)
    print("Iri: "+term.iri)
    #Getting rid of unicode symbole for printing (List as string)
    #print("{}".join(term.description))
    print(term.description)


#Print termlist, better table formats can be found here http://stackoverflow.com/questions/9535954/python-printing-lists-as-tabular-data
def showTermList():
    if (termlist == 0):
        print("Termlist is empty")
    else:
        print("Index - Label - "+"Ontology - "+"iri")
        index=0
        for element in termlist:
            print(str(index)+" - "+element.label+" - "+element.ontology+" - "+element.iri)
            index=index+1

#Show a certain term from the termlist by index (of the termlist)
def showTermByIndex(index):
    if (index>len(termlist)):
        print("Index is larger than the termlist!")
        return False
    if (index<0):
        print("Index is below 0, this is not allowed!")
        #raise Exception('Index is below 0, this is not allowed!') #code should be changed to something like this
        return False

    if (index>0 and index<len(termlist)):
        #print("Label: "+termlist[index].label)
        #print("Ontology: "+termlist[index].ontology)
        #print("Iri: "+termlist[index].iri)
        #Getting rid of unicode symbole for printing (List as string)
        #print("{}".join(termlist[index].description))
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
        print("iri not found it termlist")
        return False
    return True




#Excuting of functions during development. Obviously this will go away one day
searchforlabel("lactose")
print("\n")
#showTermList()
print("\n")
showTermByIndex(0)
print("\n")
#showTermByIri("http://purl.obolibrary.org/obo/HP_0004789")
print("\n")


#http://www.ebi.ac.uk/ols/beta/ontologies/go/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0005576
x=searchForIriInOntology("http://purl.obolibrary.org/obo/GO_0005576", "go")
showTerm(x)
#showTermByIndex(-5) - see test, covered there
#showTermByIndex(100) - see test, covered there
#showTermByIri("http://purl.obolibrary.org/obo/HP_000478239") - see test, covered there
