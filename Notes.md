# AUTH Python CW

# AUTH Python CW

### The board game Scrabble enters schools as a tool for learning Greek.

To complete the coursework correctly, you will need:

- (a) This 2023 Work Guide (which you obviously already have)
- (b) The transparency packs for Python
- (c) The greek7.txt file containing Greek words up to 7 letters long (available on the course page, in the section 'Scripts For Scrabble - 2022')

All of the above can be found on the course page.

General: Game Flow and Rules

- The simplified version of Scrabble will be played as follows:
• 1) There is an initial "bag" containing a specific number of letters.
• 2) At the beginning of the game, random 7 letters are given (removed from the bag) to the player and 7 letters to the computer.
• The letters will always be a maximum of 7. Towards the end of the game, when no more letters are available, there may be fewer than 7 letters.
• 3) The player thinks of a word they can create using the letters and types it in. The software checks if the word is acceptable, and if so:
• a) It assigns the corresponding points to the word (which is the sum of the points assigned to each letter).
• b) It replenishes the player's letters to always have 7 (or fewer if no letters are available).
• 4) Then, the computer "plays" and performs the appropriate actions according to the software.
• 5) If the player or the computer cannot find a word (or choose not to play a word), they can request a letter exchange (they change all 7 letters or the number of available letters) and lose their turn.
• 6) The game continues with similar moves from the player and the computer until there are no more letters in the bag, and no one can form an acceptable word or if someone resigns from the game (player or computer).
• 7) At that point, the software announces the end of the game, the winner, and presents the final score.

General: Game Flow and Rules

Description of the Assignment 1/2

- The general objective of the assignment is to develop a Python application that implements the simplified version of the Scrabble game on the computer.
- The specific objective of the assignment is to write an algorithm that guides the computer (or the player) to play the game.
- Your application should generally follow the analysis described in the following slides.

Development Environment

- The Python code application should be able to run in either the IDLE environment or the Jupyter Notebook environment and adhere to the principles of object-oriented programming (OOP) taught in the course.
• All information during the game's progression will be displayed using character messages (character mode), i.e., the application will not have a graphical user interface (GUI).
• For example, a possible display of messages from the game and player's word input could be as follows:

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/df4359ae-9c42-4bc8-8259-8543d4ffdbdb/Untitled.png)

Notes on the example game progress messages:

- The example demonstrates how the game can progress on the screen through messages.
- It is not mandatory to follow this exact example. You have the flexibility to customize the messages according to your preference.
- The goal is to ensure that the messages are clear and understandable for the players.
- The example includes information such as the player's name (Stavros), their score (0), and the letters they have available.
- Additionally, it shows an example word "ΑΥΤΗ" being entered by the player within a square field.
- You can modify and configure the messages to provide relevant information and enhance the gameplay experience.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b6a95b96-982d-47ed-b16b-2e7d7e3dcaa4/Untitled.png)

## Notes for the 5 classes of the game:

1. SakClass:
- Defines the functionality of the "sack" object that holds the letters for the game.
- Handles operations related to the letters in the sack, such as adding, removing, and shuffling.
- This class manages the availability of letters for the players to use during the game.
1. Player:
- Basic class from which the Human and Computer classes are derived.
- Represents a player in the game.
- Provides common attributes and methods for all players, such as the player's name, score, and available letters.
- This class serves as the base for defining player-specific functionalities.
1. Human:
- Derived class from Player.
- Defines the functionalities specific to the human player.
- Handles interactions and actions related to the human player's moves and choices in the game.
- Implements methods for inputting words, validating word submissions, and updating the player's score.
1. Computer:
- Derived class from Player.
- Defines the functionalities specific to the computer player.
- Handles automated actions and decision-making for the computer player in the game.
- Implements strategies for word generation, word evaluation, and optimizing the computer player's moves.
1. Game:
- Describes the progression and flow of a game session.
- Manages the interaction between players, the sack of letters, and the scoring system.
- Implements methods for starting a game, taking turns between players, and determining the game's end conditions.
- This class orchestrates the overall gameplay mechanics and ensures the game's integrity.

Note: Besides the above classes, you have the flexibility to implement additional classes as per your requirements. The mentioned classes serve as a foundation for the game structure, and further details about them are provided in the subsequent slides of the presentation.

## Player, Human, and Computer classes:

The Player class serves as the base class, while the Human and Computer classes are derived classes inheriting from the Player class.

