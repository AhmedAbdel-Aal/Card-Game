# Card Game Project

## Description

This is a simple card game project implemented in Python. The game involves two players drawing cards from their draw piles, comparing the values, and the player with the higher card wins both cards. In case of a tie, the winner of the next round wins all the tied cards. The game continues until one player has no cards left in both their draw and discard piles.

## How to Run the Code

### 1. Running Manually

To run the code manually on your local machine:

1. Download the code and go into the main directory:
    ```bash
    cd card_game
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the game:
    ```bash
    python main.py
    ```

### 2. Build Docker Image Yourself and Run It

To build the Docker image yourself and run it:

1. Download the code and go into the main directory:
    ```bash
    cd card_game
    ```

2. Build the Docker image:
    ```bash
    docker build -t card_game .
    ```

3. Run the Docker container:
    ```bash
    docker run -it card_game
    ```

### 3. Pull Docker Image and Run It

To pull the Docker image from Docker Hub and run it:

1. Pull the Docker image from Docker Hub:
    ```bash
    docker pull mondaaa/card_game:latest
    ```

2. Run the Docker container:
    ```bash
    docker run -it mondaaa/card_game:latest
    ```