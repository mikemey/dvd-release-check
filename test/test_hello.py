from unittest import TestCase

from hewo import Hello


class TestHello(TestCase):
    def test_greet(self):
        actual = Hello().greet("Hello", "you!")
        expected = "Hello to you!"
        self.assertEquals(actual, expected,
                          "Greetings didn't match:\n\tactual  : [{}]\n\texpected: [{}]".format(actual, expected))
