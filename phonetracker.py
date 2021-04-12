print('This program is created by Harshit Tripathi. ')
print('Copyright 2021 Harshit Tripathi. ')
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
a=input('Enter Your Phone Numbers: ')
phone_numbers=phonenumbers.parse(a)
print(geocoder.description_for_number(phone_numbers,'en'))
print(carrier.name_for_number(phone_numbers,'en'))

x=input('Do you want to ask any question? ')
