# Pasted this into main.py

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