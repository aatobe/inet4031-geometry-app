import unittest
import sphere
import math

class sphereTest(unittest.TestCase):

    #these need to be updated for a sphere
    def test_volume1(self):
        self.assertAlmostEqual(sphere.volume(1), (4/3) * math.pi * 1**3)

    def test_volume2(self):
        self.assertAlmostEqual(sphere.volume(3), (4/3) * math.pi * 3**3)

    def test_volume3(self):
        self.assertAlmostEqual(sphere.volume(0), 0.0)

    #failing test
    #def test_volume3(self):
        #assert(sphere.volume(10,1000) == ??)


if __name__ == '__main__':
    unittest.main()
