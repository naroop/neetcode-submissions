class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_dict = {}

        for s in strs:
            o = [str(0) for x in range(0, 26)]

            for char in s:
                o[ord(char) - 97] = str(int(o[ord(char) - 97]) + 1)

            parsed_o = ",".join(o)

            if parsed_o in string_dict:
                string_dict[parsed_o].append(s)
            else:
                string_dict[parsed_o] = [s]

        return list(string_dict.values())
