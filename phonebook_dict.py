#Performs tasks on phonebook dictionary

phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

print(phonebook_dict["Alice"])
#Add Kareem
phonebook_dict["Kareem"]= "938-489-1234"
#Remove Alice
phonebook_dict.pop("Alice")
#Edit Bob
phonebook_dict["Bob"] = "968-345-2345"

print(phonebook_dict)