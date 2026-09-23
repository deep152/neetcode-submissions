class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a hash table to count freuencys 

        table = {}

        for num in nums: # runs n times → O(n)
            if num not in table:
                table[num] = 0
            table[num] +=1

        returnMe = []
        # for anything in range k 
        for _ in range(k): # runs k times ← not n
            # get the number w most freq
            maxv = max(table.values()) # scans table: O(n)
# runs n times
            for num in table: # scans table: O(n)
                # find that maxv
                if table[num] == maxv:
                    # add to list and set to 0
                    returnMe.append(num)
                    table[num] = 0
                    break
        return returnMe

# the whole second part is k × O(n) = O(n·k)
'''
Heap → O(n log k). Keep a min-heap of size k.

Bucket sort → O(n). Index an array by frequency. This is the slick one, and it's the "real" answer to this exact problem.

'''