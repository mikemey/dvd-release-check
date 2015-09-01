import unittest

test_modules = [
    'test_dlc_releases',
    'test_imdb_lookup',
    'test_imdb_ratings',
    'test_mail_gen'
]

suite = unittest.TestSuite()

for t in test_modules:
    suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

unittest.TextTestRunner().run(suite)
