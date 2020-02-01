def split_number(number):
    array = []
    while number > 0:
        array.append(number % 10)
        number = number // 10
    return list(reversed(array))

###################################################

#origin_number = int(input())
origin_number  = 999123152467
control_number = 279146358279

array_origin_number = split_number(origin_number)
array_control_number = split_number(control_number)

print(array_origin_number)
print(array_control_number)

result = 0
for i in range(0, len(array_origin_number)):
    result = result + array_origin_number[i] * array_control_number[i]

result = result % 11
if result == 10:
    print(1)
else:
    print(result)
