from flask import Flask, request, render_template, jsonify, redirect, url_for, session
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SPRINGBOARD'
boggle_game = Boggle()

@app.route('/')
def index():
    """Show the game board."""
    board = boggle_game.make_board()
    session['board'] = board
    session['submitted_words'] = []
    return render_template('index.html', board=board)

@app.route('/check-word', methods=['POST'])
def check_word():
    """Check if a word is on the board."""
    word = request.json['word']
    board = session.get('board', [])
    submitted_words = session.get('submitted_words', [])

    if word in submitted_words:
        return jsonify({'result': 'already-submitted'})

    result = boggle_game.check_valid_word(board, word)

    if result == 'ok':
        submitted_words.append(word)
        session['submitted_words'] = submitted_words
        
    return jsonify({'result': result})

@app.route('/end-game', methods=['POST'])
def end_game():
    """End game screen."""
    score = request.json['score']
    high_score = session.get('high_score', 0)
    num_plays = session.get('num_plays', 0) + 1

    # Update high score if necessary
    session['high_score'] = max(score, high_score)
    session['num_plays'] = num_plays

    return jsonify({'high_score': session['high_score'], 'num_plays': session['num_plays']})

if __name__ == '__main__':
    app.run(debug=True)