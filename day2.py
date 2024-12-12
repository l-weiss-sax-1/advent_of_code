def main():
    with open("day2.txt") as file:
        amount_safe = 0
        for line in file:
            safe = calculate_valid(line.strip())
            if safe:
                amount_safe += 1
        print(amount_safe)


def calculate_valid(line: str) -> bool:
    result = False
    line_parts = line.split(" ")
    last_seen_part: int = -1  # set last_seen to negative number, as there are not negative numbers in day2 input
    difference_potential = 0  # difference_potential keeps track of weather it's an increase or decrease

    err_count_correction = 0

    for part in line_parts:
        if err_count_correction > 1:
            return False
        if last_seen_part == -1:
            last_seen_part = int(part)  # do we need to handle try [str -> int] parsing?
            continue
        else:
            difference = abs(int(part) - last_seen_part)

            if determine_is_valid_option([1, 2, 3, -1, -2, -3], difference):
                result = True
            else:
                # we still need to 'remove' the value that violated the rule and handle it
                err_count_correction += 1
                # last_seen_part = int(part)
                continue

            new_difference_potential = int(part) - last_seen_part
            if difference_potential == 0:
                difference_potential = new_difference_potential
            elif difference_potential < 0 < new_difference_potential:
                err_count_correction += 1
            elif difference_potential > 0 > new_difference_potential:
                err_count_correction += 1

            last_seen_part = int(part)

    if err_count_correction > 1:
        return False
    else:
        return result


def determine_is_valid_option(options: [int], difference):
    result = False
    for option in options:
        if difference == option:
            result = True
    return result


if "__name__" == main():
    main()
