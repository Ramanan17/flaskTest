from FDA_Project_Flask import main_functions
import requests
from flask_wtf import FlaskForm
from wtforms import StringField

class SearchByStateForm (FlaskForm):
    state_input = StringField('State')
    startdate_input = StringField('From')
    enddate_input = StringField("To")

def get_data(state, startdate, enddate):
    fda_url = "https://api.fda.gov/food/enforcement.json?search="
    search_url = fda_url + "distribution_pattern:\"" + state + "\"+AND+report_date:[" + startdate + "+TO+" + enddate + "]&limit=100"

    """Make the api request using requests and .get method"""
    response = requests.get(search_url)

    """ Save the response as a json file on the project"""
    #hint: use main_functions
    main_functions.save_to_file(response.json(),"recall.json")
    """Read the JSON file and save it to variable"""
    # hint: use main_functions
    
    recall_info = main_functions.read_from_file("recall.json")

    return recall_info