Player class (Properties, Methods):

- Represents a player in the game.
- Contains properties and methods common to both human and computer players.

Human class (Properties, Methods):

- A derived class of the Player class that defines functionalities specific to human players.
- It inherits properties and methods from the Player class.
- Contains additional properties and methods that cater to human player interactions and gameplay.

Computer class (Properties, Methods):

- A derived class of the Player class that defines functionalities specific to computer players.
- It inherits properties and methods from the Player class.
- Contains additional properties and methods that cater to computer player interactions and gameplay.

These classes are responsible for defining the behavior and characteristics of players in the game. The Player class provides a foundation for common player attributes and actions, while the Human and Computer classes extend that functionality with player-specific features. By utilizing inheritance, the code can be structured efficiently to handle different types of players while reusing shared functionality.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5d53805f-e7ea-45cf-a26f-97ba7ec0912f/Untitled.png)

## Player class:

- Represents a player in the game.
- Serves as the base class for the Human and Computer classes.

Properties:

- The specific properties of the Player class can be determined based on the requirements of the game. Some possible properties may include:
    - name: The name or identifier of the player.
    - score: The current score of the player.
    - letters: The letters available to the player.
    - other relevant attributes specific to the game.

Methods:

- **init**(): Initializes the Player object. It can accept parameters such as the player's name or any other required attributes.
- **repr**(): Returns a string representation of the Player object. This method is useful for debugging and displaying information about the player.

Additional methods:

- Apart from the required methods, you can define additional methods based on the functionality needed for the game. These methods can include actions like playing a word, updating the score, exchanging letters, etc.

The Player class serves as the foundation for defining players in the game, providing common attributes and behaviors that both human and computer players may share. It can be further extended and customized in the derived classes to include specific functionalities for each player type.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/eb3ac05c-7bb1-4bbc-91bc-cc958cb1f0a9/Untitled.png)

## Human class:

- Derived class of the Player class, representing a human player in the game.

Properties:

- The specific properties of the Human class can be determined based on the requirements of the game. Some possible properties may include:
    - input_method: The method or interface used to receive input from the human player (e.g., command line input, graphical user interface).
    - any other relevant attributes specific to the human player.

Methods:

- **init**(): Initializes the Human object. It can accept parameters specific to the human player, such as the player's name or preferred input method.
- **repr**(): Returns a string representation of the Human object. This method is useful for debugging and displaying information about the human player.
- play(): Implements the algorithm or logic for the human player's turn in the game. This method defines how the human player chooses and plays a word based on the available letters and game rules.

Additional methods:

- In addition to the required methods, you can define additional methods based on the functionality needed for the game and the interactions with the human player. These methods can include actions like exchanging letters, validating word choices, displaying game information to the human player, etc.

The Human class extends the functionality of the Player class to incorporate specific behaviors and actions associated with human players. The play() method, unique to the Human class, encapsulates the algorithm or decision-making process that determines how the human player plays the game. The class can be further customized and expanded to handle user input, provide feedback, and interact with the game interface or environment based on the specific requirements of the game.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b5902a5a-6693-4343-b3ab-7b33d1deaaad/Untitled.png)

## Computer class:

- Derived class of the Player class, representing a computer player in the game.

Properties:

- The specific properties of the Computer class can be determined based on the requirements of the game. Some possible properties may include:
    - difficulty_level: The level of difficulty for the computer player, which can affect the algorithm used to make decisions.
    - strategy: The strategy or algorithm employed by the computer player to select words.
    - any other relevant attributes specific to the computer player.

Methods:

- **init**(): Initializes the Computer object. It can accept parameters specific to the computer player, such as the difficulty level or strategy used.
- **repr**(): Returns a string representation of the Computer object. This method is useful for debugging and displaying information about the computer player.
- play(): Implements the algorithm or logic for the computer player's turn in the game. This method defines how the computer player chooses and plays a word based on the available letters, game rules, and its assigned strategy or difficulty level.

Additional methods:

- Additional methods can be added to enhance the functionality of the Computer class. These methods can include actions like generating possible words, evaluating the best word to play, simulating game scenarios, etc.

The Computer class extends the functionality of the Player class to incorporate specific behaviors and actions associated with computer players. The play() method, unique to the Computer class, implements the algorithm or decision-making process that determines how the computer player plays the game. The class can be further customized and expanded to incorporate different difficulty levels, strategies, and algorithms based on the specific requirements of the game.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a5f73063-649f-49e8-8a6c-b02679167ade/Untitled.png)

