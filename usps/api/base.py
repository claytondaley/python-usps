import urllib, urllib2
from usps.utils import utf8urlencode, xmltodict, dicttoxml
from usps.errors import USPSXMLError

try:
    from xml.etree import ElementTree as ET
except ImportError:
    from elementtree import ElementTree as ET

class USPSService(object):
    SERVICE_NAME = None
    API = None
    CHILD_XML_NAME = None
    PARAMETERS = None
    
    def __init__(self, url):
        self.url = url

    def submit_xml(self, xml):
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
        items = list()
        for item in xml.getchildren():#xml.findall(self.SERVICE_NAME+'Response'):
            items.append(xmltodict(item))
        return items
    
    def make_xml(self, userid, data):
        root = ET.Element(self.SERVICE_NAME+'Request')
        root.attrib['USERID'] = userid
        index = 0
        for data_dict in data:
            data_xml = dicttoxml(data_dict, root, self.CHILD_XML_NAME, self.PARAMETERS)
            data_xml.attrib['ID'] = str(index)
            index += 1
        return root
    
    def execute(self, userid, data):
        xml = self.make_xml(userid, data)
        return self.parse_xml(self.submit_xml(xml))