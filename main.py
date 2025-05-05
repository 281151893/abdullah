# main.py
#---------------------------------------
#  Main Application
#    Integration of all components
#---------------------------------------

import game_mechanics
import question_bank
import user_experience

def main():
    # Display welcome message
    game_mechanics.welcome_message()
    
    # Allow the player to choose a difficulty (if applicable)
    difficulty = user_experience.choose_difficulty()
    
    # Initialize game state variables
    categories = list(question_bank.questions.keys())
    score = 0
    incorrect_answers = 0
    round_number = 1
    
    # Main game loop
    while not game_mechanics.check_game_over(incorrect_answers):
        # Player chooses a category
        chosen_category = game_mechanics.choose_category(categories)
        
        # A question is selected randomly from the chosen category
        question, correct_answer = question_bank.select_random_question(chosen_category)
        
        # Display the question and accept the player's answer
        player_answer = question_bank.display_question_and_accept_answer(question)
        
        # Validate the player's answer
        correct = question_bank.check_answer(player_answer, correct_answer)
        
        # Update score and incorrect_answers based on the player's answer
        if correct:
            score = game_mechanics.update_score(score, correct)
        else:
            incorrect_answers += 1
            question_bank.display_correct_answer(correct_answer)
        
        # Display the current score and round information
        game_mechanics.display_score(score, round_number)
        
        # Prepare for the next round
        round_number = game_mechanics.next_round(round_number)
        
        # Optionally, remove the question from the pool to prevent repetition
        question_bank.remove_question(chosen_category, question)
        
        # Check if the game should continue or end based on rounds or incorrect answers
        if game_mechanics.check_game_over(incorrect_answers):
            break
    
    # Display game over message and final score
    game_mechanics.game_over_message(score)
    
    # Save the score
    player_name = input("Enter your name: ")
    user_experience.save_score(player_name, score)
    
    # Display leaderboard
    leaderboard = user_experience.load_top_scores()
    user_experience.display_leaderboard(leaderboard)
    
    # Ask the player if they want to restart or exit
    game_mechanics.restart_or_exit()


#---------------------------------
#  Application Entry Point
main()
#---------------------------------
#---------------------------------
# game_mechanics.py
#    StudentA
import random
def display_welcome_message():
    print("Welcome to the Quiz Game!")
    print("You will answer questions from various categories.")

def choose_category():
    print("Available categories:")
    for category in quiz_categories.keys():
        print(f"- {category}")
    chosen_category = input("Please choose a category: ")
    return chosen_category if chosen_category in quiz_categories
else None

def display_score_and_round(score, round_number):
    print(f"Score: {score} | Round: {round_number}")

def display_game_over(final_score):
    print("Game Over!")
    print(f"Your final score is: {final_score}")

def validate_answer(player_answer, correct_answer):
    return player_answer.strip().lower() == correct_answer.strip().lower()

def increase_round_number(round_number):
    return round_number + 1
def restart_or_exit():
    choice = input("Do you want to play again? (yes/no): ")
    return choice.strip().lower() == 'yes'

#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

# Questions and answers for categories
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("What is the chemical symbol for nitrogen?", "N"),
        ("What is the atomic number of hydrogen?", "1"),
        ("What planet is known as the Red Planet?", "Mars")
    ],
    "History": [
        ("Who was the first President of the United States?", "George Washington"),
        ("In what year did World War II end?", "1945"),
        ("Who discovered America?", "Christopher Columbus"),
        ("What ancient civilization built the pyramids?", "Egyptians")
    ],
    "Geography": [
        ("What is the capital of France?", "Paris"),
        ("Which continent is Egypt located in?", "Africa"),
        ("What is the longest river in the world?", "Amazon"),
        ("Which ocean is the largest?", "Pacific")
    ]
}

hints = {
    "Science": [
        "The chemical symbol for water is made up of two elements, one of which is hydrogen.",
        "The chemical symbol for nitrogen is a single letter.",
        "Hydrogen is the first element on the periodic table.",
        "It is the planet closest to Earth."
    ],
    "History": [
        "He was the first president of the USA and led during the American Revolution.",
        "The war ended in the mid-1940s.",
        "He sailed across the Atlantic Ocean in 1492.",
        "They were located near the Nile River."
    ],
    "Geography": [
        "It is a famous European city known for the Eiffel Tower.",
        "It's a country known for the Sahara Desert.",
        "It flows through South America.",
        "This ocean covers more than a third of the Earth's surface."
    ]
}

def select_random_question(category):
    """ Selects a random question from the specified category. """
    question = random.choice(questions[category])
    return question

def check_answer(player_answer, correct_answer):
    """ Checks if the player's answer matches the correct answer. """
    return player_answer.strip().lower() == correct_answer.lower()

def remove_question(category, question):
    """ Removes the question from the list once it has been asked. """
    questions[category].remove(question)

def display_question_and_accept_answer(question):
    """ Displays a question and accepts the player's answer. """
    print(question[0])
    player_answer = input("Your answer: ")
    return player_answer

def provide_hint(category, question):
    """ Provides a hint for the given question. """
    index = questions[category].index(question)
    return hints[category][index]

def display_correct_answer(correct_answer):
    """ Displays the correct answer if the player was incorrect. """
    print(f"The correct answer was: {correct_answer}")

