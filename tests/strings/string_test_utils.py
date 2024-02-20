def print_long_string(s):
    """
    Prints a long string, automatically wrapping lines
    at space characters to ensure the entire string fits
    within the visible screen area.

    :param s: The long string to be printed.
    :return: None
    """
    max_len = 68
    curr_index = 0

    while curr_index < len(s):
        next_index = min(curr_index + max_len, len(s))
        line = s[curr_index:next_index]

        if next_index < len(s) and s[next_index] != " ":
            last_space = line.rfind(" ")
            if last_space != -1:
                next_index = curr_index + last_space + 1
                line = s[curr_index:next_index]

        print(line)
        curr_index = next_index
