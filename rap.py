Rapper = {
    'name': ['kanye', 'lil uzi vert']
}

Age = {
    'kanye': 44,
    'lil uzi vert': 23
}

Album = {
    'lil uzi vert': [
      ('luv is Rapper 2', 2000),
      ('eternal atake', 2001)
    ], 
    'kanye': [
      ('College Drop', 2007),
      ('Life of Pablo', 2005),
      ('Yeezus', 2001),
      ('Late Registration', 1000)
    ],
}


# dirct.values 
def RapperCheck():
    # while true means loop forever!
         # made user inut translate to lowercase for case sens purposes
    user = str(input("Enter a Rapper ").lower())

    # if user input is valid, then return False
    # otherwise, return name, age and albums
    if user in Age.keys():  
      return (user, Age[user], Album[user])
    else:
      print('sorry ' + "'" + user + "'" + ' is not in our Rapperbase! ')
      return False


#what can i add into these parameters?

# While True loops infinitely untill break
while True:
  returned = RapperCheck()

  # if the user input is valid, then break the loop
  if not returned is False:
    break
name, age, album = returned

def func(x):
  return x[1]

func = lambda x : x[1]

print("before", album)
# sorting album by years
# lambda x : x[1] means sort album by the second item of each item of album
album = sorted(album, key=lambda x: x[0])
print("after", album)