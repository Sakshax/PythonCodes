"""
butterfly pattern

*        *
**      **
***    ***
****  ****
**********
**********
****  ****
***    ***
**      **
*        *

"""
def butterfly_pattern(n):
    # Upper half of the butterfly
    for i in range(n):
        stars = "*" * (i + 1)
        spaces = " " * (2 * (n - i - 1))
        print(stars + spaces + stars)
    # Lower half of the butterfly
    for i in range(n - 1, -1, -1):
        stars = "*" * (i + 1)
        spaces = " " * (2 * (n - i - 1))
        print(stars + spaces + stars)

if __name__ == "__main__":
    n = int(input("Enter the number of rows for the butterfly pattern: "))
    butterfly_pattern(n)
