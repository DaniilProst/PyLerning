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
    def test_walk(self):
        runner = Runner('TestWalk')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner1 = Runner('TestRun')
        for i in range(10):
            runner1.run()
        self.assertEqual(runner1.distance,100)

    def test_challenge(self):
        runnerWalk = Runner('walk')
        runnerRun = Runner('Run')
        for i in range(10):
            runnerWalk.walk()
            runnerRun.run()
        self.assertNotEqual(runnerWalk.distance,runnerRun.distance)


if __name__ == "__main__":
    unittest.main()