import pytest
from game import *


def test_is_exit():
    assert is_exit(0)
    assert is_exit(3) == False


def test_is_number():
    assert is_number(3)
    assert is_number('dhjd') == False


def test_evaluate_move():
    assert evaluate_move(user_choice=Move.STONE,
                         comp_choice=Move.SCISORS) == 'User wins'
    assert evaluate_move(user_choice=Move.SCISORS,
                         comp_choice=Move.PAPER) == 'User wins'
    assert evaluate_move(user_choice=Move.PAPER,
                         comp_choice=Move.STONE) == 'User wins'

    assert evaluate_move(user_choice=Move.STONE,
                         comp_choice=Move.PAPER) != 'User wins'
    assert evaluate_move(user_choice=Move.SCISORS,
                         comp_choice=Move.STONE) != 'User wins'
    assert evaluate_move(user_choice=Move.PAPER,
                         comp_choice=Move.SCISORS) != 'User wins'

    assert evaluate_move(user_choice=Move.STONE,
                         comp_choice=Move.STONE) == 'User and Computer draws'
    assert evaluate_move(user_choice=Move.SCISORS,
                         comp_choice=Move.SCISORS) == 'User and Computer draws'
    assert evaluate_move(user_choice=Move.PAPER,
                         comp_choice=Move.PAPER) == 'User and Computer draws'


def test_generate_computer_choice():
    assert generate_computer_choice() == Move.STONE or generate_computer_choice(
    ) == Move.SCISORS or generate_computer_choice() == Move.PAPER
