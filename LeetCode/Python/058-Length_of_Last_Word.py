#!/usr/bin/env python
from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Use standard functions
        """
        return len(s.split()[-1])


    def lengthOfLastWord_1(self, s: str) -> int:
        """
        Use simple reverse loop and break
        Less Runtime and memory.
        """
        word_lenght = 0
        
        for el in s[::-1]:
            if el != ' ':
                word_lenght += 1
            else:
                if word_lenght != 0:
                    break

        return word_lenght


if __name__ == "__main__":
    s = Solution()

    tests = (
        ("a", 1),
        ("a ", 1),
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
    )

    for test in tests:
        exec("assert s.lengthOfLastWord(test[0]) == test[1]")
        exec("assert s.lengthOfLastWord_1(test[0]) == test[1]")

    print("Well done!")
