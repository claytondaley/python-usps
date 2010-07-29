"""
"""
from pprint import PrettyPrinter
import unittest
from usps.api import USPS_CONNECTION_TEST, USPS_CONNECTION
from usps.api.addressinformation import AddressValidate, ZipCodeLookup, CityStateLookup
from usps.api.ratecalculator import DomesticRateCalculator, InternationalRateCalculator
from usps.api.servicestandards import PriorityMailServiceStandards, PackageServicesServiceStandards, ExpressMailServiceCommitment
from usps.api.tracking import TrackConfirm

USERID = None

class TestRateCalculatorAPI(unittest.TestCase):
    """
    Tests for Rate Calculator API wrappers
    
    @todo - get these tests fixed -- the test server doesn't respond to rate calculator V3 requests
        yet.  E-mail is out to USPS customer service to turn on production access
    """
    def test_domestic_rate(self):
        """ connector = DomesticRateCalculator(USPS_CONNECTION)
        response = connector.execute(USERID, [{'Service': 'FIRST_CLASS',
                                               'FirstClassMailType': 'LETTER',
                                               'ZipOrigination': '44106',
                                               'ZipDestination': '20770',
                                               'Pounds': '0',
                                               'Ounces': '3.5',
                                               'Size': 'REGULAR',
                                               'Machinable': 'true'
                                               },
                                               {
                                                'Service': 'PRIORITY',
                                                'ZipOrigination': '44106',
                                                'ZipDestination': '20770',
                                                'Pounds': '1',
                                                'Ounces': '8',
                                                'Container': 'NONRECTANGULAR',
                                                'Size': 'LARGE',
                                                'Width': '15',
                                                'Length': '30',
                                                'Height': '15',
                                                'Girth': '55'
                                                },
                                                {'Service': 'ALL',
                                                 'FirstClassMailType': 'LETTER',
                                                 'ZipOrigination': '90210',
                                                 'ZipDestination': '92298',
                                                 'Pounds': '8',
                                                 'Ounces': '32',
                                                 'Container': None,
                                                 'Size': 'REGULAR',
                                                 'Machinable': 'true'}
                                                ])
        """
        pass
        
        
        
        
    def test_international_rate(self):
        """
        connector = InternationalRateCalculator(USPS_CONNECTION)
        response = connector.execute(USERID, [{
                                               'Pounds': '3',
                                               'Ounces': '3',
                                               'Machinable': 'false',
                                               'MailType': 'Envelope',
                                               'Country': 'Canada',
                                               },
                                               {'Pounds': '4',
                                                'Ounces': '3',
                                                'MailType': 'Package',
                                                'GXG': {
                                                        'Length': '46',
                                                        'Width': '14',
                                                        'Height': '15',
                                                        'POBoxFlag': 'N',
                                                        'GiftFlag': 'N'
                                                        },
                                                'ValueOfContents': '250',
                                                'Country': 'Japan'
                                                }])
        """
        pass
        
    
class TestServiceStandardsAPI(unittest.TestCase):
    """
    Tests for service standards API wrappers
    """
    def test_priority_service_standards(self):
        connector = PriorityMailServiceStandards(USPS_CONNECTION_TEST)
        response = connector.execute(USERID, [{
                                                'OriginZip': '4',
                                                'DestinationZip': '4'
                                                }])[0]
        self.assertEqual(response['OriginZip'], '4')
        self.assertEqual(response['DestinationZip'], '4')
        self.assertEqual(response['Days'], '1')
        
        response = connector.execute(USERID, [{
                                                'OriginZip': '4',
                                                'DestinationZip': '5'
                                                }])[0]
                                                
        self.assertEqual(response['OriginZip'], '4')
        self.assertEqual(response['DestinationZip'], '5')
        self.assertEqual(response['Days'], '2')
        
    def test_package_service_standards(self):
        connector = PackageServicesServiceStandards(USPS_CONNECTION_TEST)
        response = connector.execute(USERID, [{
                                                'OriginZip': '4',
                                                'DestinationZip': '4'
                                                }])[0]
                                                
        self.assertEqual(response['OriginZip'], '4')
        self.assertEqual(response['DestinationZip'], '4')
        self.assertEqual(response['Days'], '2')
        
        response = connector.execute(USERID, [{
                                                'OriginZip': '4',
                                                'DestinationZip': '600'
                                                }])[0]
                                                
        self.assertEqual(response['OriginZip'], '4')
        self.assertEqual(response['DestinationZip'], '600')
        self.assertEqual(response['Days'], '3')
        
    def test_express_service_commitment(self):
        connector = ExpressMailServiceCommitment(USPS_CONNECTION_TEST)
        response = connector.execute(USERID, [{
                                                'OriginZIP': '20770',
                                                'DestinationZIP': '11210',
                                                'Date': '05-Aug-2004'
                                                }])[0]
        
        self.assertEqual(response, {
                                    'DestinationCity': 'BROOKLYN', 
                                    'OriginState': 'MD', 
                                    'DestinationState': 'NY', 
                                    'OriginZIP': '20770', 
                                    'DestinationZIP': '11210', 
                                    'Commitment': {'CommitmentTime': '12:00 PM', 
                                                   'CommitmentName': 'Next Day', 
                                                   'CommitmentSequence': 'A0112', 
                                                   'Location': {'City': 'BALTIMORE', 
                                                                'Zip': '21240', 
                                                                'CutOff': '9:45 PM', 
                                                                'Facility': 'AIR MAIL FACILITY', 
                                                                'State': 'MD', 
                                                                'Street': 'ROUTE 170 BLDG C DOOR 19'}
                                                   }, 
                                    'Time': '11:30 AM', 
                                    'Date': '05-Aug-2004', 
                                    'OriginCity': 'GREENBELT'})
        
        response = connector.execute(USERID, [{
                                                'OriginZIP': '207',
                                                'DestinationZIP': '11210',
                                                'Date': ''
                                                }])[0]
        
        self.assertEqual(response, {
                                    'Commitment': {'CommitmentName': 'Next Day',
                                                   'CommitmentSequence': 'A0115',
                                                   'CommitmentTime': '3:00 PM',
                                                   'Location': {'City': 'GREENBELT',
                                                                'CutOff': '3:00 PM',
                                                                'Facility': 'EXPRESS MAIL COLLECTION BOX',
                                                                'State': 'MD',
                                                                'Street': '7500 GREENWAY CENTER DRIVE',
                                                                'Zip': '20770'}
                                                   },
                                                   'Date': '05-Aug-2004',
                                                   'DestinationCity': 'BROOKLYN',
                                                   'DestinationState': 'NY',
                                                   'DestinationZIP': '11210',
                                                   'OriginCity': 'GREENBELT',
                                                   'OriginState': 'MD',
                                                   'OriginZIP': '207',
                                                   'Time': '11:30 AM'})



