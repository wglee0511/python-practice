get_num = int(input())

new_num = get_num

count = 0

while True:
    ten = new_num // 10
    one = new_num % 10
    sum_ten_one = ten + one
    sum_one = sum_ten_one % 10
    count += 1
    new_num = int(str(one) + str(sum_one))

    if get_num == new_num :
        break
print(count)