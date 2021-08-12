class Solution(object):
    def letterCombinations(self, digits):
        dic= {"2": "abc","3": "def","4": "ghi","5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz",
            }
        if len(digits)<1:
            return []
        else:
            aa=[c for c in dic[digits[0]]]
            for t in digits[1:]:
                aa=[s+c for s in aa for c in dic[t] ]
            return aa
