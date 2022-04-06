# Python program to triple all numbers of a given list of integers, using Map
nums = [1,2,3,4,5,6,7]
result = map(lambda X: X + X + X, nums)
print("Triple of said list numbers:")
print(list(result))
