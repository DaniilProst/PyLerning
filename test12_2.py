import unittest


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

    def test_tournament_test(self):
        tournament1 = Tournament(90, self.Usein, self.Nik)
        results = tournament1.start()
        self.all_results['T1'] = results
        fastest_runner = self.all_results['T1'][1]
        self.assertTrue(fastest_runner == "Усэйн")

    def test_tournament_test2(self):
        tournament2 = Tournament(90, self.Andrey, self.Nik)
        results = tournament2.start()
        self.all_results['T2'] = results
        fastest_runner = self.all_results['T2'][1]
        self.assertTrue(fastest_runner == "Андрей")

    def test_tournament_test3(self):
        tournament3 = Tournament(90, self.Usein, self.Andrey, self.Nik)
        results = tournament3.start()
        self.all_results['T3'] = results
        fastest_runner = self.all_results['T3'][1]
        self.assertTrue(fastest_runner == "Усэйн")


if __name__ == "__main__":
    unittest.main()
