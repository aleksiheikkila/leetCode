# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        rst = []
        words = s.split(" ")
        
        for word in words:
            if word == "":
                rst.append(" ")  # handles multiple whitespaces. Not needed per the desc.
            else:
                rst.append(word[::-1])           
                
        return " ".join(rst)
        