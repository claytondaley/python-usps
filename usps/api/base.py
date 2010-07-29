"""
Base implementation of USPS service wrapper
"""

import urllib, urllib2
from usps.utils import utf8urlencode, xmltodict, dicttoxml
from usps.errors import USPSXMLError

try:
    from xml.etree import ElementTree as ET
except ImportError:
    from elementtree import ElementTree as ET

class USPSService(object):
    """
    Base USPS Service Wrapper implementation
    """
    SERVICE_NAME = ''
    API = ''
    CHILD_XML_NAME = ''
    PARAMETERS = []
    
    def __init__(self, url):
        self.url = url

    def submit_xml(self, xml):
        """
        submit XML to USPS
        @param xml: the xml to submit
        @return: the response element from USPS
        """
        data = {'XML':ET.tostring(xml),
                'API':self.API}
        response = urllib2.urlopen(self.url, utf8urlencode(data))
        root = ET.parse(response).getroot()
        if root.tag == 'Error':
            raise USPSXMLError(root)
        error = root.find('.//Error')
        if error:
            raise USPSXMLError(error)
        return root
    
    def parse_xml(self, xml):
        """
        Parse the response from USPS into a dictionar
        @param xml: the xml to parse
        @return: a dictionary representing the XML response from USPS
        """
        items = list()
        for item in xml.getchildren():#xml.findall(self.SERVICE_NAME+'Response'):
            items.append(xmltodict(item))
        return items
    
    def make_xml(self, userid, data):
        """
        Transform the data provided to an XML fragment
        @param userid: the USPS API user id
        @param data: the data to serialize and send to USPS
        @return: an XML fragment representing data
        """
        root = ET.Element(self.SERVICE_NAME+'Request')
        root.attrib['USERID'] = userid
        index = 0
        for data_dict in data:
            data_xml = dicttoxml(data_dict, self.CHILD_XML_NAME, self.PARAMETERS)
            data_xml.attrib['ID'] = str(index)
            
            root.append(data_xml)
            index += 1
        return root
    
    def execute(self, userid, data):
        """
        Create XML from data dictionary, submit it to 
        the USPS API and parse the response
        
        @param userid: a USPS user id
        @param data: the data to serialize and submit
        @return: the response from USPS as a dictionary
        """
        xml = self.make_xml(userid, data)
        return self.parse_xml(self.submit_xml(xml))