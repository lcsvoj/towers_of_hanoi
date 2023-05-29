import pytest
from project import welcome, new_game, get_difficulty, make_move, Game


def test_welcome():
    names = ["David", "David Malan", "Lucas"]
    for name in names:
        welcome_message = welcome(name)
        assert name in welcome_message


def test_new_game():
    difficulty = [1, 2, 3]
    for i in difficulty:
        game = new_game(i)
        assert game.total_moves == 2**i - 1


def test_play_game():
    test_game = Game(3)
    test_game.move_count = test_game.total_moves - 1
    assert test_game.is_game_over() == True