## Game class:

- The main class that represents the game itself.

Properties:

- The specific properties of the Game class can be determined based on the requirements of the game. Some possible properties may include:
    - players: A list of Player objects participating in the game.
    - score_board: A data structure to keep track of the scores of each player.
    - dictionary: The game dictionary containing valid words.
    - any other relevant attributes specific to the game.

Methods:

- **init**(): Initializes the Game object. It can accept parameters related to the setup and configuration of the game, such as the number of players or specific game settings.
- **repr**(): Returns a string representation of the Game object. This method is useful for debugging and displaying information about the game.
- setup(): Performs the necessary actions to set up the game at the start, such as creating players, initializing the score board, loading the dictionary, etc.
- run(): Executes the main loop of the game, where players take turns playing and the game progresses until a certain condition is met (e.g., reaching a maximum score or exhausting the letters).
- end(): Performs the necessary actions to end the game, such as displaying the final scores, declaring the winner, saving game statistics, etc.

Additional methods:

- In addition to the mentioned methods, you can add more methods to handle various aspects of the game, such as handling player turns, checking word validity, updating scores, displaying game state, etc.

The Game class serves as the central entity that orchestrates the flow of the game. It encapsulates the logic and rules of the game, including the setup, execution, and conclusion. By defining the setup(), run(), and end() methods, the class controls the initialization, progression, and termination of the game. The class can be further expanded and customized to incorporate additional game features, rules, or functionalities based on the specific requirements of the game being implemented.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/04c63bb1-25e6-43f4-a534-be3c6e4624f1/Untitled.png)

## To manage the code for the classes and the main program, you can follow the following guidelines:

1. Create a separate file named "[classes.py](http://classes.py/)": This file will contain the code for all the classes involved in the game, including SakClass, Player, Human, Computer, and Game. Each class should be defined in this file with its respective properties and methods.
2. Create a file named "[main-AEM.py](http://main-aem.py/)": In this file, you will write the code for the main program that utilizes the classes defined in "[classes.py](http://classes.py/)". Replace "AEM" with your actual student ID number. For example, if your student ID number is 1234, the file name should be "[main-1234.py](http://main-1234.py/)".
3. Collaborative development (if working in a team): If you are working in a team, you can include both team members' student ID numbers in the main program file name. For instance, if the student ID numbers are 1234 and 3001, the file name should be "[main-12343001.py](http://main-12343001.py/)".

By separating the classes into a dedicated "[classes.py](http://classes.py/)" file, you can easily manage and reuse them in other projects if needed. The main program file, "[main-AEM.py](http://main-aem.py/)", will serve as the entry point where you can instantiate objects, invoke methods, and control the overall flow of the game.

Remember to import the necessary classes from "[classes.py](http://classes.py/)" into "[main-AEM.py](http://main-aem.py/)" to use them effectively. For example, you can use the following import statement in "[main-AEM.py](http://main-aem.py/)" to import the Game class:

```
from classes import Game
```

Organizing the code in this way promotes modularity, readability, and easier collaboration in case multiple developers are involved.

---

## Flow and Rules of the Game 1/7

1. The game can start with an introductory screen that presents a menu of options to the player. An example of such a screen is shown below:

```
***** SCRABBLE *****
--------------------
1: Score
2: Settings
3: Play
q: Quit
--------------------

```

- The program should create an object (instance) of the SakClass type initially, for example, `sak`.
- This object will implement the "sack" of the physical game. In other words, it will be a data structure that contains the letters and their corresponding values (scores) and the methods related to the "sack."
- Information about the number of available letters and their distribution can be found here.

The introductory screen allows the player to navigate through different options such as checking the score, adjusting settings, starting a new game, or quitting the program. The SakClass object, `sak`, will handle the management of letters and their distribution within the game.

Please note that the detailed information about the number of letters and their distribution is not provided in the given context. You may need to refer to the specific rules or specifications of the Scrabble game for that information.

## Flow and Rules of the Game 2/7

1. The progression of the game is as follows:
- The program draws 7 letters from the "sack" for the player and 7 letters for the computer. It presents the player with their letters along with their corresponding values (scores). The program simultaneously removes the drawn letters from the "sack." The information about the remaining letters in the sack should be visible to the player.
- The program then waits for the player to enter a word using the available letters. An indicative example of the screen is shown below (the design is for illustrative purposes only, and you can implement your own user interface):

