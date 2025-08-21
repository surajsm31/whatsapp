# import phonenumbers
# from phonenumbers import geocoder, carrier


# def trace_number(phone_number_str, region='IN'):
#     try:
#         # Parse the phone number
#         parsed_number = phonenumbers.parse(phone_number_str, region)
#
#         # Validate number
#         if not phonenumbers.is_valid_number(parsed_number):
#             return "❌ Invalid phone number."
#
#         # Get location and carrier
#         location = geocoder.description_for_number(parsed_number, 'en')
#         service_provider = carrier.name_for_number(parsed_number, 'en')
#
#         return f"📍 Location: {location}\n📞 Carrier: {service_provider}"
#
#     except phonenumbers.NumberParseException as e:
#         return f"❌ Error parsing number: {e}"
#
#
# # Example usage
# phone_input = input("Enter phone number with country code (e.g., +919876543210): ")
# result = trace_number(phone_input)
# print(result)


import phonenumbers
from phonenumbers import geocoder, carrier
import geocoder as geo


def locate_phone(number_str):
    try:
        phone_number = phonenumbers.parse(number_str)

        # Get region (like state/city)
        region = geocoder.description_for_number(phone_number, "en")

        # Get carrier (like Airtel, Jio)
        sim_carrier = carrier.name_for_number(phone_number, "en")

        # Use IP-based location (approx, since you can't track phone GPS)
        g = geo.ip('me')  # IP-based general location of your machine

        print("📞 Phone Number:", number_str)
        print("🌍 Region:", region)
        print("📡 Carrier:", sim_carrier)
        print("🗺️ Approx Location (IP-based):", g.city, g.state, g.country)

    except Exception as e:
        print("❌ Error:", str(e))


# Example usage:
number = input("Enter phone number with country code (e.g., +919876543210): ")
locate_phone(number)
