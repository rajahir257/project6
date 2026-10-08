import datetime
import os

print("welcome to the personal journal manager!")

now = datetime.datetime.now()

Entry = []

class File_Operator:
    def __init__(self):
        self.filename = "demo.txt"

    def add_entry(self):
        try:
            entry = input("Enter your journal here : ")
            f = open("demo.txt","w")
            f.write( entry + "\n")
            Entry.append(entry)

            print("entry added successfullly: ")

        except Exception as e:
            print("error while adding entry: ", e)

        finally:
            print("add entry operation sucessfully \n")

    def all_entries(self):
        try:
            print("\nHere are all the entries : ")

            file = open(self.filename,"r")
            lines = file.readlines()
            for i in lines:
                print(i, end ="")
            file.close()
            print(f"{now}")

        except Exception as e:
            print("the journal file does not exist please add new entry first.", e)

        finally:
            print("file reading operation sucessfully!")

    def search_entries(self):
        try:
            keyword = input("enter your keyword which you want to found: ")
            with open("demo.txt","r") as file:
                lines = file.readlines()

                for line in lines:
                    if keyword in line:
                        print("--------")
                        print(f"{now}")
                        print(line, "\n")
        except Exception as e:
            print("entry does not search", e)

        finally:
            print("searching file complete sucessfully")

    def del_entries(self):
        try:
            confirm = input("Are you sure you want to delete all entries (yes/no): ")

            if confirm.lower() == "yes":
                os.remove(self.filename)
                print("Your entries deleted successfully!")

            elif confirm.lower() == "no" :
                print("Your entries are safe.")

            else:
                print("Please enter the right choice!")

        except FileNotFoundError:
            print("File does not exist.")

        finally:
            print("Operation complete")

file_op = File_Operator()

while True:

    print("1. Add Entry.")
    print("2. View all Entries.")
    print("3. Search entry.")
    print("4. delete all entry.")
    print("5. exit the programme.")

    Choice = int(input("Enter your Choice here : "))

    match Choice:
        case 1:
            file_op.add_entry()

        case 2:
            file_op.all_entries()

        case 3:
            file_op.search_entries()

        case 4:
            file_op.del_entries()

        case 5:
            print("ending the program!")
            print(datetime.datetime.now())
            break

        case _:
            print("invalid choice! enter choice between 1 to 5!")