```
***********************************************************************
         ***    Player: Stavros    ***  Score: 0
         >>>  Letters:   [ 'Α',  'Ν',  'Ψ',  'Η',  'Ρ',  'Υ',  'Τ' ]

         WORD:  ΑΥΤΗ
( The user types the word "ΑΥΤΗ" within a square field)

```

The player is presented with their name, score, and the letters they have been dealt with. They need to input a word using the available letters. The user interface provided in the example above is purely indicative, and you can design your own interface accordingly.

Note: The specific rules regarding word validation, scoring, and other gameplay mechanics are not mentioned in the given context. You may need to refer to the rules of the Scrabble game or define your own rules for handling word input, scoring, and validation within your program.

## Flow and Rules of the Game 3/7

1. When the player enters a word, your program should perform the following checks:

3-A) It checks if the word is composed of letters that the player actually possesses. If not, it displays a relevant message and waits for a new word.
3-B) If the word is valid, it checks if the given word is included in the list of acceptable words obtained from the greek7.txt file.
3-C) Instead of entering a word, the player can enter 'p' (for "pass"). In this case, the program should:
a) Draw new letters for the player.
b) Return the previously used letters of the player back to the "sack."
The player loses their turn in this case.

After these checks, the program proceeds to step 5, which will be described on a subsequent slide.

Where is the greek7.txt file located?
The greek7.txt file is available on the course page under the section "Scripts For Scrabble." The construction and content of the file are explained in the workshop.

Note: To implement these checks, you can create functions or methods within your program to handle letter validation, word verification, and player actions. The greek7.txt file can be read by your program to access the list of acceptable words.

## Flow and Rules of the Game 4/7

1. If the word entered by the player is valid, the program calculates the points for that word and displays the player's new score, along with a prompt such as 'Press Enter to continue' (for example, see the sample messages below; the format is only indicative and not mandatory).

Sample Messages:

- Player: Stavros | Score: 10
- Word Entered: ΑΥΤΗ
- Points for the Word: 8
- New Score: 18
- Press Enter to continue.

After displaying the score and prompt, the program waits for the player to press Enter to proceed to the next step.

Note: The scoring system can be defined based on the rules of the game. Each letter can have a specific point value associated with it, and the total points for a word can be calculated by summing the points of its individual letters.

## Flow and Rules of the Game 5/7

1. Once the player presses 'Enter' (or 'p'), the program follows these steps:
5-1) It replenishes the player's available letters with new ones (to always have 7 letters, remembering to remove them from the "bag" at the same time).
5-2) It displays the computer's letters and the word it plays, along with the word score and the computer's total score. It secretly fills in the computer's letters and then returns to step 3.

Example Screen:

- Player's Letters: Α Τ Ρ Ο Π Ο
- Word Entered: ΑΥΤΗ
- Points for the Word: 8
- New Score: 18
- Press Enter to continue.

After displaying the screen, the program waits for the player to press Enter to proceed to the next round.

Note: The computer's letters can be generated randomly or through a predetermined algorithm.

## Flow and Rules of the Game 6/7

1. The game continues until one of the following events occurs:
6-1) The player decides to stop (or cannot find an acceptable word to play and has no letters to exchange), so they enter the character 'q' when it is their turn to enter a word, terminating the game.
6-2) There are no more letters left in the "bag" to replenish the missing ones, either for the player or the computer.
6-3) The computer cannot find an acceptable word to play and there are no letters in the "bag" to exchange.

In any of these cases, the game ends, and the final scores are displayed.

Note: You may consider additional rules or conditions for ending the game, such as reaching a specific number of rounds or a maximum time limit.

## Flow and Rules of the Game 7/7

1. In any of the previous cases, the program stops and:
7-1) It announces the scores of the Player and the Computer, declaring the winner.
7-2) It records a new entry with relevant game information into a suitable data structure stored in a file (e.g., the number of moves played, the scores of the player and computer). The program loads this data structure when starting the game and can provide the player with relevant updates.

To store data in a file, you can use the pickle library or json (preferably json). You can find information on how to use these libraries in the course's materials, specifically the "07-Python-ScriptsForScrabble-2023.pdf" document (refer to the section on "Persistence: pickle & json").

