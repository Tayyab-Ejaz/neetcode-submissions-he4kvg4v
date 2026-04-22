class Solution:
   def twoSum(self, numbers: List[int], target: int) -> List[int]:
    i = 0
    j = len(numbers) - 1

    while i < j:
        n = numbers[i] + numbers[j]
        if n == target:
            return [i + 1, j + 1]
        elif n < target:
            i += 1
        else:
            j -= 1

    return [-1, -1]

