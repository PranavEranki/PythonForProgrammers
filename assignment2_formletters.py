'''
This program will print three form letters asking for votes in the past election.
It uses hardcoded tuples to insert into a constant letter format

Pranav Eranki - 10/1/2018
'''

UNCHANGING = "Dear %s, \nI would like you to vote for %s \nbecause I think %s is best for  \nthis country. \nSincerely, \n%s"

# format = addressee, candidate, sender
letter_1 = "Steven", "Hillary Clinton", "Hillary Clinton", "Pranav"
letter_2 = "Rahul", "Donald Trump", "Donald Trump", "Pranav"
letter_3 = "Bhargav", "Bernie Sanders", "Bernie Sanders", "Pranav"
#Defining the array
letters = [letter_1, letter_2, letter_3]

#Prints the unchanging value with the letter values replaced in for the 'placeholders'
for letter in letters:
    print(UNCHANGING % letter)


# For this code, the output is:
"""
Dear Steven,
I would like you to vote for Hillary Clinton
because I think Hillary Clinton is best for
this country.
Sincerely,
Pranav

Dear Rahul,
I would like you to vote for Donald Trump
because I think Donald Trump is best for
this country.
Sincerely,
Pranav

Dear Bhargav,
I would like you to vote for Bernie Sanders
because I think Bernie Sanders is best for
this country.
Sincerely,
Pranav
"""