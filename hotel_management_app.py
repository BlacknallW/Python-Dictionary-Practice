#This program keeps track of guests by floor and room number

hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus']
  }
}

check_in = input("Good evening. Are you checking in or checking out? ('in' or 'out') ").lower()

if check_in == "in":
    floor_number = input("What floor would you like your room to be on? (1, 2, or 3) ")
    room_number = input("What would you like your room number to be? ")
    if room_number in hotel['1'] or room_number in hotel["2"] or room_number in hotel["3"]:
      print("This room is occupied. Sorry. Pick another room. ")
    else:  
      occupant_number = input("How many occupants will be staying, including yourself? ")
      occupant_names = input("Please give the first and last names of each occupant, including yourself. Separate each person's name with a comma. ").split(",")
      hotel[floor_number][room_number] = occupant_names
      print(hotel)
else:
    floor_number = input("What floor are you on? ")
    room_number = input("What is your room number? ")
    try:
        hotel[floor_number].pop(room_number)
        print(f"You have successfully been checked out of Room # {room_number}. We hope you enjoyed your stay. Come back and see us!")
        print(hotel)
    except KeyError:
        print("You never checked into the hotel to begin with. You should try checking in first.")    
    
