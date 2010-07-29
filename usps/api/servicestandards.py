"""
Service standards API wrappers
"""
from usps.utils import dicttoxml, xmltodict
from usps.api.base import USPSService

try:
    from xml.etree import ElementTree as ET
except ImportError:
    from elementtree import ElementTree as ET

class ServiceStandards(USPSService):
    SERVICE_NAME = ''
    API = SERVICE_NAME
    PARAMETERS = [
                  'OriginZip',
                  'DestinationZip'
                  ]
    
    def make_xml(self, userid, data):
        """
        Transform the data provided to an XML fragment
        @param userid: the USPS API user id
        @param data: the data to serialize and send to USPS
        @return: an XML fragment representing data
        """
        for data_dict in data:
            data_xml = dicttoxml(data_dict, self.SERVICE_NAME+'Request', self.PARAMETERS)
            data_xml.attrib['USERID'] = userid
        return data_xml
    
    def parse_xml(self, xml):
        """
        Parse the response from USPS into a dictionary
        @param xml: the xml to parse
        @return: a dictionary representing the XML response from USPS
        """
        return [xmltodict(xml),]
    

class PriorityMailServiceStandards(ServiceStandards):
    """
    Provides shipping time estimates for Priority mail shipping methods
    """
    SERVICE_NAME = 'PriorityMail'
    API = SERVICE_NAME


class PackageServicesServiceStandards(ServiceStandards):
    """
    Provides shipping time estimates for Package Services (Parcel Post, Bound Printed Matter, Library Mail, and Media Mail)
    """
    SERVICE_NAME = 'StandardB'
    API = SERVICE_NAME
    
    
class ExpressMailServiceCommitment(ServiceStandards):
    """
    Provides drop off locations and commitments for shipment on a given date
    """
    SERVICE_NAME = 'ExpressMailCommitment'
    API = SERVICE_NAME
    PARAMETERS = [
                  'OriginZIP',
                  'DestinationZIP',
                  'Date'
                  ]
    
    
    
    
