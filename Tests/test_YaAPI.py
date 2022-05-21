import unittest
import YA_translater


class TestYandexTranslator(unittest.TestCase):
    def test_translate(self):
        self.assertEqual(YA_translater.translate_it('hi')['text'][0], 'привет')

    def test_request_code(self):
        self.assertEqual(YA_translater.translate_it('hi')['code'], 200)


if __name__ == '__main__':
    unittest.main()