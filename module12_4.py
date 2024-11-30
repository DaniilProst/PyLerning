import logging
import unittest


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
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
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


logging.basicConfig(level=logging.INFO, filemode='w', filename="runner_tests.log", encoding='utf-8',
                    format='%asc_time)s| (%(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:

            runner = Runner('TestWalk', -10)
            for i in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"testwalk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner',exc_info= True)

    def test_run(self):
        try:

            runner1 = Runner(5)
            for i in range(10):
                runner1.run()
            self.assertEqual(runner1.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner',exc_info=True)

    def test_challenge(self):
        runnerWalk = Runner('walk')
        runnerRun = Runner('Run')
        for i in range(10):
            runnerWalk.walk()
            runnerRun.run()
        self.assertNotEqual(runnerWalk.distance, runnerRun.distance)


if __name__ == "__main__":
    unittest.main()
