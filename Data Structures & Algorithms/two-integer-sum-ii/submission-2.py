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


# Agar J or I ka combination target se barra he toh J ka kissi b 
# i+1, i+2, i+3 ke sath b combination nhi ban skta. So eliminate j
# So you discard all possible cominations of j.
