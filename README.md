# NAVAL WAR

## Index
+ [Overview](#overview "Overview")
+ [How to play](#how-to-play "How to play")
+ [Features](#features "Features")
  + [Existing Features](#existing-features "Existing Features")
  + [Future Features](#fture-features "Future Features")
+ [Data Model](#data-model "Data Model")
+ [Testing](#testing "Testing")
+ [Bugs](#bugs "Bugs")
  + [Solved Bugs](#solved-bugs "Solved Bugs")
  + [Remaining Bugs](#remaining-bugs "Remaining Bugs")
  + [Validator Testing](#validator-testing "Validator Testing")
+ [Deployment](#deployment "Deployment")
+ [Credits](#credits "Credits")
+ [Acknowledgments](#acknowledgments "Acknowledgments")

# Overview
Welcome to the Battleship Game! This repository houses a classic naval strategy game implemented in [Python programming language](https://github.com/Kamal-Kohli/naval-war-pp3/blob/main/run.py), which runs in the Code Institute mock terminal on Heroku app. Battle it out on the high seas, strategize your moves, and sink your opponent's ships. Test your strategic skills against a smart AI opponent in this engaging and interactive Battleship experience.

![](/assets/images/111.png)
[Click for play](https://naval-war-31e4287bc929.herokuapp.com/) - 
[Backend file](https://github.com/Kamal-Kohli/naval-war-pp3)

# How to play
Naval war game is based on the classic pen and papper game. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)).

In this version, the player enters their name and two boards are randomly generated side by side.

The player can se where their ships are, indicated by "S" alphabet, but cannt see where the opponent's ships are.

Gusses are marked on the board with "#". Hits are indiated by "X".

And players can water with sign "."

The player and the opponent then take it in turns to make gusses and try to sink each other's naval ships.

The winner is the player who sinks all of their opponent's naval ships first.

# Features

### Existing Features
![](/assets/images/110.png)
- Random board generation.
  - Ships are randomly placed on both the player and computer boards.
  - The player cannot see where the computer's ships are.

![](/assets/images/112.png)

- Play against the computer(AI).
![](/assets/images/13.png)
- Accepts user input.
- Maintains scores.

![](/assets/images/11.png)
- Input validation and error checking.
  - You cannot enter invalid coordinates. (E.g. A5,A6)
  - You must enter Alphabet and Number.
  - You cannot enter the same gusses twice.

### Future Features
- Add graphics to the game.
- Allow player to position ships themselves.
- Allow player to customize ships size

# Data Model
# Testing
I have manually tested this game by doing the following:
- Passed the code through a PEP8 linter and confirmed there are no problems
- Given invalid inputs: strings when alphabet and number are expected, out of bonds inputs, same input twice.
- Tested in my local terminal and the Code Institute Heroku terminal

## Bugs
### Solved Bugs
- When deploying the project to Heroku, I faced issues in the build log. ![](/assets/images/build.png)
-  So, after I succeeded in the deployment, I deleted all packages and kept empty requirement.txt.