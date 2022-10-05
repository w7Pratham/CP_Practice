class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        res = 0
        
        for i in items:
            if ruleKey == "type" and i[0] == ruleValue:
                res += 1
                
            if ruleKey == "color" and i[1] == ruleValue:
                res += 1
                
            if ruleKey == "name" and i[2] == ruleValue:
                res += 1
        
        return res
