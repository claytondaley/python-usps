"""
Utility functions for use in USPS app
"""
try:
    from xml.etree import ElementTree as ET
except ImportError:
    from elementtree import ElementTree as ET
    
def utf8urlencode(data):
    ret = dict()
    for key, value in data.iteritems():
        ret[key] = value.encode('utf8')
    return urllib.urlencode(ret)

def dicttoxml(dictionary, parent, tagname, attributes=None):
    element = ET.SubElement(parent, tagname)
    if attributes: #USPS likes things in a certain order!
        for key in attributes:
            ET.SubElement(element, key).text = dictionary.get(key, '')
    else:
        for key, value in dictionary.iteritems():
            ET.SubElement(element, key).text = value
    return element

def xmltodict(element):
    ret = dict()
    for item in element.getchildren():
        ret[item.tag] = item.text
    return ret