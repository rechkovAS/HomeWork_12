import unittest
import runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """ test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
        Далее вызывается метод walk у этого объекта 10 раз.
        После чего методом assertEqual сравнивается distance этого объекта со значением 50."""
        run_1 = runner.Runner('Run_1')
        for i in range(10):
            run_1.walk()
        self.assertEqual(run_1.distance, 50)
#
    def test_run(self):
        """ test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
        Далее вызывается метод run у этого объекта 10 раз.
        После чего методом assertEqual сравнивается distance этого объекта со значением 100."""
        run_2 = runner.Runner('Run_2')
        for i in range(10):
            run_2.run()
        self.assertEqual(run_2.distance, 100)

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

if __name__ == "__main__":
    unittest.main()