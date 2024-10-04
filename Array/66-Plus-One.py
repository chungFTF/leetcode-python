# 66. Plus-One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # Sol. 2
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits


        # Sol.1 
        # last_d = len(digits) - 1

        # while last_d >= 0:
        #     digits[last_d] += 1
        #     if(digits[last_d] > 9):
        #         digits[last_d] = 0

        #         if last_d == 0:
        #             digits.insert(0,1)
        #         last_d -= 1

        #     else:
        #         break                        

        # return digits

                
        