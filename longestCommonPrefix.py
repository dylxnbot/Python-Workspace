class longestCommonPrefix:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_common_prefix = len(strs[0])

        # if curr_word has same first char as prev word for entire list, common total + 1
        # want to make a loop that then checks first char of first word with first char of next word until last word
        for i in range(len(strs) - 1):
            curr_word = strs[i]
            next_word = strs[i + 1]
            
            common_prefix = 0
            
            for char in range(min(len(curr_word), len(next_word))):
                if curr_word[char] == next_word[char]:
                    common_prefix += 1  # counting number of common characters in current pair
                else:
                    break

            min_common_prefix = min(min_common_prefix, common_prefix)   # why do i need this line
                                                                        # updating the minimum number of characters by comparing the
                                                                        # matching number of characters in the first pair of words to the second
                
        common_prefix = strs[0][:min_common_prefix]
        #print(common_prefix)
        return common_prefix
                
            
test_list = ["flower","flow","flight"]
test = longestCommonPrefix()
test.longestCommonPrefix(test_list)