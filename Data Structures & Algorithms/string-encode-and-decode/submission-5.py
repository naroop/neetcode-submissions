class Solution:

    def encode(self, strs: List[str]) -> str:
        big = ""
        for string in strs:
            big += str(len(string)) + "#" + string 
        return big

    def decode(self, s: str) -> List[str]:
        decoded = []

        p = 0
        while p < len(s):
            section_length = ""

            while s[p] != "#":
                section_length += s[p]
                p += 1

            p += 1
            section_length = int(section_length)
            
            word = ""
            for i in range(0, section_length):
                word += s[p]
                p += 1

            decoded.append(word)

        return decoded

            
            




