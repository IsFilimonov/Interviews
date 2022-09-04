def first_non_repeating_letter(string):     
    s = string.lower()
    d = {}

    for i, v in enumerate(string):
        next = s.find(v.lower(), i+1)

        if next > 0 and v.lower() not in d:
            d[v.lower()] = True

        if v.lower() not in d:
            return v
        
    return ''

# FYA Best practice by str.count()
# def first_non_repeating_letter(string):
#     string_lower = string.lower()
#     for i, letter in enumerate(string_lower):
#         if string_lower.count(letter) == 1:
#             return string[i]
            
#     return ""