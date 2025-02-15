# Wordle Solver (v.1)

## Overview
This is the first sketch version of a simple Wordle solver written in Python. The program attempts to guess the correct five-letter word in a maximum of 6 tries, based on user feedback for each guess.

## Features
- Reads from a list of English words (`all_wordle_words.txt`). This list has been downloaded from https://github.com/zulkarnine/WordleSolver/blob/main/all_wordle_words.txt

- Filters words based on Wordle-style feedback:
  - **Green (g):** Letter is in the correct position.
  - **Yellow (y):** Letter is in the word but in the wrong position.
  - **Black (b):** Letter is not in the word at all.
- Iteratively refines possible words based on user input.
## Performance
- The program produces the correct word an average 85% of the time for all 5 letter words in the English Language (15428 words) and an average of 95% of the time for wordle words (<3000).

## Installation
No external dependencies are required. Ensure you have Python installed on your system.

## How to Run
1. Clone the project and navigate to the folder where `wordle.py` is located.
    ```sh
    git clone https://github.com/P-Alakara/WORDLE_SOLVER.git
    cd WORDLE_SOLVER
    ```
2. Run the script:
   ```sh
   python wordle.py
   ```
3. Follow the prompts to enter feedback for each letter.

## Known Issues & Future Improvements
- This is a **first sketch version**, and many improvements are planned.
- UI/CLI enhancements for better user experience.
- The program currently selects the next word arbitrarily; smarter word selection can be implemented. e.g. Implement a scoring system or heuristic to choose the next guess based on the remaining valid words?
- Further Performance Optimization?

## Contributions
Contributions and feedback are welcome! Feel free to fork the project and make improvements.

## License
This project is open-source under the MIT License.

