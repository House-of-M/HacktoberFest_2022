from marvel import Marvel

marvel = Marvel(
  PUBLIC_KEY='', # get your key at developer.marvel.com
  PRIVATE_KEY='') # get your key at developer.marvel.com

characters = marvel.characters

my_char = characters.all(nameStartsWith="Beyonder")["data"]["results"]

for char in my_char:
  print(char["id"], char["name"])
  for comic in char["comics"]["items"]:
    print(comic["name"])
  print("-------------------------------")
  print("-------------------------------")