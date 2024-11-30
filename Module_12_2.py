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
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    def setUp(self):
        self.runner1 = Runner('Усейн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    def test_tournament_finishers(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()

        self.assertEqual(len(results), 3)

        self.assertEqual(results[1].name, 'Усейн')
        self.assertEqual(results[2].name, 'Андрей')
        self.assertEqual(results[3].name, 'Ник')

    def test_runner_distance(self):
        tournament = Tournament(90, self.runner1)
        tournament.start()
        self.assertGreaterEqual(self.runner1.distance, 90)

    def test_runner_initial_distance(self):
        self.assertEqual(self.runner1. distance, 0)
        self.runner1.run()
        self.assertGreater(self.runner1.distance, 0)


if __name__ == '__main__':
    unittest.main()

