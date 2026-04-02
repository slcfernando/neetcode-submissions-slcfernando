class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Get counts of each number in nums
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        # Create list of lists where index corresponds to frequency and the list contains the numbers that appeared with that frequency
        frequencies = [[] for _ in range(len(nums) + 1)]
        for n, c in counts.items():
            frequencies[c].append(n)

        # Get top k frequent elements using frequencies
        top_k = []
        for lst in reversed(frequencies):
            for n in lst:
                top_k.append(n)
                if len(top_k) == k:
                    return top_k
        
        raise ValueError