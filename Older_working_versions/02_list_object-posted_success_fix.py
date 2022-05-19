# Have basic reporting bird citing function "citing"
    # add bird photo upload option
    # ability to keep track of tally of (1) which (alphabetized) and (2_ how many total birds seen on 1 outing
    # ditto for entire year
    # ditto for their own property?  
        # On bird entry page, create check boxes, so they can choose multiple boxes just entring the same bird once?
    # special category for unusual birds
    # special category for birds they've never seen before
    # whether bird is male/female?
# Need sign up module for Bird on the Brain group:
    # First name
    # Last name
    # Username
    # Password
    # Optional photo
    # Optional address/city
# Need sign in function
# Need search module
    # For bird brain group data
    # and for Cornell site data (ebirds)

# Classes:
    # Users
    # Citings
    # Bird object (one for each bird on Cornell site for Indiana for past x days?)
    # ebird/Cornell data
    # bird on brain data 
    # Lists:
    #   Life time
    #   Annual
    #   My Back yard


from asyncio.constants import SENDFILE_FALLBACK_READBUFFER_SIZE
from turtle import back


class Users():
    def __init__(self, first_name = '', last_name = '', user_name = '', password = '', password_confirm = '', email = '',  state = '', county = '', profile_pic = '', user_profile = '', users_database = ''):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
        self.email = email
        self.state = state
        self.county = county
        self.profile_pic = profile_pic        
        self.user_profile = user_profile
        self.password_confirm = password_confirm
        self.users_database = users_database

    def signup(self):
        self.user_profile = {}
        
        self.first_name = input("What is your first name? ")
        self.last_name = input("What is you last name? ")
        self.user_name = input("What username would you like to have? ")
        self.password = input("Please choose a password? ")
        self.password_confirm = input("Please confirm your password_: ")
        self.email = input("Email address:  ")
        self.state = input("What state do you live in?  ")
        self.county = input("What county do you live in? ")
        self.profile_pic = input("Optional: Upload a profile picture for yourself here:  ")

        self.profile_pic = Users({self.user_name : {
            "First name: " : self.first_name, 
            "Last name: " : self.last_name, 
            "Username: " : self.user_name, 
            "Password: " : self.password,
            "Confirm password " : self.password_confirm,
            "Email: " : self.email,
            "State: " : self.state,
            "County: " : self.county,
            "Profile picture" : self.profile_pic
            }})

        print(self.user_profile)


class Lists(Users):
    def __init__(self, life_time ='', annual='', backyard='', bird='', year='', count_lifetime='', count_annual='', count_backyard ='', count_backyard_list=''):
        self.life_time = life_time
        self.annual = annual
        self.backyard = backyard
        self.bird = bird
        self.year = year
        self.count_lifetime = count_lifetime 
        self.count_annual = count_annual
        self.count_backyard = count_backyard
        self.count_backyard_list = count_backyard_list




#????? can you help me test this one????#
    def list_backyard(self):
        self.count_backyard_list = 0
        self.list_backyard_list = [] 

        while True:
            print("\nList choices: ")
            print("\t [1] Add bird to backyard list")
            print("\t [2] See complete current backyard list")
            print("\t [3] See total count for current backyard list")
            print("\t [4] Finished adding to backyard list for now")
                # might want to add functionality of this function auto-checking if backyard bird entry is already in annual or lifetime list, and adding if not.
            choice_of_backyard_list = input(f"Use number above to indicate what you'd like to do?  ")
##--<>start here
##-****line 116 is returning an object rather than the name of the bird****
##--*****might be easier to look for a fix inside the test version since it is more contained.
##--****easy work around would be to change that print statement in 114 to something generic, that doesn't include name of bird


            if choice_of_backyard_list == '1':
                bird_backyard = input("\nWhich bird would you like to add to your backyard list?  ").title()
                print(f"{bird_backyard.title()} has been added to your list!")
                self.list_backyard_list.append(bird_backyard)
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



#????? How can I reset annual list automatically on December 31 and archive each year's list?

#???? When you are checking against the existence of a bird in an existing list, how do you handle mispellings?

