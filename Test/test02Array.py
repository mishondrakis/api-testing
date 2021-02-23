import unittest
import pytest

class Test2(unittest.TestCase):

    @pytest.mark.run(order=1)
    def testa(self):
        pass
    @pytest.mark.run(order=2)
    def testB(self):
        pass
    @pytest.mark.run(order=4)
    def testC(self):
        pass
    @pytest.mark.run(order=3)
    def testD(self):
        pass
