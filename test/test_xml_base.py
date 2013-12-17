#!/usr/bin/env python

from ota_xml_api.util.xml_base import XmlNode, PeriodNode
from ota_xml_api.util.date import Period
import unittest

class XmlNodeTC(unittest.TestCase):

    def test_init_node(self):
        raw_node = XmlNode()
        self.assertEqual(str(raw_node), '<XmlNode/>')
        raw_node = XmlNode(one=1)
        self.assertEqual(str(raw_node), '<XmlNode one="1"/>')
        attr = {'one':1}
        raw_node = XmlNode(**attr)
        self.assertEqual(str(raw_node), '<XmlNode one="1"/>')
        raw_node = XmlNode('Name')
        self.assertEqual(str(raw_node), '<Name/>')
        raw_node = XmlNode('Name', **attr)
        self.assertEqual(str(raw_node), '<Name one="1"/>')

    def test_set_attribute(self):
        raw_node = XmlNode()
        raw_node.set_attribute('two', 2)
        self.assertEqual(str(raw_node), '<XmlNode two="2"/>')
        raw_node.set_attribute('two', 3)
        self.assertEqual(str(raw_node), '<XmlNode two="3"/>')
        raw_node.set_attribute('two', 'TWO')
        self.assertEqual(str(raw_node), '<XmlNode two="TWO"/>')

    def test_add_child(self):
        parent = XmlNode('Parent')
        child = parent.add_child(XmlNode('Child'))
        self.assertEqual(str(parent), '<Parent><Child/></Parent>')
        child.set_attribute('hasParent', 'True')
        child.parent.set_attribute('hasChildren', 'True')
        self.assertEqual(str(parent), '<Parent hasChildren="True"><Child hasParent="True"/></Parent>')

    def test_add_text(self):
        raw_node = XmlNode()
        raw_node.add_text('RAW')
        self.assertEqual(str(raw_node), '<XmlNode>RAW</XmlNode>')

class PeriodNodeTC(unittest.TestCase):
    def test_init_node(self):
        node = PeriodNode('PeriodNodeName')
        self.assertEqual(str(node), '<PeriodNodeName End="%s" Start="%s"/>' % (node.period.end, node.period.start))
        node = PeriodNode()
        self.assertEqual(str(node), '<PeriodNode End="%s" Start="%s"/>' % (node.period.end, node.period.start))
        node.period = Period(3)
        self.assertEqual(str(node), '<PeriodNode End="%s" Start="%s"/>' % (node.period.end, node.period.start))

if __name__ == '__main__':
    unittest.main()
