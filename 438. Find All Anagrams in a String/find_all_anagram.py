class Solution:
    def findAnagrams(s , p):
        res = []
        if len(p) > len(s):
            return []
        map_s, map_p = {} , {}
        for i in range(len(p)):
            map_p[p[i]] = 1 + map_p.get(p[i],0)
            map_s[s[i]] = 1 + map_s.get(s[i],0)
        if map_p == map_s:
            res.append(0)
        l  = 0    # 2nd index to be return
        for r in range(len(p) , len(s)):
            map_s[s[r]] = 1 + map_s.get(s[r]  , 0) 
            # addine the new ele to teh map 
            map_s[s[l]] -=1
            # remocing ele
            if map_s[s[l]] == 0:
                map_s.pop(s[l])
            l +=1
            if map_s == map_p:
                res.append(l)
        return res

        '''
        time : O(s)
        space : O(p)
        '''