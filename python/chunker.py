class Solution:
    def evaluate(self, expr: str, **outer_scope) -> int:
        
        def splitter(expr):
            depth = 0
            chunk = ''
            for c in expr:
                if c == ' ' and depth == 0:
                    yield chunk
                    chunk = ''
                else:
                    chunk += c
                    if c == '(':
                        depth += 1
                    if c == ')':
                        depth -= 1
            yield chunk
                
        
        if expr.startswith('(') and expr.endswith(')'):
            func, *args = splitter(expr[1:-1])
            
            if func == 'add':
                a, b = args
                return self.evaluate(a, **outer_scope) + self.evaluate(b, **outer_scope)
            
            if func == 'mult':
                a, b = args
                return self.evaluate(a, **outer_scope) * self.evaluate(b, **outer_scope)
            
            else:
                *args, expr = args
                names, values = args[::2], args[1::2]
                print(names, values, expr)
                inner_scope = {name: self.evaluate(value, **outer_scope) for name, value in zip(names, values)}
                return self.evaluate(expr, **inner_scope, **outer_scope)
             
        else:
            return int(expr)

s = Solution()
s.evaluate("(let x 2 (mult x 5))")