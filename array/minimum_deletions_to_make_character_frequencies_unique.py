"""
1647. Minimum Deletions to Make Character Frequencies Unique
Difficulty:Medium
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

 

Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.
Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
Example 3:

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
 

Constraints:

1 <= s.length <= 105
s contains only lowercase English letters.

"""

class Solution:
  def minDeletions(self, s: str) -> int:
    temp = {}
    for i in s:
      if i in temp.keys():
        temp[i] += 1
      else:
        temp[i] = 1
    temp_value = sorted(temp.values(), reverse=True)

    ret = 0
    for i in range(1, len(temp_value)):
      if temp_value[i-1] == 0:
        ret = ret + temp_value[i]
        temp_value[i] = 0
      elif temp_value[i-1] == temp_value[i]:
        temp_value[i] -= 1
        ret = ret + 1
      elif temp_value[i-1] < temp_value[i]:
        ret = ret + temp_value[i] - temp_value[i-1] + 1
        temp_value[i] = temp_value[i-1] - 1

    return ret
        
if __name__ == "__main__":
  solution = Solution()
  # print(solution.minDeletions('aaabbbcc'))
  # print(solution.minDeletions('ceabaacb'))
  print(solution.minDeletions('aaaabbbbccccdddd'))
  print(solution.minDeletions('accdcdadddbaadbc'))
  print(solution.minDeletions('bbcebab'))