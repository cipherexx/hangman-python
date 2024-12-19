'''
First we make  the game state. The format is as follows(example):
{
state="a__le",
word="apple",
rem_chances=2,
guessed_letters=[],
game_status=""(ongoing,won,lost,..)(add more if i find)
}
'''

class HangmanGame:
    def __init__(self, word, max_chances=6):
        self.word=word
        self.rem_chances=max_chances
        self.guessed_letters=[]
        self.state="_"*len(word)
        self.game_status="ongoing"
    def process_chance(self,guess):
        '''Process user's input and update the current game state'''
        if guess in self.guessed_letters:
            '''TODO: add a alert/effect to user that he guessed an already guessed letter'''
            return
        self.guessed_letters.append(guess)
        '''TODO: Check if user inputted a letter or something else'''
        if guess in self.word:
            state_list=list(self.state)
            for i in range(len(self.word)):
                if self.word[i]==guess:
                    state_list[i]=guess
            self.state=''.join(state_list)
            if '_' not in self.state:
                self.game_status="won"
        else:
            self.rem_chances-=1
            if self.rem_chances==0:
                self.game_status="lost"
        return
    def get_state(self):
        return {
            "state":self.state,
            "word":self.word,
            "rem_chances":self.rem_chances,
            "guessed_letters":self.guessed_letters,
            "game_status":self.game_status,
            }

