# Code is unreachable warning in Python

# ✅ works as expected
def example():
    a = 123
    return 'bobbyhadz.com'

b = 456 # 👈️ declared outside function
print(b)

example()