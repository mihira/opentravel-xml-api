Open Travel XML API
==========================

Python API to easily generate Open Travel XML messages

## Basic Usage
```python
>>> from ota_xml_api.ota2011b import hotel_avail
>>> request = hotel_avail.HotelAvailRQ()
>>> str(request)
'<OTA_HotelAvailRQ xmlns="http://www.opentravel.org/OTA/2003/05" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opentravel.org/OTA/2003/05 OTA_HotelAvailRQ.xsd"><POS><Source><RequestorID/></Source><Source><RequestorID/></Source></POS><AvailRequestSegments><AvailRequestSegment><HotelSearchCriteria/></AvailRequestSegment></AvailRequestSegments></OTA_HotelAvailRQ>'
>>> request.info_source = 'Distribution'
>>> str(request)
'<OTA_HotelAvailRQ xmlns="http://www.opentravel.org/OTA/2003/05" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opentravel.org/OTA/2003/05 OTA_HotelAvailRQ.xsd"><POS><Source><RequestorID/></Source><Source><RequestorID/></Source></POS><AvailRequestSegments><AvailRequestSegment InfoSource="Distribution"><HotelSearchCriteria/></AvailRequestSegment></AvailRequestSegments></OTA_HotelAvailRQ>'
>>> criterion = request.add_criterion()
>>> str(request)
'<OTA_HotelAvailRQ xmlns="http://www.opentravel.org/OTA/2003/05" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opentravel.org/OTA/2003/05 OTA_HotelAvailRQ.xsd"><POS><Source><RequestorID/></Source><Source><RequestorID/></Source></POS><AvailRequestSegments><AvailRequestSegment InfoSource="Distribution"><HotelSearchCriteria><Criterion/></HotelSearchCriteria></AvailRequestSegment></AvailRequestSegments></OTA_HotelAvailRQ>'
>>> hotel = hotel_avail.HotelRef('ABCDE123', '1A')
>>> hotel.chain_code = 'AB'
>>> hotel.hotel_city_code = 'CDE'
>>> criterion.add_hotel_ref(hotel)
<HotelRef ChainCode="AB" HotelCityCode="CDE" HotelCode="ABCDE123" HotelCodeContext="1A"/>
>>> hotel = hotel_avail.HotelRef()
>>> hotel.chain_code = 'CD'
>>> criterion.add_hotel_ref(hotel)
<HotelRef ChainCode="CD"/>
>>> str(criterion)
'<Criterion><HotelRef ChainCode="AB" HotelCityCode="CDE" HotelCode="ABCDE123" HotelCodeContext="1A"/><HotelRef ChainCode="CD"/></Criterion>'
>>> str(request)
'<OTA_HotelAvailRQ xmlns="http://www.opentravel.org/OTA/2003/05" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opentravel.org/OTA/2003/05 OTA_HotelAvailRQ.xsd"><POS><Source><RequestorID/></Source><Source><RequestorID/></Source></POS><AvailRequestSegments><AvailRequestSegment InfoSource="Distribution"><HotelSearchCriteria><Criterion><HotelRef ChainCode="AB" HotelCityCode="CDE" HotelCode="ABCDE123" HotelCodeContext="1A"/><HotelRef ChainCode="CD"/></Criterion></HotelSearchCriteria></AvailRequestSegment></AvailRequestSegments></OTA_HotelAvailRQ>'
```

## Testing

_How do I run the project's automated tests?_

```shell
./run_tests.sh
```
