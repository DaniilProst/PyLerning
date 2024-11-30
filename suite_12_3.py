import unittest
import tests_12_3

RunTests = unittest.TestSuite()
RunTests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
RunTests.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(RunTests)

