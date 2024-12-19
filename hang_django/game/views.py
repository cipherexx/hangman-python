from django.http import JsonResponse
from django.shortcuts import render
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from logic.gamelogic import HangmanGame
from logic.randomwords import getRandomWords

game_instance = None

def index(request):
    # Start a new game with a random word
    global game_instance
    word = getRandomWords()
    game_instance = HangmanGame(word)
    
    return render(request, 'game/index.html', {'game_state': game_instance.get_state()})

def play_game(request):
    global game_instance
    if request.method == 'POST':
        letter = request.POST.get('letter')
        game_instance.process_chance(letter)
        return JsonResponse({'game_state': game_instance.get_state()})

def give_in(request):
    global game_instance
    if request.method == 'POST':
        game_instance.game_status = 'lost'  # End the game
        return JsonResponse({'game_state': game_instance.get_state()})

def new_game(request):
    global game_instance
    if request.method == 'POST':
        word = getRandomWords()  # Start a new game
        game_instance = HangmanGame(word)
        return JsonResponse({'game_state': game_instance.get_state()})
