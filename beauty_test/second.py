import pprint
import random

NUMBER_OF_TEST_GROUPS = 15


def get_random_group() -> list[str | int]:
    available_ids = ["665587", "669532", "669532", "665587", "669532"]
    available_versions = [1, 2, 3]
    return [random.choice(available_ids), random.choice(available_versions)]


def group_elements(versions: list[list[str | int]]) -> list[str | int]:
    unique_elements = [
        [i, v] for i, v in set(tuple(elem) for elem in versions)
    ]
    groupped_elems = []
    for group in unique_elements:
        group_count = versions.count(group)
        group.append(group_count)
        groupped_elems.append(group)
    return groupped_elems


if __name__ == "__main__":

    ungroupped_elems = [
        get_random_group() for _ in range(NUMBER_OF_TEST_GROUPS)
    ]
    groupped_elems = group_elements(ungroupped_elems)
    print(
        "\n",
        "UNGROUPPED ELEMENTS:",
        "(",
        len(ungroupped_elems),
        ")",
        "\n",
        "=" * 25,
    )
    pprint.pprint(ungroupped_elems, compact=True)
    print("\n")
    print("GROUPPED ELEMENTS:", "(", len(groupped_elems), ")", "\n", "=" * 25)
    pprint.pprint(groupped_elems, compact=True)
    print("\n")
