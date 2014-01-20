#!/usr/bin/env python

"""
This module contains the base xml Node and Period classes
"""

from xml.dom.minidom import getDOMImplementation

from date import Period

from constants import START, END

class XmlNode(object):
    """
    the name of the class will define the name of the node by default.
    classes inheriting this class will have their name set.
    """
    _impl = getDOMImplementation()
    def __init__(self, name=None, **attributes):
        if not name:
            name = self.__class__.__name__
        self._doc = XmlNode._impl.createDocument(None, name, None)
        self.element = self._doc.documentElement
        for key, value in attributes.items():
            self.set_attribute(key, value)
        self.parent = None

    def set_attribute(self, key, value):
        self.element.setAttribute(key, str(value))

    def set_parent(self, parent_node):
        self.parent = parent_node

    def add_child(self, child_node):
        child_node.set_parent(self)
        self.element.appendChild(child_node.element)
        return child_node

    def add_text(self, data):
        text = self._doc.createTextNode(data)
        self.element.appendChild(text)
        return text

    def __repr__(self):
        return self.element.toxml()

class PeriodNode(XmlNode):
    def __init__(self, *args, **kwargs):
        XmlNode.__init__(self, *args, **kwargs)
        self._period = None
        self.set_period(Period())

    def get_period(self):
        return self._period

    def set_period(self, period):
        self.set_attribute(START, period.start)
        self.set_attribute(END, period.end)
        self._period = period

    period = property(get_period, set_period)
