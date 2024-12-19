$(document).ready(function() {
    // Function to update the game state displayed on the page
    function updateGameState(gameState) {
        $('#word-state').text(gameState.state);
        $('#remaining-chances').text('Remaining chances: ' + gameState.rem_chances);
        $('#game-status').text(gameState.game_status);

        // Disable buttons when game is over
        if (gameState.game_status === 'won' || gameState.game_status === 'lost') {
            $('#alphabet-buttons').empty();  // Remove alphabet buttons
        }
    }

    // Retrieve the game state from the `game-state` script tag
    var initialGameState = JSON.parse(document.getElementById('game-state').textContent);

    // Initialize the game state on the page
    updateGameState(initialGameState);

    // Function to get the CSRF token from the page
    function getCsrfToken() {
        return $('input[name="csrfmiddlewaretoken"]').val();
    }

    // Function to make a guess (send letter to backend)
    function makeGuess(letter) {
        $.ajax({
            url: '/play-game/',  // Django URL
            method: 'POST',
            data: {
                'letter': letter,
                'csrfmiddlewaretoken': getCsrfToken()  // Include CSRF token
            },
            success: function(response) {
                updateGameState(response.game_state);  // Update state on success
            }
        });
    }

    // Function to give in and end the game
    function giveIn() {
        $.ajax({
            url: '/give-in/',  // Django URL
            method: 'POST',
            data: {
                'csrfmiddlewaretoken': getCsrfToken()  // Include CSRF token
            },
            success: function(response) {
                updateGameState(response.game_state);  // Update state on success
            }
        });
    }

    // Function to start a new game
    function startNewGame() {
        $.ajax({
            url: '/new-game/',  // Django URL
            method: 'POST',
            data: {
                'csrfmiddlewaretoken': getCsrfToken()  // Include CSRF token
            },
            success: function(response) {
                updateGameState(response.game_state);  // Update state on success
            }
        });
    }

    // Event handler for the "Give In" button
    $('#give-in-button').click(function() {
        giveIn();
    });

    // Event handler for the "New Game" button
    $('#new-game-button').click(function() {
        startNewGame();
    });

    // Dynamically create alphabet buttons for guesses
    for (let letter of 'abcdefghijklmnopqrstuvwxyz') {
        $('#alphabet-buttons').append('<button onclick="makeGuess(\'' + letter + '\')">' + letter + '</button>');
    }
});
