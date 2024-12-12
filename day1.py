from collections import Counter


def separate_numbers(input_string) -> tuple[int, int]:
    """
    Separates two numbers from a given string and returns them as integers.

    Parameters:
    input_string (str): A string containing two numbers.

    Returns:
    tuple: A tuple containing the two separated numbers as integers.
    """
    # Use split to divide the string based on whitespace
    parts = input_string.split()

    # Convert the parts to integers
    if len(parts) == 2:
        return int(parts[0]), int(parts[1])
    else:
        raise ValueError("Input does not contain exactly two numbers.")


def create_lef_and_right_list(file) -> tuple[[int], [int]]:
    left_list = []
    right_list = []
    for line in file:
        first_number, second_number = separate_numbers(line)
        left_list.append(first_number)
        right_list.append(second_number)
    return left_list, right_list


def main():
    with open("day1.txt") as file:
        result_sum = calculate_sum_of_distances(file)
        print(result_sum)
        assert result_sum == 2756096

        file.seek(0)

        calculate_similarity_score(file)


def calculate_similarity_score(file):
    left_list, right_list = create_lef_and_right_list(file)
    score = calculate_similarity(left_list, right_list)
    print(f"Total similarity score: {score}")
    return score


def calculate_similarity(left_list, right_list):
    """
    Calculate the total similarity score by counting the occurrences of each number
    from the left list in the right list and multiplying it by the number.

    Args:
        left_list (list of int): The left list of numbers.
        right_list (list of int): The right list of numbers.

    Returns:
        int: The total similarity score.
    """
    # Count occurrences of each number in the right list
    right_count = Counter(right_list)

    # Calculate the similarity score
    similarity_score = 0
    for number in left_list:
        similarity_score += number * right_count.get(number, 0)

    return similarity_score


def calculate_sum_of_distances(file):
    left_list, right_list = create_lef_and_right_list(file)

    assert len(left_list) == len(right_list)
    result_list = []

    assert len(result_list) == 0
    while len(left_list) != 0:
        # result calculation
        smallest_left = min(left_list)
        smallest_right = min(right_list)
        distance_between_smallest = abs(smallest_left - smallest_right)
        result_list.append(distance_between_smallest)

        left_list.remove(min(left_list))  # Remove smallest from lists
        right_list.remove(min(right_list))

    assert len(left_list) == 0
    assert len(right_list) == 0

    return sum(result_list)


if "__name__" == main():
    main()
