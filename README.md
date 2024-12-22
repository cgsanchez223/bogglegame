Unit 23.5 of the Software Engineering Foundations bootcamp at Stony Brook University.
- This unit focused on testing in Flask
- Unit Tests
    - Test one unit of functionality - usually 1 function or 1 method
    - To run:
        - python -m unittest test.py
- Doc Tests
    - Testable documentation
        - adder (x, y)
        - adder (1, 1)
        - 2
    - To run:
        - $ python -m doctest test.py
- Integration Tests
    - Tests components that work together.
        - "Does this route return to the right HTML"
        - "Does this route return the correct status code"

_______________________________________________________________
Boggle is a game where you look for words inside the generated grid of letters
- Words can be created from adjacent letters – that is, letters which are horizontal or vertical neighbors of each other as well as diagonals. The letters must connect to each other in the proper sequence to spell the word correctly. This means that the next letter in the word can be above, below, left, or right of the previous letter in the word (excluding any letters previously used to construct the word). 
- You have 60 seconds to find words
- Each word is a point
- The high score is recorded.

______________________________________________________________________
- Need Python, iPython and Flask to run.