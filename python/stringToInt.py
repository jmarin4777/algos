class Solution:
    def myAtoi(self, str: str) -> int:
        i = 0
        sign = 1
        num = 0
        maxInt = 2 ** 31 - 1
        minInt = -2 ** 31
        while i < len(str) and str[i] == " ":
            i += 1
        
        if i < len(str) and (str[i] == "+" or str[i] == "-"):
            sign = -1 if str[i] == "-" else 1
            i += 1
        
        while i < len(str) and str[i] >= "0" and str[i] <= "9":            
            if num > maxInt // 10 or (num == maxInt // 10 and str[i] > "7"):
                return minInt if sign == -1 else maxInt
            num = num * 10 + (ord(str[i]) - ord('0'))
            i += 1
        
        return num * sign

obj = Solution()
print(obj.myAtoi("42"))
print(obj.myAtoi("   -42"))
print(obj.myAtoi("4193 with words"))
print(obj.myAtoi("words and 987"))
print(obj.myAtoi("-91283472332"))
print(obj.myAtoi("-2147483648"))
