"""
Python script that will read and write to csv files
@author Samuel Tregea
"""

import csv
import random
import time

# Global list to contain a list of unique VIN numbers
vins = []


def random_str(start: int, end: int):
    """
    Helper function that takes a start and end point to determine
    the length of a string
    :param start: the starting range
    :param end: the ending range
    :return: a newly generated string
    """
    chars_str = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    new_string = ""
    for i in range(start, end):
        char = random.randrange(len(chars_str))
        new_string = new_string + chars_str[char]
    return new_string


def format_list(file_name: str):
    """
    Helper function that will format a string from a list
    :param file_name: the file name to choose a name
    :return: a new and random string
    """
    list_of_names = read_file(file_name)
    temp = str(random.choice(list_of_names))
    final_string = temp[2:-2]
    return final_string


def read_file(txt_file: str):
    """
    Read names from a txt file and then write the nsmes to a csv file
    :param txt_file: the file to read from
    :return: The list containing the names
    """
    with open(txt_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        my_list = list(csv_reader)

    return my_list  # return the list of names


def new_or_used(flag: bool):
    """
    Function that determines if a car is new or used
    :param flag: the flag to determine if New or Used
    :return: New if true, Used otherwise
    """
    if flag:
        return "New"
    else:
        return "Used"


def mileage():
    """
    Create a random number to represent the mileage of an automobile
    :return: the mileage of a car
    """
    miles = random.randint(0, 200000)
    return miles


def vin():
    """
    Randomly create a 17 digit vin number
    :return: the vin of a automobile
    """
    vin_id = random_str(0, 17)
    return vin_id.upper()  # could return random_str(), placed the variable for easier reading


def m_or_f():
    """
    Determine if the customer is a male or female
    :return: Male or Female
    """
    number = random.randint(1,2)

    if number == 1:
        return "M"
    if number == 2:
        return "F"


def salary():
    """
    Generate the income of a customer
    :return: the income
    """
    income = random.randint(1000, 1000000)
    return income


def create_id(counter: int, id_letter: str):
    """
    Create a customer id, uses a counter to guarantee
    unique values. Used within a loop.
    :param counter: the counter being used
    :param id_letter: 'C' for Customer, 'S' for salesman
    :return: a new id for the customer
    """
    customer_id = id_letter + str(counter)
    return customer_id


def first_name():
    """
    Generate the first name of an individual
    :return: the first name
    """
    return format_list("first_names")


def last_name():
    """
    Generate the last name of an individual
    :return: the last name
    """
    return format_list("last_names")


def format_email(emails: str, length_of_user: int):
    """
    Helper function that will format a email
    :param emails: the email to be formatted
    :param length_of_user: the length of the username
    :return: the newly formatted number
    """
    formatted_email = "{}@{}".format(emails[:length_of_user], emails[length_of_user:])
    return formatted_email


def email():
    """
    Generate an email for an individual
    :return: a new email
    """
    length_of_username = random.randint(4, 16)  # setting min length to 4, max at 16
    username = random_str(0, length_of_username)

    num = random.randint(1, 5)

    temp = ""
    if num == 1:
        temp = "yahoo.com"
    if num == 2:
        temp = "icloud.com"
    if num == 3:
        temp = "gmail.com"
    if num == 4:
        temp = "rit.edu"
    if num == 5:
        temp = "aol.com"
    if num == 6:
        temp = "live.com"

    emails = username+temp

    return format_email(emails, length_of_username)


def year():
    """
    Generate a random year between 2000 and 2020
    :return: a year
    """
    years = random.randint(2000, 2020)
    return years


def month():
    """
    Generate a month between January and December
    :return: a random month
    """
    months = random.randint(1, 12)
    return months


def day():
    """
    Generate a random day
    :return: a random day
    """
    days = random.randint(1, 31)
    return days


def sale_price():
    """
    Generate a random sale price
    :return: the sale
    """
    sale = random.randint(1000, 500000)
    return sale


def car_doors():
    """
    Generate doors between 2-4
    :return: number of doors
    """
    doors = [2, 4]
    number_of_doors = doors[random.randint(0, 1)]
    return number_of_doors


def car_brand():
    """
    Generate a random string that depicts the
    brand of a car
    :return: the car's brand
    """
    return format_list("car_brand")


def car_body():
    """
    Generate a random string that depicts the
    body of a car
    :return: the car's body
    """
    return format_list("car_body")


def car_model():
    """
    Generate a random string that depicts the
    model of a car
    :return: the car's model
    """
    return format_list("car_model")


def car_mpg():
    """
    Generate the mpg of a vehicle
    :return: the mpg
    """
    return random.randint(15, 45)


def color():
    """
    Generate a random string that depicts the
    color of a car
    :return: the car's color
    """
    return format_list("colors")


def format_phone(number: str):
    """
    Helper function that will format a phone number
    :param number: the number to be formatted
    :return: the newly formatted number
    """
    formatted_num = "({})-{}-{}".format(number[:3], number[3:6], number[6:])
    return formatted_num


def phone_number():
    """
    Function that will generate a phone number
    :return: a newly generated phone number
    """
    num_str = "0123456789"
    temp_number = ""
    new_string = ""

    for i in range(0,10):
        char = random.randrange(len(num_str))
        new_string = new_string + num_str[char]

    for number in new_string:
        temp_number += number

    formatted_number = format_phone(temp_number)

    return formatted_number


def address_number():
    """
    Create a random address number
    :return: a new address number
    """
    return random.randint(0, 10000)


def address_street():
    """
    Create a random street
    :return: a randomized street
    """
    street_list = read_file("street_names")

    temp = str(random.choice(street_list))
    street_name = temp[2:-2]

    num = random.randint(1, 5)

    if num == 1:
        temp = "Rd."
    if num == 2:
        temp = "St."
    if num == 3:
        temp = "Ave"
    if num == 4:
        temp = "Dr."
    if num == 5:
        temp = "Lane"

    rand_street = street_name + " " + temp

    return rand_street


def address_city():
    """
    Create a random city
    :return: a random city
    """
    return format_list("cities")


def address_state():
    """
    Generate a State Abbreviation
    :return: a state abbreviation
    """
    return format_list("state_initials")


def address_zip():
    """
    Generate a 5-digit zip code
    :return: a newly generated zip code
    """
    d1 = random.randint(1, 9)  # when 0 nothing shows up, therefore random num between 1 and 9
    d2 = random.randint(0, 9)
    d3 = random.randint(0, 9)
    d4 = random.randint(0, 9)
    d5 = random.randint(0, 9)

    zip_code = str(d1)+str(d2)+str(d3)+str(d4)+str(d5)
    return zip_code


def create_dealership_name():
    """
    Create a random name for a dealership
    :return: the name for the dealership
    """
    return last_name() + ' Auto'


def get_dealer_id():
    """
    Pick a random a dealer
    :return: a dealer id
    """
    return create_id(random.randint(0, 500), 'D')


def get_customer_id():
    """
    Pick a random customer
    :return: a customer id
    """
    return create_id(random.randint(0, 500), 'C')


def get_dealership_id():
    """
    Return a random dealership id
    :return: a dealership id
    """
    return create_id(random.randint(0,500), 'DS')


def create_brand_dict():
    """
    Generate a dictionary containing the car's make (brand name)
    :return: a new table for the make
    """
    brands = dict()
    with open('car_brand.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['Name'])
        list_of_makers = read_file('car_brand')

        for maker in list_of_makers:
            brand = [str(maker)[2:-2]]
            writer.writerow(brand)

        for i in range(0, 15):
            brand = str(list_of_makers[i])[2:-2]
            brands[brand] = brand

    return brands


def create_vehicle_table():
    """
    Generate a Vehicle table
    :return: a table depicting vehicles and a dictionary containing the vin and color of a car
    """
    with open('vehicle.csv', 'w', newline='') as file:

        # used to keep track of the VIN belonging to a vehicle
        vehicle_dictionary = dict()

        writer = csv.writer(file)

        # writer.writerow(['VIN', 'Color', 'Mileage', 'New/Used', 'Model'])
        for i in range(0, 500):
            vin_id = vin()
            vins.append(vin_id)

            colors = color()

            vehicle_dictionary[vin_id] = colors

            miles = mileage()
            if miles < 300:  # if a new car
                usage = new_or_used(True)  # setting to new car
            else:
                usage = new_or_used(False)

            price_of_vehicle = sale_price()

            writer.writerow([vin_id, colors, miles, usage, car_model(),price_of_vehicle])

    return vehicle_dictionary


def create_customer_table():
    """
    Generate a Customer table
    :return: a table depicting customers
    """
    with open('customer.csv', 'w', newline='') as file:

        # used to keep track of the dealer id's
        dealer_dictionary = dict()

        writer = csv.writer(file)

        # writer.writerow(['ID', 'First Name', 'Last Name', 'Address #', 'Street Name', 'City', 'State',
        #                  'Zip Code', 'Phone Number', 'Gender', 'Salary', 'Dealer ID'])

        for i in range (0, 500):

            dealer_id = get_dealer_id()

            writer.writerow([create_id(i, 'C'), first_name(), last_name(), address_number(), address_street(),
                             address_city(), address_state(), address_zip(), phone_number(),
                             m_or_f(), salary(), dealer_id])

            # using a dictionary to store dealers so a dealer_id doesn't appear more than once
            dealer_dictionary[dealer_id] = dealer_id

    return dealer_dictionary


def create_dealership_table(brand_dictionary: dict):
    """
    Generate a table for dealerships
    :return: a dealership table and a dictionary of brands to be used
    """

    list_of_brands = list()  # list that will contain a list of brands being used
    dealersip_dict = dict()

    for brand in brand_dictionary:
        list_of_brands.append(brand)

    with open('dealership.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # writer.writerow(['ID', 'Phone', 'Name', 'House Number', 'Street', 'City',
        #                  'State', 'Zip', 'Brands'])

        for i in range(len(list_of_brands)):
            ds_id = get_dealership_id()
            writer.writerow([ds_id, phone_number(), create_dealership_name(), address_number(),
                             address_street(), address_city(), address_state(), address_zip(), list_of_brands[i]])
            dealersip_dict[ds_id] = ds_id

    return dealersip_dict


def create_dealer_table(dealers: dict, dealership_id : dict):
    """
    Generate a Salesmen table
    :return: a table depicting salesmen
    """

    list_of_dealerships = list()

    for id in dealership_id:
        list_of_dealerships.append(id)

    with open('dealer.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # writer.writerow(['ID', 'First Name', 'Last Name', 'Phone', 'Email'])

        i = 0
        for dealer in dealers:
            writer.writerow([dealer, first_name(), last_name(), phone_number(), email(), list_of_dealerships[i % len(list_of_dealerships)]])
            i += 1


def create_manufacturer_table():
    """
    Create a table with manufacturers and their list of brands
    :return: a table for car manufacturers
    """
    with open('car_manufacturer.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # writer.writerow(['Manufacturer', 'Brand'])
        list_of_makers = read_file('car_manufacturer')
        for maker in list_of_makers:
            writer.writerow([maker[0], maker[1]])


def create_car_brand_table():
    """
    Generate a table for the car's make (brand name)
    :return: a new table for the make
    """
    with open('car_brand.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['Name'])
        list_of_makers = read_file('car_brand')

        for maker in list_of_makers:
            writer.writerow([str(maker)[2:-2]])


def create_car_models_table(brands: dict, vin_dictionary: dict):
    """
    Generate a table for the model of a car
    :return: a table for the model of a car
    """
    list_of_brands = list()  # list that will contain a list of brands being used
    list_of_vins = list()

    for brand in brands:
        list_of_brands.append(brand)

    for vin in vin_dictionary:
        list_of_vins.append(vin)

    with open('car_model.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # writer.writerow(['ID', 'Name', 'Year', '# of Doors', 'MPG', 'Brand', 'Body'])

        for i in range(len(list_of_vins)):
            writer.writerow([create_id(i, 'M'), car_model(), year(), car_doors(), car_mpg(),
                             list_of_brands[i % len(list_of_brands)], car_body(), vins[i]])


def create_sale_table(dealers: dict):
    """
    Generate a table for the sale of a car
    :return: a new table for the sale
    """
    list_of_dealers = list()

    # adding dealer keys into a list
    for dealer in dealers:
        list_of_dealers.append(dealer)

    with open('sales.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # writer.writerow(['Sale_ID', 'Total', 'Year', 'Month', 'Day', 'Dealer_ID', 'VIN'])
        for i in range(500):
            writer.writerow([create_id(i, 'S'), sale_price(), year(), month(), day(), create_id(i, 'C'),
                             list_of_dealers[i % len(list_of_dealers)], vins[i]])


def create_employs_table(dealerships: dict, dealers: dict):
    """
    Generate a employment relationship with a dealer and dealership.
    A dictionary is used to guarantee a unique dealer being assigned
    to a unique dealership.
    :param dealerships: the dictionary of dealerships
    :param dealers: the dictionary of dealers
    :return: none
    """
    list_of_dealerships = list()

    for dealership in dealerships:
        list_of_dealerships.append(dealership)

    with open('employs.csv', 'w', newline='') as file:

        writer = csv.writer(file)

        i = 0
        for dealerID in dealers:
            writer.writerow([list_of_dealerships[i%len(list_of_dealerships)], dealerID])
            i += 1


def main():
    """
    Generate csv files
    :return: none
    """
    brand_dict = create_brand_dict()
    start_time = time.time()
    print("Beginning process...")
    print("Creating: vehicle.csv")
    # create a dictionary with vin id's and create a table
    vin_dictionary = create_vehicle_table()
    print("Complete.")
    print("Creating: customer.csv")
    # storing dealer id's that are to be placed into a dealer table
    dealer_dictionary = create_customer_table()
    print("Complete.")
    print("Creating: dealership.csv")
    dealership_dictionary = create_dealership_table(brand_dict)
    print("Complete.")
    print("Creating: dealer.csv")
    create_dealer_table(dealer_dictionary, dealership_dictionary)
    print("Creating: car_manufacturer.csv")
    create_manufacturer_table()
    print("Complete.")
    print("Creating: car_model.csv")
    create_car_models_table(brand_dict, vin_dictionary)
    print("Complete.")
    print("Creating: sales.csv")
    create_sale_table(dealer_dictionary)
    print("Complete.")
    print("Creating: employs.csv")
    create_employs_table(dealership_dictionary, dealer_dictionary)
    print("Complete.")
    total_time = time.time()-start_time
    print("Process took: " + str(total_time) + " seconds.")


if __name__ == '__main__':
    main()