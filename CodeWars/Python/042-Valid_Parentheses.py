# Solution
def valid_parentheses(string):
    new = ''.join([i for i in string if i in '()'])
    while '()' in new:
        new = new.replace('()', '')
    return len(new) == 0

# FYA Best practices
# def valid_parentheses(string):
#     cnt = 0
#     for char in string:
#         if char == '(': cnt += 1
#         if char == ')': cnt -= 1
#         if cnt < 0: return False
#     return True if cnt == 0 else False