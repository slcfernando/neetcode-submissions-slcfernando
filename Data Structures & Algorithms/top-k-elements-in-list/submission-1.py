class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for n in nums:
            frequencies[n] = frequencies.get(n, 0) + 1

        top_k = [[] for _ in range(len(nums) + 1)]
        for n, freq in frequencies.items():
            top_k[freq].append(n)

        result = []
        for lst in reversed(top_k):
            for num in lst:
                result.append(num)
                if len(result) == k:
                    return result

        raise ValueError