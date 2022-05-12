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


class Users:
    def __init__(self, first_name, last_name, user_name, password, password_confirm, email,  state, county, profile_pic, user_profile, users_database):
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
    def __init__(self, life_time, annual, backyard, bird, year, count_lifetime, count_annual, count_backyard , list_lifetime, list_annual, list_backyard, ):
        self.life_time = life_time
        self.annual = annual
        self.backyard = backyard
        self.bird = bird
        self.year = year
        self.count_lifetime = count_lifetime 
        self.count_annual = count_annual
        self.count_backyard = count_backyard
        self.list_lifetime = list_lifetime
        self.list_annual = list_annual
        self.list_backyard = list_backyard

    def list_choice(self):
        self.count_lifetime = 0
        self.count_annual = 0
        self.count_backyard = 0
        self.list_lifetime = [] 
        self.list_annual = [] 
        self.list_backyard = [] 

        flag_list = True
       
        while True:
            print("List choices: ")
            print("\t [1] My backyard list")
            print("\t [2] Annual list")
            print("\t [3] Lifetime list")
            print("\t [4] Finished adding birds for now")
             # might want to add one-time "outing" dictionary
            # keys would include: name for outing (invite), location, date, list of birds
            choice_of_list = input(f"Which of these would you like to do [use number]?  ")

            if choice_of_list == 1:
                self.bird = input("Which bird would you like to add to your backyard list?  ")
                self.list_backyard.append(self.bird)
                self.count_backyard = self.count_backyard + 1
                show_backyard_list = input("Would you like to see your current backyard list [y/n]? ")
                if show_backyard_list == "y" or "Y" or "yes" or "Yes":
                    print("Here is your current backyard list: ")
                    for b in self.list_backyard:
                        print(f"\t {b.title()}")
                elif show_backyard_list == "n" or "N" or "yes" or "No":
                    continue  

            # <> Start here:  
            # stest list_choice function
            # complete while true loop.
            #  should be able to do a lot of copy and past from back yard if section to annual and lifetime list sections









# Ready to test sign -up module:
    # should accept input
    # print self_user profile










def citing(state, county, bird, date):
    """Report citing by state, county, date"""
    state_county = f"{county.title()} County, {state.title()}"
    report = f"The following bird was seen on {date}, in {state_county}: {bird.title()}."
    
    return(report)

while True:
    print("\nPlease enter the following data:")
    print('(enter "q" at any time to quit)')

    state_a = input("What state did you see the in bird? ")
    if state_a == 'q':
        break

    county_a = input("What county did you see the bird in? ")
    if county_a == 'q':
        break

    bird_a = input("What kind of bird did you see? ")
    if bird_a == 'q':
        break

    date_a = input("On which date did you see the bird? ")
    if county_a == 'q':
        break

    citing1 = citing(state_a, county_a, bird_a, date_a)
    print(citing1)