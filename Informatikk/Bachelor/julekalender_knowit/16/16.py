import requests

DEFAULT_TEXT = "".join(requests.get('https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-palindrom.txt').text.split(","))


def is_prime(n):
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        #print("Is_prime")
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True


def sum_digits(n):
    #print("sumDigits")
    return sum(map(int, str(n)))


def all_palindromes(text=DEFAULT_TEXT):
    biggest_prime = 0

    text_length = len(text)
    for idx, char in enumerate(text):

        # Check for longest odd palindrome(s)
        start, end = idx - 1, idx + 1
        while start >= 0 and end < text_length and text[start] == text[end]:
            num = sum_digits(text[start:end+1])
            if is_prime(num) and num > biggest_prime:
                biggest_prime = num

            start -= 1
            end += 1

        # Check for longest even palindrome(s)
        start, end = idx, idx + 1
        while start >= 0 and end < text_length and text[start] == text[end]:
            num = sum_digits(text[start:end + 1])
            if is_prime(num) and num > biggest_prime:
                biggest_prime = num

            start -= 1
            end += 1
        print(biggest_prime)
    return biggest_prime


def main(text=DEFAULT_TEXT):
    print(all_palindromes(text))


main()

#print(sum_digits(12))