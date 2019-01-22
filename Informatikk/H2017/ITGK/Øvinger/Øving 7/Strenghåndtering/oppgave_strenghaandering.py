# a


def check_equal(str1, str2):
    if str1 == str2:
        return True
    else:
        return False


str1 = 'hei'
str2 = 'hello'
str3 = 'hello'
print(check_equal(str1, str2))
print(check_equal(str2, str3))

# b


def reversed_word(str):
    new_str = str[::-1]
    return new_str


print(reversed_word("Morna Jens"))

# c


def check_palindrome(str):
    if str == reversed_word(str):
        return True
    else:
        return False


print(check_palindrome("agnes i senga"))
print(check_palindrome("hello"))


# d


def contains_string(str1, str2):
    if str2 in str1:
        return str1.index(str2)

    else:
        return -1


print(contains_string("Pepperkake", "per"))
print(contains_string("Pepperkake", "ola"))
