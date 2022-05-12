def county_list(counties):
    """Print list of counties in Indiana"""

    for county in counties:
        msg = county.title()
        print(msg)

county_names = ['grant', 'madison', 'marion', 'wayne',]
county_list(county_names)
