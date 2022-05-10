import unittest
import main


class Testsmain(unittest.TestCase):

    def test_get_doc_owner_name(self):
        self.assertEqual(main.get_doc_owner_name('10006'), 'Аристарх Павлов')

    def test_add_new_doc(self):
        self.assertEqual(main.add_new_doc('7311', 'pass', 'Shamil', 2), 2)

    def test_delete_doc(self):
        self.assertTrue(main.delete_doc('10006'), None)