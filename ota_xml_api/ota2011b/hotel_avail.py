    #!/usr/bin/env python

from ..util.xml_base import XmlNode, PeriodNode
from ..util import constants

class RequestorID(XmlNode):
    def __init__(self, **kwargs):
        XmlNode.__init__(self, **kwargs)
        self._company_name = None

    def get_company_name(self):
        if not self._company_name:
            self._company_name = self.add_child(XmlNode(constants.COMPANY_NAME))
        return self._company_name
    companyName = property(get_company_name)

class Source(XmlNode):
    def __init__(self, *args, **kwargs):
        XmlNode.__init__(self, *args, **kwargs)
        self.requestor_id = self.add_child(RequestorID())
        self._booking_channel = None

    def get_booking_channel(self):
        if not self._booking_channel:
            req_id = RequestorID(name=constants.BOOKING_CHANNEL, Type=1)
            self._booking_channel = self.add_child(req_id)
        return self._booking_channel
    bookingChannel = property(get_booking_channel)

    def set_office(self, type_attr, office_id, id_context):
        self.requestor_id.set_attribute(constants.TYPE, type_attr)
        self.requestor_id.set_attribute(constants.ID, office_id)
        self.requestor_id.set_attribute(constants.ID_CONTEXT, id_context)

class POS(XmlNode):
    def __init__(self, *args, **kwargs):
        XmlNode.__init__(self, *args, **kwargs)
        self.origin = self.add_child(Source())
        self.office = self.add_child(Source())

class RatePlanCandidate(XmlNode):
    def __init__(self, *args, **kwargs):
        XmlNode.__init__(self, *args, **kwargs)

    def set_rate_plan_code(self, rate_plan_code):
        self.set_attribute(constants.RATE_PLAN_CODE, rate_plan_code)
    rate_plan_code = property(fset=set_rate_plan_code)

class RoomStayCandidate(XmlNode):
    def __init__(self, *args, **kwargs):
        XmlNode.__init__(self, *args, **kwargs)
        self._guest_counts = self.add_child(XmlNode(constants.GUEST_COUNTS))
        self._age_map = {}

    def _set_is_per_room(self, is_per_room):
        is_per_room_str = str(is_per_room).lower()
        self._guest_counts.set_attribute(constants.IS_PER_ROOM, is_per_room_str)
    is_per_room = property(fset=_set_is_per_room)

    def _set_guest_count(self, age_code, count):
        if age_code not in self._age_map.keys():
            guest_count = XmlNode(constants.GUEST_COUNT)
            self._age_map[age_code] = self._guest_counts.add_child(guest_count)
        guest_count = self._age_map[age_code]
        guest_count.set_attribute(constants.AGE_QUALIFYING_CODE, age_code)
        guest_count.set_attribute(constants.COUNT, count)

    def _set_adults_count(self, count):
        self._set_guest_count(10, count)
    adults = property(fset=_set_adults_count)

    def _set_children_count(self, count):
        self._set_guest_count(8, count)
    children = property(fset=_set_children_count)

class HotelRef(XmlNode):
    def __init__(self, hotel_code=None, hotel_code_context=None, **kwargs):
        XmlNode.__init__(self, **kwargs)
        self._hotel_code = None
        self._hotel_code_context = None
        if hotel_code:
            self.hotel_code = hotel_code
        if hotel_code_context:
            self.hotel_code_context = hotel_code_context

    def _set_hotel_city_code(self, hotel_city_code):
        self.set_attribute(constants.HOTEL_CITY_CODE, hotel_city_code)
    hotel_city_code = property(fset=_set_hotel_city_code)

    def _set_chain_code(self, chain_code):
        self.set_attribute(constants.CHAIN_CODE, chain_code)
    chain_code = property(fset=_set_chain_code)

    def _set_hotel_code(self, hotel_code):
        self._hotel_code = hotel_code
        self.set_attribute(constants.HOTEL_CODE, hotel_code)
    hotel_code = property(fset=_set_hotel_code)

    def _set_hotel_code_context(self, hotel_code_context):
        self.set_attribute(constants.HOTEL_CODE_CONTEXT, hotel_code_context)
        self._hotel_code_context = hotel_code_context
    hotel_code_context = property(fset=_set_hotel_code_context)

class RateRange(XmlNode):
    def __init__(self, *args, **kwargs):
        XmlNode.__init__(self, *args, **kwargs)

    def _set_rate_time_unit(self, rate_time_unit):
        self.set_attribute(constants.RATE_TIME_UNIT, rate_time_unit)
    rate_time_unit = property(fset=_set_rate_time_unit)

    def _set_rate_mode(self, rate_mode):
        self.set_attribute(constants.RATE_MODE, rate_mode)
    rate_mode = property(fset=_set_rate_mode)

