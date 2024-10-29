import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add_1(self):
        time1 = data.Time(4,5,6)
        time2 = data.Time(50,40,30)
        result = lab5.time_add(time1,time2)
        expected = data.Time(54,45,36)
        self.assertEqual(expected, result)

    def test_time_add_2(self):
        time1 = data.Time(4,45,16)
        time2 = data.Time(50,40,50)
        result = lab5.time_add(time1,time2)
        expected = data.Time(54,86,6)
        self.assertEqual(expected, result)

    # Part 4
    def test_is_descending_1(self):
        lista = [4,3,2,2,1]
        result = lab5.is_descending(lista)
        expected = True
        self.assertEqual(expected, result)

    def test_is_descending_2(self):
        lista = [2,3,2,2,1]
        result = lab5.is_descending(lista)
        expected = False
        self.assertEqual(expected, result)

    # Part 5
    def test_largest_between_1(self):
        lista = [1,2,3,4,5,6,7,8,9,10]
        result = lab5.largest_between(lista,2,7)
        expected = 8
        self.assertEqual(expected,result)

    def test_largest_between_2(self):
        lista = [1,2,3,4,5,6,7,8,9,10]
        result = lab5.largest_between(lista,1,1)
        expected = 2
        self.assertEqual(expected,result)

    def test_largest_between_3(self):
        lista = [1,2,3,4,5,4,3,2,1]
        result = lab5.largest_between(lista,6,2)
        expected = 5
        self.assertEqual(expected,result)

    # Part 6
    def test_furthest_from_origin_1(self):
        lista = [data.Point(4,5),data.Point(3,2),data.Point(6,8), data.Point(1,1)]
        result = lab5.furthest_from_origin(lista)
        expected = 2
        self.assertEqual(expected,result)

    def test_furthest_from_origin_2(self):
        lista = [data.Point(4,5),data.Point(-90,-8),data.Point(6,9), data.Point(-16,16)]
        result = lab5.furthest_from_origin(lista)
        expected = 1
        self.assertEqual(expected,result)

if __name__ == '__main__':
    unittest.main()
