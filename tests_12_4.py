import unittest
import logging
from runner import Runner


logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner('Андрей', -5)
            runner.walk()
            logging.info("'test_walk' выполнен успешно")
        except ValueError as e:
            logging.warning('Неверная скорость для Runner: %s', e)


    def test_run(self):
        try:
            runner = Runner(123, 5)
            runner.run()
            logging.info("'tests_run' выполнен успешно")
        except TypeError as e:
            logging.warning('Неверный тип данных дла объекта Runner: %s', e)


if __name__ == '__main__':
    unittest.main()