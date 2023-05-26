import pytest
from game import *


def test_is_exit():
    assert is_exit(EXIT)
    assert is_exit(3) == False


def test_is_number():
    assert is_number(3)
    assert is_number('dhjd') == False


def test_evaluate_move():
    assert evaluate_move(user_choice=STONE,
                         comp_choice=SCISSORS) == 'User wins'
    assert evaluate_move(user_choice=SCISSORS,
                         comp_choice=PAPER) == 'User wins'
    assert evaluate_move(user_choice=PAPER,
                         comp_choice=STONE) == 'User wins'

    assert evaluate_move(user_choice=STONE,
                         comp_choice=PAPER) != 'User wins'
    assert evaluate_move(user_choice=SCISSORS,
                         comp_choice=STONE) != 'User wins'
    assert evaluate_move(user_choice=PAPER,
                         comp_choice=SCISSORS) != 'User wins'

    assert evaluate_move(user_choice=STONE,
                         comp_choice=STONE) == 'User and Computer draws'
    assert evaluate_move(user_choice=SCISSORS,
                         comp_choice=SCISSORS) == 'User and Computer draws'
    assert evaluate_move(user_choice=PAPER,
                         comp_choice=PAPER) == 'User and Computer draws'


def test_generate_computer_choice():
    random_choice = generate_computer_choice()
    assert random_choice == STONE or random_choice == SCISSORS or random_choice == PAPER
