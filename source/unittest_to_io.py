import unittest


class WidgetTestCase(unittest.TestCase):


    def test_default_widget_size(self):
        self.assertEqual((50,50), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.assertEqual((100,150), (100,150),
                         'wrong size after resize')

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    from io import StringIO
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=2)
    runner.run(suite())
    stream.seek(0)
    print('Test output\n' + stream.read())
