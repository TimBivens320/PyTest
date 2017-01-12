from unittest import TestCase

from SpecificFile import SpecificFile


class TestSpecificFile(TestCase):
    def test___init__(self):
        d = SpecificFile("test")
        self.assertEquals(d.name, "test")
