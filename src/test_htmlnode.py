import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode("a", "some text", None, {"class": "link", "href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' class="link" href="https://www.google.com"')

    def test_is_none(self):
        node1 = HTMLNode(None, "some text", ['child1'], {"class": "link", "href": "https://www.google.com"})
        node2 = HTMLNode("a", None, ['child1'], {"class": "link", "href": "https://www.google.com"})
        node3 = HTMLNode("a", "some text", None, {"class": "link", "href": "https://www.google.com"})
        node4 = HTMLNode("a", "some text", ['child1'], None)
        self.assertIsNone(node1.tag)
        self.assertIsNone(node2.value)
        self.assertIsNone(node3.children)
        self.assertIsNone(node4.props)
    
    def test_leaf(self):
        node = LeafNode("p", "This is a paragraph of text.", None, None)
        self.assertEqual(node.to_html(), '<p>This is a paragraph of text.</p>')


    
        


if __name__ == "__main__":
    unittest.main()