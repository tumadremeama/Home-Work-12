import unittest


def skip_if_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            print(f'Тесты в этом кейсе заморожены: {test_func.__name__}')
            raise unittest.SkipTest('Тесты в этом кейсе заморожены')
        return test_func(self, *args, **kwargs)
    return wrapper


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
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_run(self):
        runner = Runner('Усейн')
        runner.run()
        self.assertGreater(runner.distance, 0)

    @skip_if_frozen
    def test_walk(self):
        runner = Runner('Андрей')
        runner.walk()
        self.assertGreater(runner.distance, 0)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_fist_tournament(self):
        runner1 = Runner('Усейн', 10)
        runner2 = Runner('Андрей', 9)
        tournament = Tournament(90, runner1, runner2)
        results = tournament.start()
        self.assertEqual(len(results), 2)

    @skip_if_frozen
    def test_second_tournament(self):
        runner1 = Runner('Ник', 3)
        runner2 = Runner('Андрей', 9)
        tournament = Tournament(90, runner1, runner2)
        results = tournament.start()
        self.assertEqual(len(results), 2)

    @skip_if_frozen
    def test_third_tournament(self):
        runner1 = Runner('Усейн', 10)
        runner2 = Runner('Ник', 3)
        tournament = Tournament(90, runner1, runner2)
        results = tournament.start()
        self.assertEqual(len(results), 2)
