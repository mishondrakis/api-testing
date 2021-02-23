import unittest


class Test1(unittest.TestCase):
    def test1(self):
        print("hello this is me again")

    def test2(self):
        print(20 + 20)

    def test3(self):
        print("iskam water")

    def test4(self):
        print("more water for me ")

    def tearDown(self) -> None:
        print("this is a teardown")

    def setUp(self) -> None:
        print("first of all")