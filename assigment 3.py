'''
This program will define and call a combine function that merges a list of dictionaries
into one master dictionary. It tests the data on a given list of dictionaries.

Pranav Eranki - 10/9/2018
'''
def combine(dicts):
    new = {}
    for dict in dicts:
        # Defining key lists for ease in code
        newKeys = []
        oldKeys = []
        # Filling our key lists with values
        for key in new:
            newKeys.append(key)
        for key in dict:
            oldKeys.append(key)

        for key in oldKeys: # For each key in the keys of the dict given
            if key in newKeys: # If key w/ that name already exists
                vals = dict[key] # Get its value
                if type(vals) == list: # If the old dict's value for the key is a list
                    if (type(new[key])) == list: # If the new value for the key is a list also
                        new[key] = list(set(dict[key] + new[key]))
                    else: # If the new value for the key is not a list
                        if (new[key] in dict[key]): # If the new dict's key value is in the given dict's key values
                            new[key] = dict[key] # Just make the new dict's key value the given dict's key value
                        else: # If the new dict's key values is not the given dict's key values
                            new[key] = list(set(dict[key] + [new[key]]))
                else:  # If the key value is not a list
                    if type((new[key])) == list:
                        new[key] = list(set(new[key] + [dict[key]]))
                    else:
                        if not (vals == new[key]):  # If the value is not already in the new array
                            new[key] = [new[key], vals]
            else: # If key w/ the name given does not exist in the new dict
                new[key] = dict[key] # Add the key
    return new




# original dictionaries
roommate1Shopping = {'fruit': 'apples', 'meat': 'chicken', 'vegetables': 'potatoes', 'drinks': ['beer','wine'], 'dessert': 'ice cream'}
roommate2Shopping = {'fruit': 'lemons', 'meat': 'hamburger', 'drinks': ['apple juice', 'orange juice', 'vodka']}
roommate3Shopping = {'fruit': ['oranges', 'bananas'], 'vegetables': ['lettuce', 'carrots'], 'drinks': 'milk'}
# Making a list by concatenating all the dictionaries
dicts = [roommate2Shopping, roommate1Shopping, roommate3Shopping]

# Making an expected dictionary for the expected output
Expected = {'meat': ['hamburger', 'chicken'],
'fruit': ['lemons', 'apples', 'oranges', 'bananas'],
'vegetables': ['lettuce', 'carrots', 'potatoes'],
'drinks': ['beer', 'wine', 'apple juice', 'orange juice', 'vodka', 'milk'],
'dessert': 'ice cream'}

# Calling our combine function on the dictionaries
new = combine(dicts)

print("The expected dictionary is : " + str(Expected)) # This prints the expected output with the given dictionaries
print("\n")
print("The dictionary returned from our program is : " + str(new)) # This prints our generated dict from our program

'''
Output : May look like different dictionaries, but only order is different. Also, lines are split for easy readability

The expected dictionary is : {'meat': ['hamburger', 'chicken'], 'fruit': ['lemons', 'apples', 'oranges', 'bananas'], 
'vegetables': ['lettuce', 'carrots', 'potatoes'], 'drinks': ['beer', 'wine', 'apple juice', 'orange juice', 'vodka', 'milk'], 
'dessert': 'ice cream'}


The dictionary returned from our program is : {'fruit': ['bananas', 'oranges', 'lemons', 'apples'], 
'meat': ['hamburger', 'chicken'], 'drinks': ['wine', 'orange juice', 'milk', 'beer',
'apple juice', 'vodka'], 'vegetables': ['potatoes', 'carrots', 'lettuce'], 'dessert': 'ice cream'}

'''