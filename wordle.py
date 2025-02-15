#5 - letter word
#If double letter word, don't recommend same double letter again
word_guess = []
word_real = [None,None,None,None,None]
letters_in_word = []
letters_not_in_word = []
feedback = str()
new_valid_words = set()
letter_to_match = str()
flag = None
flag_two = None
flag_three = None

with open("all_wordle_words.txt") as f:
    english_words = set(f.read().split())

valid_words = {word for word in english_words if len(word) == 5}
print(len(valid_words))

for i in range(6):
    wrong_position_tracker = {}
    letters_in_word = []
    letters_not_in_word = []
    if i == 0:
        word_guess = ['a', 'u', 'd', 'i', 'o']
        print('word_guess')
    if i == 1:
        word_guess = ['b', 'l', 'e', 'n', 'd']
    for j in range(5):
        feedback = (input(f"{word_guess[j]}: (g or y or b): "))
        if feedback == 'g':
            word_real[j] = word_guess[j]
            print(f"{word_guess[j]} is at position {j}")
            flag = True
        if feedback == 'y':
            wrong_position_tracker[word_guess[j]] = j
            letters_in_word.append(word_guess[j])
            flag_two = True
        if feedback == 'b':
            letters_not_in_word.append(word_guess[j])       
            flag_three = True

    print(f"letters not in word: {letters_not_in_word}")
    print(f"letters_in_word: {letters_in_word}")

    words_to_remove = set()
    for word in valid_words:
        if flag_three:
            for not_letter in letters_not_in_word:
                if not_letter in word:
                    words_to_remove.add(word)
        if flag_two:
#            for yes_letter in letters_in_word:
#                if yes_letter not in word:
#                    words_to_remove.add(word)
            for yes_letter, position in wrong_position_tracker.items():
                if yes_letter not in word or yes_letter == word[position]:
                    words_to_remove.add(word)
        if flag:
            for i,letter in enumerate(word_real):
                if letter:
                    letter_to_match = word[i]   
                    #print(f"letter to match: {letter_to_match}")    #take the letter at the corresponding position e.g. position 1 i.e. u          
                    if letter != letter_to_match:
                        #new_valid_words.add(word)
                        words_to_remove.add(word)

    # Reset flags AFTER processing all words
    flag, flag_two, flag_three = None, None, None
    
    if None not in word_real:
        print(f"Final word is {str(word_real)}")
        break
    #print(words_to_remove)
    print(f"Words before filtering: {len(valid_words)}")
    print(f"Words to remove: {len(words_to_remove)}")

    valid_words -= words_to_remove

    print(f"Words after filtering: {len(valid_words)}")
    print(list(valid_words)[:10])
    word_guess = list(valid_words)[0] 
    print(word_guess)
    

        


    



