class Solution:
    def validate(self, s: str) -> None:
        assert 1 <= len(s[0]) <= 10**4
        assert set(s[0]).issubset(set("()[]{}"))

    def isValid(self, s: str) -> bool:
        """
            Long runtime but less memory usage.
        """
        if len(s) == 1 or (len(s) % 2) != 0:
            return False

        ss = s
        a = ["()", "[]", "{}"]

        # "()" in ss faster than ss.find()
        # while (ss.find("()") + ss.find("[]") + ss.find("{}")) > -3:
        while (("()" in ss) + ("[]" in ss) + ("{}" in ss)) > 0:
            for el in a:
                ss = ss.replace(el, "")
        else:
            return True if len(ss) == 0 else False

    def isValid_stack(self, s: str) -> bool:
        if len(s) == 1 or (len(s) % 2) != 0:
            return False

        open = set('([{')
        pair = set([('(', ')'), ('[', ']'), ('{', '}')])
        stack = []

        for el in s:
            if el in open:
                stack.append(el)
            else:
                if len(stack) == 0:
                    return False

                if (stack.pop(), el) not in pair:
                    return False

        return len(stack) == 0


if __name__ == "__main__":
    s = Solution()

    tests = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("(", False),
        ("((", False),
        (")[]", False),
        ("{[]}[({})]", True),
        ("((()))", True),
        ("(((()))", False),
        ("((()(]))", False)
    ]

    for test in tests:
        exec("s.validate(test)")
        exec("assert s.isValid(test[0]) == test[1]")
        exec("assert s.isValid_stack(test[0]) == test[1]")

    print("Well done!")
