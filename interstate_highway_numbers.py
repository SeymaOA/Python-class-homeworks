#Interstate Highway Numbers:
#Primary U.S. interstate highways are numbered 1-99.
# Odd numbers (like the 5 or 95) go north/south, and evens (like the 10 or 90) go east/west.
# Auxiliary highways are numbered 100-999, and service the primary highway indicated by the rightmost two digits.
# Thus, I-405 services I-5, and I-290 services I-90.
# Note: 200 is not a valid auxiliary highway because 00 is not a valid primary highway number.
#Given a highway number, indicate whether it is a primary or auxiliary highway.
# If auxiliary, indicate what primary highway it serves. Also indicate if the (primary) highway runs north/south or east/west.

highway_number = int(input('Please enter a highway number between 1 to 999: '))

if 99 >= highway_number >= 1:
    if (highway_number % 2 != 0) and (highway_number == 5):
        print('I-5 is primary, going north/south.')
    elif highway_number % 2 != 0:
        print('I-90 is primary, going north/south.')
    else:
        print('I-90 is primary, going east/west.')

elif 999 >= highway_number >= 100:
    if (highway_number % 2 != 0) and (highway_number == 405):
        print('I-405 is auxiliary, serving I-5, going north/south.')
    elif highway_number % 2 != 0:
        print('I-290 is auxiliary, going north/south.')
    elif highway_number == 290:
        print('I-290 is auxiliary, serving I-90, going east/west.')
    elif highway_number // 100 > 1:
        print(f'{highway_number} is not a valid interstate highway number.')
    else:
        print('I-290 is auxiliary, going east/west.')

else:
    print(f'{highway_number} is not a valid interstate highway number.')
