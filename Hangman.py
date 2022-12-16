# Created May 8th 2021 -> https://youtu.be/m4nEnsavl6w

import random

wordinput = input()
thing = len(wordinput)
def get_word():
        return wordinput.upper

def play(word):
    word_completion = "_" * thing
    uppercase = wordinput.upper()
    wordlist= list(uppercase)
    wordlist.append(uppercase)
    lowercase = wordinput.lower()
    splitlower = list(lowercase)
    wordlist.append(lowercase)
    for letter in splitlower:
        wordlist.append(letter)
#        print(wordlist)
#        print(wordinput)

    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 7
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print('\n')


    
    while not guessed and tries > 0:
        guess= input("Please guess a letter or word: ")
        guesslower = guess.lower()
        guessupper = guess.upper()
        thing3 = (int(thing)+1)
        fullword = wordlist[thing3].upper()
        if len(guess) == 1:
            if guesslower in guessed_letters:
                print("You already guessed the letter", guess)
            elif guessupper in guessed_letters:
                    print("You already guessed the letter", guess)
            elif guessupper == fullword:
                    guessed = True
            elif guess not in wordlist:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(wordinput) if letter == guess.upper()]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(wordinput):
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess not in wordlist:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = wordinput
            if guessed:
                print("Congrats, you guessed the word! You win!")
            else:
                print("Sorry, you ran out of tries. The word was "+str(wordinput)+". Maybe next time!")


        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

def display_hangman(tries):
    stages = [  """
                            - - - - - - - -
                            |                     |
                            |                    0
                            |                   \\|/
                            |                     |
                            |                   / \\
                            -
                        """,
                        """
                             - - - - - - - -
                            |                     |
                            |                    0
                            |                   \\|/
                            |                     |
                            |                   / 
                            -
                        """,
                        """
                             - - - - - - - -
                            |                     |
                            |                    0
                            |                   \\|/
                            |                     |
                            |                   
                            -
                        """,
                        """
                             - - - - - - - -
                            |                     |
                            |                    0
                            |                   \\|
                            |                     |
                            |               
                            -
                        """,
                        """
                             - - - - - - - -
                            |                     |
                            |                    0
                            |                     |
                            |                     |
                            |                   
                            -

                        """,
                        """
                             - - - - - - - -
                            |                     |
                            |                    0
                            |                  
                            |                     
                            |                   
                            -
                        """,
                        """
                             - - - - - - - -
                            |                     |
                            |                    
                            |                  
                            |                     
                            |                   
                            -
                        """,
                        """
                             - - - - - - - -
                            |                     
                            |                    
                            |                  
                            |                     
                            |                   
                            -
                        """
                ]
    return stages[tries]
            
                            
def main():
    word = get_word()
    play(word)
    while input("Play again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
        main()


