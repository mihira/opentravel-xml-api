#!/usr/bin/env python

from ota_xml_api.ota2011b import hotel_avail
from ota_xml_api.util.date import Period
import unittest

class SourceTC(unittest.TestCase):

    def test_source(self):
        node = hotel_avail.Source()
        self.assertEqual(str(node), '<Source><RequestorID/></Source>')
        node.set_office(22, 'ABCDEF', '1A')
        self.assertEqual(str(node), '<Source><RequestorID ID="ABCDEF" ID_Context="1A" Type="22"/></Source>')

class POSTC(unittest.TestCase):

    def test_pos(self):
        node = hotel_avail.POS()
        self.assertEqual(str(node), '<POS><Source><RequestorID/></Source><Source><RequestorID/></Source></POS>')

class RatePlanCandidateTC(unittest.TestCase):

    def test_rate_plan_candidate(self):
        node = hotel_avail.RatePlanCandidate()
        node.rate_plan_code = '456'
        self.assertEqual(str(node), '<RatePlanCandidate RatePlanCode="456"/>')

class TPAExtensionsTC(unittest.TestCase):

    def test_tpa_extensions(self):
        node = hotel_avail.TPAExtensions()
        node.add_price_group_criterion('Property')
        self.assertEqual(str(node), '<TPA_Extensions><PriceGroup><GroupCriterion Name="Property"/></PriceGroup></TPA_Extensions>')
        node.add_price_group_criterion('Occupancy')
        self.assertEqual(str(node), '<TPA_Extensions><PriceGroup><GroupCriterion Name="Property"/><GroupCriterion Name="Occupancy"/></PriceGroup></TPA_Extensions>')

class RateRangeTC(unittest.TestCase):

    def test_rate_range(self):
        node = hotel_avail.RateRange()
        node.rate_time_unit = 'FullDuration'
        node.rate_mode = '10'
        self.assertEqual(str(node), '<RateRange RateMode="10" RateTimeUnit="FullDuration"/>')

class RoomStayCandidateTC(unittest.TestCase):

    def test_room_stay_candidate(self):
        node = hotel_avail.RoomStayCandidate()
        node.adults = 3
        self.assertEqual(str(node), '<RoomStayCandidate><GuestCounts><GuestCount AgeQualifyingCode="10" Count="3"/></GuestCounts></RoomStayCandidate>')
        node.is_per_room = True
        self.assertEqual(str(node), '<RoomStayCandidate><GuestCounts IsPerRoom="true"><GuestCount AgeQualifyingCode="10" Count="3"/></GuestCounts></RoomStayCandidate>')
        node.is_per_room = False
        node.children = 2
        self.assertEqual(str(node), '<RoomStayCandidate><GuestCounts IsPerRoom="false"><GuestCount AgeQualifyingCode="10" Count="3"/><GuestCount AgeQualifyingCode="8" Count="2"/></GuestCounts></RoomStayCandidate>')

class HotelRefTC(unittest.TestCase):
    def test_hotel_ref(self):
        node = hotel_avail.HotelRef('ABCDE123', '1A')
        self.assertEqual(str(node), '<HotelRef HotelCode="ABCDE123" HotelCodeContext="1A"/>')
        node = hotel_avail.HotelRef()
        node.chain_code = 'NS'
        self.assertEqual(str(node), '<HotelRef ChainCode="NS"/>')
        node = hotel_avail.HotelRef()
        node.hotel_city_code = 'PAR'
        self.assertEqual(str(node), '<HotelRef HotelCityCode="PAR"/>')

