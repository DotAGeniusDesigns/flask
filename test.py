from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        # Set up test client
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Test that the homepage shows the board and session is set up correctly."""

        with self.client as client:
            response = client.get('/')
            self.assertIn('board', session)
            self.assertIsNone(session.get('high_score'))
            self.assertEqual(session.get('num_plays', 0), 0)
            self.assertIn(b'<div id="board">', response.data)
    
    def test_valid_word(self):
        """Test submitting a valid word."""

        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [["D", "O", "G", "G", "Y"], 
                                 ["D", "O", "G", "G", "Y"], 
                                 ["D", "O", "G", "G", "Y"], 
                                 ["D", "O", "G", "G", "Y"], 
                                 ["D", "O", "G", "G", "Y"]]
            response = client.post('/check-word', json={'word': 'dog'})
            self.assertEqual(response.json['result'], 'ok')

    def test_invalid_word(self):
        """Test submitting an invalid word."""
        
        with self.client as client:
            client.get('/')  # This sets up the session including the board
            response = client.post('/check-word', json={'word': 'impossibleword'})
            self.assertEqual(response.json['result'], 'not-word')

    def test_word_not_on_board(self):
        """Test submitting a valid dictionary word that is not on the board."""
        
        with self.client as client:
            client.get('/')
            response = client.post('/check-word', json={'word': 'python'})
            self.assertEqual(response.json['result'], 'not-on-board')

    def test_end_game(self):
        """Test the end game route updates the number of plays and possibly the high score."""

        with self.client as client:
            response = client.post('/end-game', json={'score': 10})
            self.assertEqual(session.get('num_plays'), 1)
            self.assertEqual(session.get('high_score'), 10)

            # Try a lower score, high score should not change
            client.post('/end-game', json={'score': 5})
            self.assertEqual(session.get('high_score'), 10)
