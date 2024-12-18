import runner
import unittest
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        object1 = runner.Runner('ex')
        for _ in range(10):
            object1.walk()
        self.assertEqual(object1.distance,50)
    def test_run(self):
        object2 = runner.Runner('ux')
        for _ in range(10):
            object2.run()
        self.assertEqual(object2.distance, 100)
    def test_challenge(self):
        object3 = runner.Runner('oh')
        object4 = runner.Runner('ah')
        for _ in range(10):
            object3.walk()
            object4.run()
        self.assertNotEqual(object3.distance, object4.distance)

if __name__ == "__main__":
    unittest.main()