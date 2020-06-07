# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.

def verbing(s):
    if len(s) >= 3:
        if s[-3:] != 'ing': s +='ing'
    else:
        s += 'ly'
    return s



# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!


def not_bad(s):
    n = s.find('not')
    b = s.find('bad')
    if n != -1 and b != -1 and b > n:
        s = s.replace(s[n:b+3],'good')
    return s


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back

def front_back(a, b):
    a_front = len(a)/2
    b_front = len(b)/2
    a_back =  len(a)/2 
    b_back = len(b)/2
   
    if len(a)%2 == 1: 
        a_front += 1
        
    if len(b)%2 == 1: 
        b_front += 1   
    return a[:a_front] + b[:b_front] + a[a_front:] + b[b_front:]
