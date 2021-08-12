class Solution(object):
    def game(self, guess, answer):
        c=0
        for i in range(len(guess)):
            if guess[i]==answer[i]:
                c=c+1
        return c
