# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.

def close_far(a, b, c):
  con1 = abs(a - b) <= 1 and abs(b - c) >= 2 and abs(a - c) >= 2
  con2 = abs(a - c) <= 1 and abs(a - b) >= 2 and abs(b - c) >= 2

  return con1 or con2
