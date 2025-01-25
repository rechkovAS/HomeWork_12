import unittest
import runner

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        """ test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
        Далее вызывается метод walk у этого объекта 10 раз.
        После чего методом assertEqual сравнивается distance этого объекта со значением 50."""
        run_1 = runner.Runner('Run_1')
        for i in range(10):
            run_1.walk()
        self.assertEqual(run_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        """ test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
        Далее вызывается метод run у этого объекта 10 раз.
        После чего методом assertEqual сравнивается distance этого объекта со значением 100."""
        run_2 = runner.Runner('Run_2')
        for i in range(10):
            run_2.run()
        self.assertEqual(run_2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        """ test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
        Далее 10 раз у объектов вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными,
        используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
        Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку."""
        run_1 = runner.Runner('Run_1')
        run_2 = runner.Runner('Run_2')
        for i in range(10):
            run_1.walk()
            run_2.run()
        self.assertNotEqual(run_1.distance, run_2.distance)

import runner_and_tournament as rat
class TournamentTest(unittest.TestCase):
    is_frozen = True
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
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start1(self):
        tornament_1 = rat.Tournament(90, self.run_1, self.run_3)
        ts = tornament_1.start()
        ts_name = {x: y.name for x, y in ts.items()}
        self.assertTrue('Ник' == ts_name[2])
        TournamentTest.all_results['1й забег'] = ts_name
        return TournamentTest.all_results
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start2(self):
        tornament_2 = rat.Tournament(90, self.run_2, self.run_3)
        ts = tornament_2.start()
        ts_name = {x: y.name for x, y in ts.items()}
        self.assertTrue('Ник' == ts_name[2])
        TournamentTest.all_results['2й забег'] = ts_name
        return TournamentTest.all_results
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start3(self):
        tornament_3 = rat.Tournament(90, self.run_1, self.run_2, self.run_3)
        ts = tornament_3.start()
        ts_name = {x: y.name for x, y in ts.items()}
        self.assertTrue(ts_name[3] == str(self.run_3))
        TournamentTest.all_results['3й забег'] = ts_name
        return TournamentTest.all_results

if __name__ == "__main__":
    unittest.main()