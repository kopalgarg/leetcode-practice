class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        result = 0
        index = 0
        n = len(s)
        
        INT_MAX = pow(2, 31)-1
        INT_MIN = -pow(2, 31)
        
        # skip over all leading spaces
        while index < n and s[index] == ' ':
            index +=1
     
        # check if -ve sign
        if index < n and s[index] == '+':
            sign = 1
            index +=1
        elif index < n and s[index] == '-':
            sign = -1
            index +=1
        
        # traverse and stop if non-numeric
        while index < n and s[index].isdigit():
            digit = int(s[index])
            # overflow and underflow conditions
            if ((result > INT_MAX//10) or (result == INT_MAX//10 and digit > INT_MAX %10)):
                return INT_MAX if sign ==1 else INT_MIN
            
            result = 10*result + digit
            index +=1
        return sign * result
            