__author__ = 'KCP'
__date__ = '2015-05-06'

from urllib import parse, request
import xml.etree.ElementTree as et


def getsearchresult(target, query):
    """Return a xml tree or xml root element
    Keyword argument:
    target -- Request URL
    query -- Dictionary for search
    """

    xmldata = request.urlopen(target+'?'+parse.urlencode(query)).read().decode('utf-8')
    xmltree = et.fromstring(xmldata)
    return xmltree


def parsenaverxml(xmlroot):
    return False

def parsedaumxml(xmlroot):
    return False

def parsetwitterxml(xmlroot):
    return False
