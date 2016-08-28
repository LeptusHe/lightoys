class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        min_pos,  min_len, s= self.manacher(s)
        ans = ""
        for i in range(min_pos - min_len, min_pos + min_len):
            ans += s[i] if s[i] != "#" else ""
        return ans

    def manacher(self, s):
        s = '#' + '#'.join(s) + '#'

        RL = [0] * len(s)
        MaxRight = 0
        pos = 0
        max_pos, MaxLen = 0, 0
        for i in range(len(s)):
            if i < MaxRight:
                RL[i] = min(RL[2 * pos - i], MaxRight - i)
            else:
                RL[i] = 1
            while i - RL[i] >= 0 and i + RL[i] < len(s) and s[i - RL[i]] == s[i + RL[i]]:
                RL[i] += 1
            if RL[i] + i - 1 > MaxRight:
                MaxRight = RL[i] + i - 1
                pos = i
            if RL[i] > MaxLen:
                MaxLen = RL[i]
                max_pos = i
        if s == "##":
            return [0, 0, s]
        else:
            min_pos, min_len = 0, len(s) + 1
            for i in range(len(s)):
                if s[i] != '#' and RL[i] < min_len:
                    min_pos = i
                    min_len = RL[i]
        print(s, RL)
        return [min_pos, min_len, s]

# testing cases
test_cases = ["ab",
              "",
              "a",
              "aa",
              "abc",
              "abab",
              "abab",
              "aacecaaa"]
for test_case in test_cases:
    print(Solution().shortestPalindrome(test_case))