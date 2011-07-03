import os
import urllib2

MEDIA = [
    ('http://upload.wikimedia.org/wikipedia/commons/8/80/FRBR-Group-1-entities-and-basic-relations.svg', 'frbr.svg'),
    ('http://www.w3.org/DesignIssues/diagrams/n3/venn', 'serialization-venn.svg'),
]

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), 'media'))

if __name__ == '__main__':
    if not os.path.exists(BASE):
        os.makedirs(BASE)

    for source, destination in MEDIA:
        destination = os.path.join(BASE, destination)
        request = urllib2.Request(source)
        request.headers['User-agent'] = 'Mozilla (Python/urllib2; https://github.com/alexsdutton/dhss-2011-rdf'
        response = urllib2.urlopen(request)
        with open(destination, 'w') as f:
            for chunk in response:
                f.write(chunk)
