import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner = Runner('TestWalk')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner1 = Runner('TestRun')
        for i in range(10):
            runner1.run()
        self.assertEqual(runner1.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runnerWalk = Runner('walk')
        runnerRun = Runner('Run')
        for i in range(10):
            runnerWalk.walk()
            runnerRun.run()
        self.assertNotEqual(runnerWalk.distance, runnerRun.distance)


if __name__ == "__main__":
    unittest.main()


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Usein = Runner('Усэйн', 10)
        self.Andrey = Runner('Андрей', 9)
        self.Nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for tournament, results in cls.all_results.items():
            print(f"{results}")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_test(self):
        tournament1 = Tournament(90, self.Usein, self.Nik)
        results = tournament1.start()
        self.all_results['T1'] = results
        fastest_runner = self.all_results['T1'][1]
        self.assertTrue(fastest_runner == "Усэйн")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_test2(self):
        tournament2 = Tournament(90, self.Andrey, self.Nik)
        results = tournament2.start()
        self.all_results['T2'] = results
        fastest_runner = self.all_results['T2'][1]
        self.assertTrue(fastest_runner == "Андрей")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_test3(self):
        tournament3 = Tournament(90, self.Usein, self.Andrey, self.Nik)
        results = tournament3.start()
        self.all_results['T3'] = results
        fastest_runner = self.all_results['T3'][1]
        self.assertTrue(fastest_runner == "Усэйн")

    if __name__ == "__main__":
        unittest.main()
