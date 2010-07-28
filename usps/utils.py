"""
Utility functions for use in USPS app
"""
import urllib
try:
    from xml.etree import ElementTree as ET
except ImportError:
    from elementtree import ElementTree as ET
    
def utf8urlencode(data):
    """
    utf8 URL encode the given dictionary's data
    
    @param data: a dictionary of data to be encoded
    """
    ret = dict()
    for key, value in data.iteritems():
        ret[key] = value.encode('utf8')
    return urllib.urlencode(ret)

def dicttoxml(dictionary, tagname, parent=None, attributes=None):
    """
    Transform a dictionary to xml
    
    @param dictionary: a dictionary
    @param parent:  a parent node
    @return: XML serialization of the given dictionary
    """
    if parent:
        element = ET.SubElement(parent, tagname)
    else: 
        element = ET.Element(tagname)
    
    if attributes: #USPS likes things in a certain order!
        for key in attributes:
            value = dictionary.get(key, '')
            if type(value).__name__ == 'dict':
                elem = dicttoxml(value, key)
                element.append(elem)
            else:
                ET.SubElement(element, key).text = value
    else:
        for key, value in dictionary.iteritems():
            if type(value).__name__ == 'dict':
                elem = dicttoxml(value, key)
                element.append(elem)
            else:
                ET.SubElement(element, key).text = value
    return element

def xmltodict(element):
    """
    Transform an xml fragment into a python dictionary
    
    @param element: an XML fragment
    """
    ret = dict()
    for item in element.getchildren():
        ret[item.tag] = item.text
    return ret