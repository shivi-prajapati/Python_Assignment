'''Assignment 2: Robust Phonebook Contact Registry
Scenario
You are writing a Command-Line Interface (CLI) contact registry that maps user names to their 
phone numbers. The program needs to validate user inputs robustly to prevent corrupted formatting 
or empty values from breaking the registry database.'''


class InvalidPhoneNumberError(Exception):
    pass


def register_details(contact_details, name_inp, contact_inp):

    # Validate name
    if not name_inp or not all(char.isalpha() or char == " " for char in name_inp):
        raise ValueError("Contact name must be a non-empty alphabetic string.")

    # Validate phone number
    try:
        int(contact_inp)
        if len(contact_inp)!=10:
            raise InvalidPhoneNumberError('Phone number must contain exactly 10 digits')
    except ValueError:
        raise InvalidPhoneNumberError("Phone number must contain digits only.")

    # Store the contact
    contact_details[name_inp] = contact_inp

    return contact_details


def main():

    contact_details = {}

    name = input("Enter Your Name : ").title()
    contact = input("Enter Your Phone Number : ")

    try:
        register_details(contact_details, name, contact)
        print(contact_details)

    except ValueError as e:
        print(e)

    except InvalidPhoneNumberError as e:
        print(e)


main()