## Data structure for words: Dictionary or List

Your program should perform another important task at the beginning:

1. Load the words of the language from the file "greek7.txt" and transfer them to a suitable data structure in your code to enable necessary checks in the game.

You need to decide on the data structure that will contain the language words consulted by your program. The efficiency of your code will depend on the chosen data structure.

Pay attention to this point, as it will be presented in the workshop, and we have provided the answer.

## Choose the algorithm for the computer player (Computer class)

An important decision and task you need to make is to choose the algorithm that the computer player (Computer class) will use.

You have two options:
A) Select one of the algorithms suggested below.
B) Define your own algorithm. In this case, please inform me in advance so that I can review the algorithm you propose and provide you with approval.

Please let me know which option you would like to pursue, and if you have any specific algorithms in mind, provide the details.

## The provided text describes five different algorithms for a computer game. Here's a brief summary of each algorithm:

Algorithm 1: Min Max Smart

- Generates all possible permutations of letters from 2 to 7.
- Checks if each permutation is a valid word and plays the first valid word found.
- Three variations: MIN Letters, MAX Letters, and SMART.

Algorithm 2: Smart Fail

- Combines the SMART algorithm with a FAIL algorithm.
- SMART generates a list of possible words.
- FAIL selects a word from the list, potentially not choosing the best word.

Algorithm 3: Smart Expert

- Similar to the SMART algorithm.
- Includes an "expert" component that simulates specialized knowledge.
- The word list used is enriched or replaced with a more extensive or specialized dictionary.

Algorithm 4: Smart Learn

- Incorporates a learning component.
- If a player enters a word not present in the current word list, the algorithm asks the player if they want to include it.
- If approved, the word is added to the word structure for future recognition.
- At the end of the game, the word list is updated with the new words.

Algorithm 5: Smart Teach

- Combines the SMART algorithm with a teaching component.
- The computer teaches the player by informing them of the best possible word or providing hints.

Please note that the provided text seems to be a mix of Greek and English. Let me know if you need any further clarification or assistance with these algorithms.

### Algorithms and Game Settings

• In your assignment, you should choose which algorithm to implement in your code.
• If the assignment is done by a team of 2 people, two different algorithms should be implemented.
• Note: Algorithm 1 (Min Max Smart) is considered one algorithm.
• When the player selects "Settings" at the beginning of the game, the software should allow the player to choose how the AI will play.
• For example, if you applied the Min Max Smart algorithm, from the settings, the player should be able to determine whether the AI will play with the Min option, Max option, or Smart option.

## Grading Criteria

To evaluate your assignment, pay attention to the following:

- The docstring of the guidelines should include the following information:
1. Which classes you have implemented in your code.
2. What inheritance you have implemented (e.g., the base class and any derived classes).
3. What method extensions you have implemented (e.g., methods that extend the superclass in the classes you created).
4. If you have applied operator overloading or used decorators in your code and where (it will be considered positively in the overall evaluation of your performance in the course).
5. In which data structure (list or dictionary) your application organizes the language words during the game.
6. Which algorithm(s) you have implemented for the AI to play.

Evaluation Criteria
1/2

- The evaluation of the assignment will be based on the following criteria:

CRITERIA CHARACTERISTICS COMMENTS EXPLANATIONS
1 CLASSES If classes have been implemented, inheritance, method extension. Operator overloading and the use of decorators are not required, but if implemented, they will be positively considered in the overall grade.
2 WORD STRUCTURE Explain the data structure you used to manage the language words in your code. - (Explain it in the docstring).
3 MODULE The code of the classes should be in a separate library module file, as described.
4 AI ALGORITHM Which algorithm(s) have been implemented for the AI to play? - (Explain it in the docstring).

Evaluation Criteria
2/2

CRITERIA CHARACTERISTICS COMMENTS EXPLANATIONS
5 CODE ACCURACY & MESSAGES The correctness of the code to ensure the game is played correctly, as well as clear display of messages and implementation of the intended functionalities, will be evaluated.
6 DOCUMENTATION The necessary information should be included in the docstring, as described in the previous slide (or any other relevant information for understanding the functioning of your code).
7 FILES If the two necessary files for the proper execution of your code have been submitted. That is, the code of the classes and the code of the main program (or any other files required by the logic of your application, e.g., an initial settings file, etc.).

> 
> 

You do not need to submit the greek7.txt file.