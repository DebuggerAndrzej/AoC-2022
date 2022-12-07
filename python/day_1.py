import pytest
from utils import get_input


def get_total_carried_per_elf(type: str) -> list[int]:
    return [
        sum([int(carried_element) for carried_element in elf_backpack.split("\n") if carried_element])
        for elf_backpack in get_input(type).split("\n\n")
    ]


# **************************************** PART ONE ****************************************
def first_subtask(type: str) -> int:
    return max(get_total_carried_per_elf(type))


# **************************************** PART TWO ****************************************
def second_subtask(type: str) -> int:
    return sum(sorted(get_total_carried_per_elf(type))[-3:])


# ************************************* PRINT RESULTS **************************************
print(f"First subtask: {first_subtask('standard')}")
print(f"Second subtask: {second_subtask('standard')}")


# **************************************** TESTS *******************************************
@pytest.mark.parametrize(
    ("input_type", "expected"), [("dummy", 24000), ("standard", 71300)], ids=["dummy_input", "standard_input"]
)
def test_fist_subtask(input_type, expected):
    assert first_subtask(input_type) == expected


@pytest.mark.parametrize(
    ("input_type", "expected"), [("dummy", 45000), ("standard", 209691)], ids=["dummy_input", "standard_input"]
)
def test_second_subtask(input_type, expected):
    assert second_subtask(input_type) == expected
