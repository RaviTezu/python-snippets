from ps4a import *
import time

#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score = 0 
    # Create a new variable to store the best word seen so far (initially None)  
    best_word = None
    # For each word in the wordList
    for word in wordList:
        wordhand = {}
        valid = True
        #check all letters in word
        for i in word:
            if i in hand.keys():
                pass
            else:
                 valid = False
                 break 
        #check of no. of letter occurences
        if valid:
            for i in word:             
                wordhand[i] = wordhand.get(i,0) + 1
            for k,v in wordhand.items():
                if hand[k] >= v:
                    pass
                else:
                    valid = False
        if valid:
            cur_score = getWordScore(word,n)
            #print word, cur_score
            if cur_score > max_score:
               best_word = word
               max_score = cur_score
    if best_word is not None:
        return best_word
    else: 
        return None
    # return the best word you found.


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    total_score = 0
    user_break = False
    while sum(hand.values())!=0:
        # Display the hand
        print "Current Hand: ", displayHand(hand)        
        ip = compPlayHand(hand,  wordList, n)
        if ip == ".":
            user_break = True
            break
            # End the game (break out of the loop)
        else:   
        #Otherwise (the input is not a single period):
            if not isValidWord(ip, hand, wordList):
            # If the word is not valid:
                print "Invalid word, please try again."
                print 
                # Reject invalid word (print a message followed by a blank line)
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                wordscore = getWordScore(ip, n)
                total_score = total_score + wordscore
                print '"'+ip + '" earned '+ str(wordscore) +' points. Total: ' +str(total_score)
                # Update the hand 
                hand = updateHand(hand, ip)
    if not user_break:
        print "Run out of letters. Total score: "+ str(total_score)+" points."
    else: 
        print "Goodbye! Total score: "+str(total_score)+" points."



#
#Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    print "playGame not yet implemented." # <-- Remove this when you code this function

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    #playGame(wordList)
    compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
