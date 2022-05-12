def import_counties(incoming_counties, county_output):
    """Import list of counties"""

    while incoming_counties:
        current_county = incoming_counties.pop()

        print(f"Importing County: {current_county.title()}")
        county_output.append(current_county)

def show_county_output(county_output):
    """Show input county list"""

    print(f"\nThe following counties have been imported: ")
    for county in county_output:
        print("\t" + county.title())


incoming_counties = ['grant', 'marion', 'howard', 'wayne', 'madison',]
county_output = []
import_counties(incoming_counties, county_output)
show_county_output(county_output)
print(incoming_counties)
