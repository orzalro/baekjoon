def solution(phone_book):

    d = {key:0 for key in phone_book}
    for num in phone_book:
        n = ''
        for char in num[:-1]:
            n += char
            if n in d:
                return False
   
    return True