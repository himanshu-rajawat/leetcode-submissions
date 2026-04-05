class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_map = {5:0, 10:0, 20: 0}

        for bill in bills:
            bill_map[bill] = bill_map[bill]+1

            if bill==10:
                bill_map[5]= bill_map[5] - 1 
            elif bill==20:
                if bill_map[10]>0:
                    bill_map[10]= bill_map[10] - 1
                    bill_map[5]= bill_map[5] - 1
                else:
                    bill_map[5]= bill_map[5] - 3
            if any(v < 0 for v in bill_map.values()):
                return False

        return True