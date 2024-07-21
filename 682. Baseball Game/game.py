class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        if len(operations) == 0:
            return 0

        for index, value in enumerate(operations):
            if value == "C":
                record.pop()
            elif value == "D" and index != 0:
                record.append(record[-1]*2)
            elif value == "+" and index != 0:
                record.append(record[-1] + record[-2])
            else:
                record.append(int(value))

        return sum(record)
            
        