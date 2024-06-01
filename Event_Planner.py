#Task 1

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)


#Task 2

#audio system
#projector
additional_facilities = "audio system" if venue == "large hall" else "projector"
print(additional_facilities)


#Task 3

vegetarian = input("Do you want vegetarian food (yes/no): ")
caterers = "Veggie Delight Caterers" if vegetarian == "yes" else "Gourmet Meals Caterers"
print(caterers)