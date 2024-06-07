from flask import Flask, request, render_template, jsonify, session
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = "abc123"

boggle_game = Boggle()

@app.route("/")
def index():
    """Home - Displays Board"""

    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("highscore", 0)
    plays = session.get("plays", 0)

    return render_template("index.html", board=board, highscore=highscore, plays=plays)


@app.route("/check-word")
def check_word():
    """Checks to see if the word is in provided list"""

    word = request.args["word"]
    board = session["board"]
    res = boggle_game.check_valid_word(board, word)

    return jsonify({'result': res})


@app.route("/post-score", methods=["POST"])
def post_score():
    """Gets score and updates it"""

    score = request.json["score"]
    highscore = session.get("highscore", 0)
    plays = session.get("plays", 0)

    session['plays'] = plays + 1
    session['highscore'] = max(score, highscore)

    return jsonify(newRecord=score > highscore)