class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # function to get counter representation
        def get_counter(word):
            counter = [0]*26

            for char in word:
                counter[ord(char)-ord('a')]+=1
            return tuple(counter)

        groups = {}
        for word in strs:
            key = get_counter(word)
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        return list(groups.values())
            
        