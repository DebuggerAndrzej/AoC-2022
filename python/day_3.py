import pytest
from utils import get_input


def get_score_for_letter(letter: str) -> int:
    unicode_code = ord(letter)
    return unicode_code - (38 if letter.isupper() else 96)


# **************************************** PART ONE ****************************************
def split_in_half(str_to_split: str) -> tuple[str, str]:
    splitted_lenght = len(str_to_split) // 2
    return str_to_split[:splitted_lenght], str_to_split[splitted_lenght:]


def first_subtask(input_type: str) -> int:
    score = 0
    for backpack in get_input(input_type).split("\n")[:-1]:
        compartment_1, compartment_2 = split_in_half(backpack)
        for letter in set(compartment_1):
            if letter in compartment_2:
                score += get_score_for_letter(letter)
    return score


# **************************************** PART TWO ****************************************
def second_subtask(input_type: str) -> int:
    score = 0
    input = get_input(input_type).split("\n")[:-1]
    elfs_grouped_backpacks = [input[i : i + 3] for i in range(0, len(input), 3)]
    for pack_1, pack_2, pack_3 in elfs_grouped_backpacks:
        for letter in pack_1:
            if letter in pack_2 and letter in pack_3:
                score += get_score_for_letter(letter)
                break
    return score


# ************************************* PRINT RESULTS **************************************
print(f"First subtask: {first_subtask('standard')}")
print(f"Second subtask: {second_subtask('standard')}")


# **************************************** TESTS *******************************************
@pytest.mark.parametrize(
    ("input_type", "expected"), [("dummy", 157), ("standard", 7597)], ids=["dummy_input", "standard_input"]
)
def test_fist_subtask(input_type, expected):
    assert first_subtask(input_type) == expected


@pytest.mark.parametrize(
    ("input_type", "expected"), [("dummy", 70), ("standard", 2607)], ids=["dummy_input", "standard_input"]
)
def test_second_subtask(input_type, expected):
    assert second_subtask(input_type) == expected
