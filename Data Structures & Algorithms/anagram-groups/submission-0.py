class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = {}

        for s in strs:
            count_array = [0] * 26
            for c in s:
                count_array[ord(c) - ord('a')] += 1
            count_tuple = tuple(count_array)

            if count_tuple not in counts:
                counts[count_tuple] = [s]
            else:
                counts[count_tuple].append(s)

        return list(counts.values())