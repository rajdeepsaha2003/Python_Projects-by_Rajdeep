import phonenumbers 
from phonenumbers import timezone,geocoder,carrier,carrierdata
while True:
    number=input("Entar a number with country code:\t")
    phone=phonenumbers.parse(number)
    time=timezone.time_zones_for_geographical_number(phone)
    cari=carrier.name_for_number(phone,"en")
    reg=geocoder.description_for_number(phone,"en")
    # Validating a phone number
    valid = phonenumbers.is_valid_number(phone)
  
# Checking possibility of a number
    possible = phonenumbers.is_possible_number(phone)
    print(f"Phone number:\t{phone}\nValid:\t{valid}\nPossible:\t{possible}\nTimezone:\t{time}\nService Provider:\t{cari}\nCountry:\t{reg}")