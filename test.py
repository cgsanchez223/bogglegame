from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def setUp(self):
        """Before tests"""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Everything in session"""

        with self.client:
            res = self.client.get('/')
            self.assertIn('board', session)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('plays'))
            self.assertIn(b'<p>High Score:', res.data)
            self.assertIn(b'Score:', res.data)
            self.assertIn(b'Seconds Left:', res.data)

    def test_valid_word(self):
        """Test if word is valid"""

        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [["C", "A", "T", "T", "T"],
                                ["C", "A", "T", "T", "T"],
                                ["C", "A", "T", "T", "T"],
                                ["C", "A", "T", "T", "T"],
                                ["C", "A", "T", "T", "T"]]
                res = self.client.get('/check-word?word=cat')
                self.assertEqual(res.json['result'], 'ok')


    def test_invalid_word(self):
        """Test if word is in dictionary"""

        self.client.get('/')
        res = self.client.get('/check-word?word=impossible')
        self.assertEqual(res.json['result'], 'not-on-board')


    def non_english_word(self):
        """Test if words is foreign"""

        self.client.get('/')
        res = self.client.get('/check-word?word=gibberish')
        self.assertEqual(res.json['result'], 'not-word')
                


