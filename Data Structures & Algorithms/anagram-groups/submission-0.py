class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = {}

        # iterate thru each string here
        for s in strs:
            # each string put in abc order no space in btwen
            key = ''.join(sorted(s))
            # if not in hashtable make a bucket at the key
            if key not in hashtable:
                hashtable[key] = []
            # add that string to respective bucket
            hashtable[key].append(s)
        return list(hashtable.values())
        