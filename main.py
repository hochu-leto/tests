import unittest
from unittest.mock import patch

from app import get_all_doc_owners_names, get_doc_owner_name, remove_doc_from_shelf, get_doc_shelf, \
    move_doc_to_shelf, add_new_doc, show_all_docs_info


class TestSomething(unittest.TestCase):

    @patch('builtins.input', lambda *args: '11-2')
    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name(), "Геннадий Покемонов")

    def test_get_all_owners_name(self):
        self.assertIn("Геннадий Покемонов", get_all_doc_owners_names())

    @patch('builtins.input', lambda *args: '11-2')
    def test_remove_doc_from_shelf(self):
        directory_number = get_doc_shelf()
        print(directory_number)
        remove_doc_from_shelf('11-2')
        self.assertNotEqual(get_doc_shelf(), directory_number)

    @patch('builtins.input', lambda *args: '11-2')
    def test_move_doc_from_shelf(self):
        directory_number = get_doc_shelf()
        move_doc_to_shelf()
        self.assertNotEqual(get_doc_shelf(), directory_number)
        self.assertEqual(get_doc_shelf(), '11-2')

    @patch('builtins.input', lambda *args: '22-2')
    def test_add_new_doc(self):
        add_new_doc()
        self.assertEqual(get_doc_owner_name(), "22-2")
        self.assertIn("22-2", get_all_doc_owners_names())
        self.assertEqual(get_doc_shelf(), '22-2')
        show_all_docs_info()


if __name__ == '__main__':
    unittest.main()
