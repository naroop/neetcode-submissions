import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)

        start_pointer = 0
        end_pointer = len(s) - 1

        while start_pointer < end_pointer:
            if s[start_pointer].lower() != s[end_pointer].lower():
                return False

            start_pointer += 1
            end_pointer -= 1

        return True