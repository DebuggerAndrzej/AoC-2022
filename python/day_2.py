import pytest
from utils import get_input

scores_per_shape = {"X": 1, "Y": 2, "Z": 3}
map_player_1_to_player_2 = {"A": "X", "B": "Y", "C": "Z"}


# **************************************** PART ONE ****************************************
def get_scores_for_game(player_1: str, player_2: str) -> int:
    score_for_shape = scores_per_shape[player_2]

    if is_draw(player_1, player_2):
        return score_for_shape + 3

    return 6 * did_player_2_win(player_1, player_2) + score_for_shape


def is_draw(player_1: str, player_2: str) -> bool:
    return map_player_1_to_player_2[player_1] == player_2


def did_player_2_win(player_1: str, player_2: str) -> bool:
    match player_1:
        case "A" if player_2 == "Y":
            return True
        case "B" if player_2 == "Z":
            return True
        case "C" if player_2 == "X":
            return True
    return False


def first_subtask(input_type: str) -> int:
    score = 0

    for single_game in get_input(input_type).split("\n")[:-1]:
        player_1, player_2 = single_game.split(" ")
        score += get_scores_for_game(player_1, player_2)

    return score


# **************************************** PART TWO ****************************************
map_game_state = {"X": "lose", "Y": "draw", "Z": "win"}


def get_player_2_shape_score(player_1: str, game_result: str) -> int:
    match player_1:
        case "A":
            return 2 if game_result == "win" else 3
        case "B":
            return 3 if game_result == "win" else 1
        case "C":
            return 1 if game_result == "win" else 2


def get_scores_for_game_with_game_result(player_1: str, game_result: str) -> int:
    if game_result == "draw":
        return scores_per_shape[map_player_1_to_player_2[player_1]] + 3
    else:
        shape_score = get_player_2_shape_score(player_1, game_result)
        result_score = 6 if game_result == "win" else 0
        return shape_score + result_score


def second_subtask(input_type: str) -> int:
    score = 0

    for single_game in get_input(input_type).split("\n")[:-1]:
        player_1, game_result = single_game.split(" ")
        score += get_scores_for_game_with_game_result(player_1, map_game_state[game_result])

    return score


# ************************************* PRINT RESULTS **************************************
print(f"First subtask: {first_subtask('standard')}")
print(f"Second subtask: {second_subtask('standard')}")


# **************************************** TESTS *******************************************
@pytest.mark.parametrize(
    ("input_type", "expected"), [("dummy", 15), ("standard", 13682)], ids=["dummy_input", "standard_input"]
)
def test_fist_subtask(input_type, expected):
    assert first_subtask(input_type) == expected


@pytest.mark.parametrize(
    ("input_type", "expected"), [("dummy", 12), ("standard", 12881)], ids=["dummy_input", "standard_input"]
)
def test_second_subtask(input_type, expected):
    assert second_subtask(input_type) == expected
