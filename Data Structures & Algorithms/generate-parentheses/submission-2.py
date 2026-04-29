class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrace(opened, closed):
            if(opened == closed and opened == n):
                res.append("".join(stack))
                return 

            if(opened < n):
                stack.append("(")
                backtrace(opened + 1, closed)
                stack.pop()
            
            if(closed<opened):
                stack.append(")")
                backtrace(opened, closed + 1)
                stack.pop()


        backtrace(0, 0)
        return res