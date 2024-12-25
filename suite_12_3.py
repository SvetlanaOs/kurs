import unittest
import modul_12_3
import tests_12_3
runn_tourn = unittest.TestSuite()
runn_tourn.addTest(unittest.TestLoader().loadTestsFromTestCase(modul_12_3.RunnerTest))
runn_tourn.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runn_tourn)