class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Make two different dictionaries for each strings 
        # Loop through both of the strings and add them to the value
        # Compare both of the dictionaries to see if they both are equal 
            # If they both are the same it will return True
            # Else return False 
        # Make a base case to check if the len of both strings are not the same
        if len(s) != len(t):
            return False
        sDic = dict()
        tDic = dict()
        for i in range(len(s)): 
            if s[i] not in sDic: 
                sDic[s[i]] = 1
            else:
                sDic[s[i]] += 1
            if t[i] not in tDic: 
                tDic[t[i]] = 1
            else:
                tDic[t[i]] += 1
        return sDic == tDic
            
        
        