#??? Similarly, is there a way to present to the user a list of similarly spelled words that they can check/choose from that do exist?

    def list_annual(self):
        self.count_annual_list = 0
        self.list_annual_list = [] 

        while True:
            print("\nList choices: ")
            print("\t [1] Add bird to annual list")
            print("\t [2] See complete current annual list")
            print("\t [3] See total count for current annual list")
            print("\t [4] Finished adding to annual list for now")
                # might want to add functionality of this function auto-checking if backyard bird entry is already in annual or lifetime list, and adding if not.
            choice_of_annual_list = input(f"Use number above to indicate what you'd like to do?  ")

            if choice_of_annual_list == '1':
                bird_annual = input("\nWhich bird would you like to add to your annual list?  ")
                print(f"{bird_annual.title()} has been added to your list!")
                self.list_annual_list.append(bird_annual)
                self.count_annual_list = self.count_annual_list + 1
                continue
            elif choice_of_annual_list == '2':    
                print("\nHere is your current annual list: ")
                for b in self.list_annual_list:
                    print(f"\n\t {b.title()}")
                continue
            elif choice_of_annual_list == '3':
                print(f"\nThis is the number of birds you currently have in your annual list: {self.count_annual_list}.")
            
            elif choice_of_annual_list == '4':
                print("\nThank you for adding to your annual list. You will now be returned to the main menu.")
                break
            elif choice_of_annual_list != '1' or '2' or '3' or '4':
                print("n\Try again, you have not yet entered a valid number.")
                continue

    def list_lifetime(self):
        self.count_lifetime_list = 0
        self.list_lifetime_list = [] 

        while True:
            print("\nList choices: ")
            print("\t [1] Add bird to lifetime list")
            print("\t [2] See complete current lifetime list")
            print("\t [3] See total count for current lifetime list")
            print("\t [4] Finished adding to lifetime list for now")
                # might want to add functionality of this function auto-checking if backyard bird entry is already in annual or lifetime list, and adding if not.
            choice_of_lifetime_list = input(f"Use number above to indicate what you'd like to do?  ")

            if choice_of_lifetime_list == '1':
                bird_lifetime = input("\nWhich bird would you like to add to your lifetime list?  ")
                print(f"{bird_lifetime.title} has been added to your list!")
                self.list_lifetime_list.append(bird_lifetime)
                self.count_lifetime_list = self.count_lifetime_list + 1
                continue
            elif choice_of_lifetime_list == '2':    
                print("\nHere is your current lifetime list: ")
                for b in self.list_lifetime_list:
                    print(f"\n\t {b.title()}")
                continue
            elif choice_of_lifetime_list == '3':
                print(f"\nThis is the number of birds you currently have in your annual list: {self.count_lifetime_list}.")
            
            elif choice_of_lifetime_list == '4':
                print("\nThank you for adding to your lifetimerd list. You will now be returned to the main menu.")
                break
            elif choice_of_lifetime_list != '1' or '2' or '3' or '4':
                print("n\Try again, you have not yet entered a valid number.")
                continue

    def list_choice(self):
        self.count_lifetime = 0
        self.count_annual = 0
        self.count_backyard = 0
    
        while True:
            print("List choices: ")
            print("\t [1] My backyard list")
            print("\t [2] Annual list")
            print("\t [3] Lifetime list")
            print("\t [4] Finished adding birds for now")
             # might want to add one-time "outing" dictionary
            # keys would include: name for outing (invite), location, date, list of birds
            choice_of_list = input(f"Which of these lists would you like to do [use number]?  ")

            if choice_of_list == '1':
                self.list_backyard()
            elif choice_of_list == '2':
                self.list_annual()
            elif choice_of_list == '3':
                self.list_lifetime()
            elif choice_of_list == '4':
                break
    


class Run():
    """Runs program"""

    def __init__(self, user):
        self.user = user
    
#??? do I have to define variables after init statement above?

#???Why does below "def" indicate an indention problem?
    
    def run_program(self, the_list_class):

        while True:
            print(f"\nWhat would you like to do ?")
            print("[1]: Sign up")
            # Should probably split lists into 
            #separate lists at some point
            print("[2]: Add to backyard, annual, or lifetime list")
            # print("[3]: Add to annual list")
            # print("[4]: Add to lifetime list")
            choice = input("Choose a number to indicate what you'd like to do:  ")
            if choice == '1':
                signup_para.signup()
            elif choice == '2':
                the_list_class.list_choice() 
            
            elif choice != '1' or choice != '2' or choice != '3' or choice != '4' or choice != '5' or choice != '6':
                print("\nYou have not entered a valid number. \nPlease try again.")
                continue
            else:
                continue
user_1 = Users()  

run = Run(user_1)

myList = Lists(user_1)

run.run_program(myList)


# Can I ingegrate below into one of the classes above?

# def citing(state, county, bird, date):
#     """Report citing by state, county, date"""
#     state_county = f"{county.title()} County, {state.title()}"
#     report = f"The following bird was seen on {date}, in {state_county}: {bird.title()}."
    
#     return(report)

# while True:
#     print("\nPlease enter the following data:")
#     print('(enter "q" at any time to quit)')

#     state_a = input("What state did you see the in bird? ")
#     if state_a == 'q':
#         break

#     county_a = input("What county did you see the bird in? ")
#     if county_a == 'q':
#         break

#     bird_a = input("What kind of bird did you see? ")
#     if bird_a == 'q':
#         break

#     date_a = input("On which date did you see the bird? ")
#     if county_a == 'q':
#         break

#     citing1 = citing(state_a, county_a, bird_a, date_a)
#     print(citing1)