class CriterionTC(unittest.TestCase):

    def test_criterion(self):
        node = hotel_avail.Criterion()
        hotel = hotel_avail.HotelRef('ABCDE123', '1A')
        hotel.chain_code = 'AB'
        hotel.hotel_city_code = 'CDE'
        node.add_hotel_ref(hotel)
        self.assertEqual(str(node), '<Criterion><HotelRef ChainCode="AB" HotelCityCode="CDE" HotelCode="ABCDE123" HotelCodeContext="1A"/></Criterion>')
        node.exact_match = True
        self.assertEqual(str(node), '<Criterion ExactMatch="true"><HotelRef ChainCode="AB" HotelCityCode="CDE" HotelCode="ABCDE123" HotelCodeContext="1A"/></Criterion>')
        period = Period(3)
        node.stay_date_range.period = period
        self.assertEqual(str(node), '<Criterion ExactMatch="true"><HotelRef ChainCode="AB" HotelCityCode="CDE" HotelCode="ABCDE123" HotelCodeContext="1A"/><StayDateRange End="%s" Start="%s"/></Criterion>' % (period.end, period.start))
        node.rate_range.rate_time_unit = 'FullDuration'
        node.rate_range.rate_mode = '10'
        self.assertEqual(str(node), '<Criterion ExactMatch="true"><HotelRef ChainCode="AB" HotelCityCode="CDE" HotelCode="ABCDE123" HotelCodeContext="1A"/><StayDateRange End="%s" Start="%s"/><RateRange RateMode="10" RateTimeUnit="FullDuration"/></Criterion>' % (period.end, period.start))
        node.add_rate_plan_candidate('123')
        self.assertEqual(str(node), '<Criterion ExactMatch="true"><HotelRef ChainCode="AB" HotelCityCode="CDE" HotelCode="ABCDE123" HotelCodeContext="1A"/><StayDateRange End="%s" Start="%s"/><RateRange RateMode="10" RateTimeUnit="FullDuration"/><RatePlanCandidates><RatePlanCandidate RatePlanCode="123"/></RatePlanCandidates></Criterion>' % (period.end, period.start))
        node.add_room_stay_candidate(2)
        self.assertEqual(str(node), '<Criterion ExactMatch="true"><HotelRef ChainCode="AB" HotelCityCode="CDE" HotelCode="ABCDE123" HotelCodeContext="1A"/><StayDateRange End="%s" Start="%s"/><RateRange RateMode="10" RateTimeUnit="FullDuration"/><RatePlanCandidates><RatePlanCandidate RatePlanCode="123"/></RatePlanCandidates><RoomStayCandidates><RoomStayCandidate Quantity="2" RoomID="0"><GuestCounts/></RoomStayCandidate></RoomStayCandidates></Criterion>' % (period.end, period.start))
        node.add_room_stay_candidate(1)
        self.assertEqual(str(node), '<Criterion ExactMatch="true"><HotelRef ChainCode="AB" HotelCityCode="CDE" HotelCode="ABCDE123" HotelCodeContext="1A"/><StayDateRange End="%s" Start="%s"/><RateRange RateMode="10" RateTimeUnit="FullDuration"/><RatePlanCandidates><RatePlanCandidate RatePlanCode="123"/></RatePlanCandidates><RoomStayCandidates><RoomStayCandidate Quantity="2" RoomID="0"><GuestCounts/></RoomStayCandidate><RoomStayCandidate Quantity="1" RoomID="1"><GuestCounts/></RoomStayCandidate></RoomStayCandidates></Criterion>' % (period.end, period.start))
        node.tpa_extensions.add_price_group_criterion('Property')
        self.assertEqual(str(node), '<Criterion ExactMatch="true"><HotelRef ChainCode="AB" HotelCityCode="CDE" HotelCode="ABCDE123" HotelCodeContext="1A"/><StayDateRange End="%s" Start="%s"/><RateRange RateMode="10" RateTimeUnit="FullDuration"/><RatePlanCandidates><RatePlanCandidate RatePlanCode="123"/></RatePlanCandidates><RoomStayCandidates><RoomStayCandidate Quantity="2" RoomID="0"><GuestCounts/></RoomStayCandidate><RoomStayCandidate Quantity="1" RoomID="1"><GuestCounts/></RoomStayCandidate></RoomStayCandidates><TPA_Extensions><PriceGroup><GroupCriterion Name="Property"/></PriceGroup></TPA_Extensions></Criterion>' % (period.end, period.start))

class HotelAvailRQTC(unittest.TestCase):

    def test_hotel_avail_rq(self):
        node = hotel_avail.HotelAvailRQ()
        self.assertEqual(str(node), '<OTA_HotelAvailRQ xmlns="http://www.opentravel.org/OTA/2003/05" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opentravel.org/OTA/2003/05 OTA_HotelAvailRQ.xsd"><POS><Source><RequestorID/></Source><Source><RequestorID/></Source></POS><AvailRequestSegments><AvailRequestSegment><HotelSearchCriteria/></AvailRequestSegment></AvailRequestSegments></OTA_HotelAvailRQ>')
        node.info_source = 'Distribution'
        self.assertEqual(str(node), '<OTA_HotelAvailRQ xmlns="http://www.opentravel.org/OTA/2003/05" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opentravel.org/OTA/2003/05 OTA_HotelAvailRQ.xsd"><POS><Source><RequestorID/></Source><Source><RequestorID/></Source></POS><AvailRequestSegments><AvailRequestSegment InfoSource="Distribution"><HotelSearchCriteria/></AvailRequestSegment></AvailRequestSegments></OTA_HotelAvailRQ>')
        node.add_criterion()
        self.assertEqual(str(node), '<OTA_HotelAvailRQ xmlns="http://www.opentravel.org/OTA/2003/05" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opentravel.org/OTA/2003/05 OTA_HotelAvailRQ.xsd"><POS><Source><RequestorID/></Source><Source><RequestorID/></Source></POS><AvailRequestSegments><AvailRequestSegment InfoSource="Distribution"><HotelSearchCriteria><Criterion/></HotelSearchCriteria></AvailRequestSegment></AvailRequestSegments></OTA_HotelAvailRQ>')

if __name__ == '__main__':
    unittest.main()
