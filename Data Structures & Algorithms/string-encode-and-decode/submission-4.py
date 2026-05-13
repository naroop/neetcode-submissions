class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        l = []
        for string in strs:
            if string == "":
                l.append("$")
                continue

            s = []
            for char in string:
                s.append(str(ord(char)))
            l.append(",".join(s))
        
        return '%'.join(l)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        split_s = s.split('%')
        l = []
        for string in split_s:
            if string == "$":
                l.append("")
                continue

            split_string = string.split(",")
            s = ""
            for n in split_string:
                s += chr(int(n))
            l.append(s)

        return l