class TPAExtensions(XmlNode):
    def __init__(self, **kwargs):
        XmlNode.__init__(self, constants.TPA_EXTENSIONS, **kwargs)
        self._price_group = None

    def _get_price_group(self):
        if not self._price_group:
            self._price_group = self.add_child(XmlNode(constants.PRICE_GROUP))
        return self._price_group
    price_group = property(_get_price_group)

    def add_price_group_criterion(self, name):
        group_criterion_node = XmlNode(constants.GROUP_CRITERION)
        group_criterion = self.price_group.add_child(group_criterion_node)
        group_criterion.set_attribute(constants.NAME, name)
        return group_criterion


class Criterion(XmlNode):
    def __init__(self, *args, **kwargs):
        XmlNode.__init__(self, *args, **kwargs)
        self._stay_date_range = None
        self._room_stay_candidates = None
        self._rate_plan_candidates = None
        self._rate_range = None
        self._tpa_extensions = None

    def add_hotel_ref(self, hotel_ref):
        return self.add_child(hotel_ref)

    def _set_exact_match(self, exact_match):
        self.set_attribute(constants.EXACT_MATCH, str(exact_match).lower())
    exact_match = property(fset=_set_exact_match)

    def _get_stay_date_range(self):
        if not self._stay_date_range:
            period = PeriodNode(constants.STAY_DATE_RANGE)
            self._stay_date_range = self.add_child(period)
        return self._stay_date_range
    stay_date_range = property(_get_stay_date_range)

    def _get_rate_range(self):
        if not self._rate_range:
            self._rate_range = self.add_child(RateRange())
        return self._rate_range
    rate_range = property(_get_rate_range)

    def _get_room_stay_candidates(self):
        if not self._room_stay_candidates:
            room_stay = XmlNode(constants.ROOM_STAY_CANDIDATES)
            self._room_stay_candidates = self.add_child(room_stay)
        return self._room_stay_candidates
    room_stay_candidates = property(_get_room_stay_candidates)

    def _get_rate_plan_candidates(self):
        if not self._rate_plan_candidates:
            rate_plan = XmlNode(constants.RATE_PLAN_CANDIDATES)
            self._rate_plan_candidates = self.add_child(rate_plan)
        return self._rate_plan_candidates
    rate_plan_candidates = property(_get_rate_plan_candidates)

    def _get_tpa_extensions(self):
        if not self._tpa_extensions:
            self._tpa_extensions = self.add_child(TPAExtensions())
        return self._tpa_extensions
    tpa_extensions = property(_get_tpa_extensions)

    def add_room_stay_candidate(self, quantity=None):
        room_id = len(self.room_stay_candidates.element.childNodes)
        attributes = {constants.ROOM_ID: room_id}
        if quantity:
            attributes[constants.QUANTITY] = quantity
        room_stay = RoomStayCandidate(**attributes)
        return self.room_stay_candidates.add_child(room_stay)

    def add_rate_plan_candidate(self, rate_plan_code):
        rate_plan = RatePlanCandidate()
        rate_plan_candidate = self.rate_plan_candidates.add_child(rate_plan)
        rate_plan_candidate.rate_plan_code = rate_plan_code
        return rate_plan_candidate

class HotelAvailRQ(XmlNode):
    def __init__(self, **kwargs):
        kwargs[constants.XMLNS] = "http://www.opentravel.org/OTA/2003/05"
        url = "http://www.w3.org/2001/XMLSchema-instance"
        kwargs[constants.XMLNS_XSI] = url
        url = "http://www.opentravel.org/OTA/2003/05 OTA_HotelAvailRQ.xsd"
        kwargs[constants.XSI_SCHEMALOCATION] = url
        XmlNode.__init__(self, constants.OTA_HOTELAVAILRQ, **kwargs)
        self.pos = self.add_child(POS())
        avl_req_segs_node = XmlNode(constants.AVAIL_REQUEST_SEGMENTS)
        avl_req_segs = self.add_child(avl_req_segs_node)
        avl_req_seg_node = XmlNode(constants.AVAIL_REQUEST_SEGMENT)
        avl_req_seg = avl_req_segs.add_child(avl_req_seg_node)
        hsc_node = XmlNode(constants.HOTEL_SEARCH_CRITERIA)
        self._hotel_search_criteria = avl_req_seg.add_child(hsc_node)

    def _set_info_source(self, info_source):
        parent_node = self._hotel_search_criteria.parent
        parent_node.set_attribute(constants.INFO_SOURCE, info_source)
    info_source = property(fset=_set_info_source)

    def _get_hsc(self):
        return self._hotel_search_criteria
    hotel_search_criteria = property(_get_hsc)

    def add_criterion(self):
        return self._hotel_search_criteria.add_child(Criterion())
