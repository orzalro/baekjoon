s = input().split()
word_list = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
new_s = ''
if s[0] in word_list:
    new_s = s[0][0].upper()
for word in s:
    if word not in word_list:
        new_s = ''.join([new_s, word[0].upper()])
print(new_s)