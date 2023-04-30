class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """       
        str_list = s.split(" ")
        output = [" " for i in range(len(str_list))]
        
        for i in range(len(str_list)):
            output[int(str_list[i][-1]) - 1] = str_list[i][:-1]
        
        return " ".join(output)
