from biosamples.biosamples_api import Api

api = Api()
# api.getGroupSamples('SAMEG82620')
sample = api.getSample('SAMEA4448577')
sample.printDoc()
sampleorigin = sample.getorigin()
sample.printderivationtree()