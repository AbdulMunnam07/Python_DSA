class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
    
        def rec_adder(x, n):
            if x > n:
                return
            res.append(x)
            m = x * 10
            for i in range(10):
                rec_adder(m + i, n)
        
        for i in range(1, 10):
            rec_adder(i, n)
        
        return res