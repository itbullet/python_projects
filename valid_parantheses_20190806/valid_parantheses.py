class Solution:

    def isValid(self, s):

        s = list(s)

        if s == "":

            return True

        if len(s)%2 != 0:

            return False

        i = 0

        while i < len(s)-1:

            size = len(s)

            if not s:

               return True

            if ((s[i] == "(" and s[i+1] == ")") or (s[i] == "[" and s[i+1] == "]") or (s[i] == "{" and s[i+1] == "}")):

                s.pop(i)
                s.pop(i)
                i -= 1

            else:

                i += 1

        if len(s) > 0:

            return False

        else:

            return True

    def isValidRecursion(self, s):

        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack


test1 = Solution()

print(test1.isValidRecursion("(("))
print(test1.isValid("()"))
print(test1.isValidRecursion("()[]{}"))
print(test1.isValid("(]"))
print(test1.isValidRecursion("([)]"))
print(test1.isValid("{[]}"))