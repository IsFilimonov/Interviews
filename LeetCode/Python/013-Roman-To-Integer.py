class Solution:
    d = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        # 6 subtraction rules:
        # - I can be placed before V (5) and X (10) to make 4 and 9.
        # - X can be placed before L (50) and C (100) to make 40 and 90.
        # - C can be placed before D (500) and M (1000) to make 400 and 900.
        "CM": 900,
        "CD": 400,
        "XC": 90,
        "XL": 40,
        "IX": 9,
        "IV": 4
    }

    def romanToInt(self, s: str) -> int:
        ss = s
        out = 0

        assert 1 <= len(s) <= 15
        assert set(s).issubset(self.d.keys())

        while len(ss) > 0:

            if ss[0] in ["C", "X", "I"] and ss[0:2] in self.d:
                out += self.d[ss[0:2]]
                ss = ss[2:]
            else:
                out += self.d[ss[0]]
                ss = ss[1:]

        assert 1 <= out <= 3999

        return out


if __name__ == "__main__":
    s = Solution()

    assert s.romanToInt("III") == 3
    assert s.romanToInt("LVIII") == 58
    assert s.romanToInt("MCMXCIV") == 1994
