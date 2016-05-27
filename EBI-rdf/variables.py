atlas="http://www.ebi.ac.uk/rdf/services/atlas/servlet/query?query="
biomodels="http://www.ebi.ac.uk/rdf/services/biomodels/servlet/query?query="
biosamples="https://www.ebi.ac.uk/rdf/services/biosamples/servlet/query?query="
chembl="https://www.ebi.ac.uk/rdf/services/chembl/servlet/query?query="
reactome="http://www.ebi.ac.uk/rdf/services/reactome/servlet/query?query="


#uniprot = ""  - no json enpoint? different enpoint?
#ensemble="https://www.ebi.ac.uk/rdf/services/ensembl/sparql" No json reply


atlasQuery="""PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX sio: <http://semanticscience.org/resource/>
PREFIX efo: <http://www.ebi.ac.uk/efo/>
PREFIX atlas: <http://rdf.ebi.ac.uk/resource/atlas/>
PREFIX atlasterms: <http://rdf.ebi.ac.uk/terms/atlas/>
PREFIX identifiers:<http://identifiers.org/ensembl/>
SELECT distinct ?diffValue ?expUri ?propertyType ?propertyValue ?pvalue
WHERE {
?expUri atlasterms:hasAnalysis ?analysis .
?analysis atlasterms:hasExpressionValue ?value .
?value rdfs:label ?diffValue .
?value atlasterms:hasFactorValue ?factor .
?factor atlasterms:propertyType ?propertyType .
?factor atlasterms:propertyValue ?propertyValue .
?value atlasterms:pValue ?pvalue .
?value atlasterms:isMeasurementOf ?probe .
?probe atlasterms:dbXref identifiers:ENSG00000129991 .
}
ORDER BY ASC (?pvalue) """

chemblQuery="""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX cco: <http://rdf.ebi.ac.uk/terms/chembl#>
SELECT ?molecule
WHERE {
  ?molecule a ?type .
  ?type rdfs:subClassOf* cco:Substance .
}
"""

biomodelsQuery="""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX sbmlrdf: <http://identifiers.org/biomodels.vocabulary#>

SELECT ?speciesid ?name WHERE {
 <http://identifiers.org/biomodels.db/BIOMD0000000001> sbmlrdf:species ?speciesid .
 ?speciesid sbmlrdf:name ?name}
"""

biosamplesQuery="""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX efo: <http://www.ebi.ac.uk/efo/>
PREFIX biosd-terms: <http://rdf.ebi.ac.uk/terms/biosd/>
PREFIX pav: <http://purl.org/pav/2.0/>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX sio: <http://semanticscience.org/resource/>
PREFIX atlas: <http://rdf.ebi.ac.uk/terms/atlas/>
PREFIX oac: <http://www.openannotation.org/ns/>

SELECT DISTINCT *
WHERE {
  { select ?item WHERE { ?item a biosd-terms:BiosamplesSubmission. } LIMIT 3}
  UNION { select ?item { ?item a biosd-terms:SampleGroup. } LIMIT 3 }
  UNION { select ?item { ?item a biosd-terms:Sample. } LIMIT 3 }
}
"""

reactomeQuer="""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX biopax3: <http://www.biopax.org/release/biopax-level3.owl#>

SELECT DISTINCT ?pathway ?pathwayname
WHERE
{
 ?pathway rdf:type biopax3:Pathway .
 ?pathway biopax3:displayName ?pathwayname
}
"""
