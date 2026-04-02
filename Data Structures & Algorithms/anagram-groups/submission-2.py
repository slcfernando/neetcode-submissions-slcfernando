from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use character counts as keys to a hashmap, which has values that have that hashmap (aka anagrams of each other)
        character_counts_hash = defaultdict(list)

        for s in strs:
            # use a list (to be converted to tuple) to track counts of 26 lowercase English letters
            character_counts = [0] * 26
            for c in s:
                character_counts[ord(c) - ord('a')] += 1

            tuple_character_counts = tuple(character_counts)
            character_counts_hash[tuple_character_counts].append(s)

        return list(character_counts_hash.values())