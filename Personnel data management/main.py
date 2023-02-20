# This class is used to represent an instance of a person with the following attributes
class Person:
    # Initializing the instance of a person with the provided name, date_of_birth, age, marital_status and children
    def __init__(self, name, date_of_birth, age, marital_status, children=0):
        self.name = name
        self.date_of_birth = date_of_birth
        self.age = age
        self.marital_status = marital_status
        self.children = children
    
    # Returns a string representation of the Person object, which includes its 5 instance variables
    def __repr__(self):
        return f"Person(name={self.name}, date_of_birth={self.date_of_birth}, age={self.age}, marital_status={self.marital_status}, children={self.children})"
    
# A function to draw the table
def draw_table(data):
    # Prints the header for the table
    print("Table:\n")
    print("Name:\t\tDOB:\t\tAge: \tStatus:\t\tChildren:")

    # Loops through each person object in the data list
    for person in data:
        # Uses string formatting to display the person's details
        print(f"{person.name}\t{person.date_of_birth}\t{person.age}\t{person.marital_status}\t\t{person.children}")
    # Adds a blank line for formatting
    print("\n")

def sort_by_age(data):
    # # Sort the data list based on the age attribute of each person
    return sorted(data, key=lambda x: x.age)

def sort_by_last_name(data):
    # sort the data by last name
    return sorted(data, key=lambda x: x.name.split()[-1])

def show_people_with_children(data, children):
    # show people with specific number of children
    return [person for person in data if person.children == children]

def main():
    # create the dataset for the following people: 
    people = [
        Person("John Doe", "01-01-2000", 23, "Single", 0),
        Person("Jane Doe", "01-01-1998", 25, "Single", 0),
        Person("Jim Smith", "01-01-1973", 50, "Married", 5),
        Person("Emily Johnson", "01-01-1980", 43, "Married", 3),
        Person("Kaely Goodwill", "01-01-1970", 49, "Married", 5),
        Person("Robert Brown", "01-01-1997", 26, "Single"),
        Person("Sarah Davis", "01-01-2001", 22, "Single", 0),
        Person("William Wilson", "01-01-1968", 54, "Married", 3),
        Person("Michael Jackson", "01-01-1974", 49, "Married", 2),
        Person("Emily Davis", "01-01-1996", 27, "Single"),
        Person("James Johnson", "01-01-2000", 23, "Single", 0)
    ]

    while True:
        # display options to the user
        print("Select an option:")
        print("1. Show original table")
        print("2. Sort by age")
        print("3. Sort by last name")
        print("4. Show people with specific number of children")
        print("5. Exit")

        # get user input
        try:
            option = int(input("Enter option: "))
        except ValueError:
            print("Invalid input, please enter a number.")
            continue

        # clear the screen
        print("\033c", end="")

        # perform the selected action
        if option == 1:
            draw_table(people)
        elif option == 2:
            draw_table(sort_by_age(people))
        elif option == 3:
            draw_table(sort_by_last_name(people))
        elif option == 4:

            # Try to get the number of children from the user and display the table of people with that number of children
            try:
                # Get the number of children from the user
                children = int(input("Enter number of children: "))

                # Draw the table of people with the specified number of children
                draw_table(show_people_with_children(people, children))  

            # If the user inputs an invalid value, catch the ValueError and display an error message
            except ValueError:
                print("Invalid input, please enter a number.")

        # Check if the user selected option 5 to break from the loop
        elif option == 5:
            break

        # If the user inputs an invalid option, display an error message
        else:
            print("Invalid option, please select a number between 1 and 5.")

main()