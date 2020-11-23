# the sum of 2 nums unless they are the same, if a = b return double their sum

def sum_double(a, b):
  if a != b:
    return a + b
  elif a == b:
    return (a + b) * 2
