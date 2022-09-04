from typing import (List,)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        assert 1 <= len(strs) <= 200
        assert all([0 <= len(strs[i]) <= 200 for i in range(len(strs))])
        assert all([el.islower() for el in strs])

        # First reference object
        f = strs[0]
        # Output prefix
        o = ''
        # Check prefix status
        s = True

        # The first object is not empty
        if f:
            while s and len(f) > 0:
                # Check prefix + 1 symbol
                if all([el.startswith(o+f[0]) for el in strs]):
                    o += f[0]
                    f = f[1:]
                else:
                    s = False

        return o

    def longestCommonPrefix_MostPythonic(self, strs: List[str]) -> str:
        """
        Most pythonic:
            find min value and use double loop to check for a match
            before the first difference.
        """
        if not strs:
            return ""

        shortest = min(strs, key=len)

        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]

        return shortest

    def longestCommonPrefix_BestPractice(self, strs: List[str]) -> str:
        """
        Best practice:
            loop by first zip symbols!
        """
        pre = ""
        for t in zip(*strs):
            if len(set(t)) == 1:
                pre += t[0]
            else:
                break
        return pre


if __name__ == "__main__":
    s = Solution()

    tests = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["a"], "a")
    ]

    for test in tests:
        exec("assert s.longestCommonPrefix(test[0]) == test[1]")
        exec("assert s.longestCommonPrefix_MostPythonic(test[0]) == test[1]")
        exec("assert s.longestCommonPrefix_BestPractice(test[0]) == test[1]")

    print("Done!")
