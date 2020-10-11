# simple PhoneBook CRUD

## The main features of the program are as follows:

### Phone Books:
Each user can have a number of phonebooks. Each phonebook contains a history and a number of contacts.

### Contacts: 
 Each contact includes first name, last name and nickname, of which at least one of these must be entered.
Each contact can also contain 0 or more phone numbers, which are displayed by default with mobile or work tags.

### Tag:
 The owner of the Phone Book can create a new tag for each number of contacts in his phonebook and 
display his phone number with this new tag. It can also select one of the Phone,
Home and Work tags as a tag for each of its phone numbers.

### Filter:
 The user has the ability to see the contacts of each of his phonebook and should be able to filter  them:
1-Combine first name, last name and nickname
2-phone number


### Sort:
 The user can view their phonebook and sort it by alphabetical name, A_Z or Z_A based on the name, surname and nickname set.


## To Run the project
after cloning the project to your local machine, install the requirements and start the server.

```sh
$ cd simpleDjangoPhonebook
$ pip install requirements
$ python manage.py makemigrations
$ python manage.py runserver
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```

and for checking APIs documents :

```sh
127.0.0.1:8000/swagger
```