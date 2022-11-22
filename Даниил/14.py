string = "aabbcde"

def func(string):
    if string(lambda x,y: str(len(x)) == str(len(y))):
        num = 1
        num += 1
        return f" {x} встречается дважды  и {x}"

print(func(string))

def duplicate_count(string):
    seen = set()
    more_than_one = set()
    for letter in string:
        if letter in seen:
            more_than_one.add(letter)
        else:
            seen.add(letter)
    return len(more_than_one)

print(duplicate_count(string))