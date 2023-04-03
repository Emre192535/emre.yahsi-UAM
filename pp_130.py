def get_sum(num: int) -> int:
    if num < 10:
        return num
    else:
        return num % 10 + get_sum(num // 10)
    
num = int(input("enter the number"))
sum_of_digits = get_sum(num)
print(sum_of_digits) 