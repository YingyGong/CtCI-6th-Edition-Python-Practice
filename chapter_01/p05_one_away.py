# O(N)
import time
import unittest


def are_one_edit_different(s1, s2):
    """Check if a string can converted to another string with a single edit"""
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    if len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    if len(s1) - 1 == len(s2):
        return one_edit_insert(s2, s1)  # noqa
    return False


def one_edit_replace(s1, s2):
    edited = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if edited:
                return False
            edited = True
    return True


def one_edit_insert(s1, s2):
    edited = False
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True

def my_sol(s1, s2):
    m = len(s1)
    n = len(s2)
    if abs(m - n) > 1:
        return False
    if m == n:
        p = 0
        count = 0
        while p < m:
            if s1[p] == s2[p]:
                p += 1
                continue
            count += 1
            p += 1
            if count > 1:
                return False
        return True
    
    # I should write a helper function to avoid overlapping.
    elif m > n: # m > n by 1
        p1, p2 = 0, 0
        only_one_mismatch = True
        while p1 < m and p2 < n:
            if s1[p1] != s2[p2]:
                if only_one_mismatch:
                    p1 += 1
                    only_one_mismatch = False

                else:
                    return False
            else:
                p1 += 1
                p2 += 1
        return True
    else:
        p1, p2 = 0, 0
        only_one_mismatch = True
        while p1 < m and p2 < n:
            if s1[p1] != s2[p2]:
                if only_one_mismatch:
                    p2 += 1
                    only_one_mismatch = False
                else:
                    return False
            else:
                p1 += 1
                p2 += 1
        return True



class Test(unittest.TestCase):
    test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        # permutation with insert shouldn't match
        ("ale", "elas", False),
    ]

    testable_functions = [are_one_edit_different, my_sol]

    def test_one_away(self):

        for f in self.testable_functions:
            start = time.perf_counter()
            for _ in range(100):
                for [text_a, text_b, expected] in self.test_cases:
                    assert f(text_a, text_b) == expected
            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    unittest.main()
