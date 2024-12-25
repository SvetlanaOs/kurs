import runner
import unittest
class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
       self.all_results = {}

    def setUp(self):
        self.object1 = runner.Runner('Усейн',10)
        self.object2 = runner.Runner('Андрей', 9)
        self.object3 = runner.Runner('Ник', 3)

    def test_turn1(self):
        turn_1= runner.Tournament(90, self.object1, self.object3)
        results = turn_1.start()
        self.assertTrue(results[max(results.keys())].name == 'Ник')
        self.all_results[1]=results

    def test_turn2(self):
        turn_1= runner.Tournament(90, self.object2, self.object3)
        results = turn_1.start()
        self.assertTrue(results[max(results.keys())].name == 'Ник')
        self.all_results[2] = results

    def test_turn3(self):
        turn_1= runner.Tournament(90, self.object1, self.object2, self.object3)
        results = turn_1.start()
        self.assertTrue(results[max(results.keys())].name == 'Ник')
        self.all_results[3] = results

    @classmethod
    def tearDownClass(self):
        for test_turn in self.all_results:
            print({k: str(v) for k, v in self.all_results[test_turn].items()})

if __name__ == "__main__":
    unittest.main()