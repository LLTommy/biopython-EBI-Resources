import requests
import simplejson as json
from lxml import etree
"""Base class to get BioSamples and BioSamplesGroup usign the BioSample API"""

__BASE_URL = 'https://www.ebi.ac.uk/biosamples/xml'
__DEFAULT_ENCODING = "UTF-8"


def get_sample_xml(accession):
    """Get the BioSample xml with specific id"""
    url = compose_url("sample", accession)
    return query_api(url)


def get_group_xml(accession):
    """Get the BioSampleGroup with specific id"""
    url = compose_url("group", accession)
    return query_api(url)


def get_group_samples(accession, query="", sort_by='relevance', sort_order='descending', page_size=10, page=1):
    """Get the BioSamples accessions associated with the group"""
    base_url = compose_url("groupsamples", accession)
    url = '{base_url}/query={query}&sortby={sort_by}&sortorder={sort_order}&pagesize={page_size}&page={page}'.format(**locals())
    return query_api(url)


def query_api(url):
    """Return the xml document parsed from the url"""
    r = requests.get(url)
    return etree.fromstring(r.content, etree.XMLParser(encoding=__DEFAULT_ENCODING))


def compose_url(doc_type, accession):
    return  "{}/{}/{}".format(__BASE_URL, doc_type, accession)


def print_xml(doc):
    """Print the XML document"""
    print(etree.tostring(doc, pretty_print=True, method="xml").decode(__DEFAULT_ENCODING))


def sampletab_json(file_path):
    """Convert a given sampletab file to a json matrix string"""

    import re
    sampletab = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.rstrip("\n")
            current_line = []
            for word in line.split("\t"):
                new_word = re.sub(r"\"", "\\\"", word)
                current_line.append(new_word)
            sampletab.append(current_line)
    sampletab_dict = dict()
    sampletab_dict["sampletab"] = sampletab
    return json.dump(sampletab_dict, None)


if __name__ == "__main__":
    print(sampletab_json("WTSIi168-A.txt"))
