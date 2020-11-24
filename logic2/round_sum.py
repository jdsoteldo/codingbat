def round_sum(a, b, c):

  def round10(num):
    return (num+5)//10*10

  return round10(a) + round10(b) + round10(c)

# other solution
# def round_sum(a, b, c):
#   return round10(a) + round10(b) + round10(c)
#
# def round10(num):
#     residual = num % 10
#     if(residual>=5):
#         return (num-residual+10)
#     else:
        # return (num-residual)


print(round_sum(16, 17, 18))
print(round_sum(12, 13, 14))
print(round_sum(25, 32, 102))
