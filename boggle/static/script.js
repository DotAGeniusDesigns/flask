$(document).ready(function() {
    let score = 0; // Initialize score
    let timeLeft = 60; // Initialize timer
    let highScore = localStorage.getItem('high_score') || 0;
    let numPlays = localStorage.getItem('num_plays') || 0;
    $('#high-score').text('High Score: ' + highScore);
    $('#num-plays').text('Number of Plays: ' + numPlays);
    $('#timer').text(`${timeLeft} seconds remaining`); // Display initial time

    $('#guess-form').on('submit', function(e) {
        e.preventDefault();
        
        const word = $('input[name="guess"]').val();
        $('input[name="guess"]').val(''); // Clear input
        
        console.log("Submitting word:", word);
        axios.post('/check-word', { word: word })
            .then(function (response) {
                const result = response.data.result;
                let message = '';
                if (result === 'ok') {
                    message = 'Nice!';
                    let wordLength = word.length;
                    score += wordLength; // Update score
                    $('#score').text(`Score: ${score}`); // Display score
                } else if (result === 'not-on-board') {
                    message = 'Sorry, that word does not appear on the board,';
                } else if (result === 'not-word') {
                    message = 'Not a valid word.';
                } else if (result === 'already-submitted') {
                    message = 'This word has already been submitted.';
                }
                
                $('#result').stop(true, true).show().text(message).delay(2000).fadeOut(400);

                if (timeLeft <= 0) {
                    clearInterval(timerId);
                    $('#guess-form button').prop('disabled', true);
                    $('#timer').text('Time is up!');
                    $('#play-again').show(); // Show the play again button
                }                
            })
            .catch(function(error) {
                console.log(error);
                $('#result').text('There was an error processing your request.');
            });
    });

    let timerId = setInterval(function() {
        timeLeft -= 1;
        $('#timer').text(`${timeLeft} seconds remaining`);
        
        if (timeLeft <= 0) {
            clearInterval(timerId);
            $('#guess-form button').prop('disabled', true);
            $('#timer').text('Time is up!');
            $('#play-again').show(); // Show the play again button
        
            // The AJAX call should be here, outside of the $('#play-again').click() handler
            axios.post('/end-game', { score: score })
                .then(function(response) {
                    localStorage.setItem('high_score', response.data.high_score);
                    localStorage.setItem('num_plays', response.data.num_plays);
                    $('#high-score').text('High Score: ' + response.data.high_score);
                    $('#num-plays').text('Number of Plays: ' + response.data.num_plays);
                }).catch(function(error) {
                    console.log('Error posting end game:', error);
                });
        }        
    }, 1000);

    $('#play-again').click(function() {
        window.location.reload(); // Reloads the current page
    });
});



