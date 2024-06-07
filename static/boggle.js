class BoggleGame {

    constructor(boardId, secs = 60) {
        this.secs = secs;
        this.showTimer();
        this.score = 0;
        this.words = new Set();
        this.board = $("#" + boardId);

        // ticks every 1000 millisecond
        this.timer = setInterval(this.tick.bind(this), 1000);

        $(".addWord", this.board).on("submit", this.handleSubmit.bind(this));
    }
    // Displays a word from the list of words
    showWord(word) {
        $(".words", this.board).append($("<li>", { text: word }));
    }
    
    // Displays the score
    showScore() {
        $(".score", this.board).text(this.score);
    }

    // Displays a status message
    showMessage(msg, cls) {
        $(".msg", this.board)
        .text(msg)
        .removeClass()
        .addClass(`msg ${cls}`);
    }

    // Gets submission of score. If needs to update, updates
    async handleSubmit(e) {
        e.preventDefault();
        const $word = $(".word", this.board);

        let word = $word.val();
        if (!word) return;

        if (this.words.has(word)) {
            this.showMessage(`Already found ${word}`, "error");
            return;
        }


        const res = await axios.get("/check-word", { params: { word: word }});
        if (res.data.result === "not-word") {
            this.showMessage(`${word} is not a valid word`, "error");
        } else if (res.data.result === "not-on-board") {
            this.showMessage(`${word} is not a valid word`, "error");
        } else {
            this.showWord(word);
            this.score += word.length;
            this.showScore();
            this.words.add(word);
            this.showMessage(`Add: ${word}`, "ok")
        }

        $word.val("").focus();
    }
    // Displays and updates timer
    showTimer() {
        $(".timer", this.board).text(this.secs);
    }

    // Seconds passing in game
    async tick() {
        this.secs -= 1;
        this.showTimer();

        if (this.secs === 0) {
            clearInterval(this.timer);
            await this.scoreGame();
        }
    }

    // end of game display

    async scoreGame() {
        $(".addWord", this.board).hide();
        const res = await axios.post("/post-score", { score: this.score });
        if (res.data.newRecord) {
            this.showMessage(`New record: ${this.score}`, "ok");
        } else {
            this.showMessage(`Final score: ${this.score}`, "ok");
        }
    }
}