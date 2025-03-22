"""
Problem: Longest Common Subsequence
Given two strings, find the length of the longest common subsequence.

Example:
Input: s1 = "abcde", s2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace".

Input: s1 = "abc", s2 = "def"
Output: 0

Input: s1 = "abc", s2 = "abc"
Output: 3
"""


def longestCommonSubsequence(s1, s2):
    rows, cols = len(s1), len(s2)
    dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if s1[r - 1] == s2[c - 1]:
                dp[r][c] = dp[r - 1][c - 1] + 1
            else:
                dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])
    return dp[rows][cols]


# Example usage
s1 = "abcde"
s2 = "ace"
print(longestCommonSubsequence(s1, s2))  # 3

s1 = "abc"
s2 = "def"
print(longestCommonSubsequence(s1, s2))  # 0

s1 = "abc"
s2 = "abc"
print(longestCommonSubsequence(s1, s2))  # 3