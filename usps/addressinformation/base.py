'''
See http://www.usps.com/webtools/htm/Address-Information.htm for complete documentation of the API
'''
from usps.base import USPSService

class AddressValidate(USPSService):
    SERVICE_NAME = 'AddressValidate'
    CHILD_XML_NAME = 'Address'
    API = 'Verify'
    PARAMETERS = ['FirmName',
                  'Address1',
                  'Address2',
                  'City',
                  'State',
                  'Zip5',
                  'Zip4',]
    
class ZipCodeLookup(USPSService):
    SERVICE_NAME = 'ZipCodeLookup'
    CHILD_XML_NAME = 'Address'
    API = 'ZipCodeLookup'
    PARAMETERS = ['FirmName',
                  'Address1',
                  'Address2',
                  'City',
                  'State',]

class CityStateLookup(USPSService):
    SERVICE_NAME = 'CityStateLookup'
    CHILD_XML_NAME = 'ZipCode'
    API = 'CityStateLookup'
    PARAMETERS = ['Zip5',]

