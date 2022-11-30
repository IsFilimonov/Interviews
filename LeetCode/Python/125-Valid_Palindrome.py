import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Best practices.
        str.translate() more faster that regulars and loops.
        R: O(n)
        M: O(1)
        """
        s = s.translate(str.maketrans('','',string.punctuation))  # drop punctuation
        s = "".join(s.split())  # drop spaces
        s = s.lower()  # casefold more agressive (ASCII vs UNICODE)

        return s == s[::-1]


    def isPalindrome_1(self, s: str) -> bool:
        """
        str.casefold(): to capeless
        str.isalnum(): only letters and numbers
        R: O(n)
        M: O(1)
        """
        s = list(filter(str.isalnum, s.casefold()))
        for i in range(0,len(s)//2):
            if s[i] == s[(i*-1)-1]:
                continue
            else:
                return False
        return True


if __name__ == "__main__":
    s = Solution()

    tests = (
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("   ", True),
    )

    for test in tests:
        exec("assert s.isPalindrome(test[0]) == test[1]")

    print("Well done!")