class TestTrackConfirmAPI(unittest.TestCase):
    """
    Tests for Track/Confirm API wrapper
    """
    def test_tracking(self):
        """
        Test Track/Confirm API connector
        """
        connector = TrackConfirm(USPS_CONNECTION_TEST)
        response = connector.execute(USERID, [{'ID':'EJ958083578US'},])[0]
        
        self.assertEqual(response['TrackSummary'], 'Your item was delivered at 8:10 am on June 1 in Wilmington DE 19801.')
        self.assertEqual(response['TrackDetail'][0], 'May 30 11:07 am NOTICE LEFT WILMINGTON DE 19801.')
        self.assertEqual(response['TrackDetail'][1], 'May 30 10:08 am ARRIVAL AT UNIT WILMINGTON DE 19850.')
        self.assertEqual(response['TrackDetail'][2], 'May 29 9:55 am ACCEPT OR PICKUP EDGEWATER NJ 07020.')

        response = connector.execute(USERID, [{'ID': 'EJ958088694US'}])[0]
        self.assertEqual(response['TrackSummary'], 'Your item was delivered at 1:39 pm on June 1 in WOBURN MA 01815.')
        self.assertEqual(response['TrackDetail'][0], 'May 30 7:44 am NOTICE LEFT WOBURN MA 01815.')
        self.assertEqual(response['TrackDetail'][1], 'May 30 7:36 am ARRIVAL AT UNIT NORTH READING MA 01889.')
        self.assertEqual(response['TrackDetail'][2], 'May 29 6:00 pm ACCEPT OR PICKUP PORTSMOUTH NH 03801.')
        

class TestAddressInformationAPI(unittest.TestCase):
    """
    Tests for address lookup and validation services
    """
    def test_address_validate(self):
        connector = AddressValidate(USPS_CONNECTION_TEST)
        response = connector.execute(USERID, [{'Address2':'6406 Ivy Lane',
                                               'City':'Greenbelt',
                                               'State':'MD'}])[0]
        self.assertEqual(response['Address2'], '6406 IVY LN')
        self.assertEqual(response['City'], 'GREENBELT')
        self.assertEqual(response['State'], 'MD')
        self.assertEqual(response['Zip5'], '20770')
        self.assertEqual(response['Zip4'], '1440')
        
        response = connector.execute(USERID, [{'Address2':'8 Wildwood Drive',
                                               'City':'Old Lyme',
                                               'State':'CT',
                                               'Zip5':'06371',}])[0]
        self.assertEqual(response['Address2'], '8 WILDWOOD DR')
        self.assertEqual(response['City'], 'OLD LYME')
        self.assertEqual(response['State'], 'CT')
        self.assertEqual(response['Zip5'], '06371')
        self.assertEqual(response['Zip4'], '1844')
    
    def test_zip_code_lookup(self):
        connector = ZipCodeLookup(USPS_CONNECTION_TEST)
        response = connector.execute(USERID, [{'Address2':'6406 Ivy Lane',
                                               'City':'Greenbelt',
                                               'State':'MD'}])[0]
        self.assertEqual(response['Address2'], '6406 IVY LN')
        self.assertEqual(response['City'], 'GREENBELT')
        self.assertEqual(response['State'], 'MD')
        self.assertEqual(response['Zip5'], '20770')
        self.assertEqual(response['Zip4'], '1440')
        
        response = connector.execute(USERID, [{'Address2':'8 Wildwood Drive',
                                               'City':'Old Lyme',
                                               'State':'CT',
                                               'Zip5':'06371',}])[0]
        self.assertEqual(response['Address2'], '8 WILDWOOD DR')
        self.assertEqual(response['City'], 'OLD LYME')
        self.assertEqual(response['State'], 'CT')
        self.assertEqual(response['Zip5'], '06371')
        self.assertEqual(response['Zip4'], '1844')
    
    def test_city_state_lookup(self):
        connector = CityStateLookup(USPS_CONNECTION_TEST)
        response = connector.execute(USERID, [{'Zip5':'90210'}])[0]
        self.assertEqual(response['City'], 'BEVERLY HILLS')
        self.assertEqual(response['State'], 'CA')
        self.assertEqual(response['Zip5'], '90210')
        
        response = connector.execute(USERID, [{'Zip5':'20770',}])[0]
        self.assertEqual(response['City'], 'GREENBELT')
        self.assertEqual(response['State'], 'MD')
        self.assertEqual(response['Zip5'], '20770')

if __name__ == '__main__':
    #please append your USPS USERID to test against the wire
    import sys
    if len(sys.argv) < 1:
        print "You must provide a USERID"
        exit()
    else:
        USERID = sys.argv.pop()
        unittest.main()
