import pandas as pd
from flask import *
import os
import sys
sys.path.append('./src')
from werkzeug.utils import secure_filename
from validate_date_format import date_month_year_format

UPLOAD_FOLDER = os.path.join('staticFiles', 'uploads')

# Define allowed files
ALLOWED_EXTENSIONS = {'csv'}
app = Flask(__name__)
# Configure upload file path flask
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'jai1234'

def validate_date():
    data_file_path = session.get('uploaded_data_file_path', None)
	# read csv
    df = pd.read_csv(data_file_path,encoding='unicode_escape',sep=",", header=None, skiprows=[0] , on_bad_lines='skip',
                 names=["Order Number","Customer Tel","Created At","Product SKU","Price","Quantity","Total"])
    df.index = list(range(1, len(df) + 1))
    total_valid = 0
    total_invalid = 0
    list_invalid_dateformat = []
    list_valid_dateformat = []
    for index , row in df.iterrows():
        if date_month_year_format(row["Created At"]):
            list_valid_dateformat.append(index)
            total_valid += 1
        else :
            list_invalid_dateformat.append(index)
            total_invalid += 1
    return total_valid , total_invalid , list_invalid_dateformat

@app.route('/', methods=['GET', 'POST'])
def uploadFile():
	if request.method == 'POST':
	# upload file flask
		f = request.files.get('file')

		# Extracting uploaded file name
		data_filename = secure_filename(f.filename)

		f.save(os.path.join(app.config['UPLOAD_FOLDER'],data_filename))

		session['uploaded_data_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'],data_filename)

		return render_template('uploaded.html')
	return render_template("home.html")


@app.route('/show_data')
def showData():
    total_valid , total_invalid , list_invalid_dateformat = validate_date()
	# Uploaded File Path
    data_file_path = session.get('uploaded_data_file_path', None)
	# read csv
    uploaded_df = pd.read_csv(data_file_path,encoding='unicode_escape', sep=",", header=None, skiprows=[0] , on_bad_lines='skip',
                 names=["Order Number","Customer Tel","Created At","Product SKU","Price","Quantity","Total"])
	# Converting to html Table
    uploaded_df.index = list(range(1, len(uploaded_df) + 1))
    uploaded_df_html = uploaded_df.to_html()
    return render_template('show_csv_data.html',data_var=uploaded_df_html,total_valid_dateformat=total_valid
                           ,total_invalid_dateformat=total_invalid,list_invalid_dateformat=list_invalid_dateformat)

    
if __name__ == '__main__':
	app.run(debug=True)