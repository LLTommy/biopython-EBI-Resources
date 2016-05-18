```Note: This is in a very very early development stage```


# Introduction
The goal of this repo is to bring EBI Resources to python and ultimately to merge it into biopython. There is still a long way to go.

#usage

From console:
python ols.py
python test_ols.py

In python (start python in console with *python*):
import ols

Search for a term:
ols.searchForLabel(term) e.g. ols.searchForLabel("lactose")

This fills the termlist with terms, to browse this termslist you can use:
ols.showTermList();

To further investigate the termlist, you can use:

ols.showTermByIndex(index)
ols.showTermByIri(iri)



Search for an ontology:
x=ols.searchForOntology('efo')
ols.showOntology(x)
