class Solution:
    def findComplement(self, num: int) -> int:
        n = num
        binary_list = list(bin(n)[2:])
        
        for idx, c in enumerate(binary_list):
            if c == "0":
                binary_list[idx] = "1"
            else:
                binary_list[idx] = "0"
        
        return int("".join(binary_list), 2) 
