import sys
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]
answer = 0

for word in words:
    answer += 1
    word_length = len(word)
    for char in dict.fromkeys(word):
        i = word.index(char)
        count = 0
        while True:
            if i + count >= word_length or word[i + count] != char:
                break
            else:
                count += 1
        if word.count(char) != count:
            answer -= 1
            break

print(answer)