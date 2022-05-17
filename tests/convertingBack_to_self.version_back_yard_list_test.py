def list_backyard():
    self.count_backyard_list = 0
    self.list_backyard_list = [] 

#    flag_list = True
    #why won't flag_list turn light blue (be recognized as defined?)
    #above or at end of while loop?
    while True:
        print("\nList choices: ")
        print("\t [1] Add bird to backyard list")
        print("\t [2] See complete current backyard list")
        print("\t [3] See total count for current backyard list")
        print("\t [4] Finished adding to backyard list for now")
            # might want to add one-time "outing" dictionary
        # keys would include: name for outing (invite), location, date, list of birds
        choice_of_backyard_list = input(f"Use number above to indicate what you'd like to do?  ")

        if choice_of_backyard_list == '1':
            self.bird_backyard = input("\nWhich bird would you like to add to your backyard list?  ")
            print(f"{bird_backyard.title} has been added to your list!")
            self.list_backyard_list.append(self.bird_backyard)
            self.count_backyard_list = self.count_backyard_list + 1
            continue
        elif choice_of_backyard_list == '2':    
            print("\nHere is your current backyard list: ")
            for b in self.list_backyard_list:
                print(f"\n\t {b.title()}")
            continue
        elif choice_of_backyard_list == '3':
            print(f"\nThis is the number of birds you currently have in your backyard list: {self.count_backyard_list}.")
        
        elif choice_of_backyard_list == '4':
            print("\nThank you for adding to your backyard list. You will now be returned to the main menu.")
            break
        elif choice_of_backyard_list != '1' or '2' or '3' or '4':
            print("n\Try again, you have not yet entered a valid number.")
            continue

list_backyard()