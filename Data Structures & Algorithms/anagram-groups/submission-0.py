class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def func(s):
            binary = [0]*26
            for i in s:
                index = ord('a') - ord(i)
                binary[index] += 1
            return tuple(binary)

        new = []
        dic = {}
        for i in range(len(strs)):
            word = strs[i]
            binary = func(word)
            if binary in dic:
                dic[binary].append(word)
            else:
                dic[binary] = [word]
        res = []
        for key in dic:
            res.append(dic[key])
        return res

