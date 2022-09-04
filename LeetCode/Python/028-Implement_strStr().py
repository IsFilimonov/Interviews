from string import ascii_lowercase


class Solution:
    def validate(self, haystack: str, needle: str) -> None:
        assert 1 <= len(haystack) <= 104
        assert 1 <= len(needle) <= 104
        assert all([el in ascii_lowercase for el in haystack + needle])

    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == "__main__":
    s = Solution()

    tests = (
        ("hello", "ll", 2),
        ("aaaaa", "bba", -1),
    )

    for test in tests:
        exec("s.validate(*test[:2])")
        exec("assert s.strStr(*test[:2]) == test[2]")

    print("Well done!")
