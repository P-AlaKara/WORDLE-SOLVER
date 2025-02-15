# Wordle Solver (v.1)

## Overview
This is the first sketch version of a simple Wordle solver written in Python. The program attempts to guess the correct five-letter word based on user feedback for each guess.

## Features
- Reads from a dictionary of English words (`words_alpha.txt`). This dictionary has been downloaded from https://github.com/dwyl/english-words/blob/master/words_alpha.txt

- Filters words based on Wordle-style feedback:
  - **Green (g):** Letter is in the correct position.
  - **Yellow (y):** Letter is in the word but in the wrong position.
  - **Black (b):** Letter is not in the word at all.
- Iteratively refines possible words based on user input.

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
- The program currently selects the next word arbitrarily; smarter word selection can be implemented.
- UI/CLI enhancements for better user experience.
- Performance Optimization.

## Contributions
Contributions and feedback are welcome! Feel free to fork the project and make improvements.

## License
This project is open-source under the MIT License.

