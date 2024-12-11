## zip(*iterables) = aggregate elemts from two or more iterables (list, tuples, sets, etc.)
#                    creates a zip object with paired stored in tuples for each element

# usernames = ['Dude','Bro', 'Mister']
# passwords= ('damn', 'abc123', 'guest')

# users = dict(zip(usernames, passwords))
# print(type(users ))
# login_date = ['1/1/2021','1/3/2024','1/3/2024']
# # for key, value in users.items():
# #     print(key+":"+value)

# users = zip(usernames,passwords,login_date)
# for i in users: 
#     print(i)






######################################### zip in python############################################



# Zip Practice #1
# Print to the screen phrases like the following example:

# "The capital of Germany is Berlin"

# Use the zip function, loops, and the following lists of countries and capitals to solve it quickly and efficiently.

capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]

countCaps = dict(zip(countries,capitals))

for count,cap in countCaps.items():
    print('The capital of '+ count+' is '+ cap)


# Zip Practice #2
# Create a zip object made up of lists, of a set of brands and products that you prefer, inside the my_zip variable.
brands = ['nike','lelabo','GM','Acne']
products =['shoes','perfume','glasses','Jeans']

brand = dict(zip(brands,products))
print((brand))

# Zip Practice #3
# Create a zip object with the translations of the numbers from 1 to 5 in Spanish, Portuguese and English (in that same order), and then convert the generated object into a list called numbers:

# one / um / one

# two / two / two

# three / three / three

# four / four / four

# five / five / five

# The result should follow the structure:

# [('one', 'um', 'one'), ('two', 'dois', 'two'), ... ]

# 1: uno / um / one
# 2: dos / dois / two
# 3: tres / três / three
# 4: cuatro / quatro / four
# 5: cinco / cinco / five


#######################zip function challenge#####################
# Challenge: Create a list of countries and their capitals, then zip them together and print
# each country with its capital.

# Two lists: countries and capitals


# Use zip to pair countries with their capitals