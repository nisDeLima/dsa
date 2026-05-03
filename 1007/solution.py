class Solution:
    def minDominoRotations_removed(self, tops: List[int], bottoms: List[int]) -> int:
        res = float("inf")
        for cand in [tops[0], bottoms[0]]:
            curr_res = 0
            for i in range(len(tops)):
                if tops[i] != cand and bottoms[i] == cand:
                    curr_res += 1
                elif tops[i] != cand:
                    curr_res = float("inf")
            res = min(res, curr_res)


        for cand in [tops[0], bottoms[0]]:
            curr_res = 0
            for i in range(len(bottoms)):
                if bottoms[i] != cand and tops[i] == cand:
                    curr_res += 1
                elif bottoms[i] != cand:
                    curr_res = float("inf")
            res = min(res, curr_res)
        return res if res != float("inf") else -1
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            t_c , b_c = 0, 0
            for i,j in zip(tops,bottoms):
                if i!= x and j!= x:
                    return float('inf')
                if i!=x:
                    t_c+= 1
                if j!=x :
                    b_c +=1 
            return min(t_c,b_c)       
        
        c1 = tops[0]
        c2 = bottoms[0]
        res = min(check(c1), check(c2))
        return -1 if res ==float('inf') else res
