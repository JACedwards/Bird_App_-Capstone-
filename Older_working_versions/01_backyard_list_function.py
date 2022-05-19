    def list_backyard(self):
        self.count_backyard_list = 0
        self.list_backyard_list = [] 

        while True:
            print("Options: ")
            print("\t [1] Add bird to backyard list")
            print("\t [2] See complete current backyard list")
            print("\t [3] See total count for current backyard list")
            print("\t [4] Finished adding to backyard list for now")
 
            choice_of_backyard_list = input(f"Use number above to indicate what you'd like to do?  ")
            # could add functionality of checking each backyard entry against annual and lifetime list and adding to them if not in yet.
            if choice_of_backyard_list == '1':
                self.bird_backyard = input("Which bird would you like to add to your backyard list?  ")
                self.list_backyard_list.append(self.bird)
                self.count_backyard = self.count_backyard + 1
                continue
            elif choice_of_backyard_list == '2':    
                print("Here is your current backyard list: ")
                for b in self.list_backyard_list:
                    print(f"\t {b.title()}")
                continue
            elif choice_of_backyard_list == '3':
                print(f"You currently have {self.count_backyard_list} in your backyard list.")
            elif choice_of_backyard_list != '1' or '2' or '3' or '4':
                print("Try again, you have not yet entered a valid number.")
            elif choice_of_backyard_list == '4':
                print("Thank you for adding to your backyard list. You will now be returned to the main menu.")
                flag_list = False
                break