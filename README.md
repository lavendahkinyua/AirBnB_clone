AirBnB Clone
This project is a clone of the popular vacation rental platform Airbnb. It aims to replicate some of the core functionalities of the Airbnb platform through a command-line interface (CLI)

Command Interpreter
The command interpreter is a text-based interface that allows users to interact with the AirBnB clone. It provides a set of commands to perform various operations, such as creating and managing user accounts, searching and booking properties, messaging other users, and administrative tasks.

How to Start the Command Interpreter
To start the command interpreter, follow these steps:
Clone the repository from GitHub: AirBnB Clone
Navigate to the project directory.
Run the command ./console.py to start the command interpreter.

How to Use the Command Interpreter
Once the command interpreter is running, you can enter commands to interact with the AirBnB clone. Here are some examples of available commands:

help: Display a list of available commands and their descriptions.
create <class_name>: Create a new instance of a specific class, such as User or Property.
search <location>: Search for available properties in the specified location.
book <property_id> <start_date> <end_date>: Book a property for a specific period.
message <user_id> <message_content>: Send a message to another user.
admin <command>: Perform administrative tasks, such as managing user accounts or property listings.

Examples
Here are a few examples to demonstrate the usage of the command interpreter:

Creating a User:
(AirBnB_clone) create User
Enter user details:
Name: Lavendah kinyua
Email: lavendah17@gmail.com
Password: ********
User created with ID: 1

Searching for Properties:
(AirBnB_clone) search New York
Properties found in New York:
- Property 1: Apartment in Manhattan
- Property 2: Cozy Studio near Central Park

Booking a Property:
(AirBnB_clone) book 1 2023-07-01 2023-07-07
Property booked successfully. Booking ID: 1

Sending a Message:
(AirBnB_clone) message 2 "Hello, I'm interested in your property."
Message sent to User with ID: 2

Authors:
Lavendah Kinyua
