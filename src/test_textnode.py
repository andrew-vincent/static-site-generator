import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_uneq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is NOT a text node", "bold")
        self.assertNotEqual(node, node2) == False

    def test_uneq_type(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is NOT a text node", "italic")
        self.assertNotEqual(node, node2) == False
    
    def test_url_none(self):
        node = TextNode("This is a text node", "bold")
        self.assertIsNone(node.url)

    
        


if __name__ == "__main__":
    unittest.main()