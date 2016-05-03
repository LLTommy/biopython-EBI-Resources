class ResultQuery(Object):

    _NS = "http://www.ebi.ac.uk/biosamples/ResultQuery/1.0"

    def __init__(self,doc):
        self.doc = doc
        self.totalsamples = 0
        self.actualsamples = 0
    
    def total(self):
        return self.total

    def results(self):
        return self.results
