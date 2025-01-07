class Solution:
    def reverseWords(self, s: str) -> str:
        ans=""
        words = s.strip().split() #remove spaces

        for i in range(len(words)-1,-1,-1): #traverse in reverse
            ans+=words[i] #add each word
            ans+=" " #add space
        ans = ans.strip() #remove space at the beginning and ending

        return ans