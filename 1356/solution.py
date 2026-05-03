class Solution_rmvd:
    def sortByBits(self, arr: List[int]) -> List[int]:
        tuples = []

        for num in arr:
            tuples.append((Counter((bin(num).replace("0b", "")))["1"], num))
        
        tuples.sort()

        return [num for _, num in tuples]
        
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key = lambda num: (num.bit_count(), num))
        return arr
