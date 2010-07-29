'''
See http://www.usps.com/webtools/htm/Address-Information.htm for complete documentation of the API
'''
from usps.api.base import USPSService

class AddressValidate(USPSService):
    SERVICE_NAME = 'AddressValidate'
    CHILD_XML_NAME = 'Address'
    PARAMETERS = ['FirmName',
                  'Address1',
                  'Address2',
                  'City',
                  'State',
                  'Zip5',
                  'Zip4',]
    
    @property
    def API(self):
        return 'Verify'
    
class ZipCodeLookup(USPSService):
    SERVICE_NAME = 'ZipCodeLookup'
    CHILD_XML_NAME = 'Address'
    PARAMETERS = ['FirmName',
                  'Address1',
                  'Address2',
                  'City',
                  'State',]  
    @property
    def API(self):
        return 'ZipCodeLookup'

class CityStateLookup(USPSService):
    SERVICE_NAME = 'CityStateLookup'
    CHILD_XML_NAME = 'ZipCode'
    PARAMETERS = ['Zip5',]

    @property
    def API(self):
        return 'CityStateLookup'
