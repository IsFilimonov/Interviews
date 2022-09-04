class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Check input constraint.
        assert x >= (-2**31) and x <= ((2**31)-1)

        # Use simple str reverse sort.
        # Note: all negative numbersa are not polindrom (-100 -> 001-)
        # Another solution but more longer: ''.join(reverse(x))
        return True if x == 0 or str(x) == str(x)[::-1] else False


if __name__ == "__main__":
    s = Solution()

    assert s.isPalindrome(0) == True
    assert s.isPalindrome(-1000) == False
    assert s.isPalindrome(-2**31) == False
    assert s.isPalindrome(121) == True
