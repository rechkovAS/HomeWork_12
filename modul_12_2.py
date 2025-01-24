import unittest
import runner_and_tournament as rat
class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}


    def setUp(self):
        self.run_1 = rat.Runner('Усэйн', 10)
        self.run_2 = rat.Runner('Андрей', 9)
        self.run_3 = rat.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):# tearDownClass - метод, где выводятся all_results по очереди в столбец.
        print()
        for result in cls.all_results.values():
            print(result)

    def test_start1(self):
        tornament_1 = rat.Tournament(90, self.run_1, self.run_3)
        ts = tornament_1.start()
        ts_name = {x: y.name for x, y in ts.items()}
        self.assertTrue('Ник' == ts_name[2])
        TournamentTest.all_results['1й забег'] = ts_name
        return TournamentTest.all_results

    def test_start2(self):
        tornament_2 = rat.Tournament(90, self.run_2, self.run_3)
        ts = tornament_2.start()
        ts_name = {x: y.name for x, y in ts.items()}
        self.assertTrue('Ник' == ts_name[2])
        TournamentTest.all_results['2й забег'] = ts_name
        return TournamentTest.all_results

    def test_start3(self):
        tornament_3 = rat.Tournament(90, self.run_1, self.run_2, self.run_3)
        ts = tornament_3.start()
        ts_name = {x: y.name for x, y in ts.items()}
        self.assertTrue(ts_name[3] == str(self.run_3))
        TournamentTest.all_results['3й забег'] = ts_name
        return TournamentTest.all_results

if __name__ == '__main__':
    unittest.main()
