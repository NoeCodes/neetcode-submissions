class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        master_dict = {}
        output = []

        # Return empty nested list if given empty list
        if (len(strs) == 0):
            return [[]]

        # Return standalone list if standalone was given
        if (len(strs) == 1):
            return[[strs[0]]]

        # Sort the string and use it as a key for a frequency dict
        for i in range(len(strs)):
            sorted_string = "".join(sorted(strs[i]))

            if (sorted_string not in master_dict):
                master_dict[sorted_string] = [strs[i]]

            else:
                master_dict[sorted_string].append(strs[i])

        # Build the output
        for key in master_dict:
            output.append(master_dict[key])



        return output