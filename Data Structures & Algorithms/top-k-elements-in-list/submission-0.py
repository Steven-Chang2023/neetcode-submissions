class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lowend = 100000
        highend = 0

        hm = {}

        for val in nums:
            if val not in hm:
                hm[val] = 1
            else:
                hm[val] += 1

            if hm[val] < lowend:
                lowend = hm[val]
            if hm[val] > highend:
                highend = hm[val]
        

        buckets = [0] * (highend - lowend + 1)


        
        for i in range(highend - lowend + 1):
            buckets[i] = []
        
        for key, value in hm.items():
            buckets[value - lowend].append(key)
        
        output = []

        reverse_index = len(buckets) - 1

        while(len(output) < k):
            for num in buckets[reverse_index]:
                if len(output)< k:
                    output.append(num)
                else:
                    break
            reverse_index -= 1

        return output




