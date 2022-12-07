import pytest
from utils import get_input


def get_bounds_for_elf(elf_data: str) -> tuple[int, int]:
    lower_bound, upper_bound = elf_data.split("-")
    return int(lower_bound), int(upper_bound)


# **************************************** PART ONE ****************************************
def first_subtask(input_type: str) -> int:
    fully_contained = 0
    for pair in get_input(day=4, type=input_type).split("\n")[:-1]:
        first_elf, second_elf = pair.split(",")
        first_elf_lower_bound, first_elf_upper_bound = get_bounds_for_elf(first_elf)
        second_elf_lower_bound, second_elf_upper_bound = get_bounds_for_elf(second_elf)
        if first_elf_lower_bound <= second_elf_lower_bound and first_elf_upper_bound >= second_elf_upper_bound:
            fully_contained += 1
        elif first_elf_lower_bound >= second_elf_lower_bound and first_elf_upper_bound <= second_elf_upper_bound:
            fully_contained += 1
    return fully_contained


# **************************************** PART TWO ****************************************
def second_subtask(input_type: str) -> int:
    overlaps = 0
    for pair in get_input(day=4, type=input_type).split("\n")[:-1]:
        first_elf, second_elf = pair.split(",")
        first_elf_lower_bound, first_elf_upper_bound = get_bounds_for_elf(first_elf)
        second_elf_lower_bound, second_elf_upper_bound = get_bounds_for_elf(second_elf)
        if first_elf_lower_bound <= second_elf_lower_bound and first_elf_upper_bound >= second_elf_lower_bound:
            overlaps += 1
        elif first_elf_lower_bound >= second_elf_lower_bound and first_elf_lower_bound <= second_elf_upper_bound:
            overlaps += 1
    return overlaps


# ************************************* PRINT RESULTS **************************************
print(f"First subtask: {first_subtask('standard')}")
print(f"Second subtask: {second_subtask('standard')}")


# **************************************** TESTS *******************************************
@pytest.mark.parametrize(
    ("input_type", "expected"), [("dummy", 2), ("standard", 573)], ids=["dummy_input", "standard_input"]
)
def test_fist_subtask(input_type, expected):
    assert first_subtask(input_type) == expected


@pytest.mark.parametrize(
    ("input_type", "expected"), [("dummy", 4), ("standard", 867)], ids=["dummy_input", "standard_input"]
)
def test_second_subtask(input_type, expected):
    assert second_subtask(input_type) == expected
