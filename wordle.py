word_guess = []
word_real = [None,None,None,None,None]
letters_in_word = set()
letters_not_in_word = set()
flag = None

def process_feedback(word_guess, word_real, wrong_position_tracker, letters_in_word, letters_not_in_word, flag):
    """Processes user feedback and updates known information about the word"""
    for j, letter in enumerate(word_guess):
        feedback = input(f"{letter}: (g or y or b): ").strip().lower()
        
        if feedback == 'g':  # Green: Correct letter, correct position
            word_real[j] = letter
            flag = True       
        elif feedback == 'y':  # Yellow: Letter exists but in wrong position
            wrong_position_tracker[letter] = j
            letters_in_word.add(letter)       
        elif feedback == 'b':  # Black: Letter does not exist
            letters_not_in_word.add(letter)

    return flag   

def filter_words(valid_words, word_real, letters_not_in_word, wrong_position_tracker, flag):
    """Filters valid words based on known letter positions and exclusions."""
    words_to_remove = set()
    for word in valid_words: 
        if letters_not_in_word:
            # Check for letters that must NOT be in the word
            if any(letter in word for letter in letters_not_in_word):
                words_to_remove.add(word)
                continue

        if wrong_position_tracker:
#            for yes_letter in letters_in_word:
#                if yes_letter not in word:
#                    words_to_remove.add(word)
            # Check for misplaced letters. 
            if any(word[pos] == letter for letter, pos in wrong_position_tracker.items()):
                words_to_remove.add(word)
                continue

        if letters_in_word:
            #Check for letters that MUST be in the word
            if not all(letter in word for letter in letters_in_word):
                words_to_remove.add(word)
                continue

        if flag:
            # Ensure all known letters in the word are present somewhere
            if any(word[i] != letter for i, letter in enumerate(word_real) if letter is not None):
                words_to_remove.add(word)

    print(f"Words to remove: {len(words_to_remove)}")
    return valid_words - words_to_remove


with open("all_wordle_words.txt") as f:
    english_words = set(f.read().split())

valid_words = {word for word in english_words if len(word) == 5}
print(len(valid_words))

for i in range(6):
    wrong_position_tracker = {}     # Tracks letters in the word but in the wrong position
    letters_in_word = set()         # Tracks letters that must be in the word
    letters_not_in_word = set()     # Tracks letters that must NOT be in the word
    
    # First two guesses are predetermined. We use words with a lot of vowels and a lot of consonants to eliminate words quickly and early
    if i == 0:
        word_guess = ['a', 'u', 'd', 'i', 'o']
        print('word_guess')
    elif i == 1:
        word_guess = ['b', 'l', 'e', 'n', 'd']
    else:
        word_guess = list(valid_words)[0]      #Not very optimal

    print(word_guess)

    flag = process_feedback(word_guess, word_real, wrong_position_tracker, letters_in_word, letters_not_in_word, flag)

    print(f"letters not in word: {letters_not_in_word}")
    print(f"letters_in_word: {letters_in_word}")

    words_to_remove = set()
    print(f"Words before filtering: {len(valid_words)}")
    valid_words = filter_words(valid_words, word_real, letters_not_in_word, wrong_position_tracker, flag)

    # Reset flags AFTER processing all words
    flag, flag_two, flag_three = None, None, None
    
    if None not in word_real:  #word_real is full if all letters are know and in correct positions
        print(f"Final word is {str(word_real)}")
        break
    #print(words_to_remove)

    print(f"Words after filtering: {len(valid_words)}")
    print(list(valid_words)[:10])