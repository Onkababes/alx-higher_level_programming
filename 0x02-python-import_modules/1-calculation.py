#!/usr/bin/python3
from calculator_1 import div, mul, add, sub

a = 10
b = 5

result_div = div(a, b)
result_mul = mul(a, b)
result_add = add(a, b)
result_sub = sub(a, b)

print("{} / {} = {}".format(a, b, result_div))
print("{} * {} = {}".format(a, b, result_mul))
print("{} + {} = {}".format(a, b, result_add))
print("{} - {} = {}".format(a, b, result_sub))
