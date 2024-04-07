#!/usr/bin/env python3
""" Test link Many-To-Many Place <> Amenity
"""
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

# creation of a State
state = State(name="California")
state.save()
print("State: {}".format(state))

# creation of a City
city = City(state_id=state.id, name="San Francisco")
city.save()
print("City: {}".format(city))

new_city = City(state_id=state.id, name="Los Angeles")
new_city.save()

# creation of a User
user = User(email="john@snow.com", password="johnpwd")
user.save()

# create another user
user2 = User(email="abdelrahman@greencoder.tech", password="abdelrahmanpwd")
user2.save()

print("User: {}".format(user))
print("User 2: {}".format(user2))

# creation of 2 Places
place_1 = Place(user_id=user.id, city_id=city.id, name="House 1")
place_1.save()
print("Place 1: {}".format(place_1))
place_2 = Place(user_id=user.id, city_id=city.id, name="House 2")
place_2.save()
print("Place 2: {}".format(place_2))

another_place_for_user2 = Place(user_id=user2.id, city_id=new_city.id, name="House 3 in los angeles")
another_place_for_user2.save()

# creation of 3 various Amenity
amenity_1 = Amenity(name="Wifi")
amenity_1.save()
print("Amenity 1: {}".format(amenity_1))
amenity_2 = Amenity(name="Cable")
amenity_2.save()
print("Amenity 2: {}".format(amenity_2))
amenity_3 = Amenity(name="Oven")
amenity_3.save()
print("Amenity 3: {}".format(amenity_3))

# link place_1 with 2 amenities
place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)

# link place_2 with 3 amenities
place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)

another_place_for_user2.amenities.append(amenity_1)
another_place_for_user2.amenities.append(amenity_2)
another_place_for_user2.amenities.append(amenity_3)

# create review_1 and link it to place_1
review_1 = Review(place_id=place_1.id, user_id=user.id, text="Great place")
review_1.save()
print("Review 1: {}".format(review_1))

# create review_2 and link it to place_1
review_2 = Review(place_id=place_1.id, user_id=user.id, text="really amazing place")
review_2.save()
print("Review 2: {}".format(review_2))

# create review_3 and link it to place_2
review_3 = Review(place_id=place_2.id, user_id=user.id, text="terrible place")
review_3.save()
print("Review 3: {}".format(review_3))

# create review_4 and link it to place_1
review_4 = Review(place_id=another_place_for_user2.id, user_id=user2.id, text="awesome place")
review_4.save()

review_5 = Review(place_id=place_1.id, user_id=user2.id, text="I love this place")
review_5.save()

review_6 = Review(place_id=place_2.id, user_id=user2.id, text="I hate this place")
review_6.save()

storage.save()

print("OK")
