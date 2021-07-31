from FDA_Project_Flask import app, forms
from flask import request, render_template

@app.route('/')
@app.route('/search',methods=["GET","POST"])
def search():
    search_form = forms.SearchByStateForm(request.form)

    if request.method == 'POST':
        """Assign to the following variables the input values by the user"""
        state = search_form.state_input.data
        startdate = search_form.startdate_input.data
        enddate = search_form.enddate_input.data

        """Pass the variables above as arguments to the get_data function 
        and assign the return value to fda_recall"""
        fda_recall = forms.get_data(state,startdate,enddate)
        return render_template('recall_results.html', form=search_form, statename=state, startdate=startdate,
                               enddate=enddate, recall=fda_recall)
                

    return render_template('recall_search.html', form=search_form)