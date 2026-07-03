class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}  # dictionary to store groups of anagrams
        for word in strs:  # loop through each word
            key = tuple(sorted(word))  # sort the word to use as a key
            if key not in result:  # if this key doesn't exist yet
                result[key] = []  # create an empty list for it
            result[key].append(word)  # add the word to its group
        return list(result.values())  # return all the groups