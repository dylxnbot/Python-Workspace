class romanToInteger:
    def romanToInt(self, s: str) -> int:
        numbers = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        # evaluate from back to front
        # if num starting at back is less than the one in front add if not subtract
        # IV 5 > 1 so 5 - 1
        # VI 1 < 5 so 5 + 1
        
        # create loop that runs for the amount of characters in roman number
        
        total = 0
        prev_num = 0
        
        backwards_s = s[::-1]
        
        for char in backwards_s:
            curr_num = numbers[char]
            
            if curr_num < prev_num:
                total -= curr_num
            else:
                total += curr_num
            
            prev_num = curr_num
            
        print(total)
        return total
        
        
test = romanToInteger()
test.romanToInt("XIV")