class Solution:
    def isValid(self, s: str) -> bool:
        brack_map = {")":"(", "}":"{", "]":"["}
        stack = []

        for char in s: 
            if char in brack_map:
                if not stack:
                    return False
                top_element = stack.pop()
                if brack_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack 