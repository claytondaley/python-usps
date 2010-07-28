"""
Rate Calculator classes
"""
from usps.api.base import USPSService

class DomesticRateCalculator(USPSService):
    """
    Calculator for domestic shipping rates
    """
    SERVICE_NAME = 'RateV3Request'
    CHILD_XML_NAME = 'Package'
    API = 'RateV3'
    PARAMETERS = ['Service',
                  'FirstClassMailType',
                  'ZipOrigination',
                  'ZipDestination',
                  'Pounds',
                  'Ounces',
                  'Container',
                  'Size',
                  'Width',
                  'Length',
                  'Height',
                  'Girth',
                  'Machinable',
                  'ReturnLocations',
                  'ShipDate',
                  ]
    
    
class InternationalRateCalculator(USPSService):
    """
    Calculator for international shipping rates
    """
    SERVICE_NAME = 'IntlRateRequest'
    CHILD_XML_NAME = 'Package'
    API = 'IntlRate'
    PARAMETERS = [
                  'Pounds',
                  'Ounces',
                  'Machinable',
                  'MailType',
                  'GXG',
                  'ValueOfContents',
                  'Country',
                  ]