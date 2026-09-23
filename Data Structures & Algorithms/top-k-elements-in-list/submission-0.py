class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a hash table to count freuencys 

        table = {}

        for num in nums:
            if num not in table:
                table[num] = 0
            table[num] +=1
        #return list(table.keys())

        returnMe = []
        # for anything in range k 
        for _ in range(k):
            maxv = max(table.values())
            for num in table:
                if table[num] == maxv:
                    returnMe.append(num)
                    table[num] = 0
                    break
            

        return returnMe

