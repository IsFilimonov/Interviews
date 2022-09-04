def count_sheeps(sheep):
  return sum([el for el in sheep if el is not None])

"""
Best practices:

def count_sheeps(sheep):
  return sheep.count(True)
"""