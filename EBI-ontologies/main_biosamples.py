from biosamples import Api, BioSample

api = Api()
# api.getGroupSamples('SAMEG82620')
sample = BioSample(api.getSampleXml('SAMEA4448577'))
sample.printDoc()
sampleorigin = sample.getorigin()
sample.printderivationtree()