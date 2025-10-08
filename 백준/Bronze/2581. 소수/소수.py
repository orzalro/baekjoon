m, n = int(input()), int(input())

prime_list = [i for i in range(2, n + 1)]
prime_i = 0
while prime_i < len(prime_list):
    prime_num = prime_list[prime_i]
    if prime_num > int(n ** 0.5): break
    del_list = [i for i in range(prime_num * 2, n + 1, prime_num)]
    prime_list = [num for num in prime_list if num not in del_list]
    prime_i += 1

answer_list = [num for num in prime_list if num >= m]
if answer_list:
    print(sum(answer_list), answer_list[0], sep = '\n')
else:
    print('-1')