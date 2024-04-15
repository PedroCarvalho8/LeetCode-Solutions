class Solution(object):
    def romanToInt(self, s):

        convertion = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        global result
        result = 0

        global counter
        counter = 0
        for i in s:
            if(counter <= len(s)-1):
                if (counter+1 < len(s)):
                    if convertion[s[counter]] < convertion[s[counter+1]]:
                        result += int(convertion[s[counter+1]]) - int(convertion[s[counter]])
                        counter += 2
                    else:
                        result += convertion[s[counter]]
                        counter += 1
                else:
                    result += convertion[s[counter]]
                    counter += 1

        return(result) 
