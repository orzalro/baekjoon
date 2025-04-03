import sys

input = sys.stdin.readline

n, m = map(int, (input().split()))
num = list(map(int, input().split()))

def calc(arr, m):
    result = []
    if m < 1:
        return
    else:
        for i in range(0, len(arr)):
            new_arr = arr[:i];new_arr.extend(arr[i + 1:])
            temp = calc(new_arr, m - 1)
            if temp is not None:
                for j in temp:
                    result.append([arr[i], j])
            else: result.append(arr[i])
        return result

def answer(result):
    if type(result) is int:
            return str(result)
    else:
        ans = ''
        for i in range(len(result)):
            ans = ' '.join([ans, answer(result[i])])
        return ans.lstrip()

num.sort()
result = calc(num, m)
s = set()
for i in range(len(result)):
    string = answer(result[i])
    if string not in s:
        s.add(string)
        print(string)