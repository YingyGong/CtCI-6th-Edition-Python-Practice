# O(N)
import unittest


def urlify_algo(string, length):
    """replace spaces with %20 and removes trailing spaces"""
    # convert to list because Python strings are immutable
    char_list = list(string)
    new_index = len(char_list)

    for i in reversed(range(length)):
        if char_list[i] == " ":
            # Replace spaces
            char_list[new_index - 3 : new_index] = "%20"
            new_index -= 3
        else:
            # Move characters
            char_list[new_index - 1] = char_list[i]
            new_index -= 1
    # convert back to string
    return "".join(char_list[new_index:])


def urlify_pythonic(text, length):
    """solution using standard library"""
    return text[:length].replace(" ", "%20")

# I made three errors initially: first, str in Python can not be modified in place; 
# secondly, when I do reverse replacing, remember that indexing in Python is [a: b] (a inclusive but b exclusive)
# lastly, if I modify char_list, I need to clear first few chars
def my_sol(string: str, length: int) -> str:
    n = len(string)
    i = n - 1
    forward_idx = length - 1
    char_list = list(string)
    new_list = [''] * n 
    while i > -1 and forward_idx > -1:
        if char_list[forward_idx] != ' ':
            new_list[i] = char_list[forward_idx]  
            i -= 1
            forward_idx -= 1

        else:
            new_list[i-2:i+1] = "%20"
            i -= 3
            forward_idx -= 1 
    
    # remove trailing zero
    string = "".join(new_list)
    return string.strip()


class Test(unittest.TestCase):
    """Test Cases"""

    test_cases = {
        ("much ado about nothing      ", 22): "much%20ado%20about%20nothing",
        ("Mr John Smith       ", 13): "Mr%20John%20Smith",
        (" a b    ", 4): "%20a%20b",
        (" a b       ", 5): "%20a%20b%20",
    }
    testable_functions = [urlify_algo, urlify_pythonic, my_sol]

    def test_urlify(self):
        for urlify in self.testable_functions:
            for args, expected in self.test_cases.items():
                actual = urlify(*args)
                assert actual == expected, f"Failed {urlify.__name__} for: {[*args]}"


if __name__ == "__main__":
    unittest.main()
