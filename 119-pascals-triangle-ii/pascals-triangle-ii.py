from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]  # ✅ Start with the first row of Pascal's Triangle
        
        for i in range(1, rowIndex + 1):  # ✅ Iterate from 1 to rowIndex (inclusive)
            row = [1] * (i + 1)  # ✅ Initialize row with all 1s
            
            for j in range(1, i):  # ✅ Fill middle values using previous row
                row[j] = res[i - 1][j - 1] + res[i - 1][j]

            res.append(row)  # ✅ Append the row to result
        
        return res[-1]  # ✅ Return the last row
