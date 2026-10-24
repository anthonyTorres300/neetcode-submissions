class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # I want to loop through the whole list 
        # Find whether they are in a dictionary
            # If they are not in a dictionary add them 
            # If they are +1 to the value 
        # Once the loop is done, do another loop for k times
        # This is to find the max 

        result = []
        temp = {}
        for num in nums: 
            if num not in temp: 
                temp[num] = 1
            else:
                temp[num] += 1
        for i in range(k): 
            high = max(temp, key=temp.get)
            result.append(high)
            temp.pop(high)
        return result

        