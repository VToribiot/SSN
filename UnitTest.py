import unittest as u
import main as m


class MyTestCase(u.TestCase):
    def test01(self):
        self.assertTrue(m.check(['12', '56', '9715']))

    def test02(self):
        self.assertTrue(m.check(['137', '1', '8468']))

    def test03(self):
        self.assertTrue(['137', '1', '8468'])


def run():
    suite = u.TestLoader().loadTestsFromTestCase(MyTestCase)
    u.TextTestRunner(verbosity=3).run(suite)

run()