import random

class GuessGame:
    
    def guess(self):
        low=1 #minimum 
        high=10 #maxium
        user_opinoion=''
        computer_guess=1
        while user_opinoion!='c':
            computer_guess= random.randint(low,high) if low!=high else low

            computer_guess=random.randint(low,high)
            user_opinoion=input(f'Is {computer_guess} high (h) or low (l)\
                correct (c)?').lower()
            if user_opinoion=='h': high=high-1 
            if user_opinoion=='l':low=low+1
                

        print('Congrats to computer, computer guessed the number')


guess_instance=GuessGame()
guess_instance.guess()



