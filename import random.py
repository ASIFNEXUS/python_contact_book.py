import random

def generate_unique_id():
  """Generates a unique identifier for a contact."""
  return random.randint(1, 100000)

def add_contact(contact_list, name, phone_number, email):
  """Adds a new contact to the contact list."""
  contact = {
    "id": generate_unique_id(),
    "name": name,
    "phone_number": phone_number,
    "email": email
  }
  contact_list.append(contact)

def view_contact_list(contact_list):
  """Displays the contact list."""
  for contact in contact_list:
    print(contact)

def search_contacts(contact_list, search_query):
  """Searches for contacts by name or number."""
  matching_contacts = []
  for contact in contact_list:
    if search_query.lower() in contact["name"].lower() or search_query.lower() in contact["phone_number"].lower():
      matching_contacts.append(contact)
  return matching_contacts

def delete_contact(contact_list, contact_id):
  """Deletes a contact by its unique identifier."""
  for index, contact in enumerate(contact_list):
    if contact["id"] == contact_id:
      del contact_list[index]
      break

def edit_contact(contact_list, contact_id, name, phone_number, email):
  """Edits a contact by its unique identifier."""
  for index, contact in enumerate(contact_list):
    if contact["id"] == contact_id:
      contact["name"] = name
      contact["phone_number"] = phone_number
      contact["email"] = email
      break

def main():
  """The main function of the Contact Book application."""
  contact_list = []
  while True:
    print("1. Add a contact")
    print("2. View contact list")
    print("3. Search contacts")
    print("4. Delete a contact")
    print("5. Edit a contact")
    print("6. Exit")
    option = input("Enter your choice: ")
    if option == "1":
      name = input("Enter the contact name: ")
      phone_number = input("Enter the contact phone number: ")
      email = input("Enter the contact email address: ")
      add_contact(contact_list, name, phone_number, email)
    elif option == "2":
      view_contact_list(contact_list)
    elif option == "3":
      search_query = input("Enter the search query: ")
      matching_contacts = search_contacts(contact_list, search_query)
      for contact in matching_contacts:
        print(contact)
    elif option == "4":
      contact_id = input("Enter the contact ID to delete: ")
      delete_contact(contact_list, contact_id)
    elif option == "5":
      contact_id = input("Enter the contact ID to edit: ")
      name = input("Enter the new contact name: ")
      phone_number = input("Enter the new contact phone number: ")
      email = input("Enter the new contact email address: ")
      edit_contact(contact_list, contact_id, name, phone_number, email)
    elif option == "6":
      break

if __name__ == "__main__":
  main()
