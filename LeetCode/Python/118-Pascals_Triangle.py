from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]

        result = [[1],[1,1]]
        step = 2

        while step < numRows:
            last_array = result[-1]
            append_array = [1]
            for i in range(1, len(last_array)):
                append_array += [last_array[i] + last_array[i-1]]
            append_array += [1]
            result.append(append_array)
            step += 1

        return result



if __name__ == "__main__":

    s = Solution()

    tests = (
        (1, [[1]]),
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
    )

    for test in tests:
        exec("assert s.generate(test[0]) == test[1]")

    print("Well done!")
