import unittest


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


class fibonacci_test(unittest.TestCase):
    def test_um(self):
        self.assertEqual(fibonacci(0), 0)

    def test_dois(self):
        self.assertEqual(fibonacci(1), 1)

    def test_tres(self):
        self.assertEqual(fibonacci(10), 55)


if __name__ == "__main__":
    unittest.main()
