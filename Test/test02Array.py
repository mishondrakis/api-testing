import unittest
import pytest

class Test2(unittest.TestCase):

    @pytest.mark.run(order=1)
    def testa(self):
        assert False
    @pytest.mark.run(order=2)
    def testB(self):
        pass
    @pytest.mark.dependency(depend = ['Test::testa'])
    def testC(self):
        pass
    @pytest.mark.run(order=3)
    def testD(self):
        assert False
