import unittest as u
import main as m


class MyTestCase(u.TestCase):
    def test01(self):
        self.assertFalse(m.check(['12', '56', '9715']))

    def test02(self):
        self.assertFalse(m.check(['137', '1', '8468']))

    def test03(self):
        self.assertFalse(m.check(['198', '65', '13']))

    def test04(self):
        self.assertFalse((m.check(['000', '51', '3854'])))

    def test05(self):
        self.assertFalse((m.check(['666', '17', '3546'])))

    def test06(self):
        self.assertFalse((m.check(['943', '34', '1389'])))

    def test07(self):
        self.assertFalse((m.check(['123', '00', '4683'])))

    def test08(self):
        self.assertFalse((m.check(['123', '09', '0000'])))

    def test09(self):
        self.assertTrue((m.check(['357', '54', '9878'])))

    def test10(self):
        self.assertFalse((m.string_validation('13?-48-118/')))

    def test11(self):
        self.assertFalse((m.string_validation('12-5-384')))

    def test12(self):
        self.assertFalse((m.string_validation('159-w4-3848')))

    def test13(self):
        self.assertTrue((m.string_validation('123-45-6789')))


def run():
    suite = u.TestLoader().loadTestsFromTestCase(MyTestCase)
    u.TextTestRunner(verbosity=3).run(suite)

run()