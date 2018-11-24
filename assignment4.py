'''
This program inputs a number and returns a word version of that number (i.e. 0 to zero)
'''

# First, let's define the dictionaries. I'm, only going to go up to undecillion because I doubt we need to go past this
ones = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ",
        "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]

twenties = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]

thousands = ["", "thousand ", "million ", "billion ", "trillion ", "quadrillion ", "quintillion ", "sextillion ",
             "septillion ", "octillion ", "nonillion ", "decillion ", "undecillion "]


def takeThree(n): # Helper function
    """
    This is a helper function takes which takes in a value less than
    1000, and then returns the word version of it.

    :param n: a number less than 1000 to convert
    :return : the returned word version of the number passed
    """
    c = n % 10  # singles digit
    b = ((n % 100) - c) / 10  # tens digit
    a = ((n % 1000) - (b * 10) - c) / 100  # hundreds digit
    t = ""
    h = ""
    if a != 0 and b == 0 and c == 0: # If it is only hundreds
        t = ones[int(a)] + "hundred "
    elif a != 0: # If it is hundreds and other stuff
        t = ones[int(a)] + "hundred and "
    if b <= 1:
        h = ones[int(n) % 100]
    elif b > 1:
        h = twenties[int(b)] + ones[int(c)]
    st = t + h
    return st

def spell(num):
    """
    This function is the main function which can be used by the user, turning the accepted number into a spelled version
    of itself. Can be any fairly large negative to positive number

    :param num: the number which this function accepts to turn
    :return: the word version of the number passed
    """
    if num == 0:  # Safety case
        return 'zero'
    negative = False
    if (num < 0):
        negative = True
        num = abs(num)
    i = 3
    n = str(num)
    word = ""
    k = 0
    while(i == 3):
        nw = n[-i:]
        n = n[:-i]
        if int(nw) == 0:
            word = takeThree(int(nw)) + thousands[int(nw)] + word
        else:
            word = takeThree(int(nw)) + thousands[k] + word
        if n == '':
            i = i+1
        k += 1
    if not negative:
        return word[:-1]
    else :
        return "negative " + word[:-1]

print (spell (123456789) )
print (spell (456678) )
print (spell (66) )
print (spell (-123456789) )
print (spell (-456678) )
print (spell (-418) )
print (spell (-13456678) )
print (spell (0) )
print (spell (10004) )


''' 
####### OUTPUT #######

one hundred and twenty three million four hundred and fifty six thousand seven hundred and eighty nine
four hundred and fifty six thousand six hundred and seventy eight
sixty six
negative one hundred and twenty three million four hundred and fifty six thousand seven hundred and eighty nine
negative four hundred and fifty six thousand six hundred and seventy eight
negative four hundred and eighteen
negative thirteen million four hundred and fifty six thousand six hundred and seventy eight
zero
ten thousand four

'''