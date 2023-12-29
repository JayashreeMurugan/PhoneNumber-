import phonenumbers
from phonenumbers import geocoder,carrier,timezone

phone=input("Enter phone number with country code here: ")
phone_number=phonenumbers.parse(phone)

#here how to know the country name
country_name=geocoder.description_for_number(phone_number,'en')
service_provider=carrier.name_for_number(phone_number,'en')

#to know the time zone
time_zone=timezone.time_zones_for_number(phone_number)
print("Country Name: ",country_name)
print("Service Provider: ",service_provider)
print("Time Zone: ",time_zone)