class Solution:

    def encode(self, strs: List[str]) -> str:
        # Converting a list of str to one str
        # What's the separator?
        # How to efficiently use the bit operators?

        if len(strs) == 0:
            return ""

        # Try XOR first
        temp_list = []
        for string in strs:
            if not string:
                temp_list.append("WtFwTf")
            else:
                new_string = ''.join([chr(ord(char) ^ 69) for char in string])
                temp_list.append(new_string)
        return "\t\n\t".join(temp_list)
        # \n would be wrong for dummy_input=["@?wO"]
        # \t would be wrong for dummy_input=["L","k>D"]


    def decode(self, s: str) -> List[str]:

        if len(s) == 0:
            return []

        res = []
        split = s.split("\t\n\t")
        for string in split:
            if string == "WtFwTf":
                res.append("")
            else:
                ori_str = ''.join([chr(ord(char) ^ 69) for char in string])
                res.append(ori_str)
        return res
