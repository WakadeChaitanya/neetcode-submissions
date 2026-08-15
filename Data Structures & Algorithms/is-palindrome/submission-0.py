class Solution:
    def isPalindrome(self,s):
        arr = "".join(char.lower() for char in s if char.isalnum())
        left = 0 
        right = len(arr) -1 

        while left < right: 
            if arr[left] != arr[right]:
                return False 
            left +=1
            right -=1
        return True 

l = Solution()
print(l.isPalindrome("Was it a car or a cat I saw ?"))