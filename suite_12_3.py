import unittest
import test_runner_and_tour_from_12_3
runner_test = unittest.TestSuite
runner_test.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner_and_tour_from_12_3.RunnerTest))
runner_test.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner_and_tour_from_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runner_test)


