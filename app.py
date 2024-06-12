import pandas as pd
from flask import *
import os
import sys
sys.path.append('./src')
from werkzeug.utils import secure_filename
from validate_date_format import date_month_year_format
from io import BufferedReader

app = Flask(__name__)
app.secret_key = 'jai1234'

def validate_date(df):
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

@app.route('/')
def landing():
    return render_template("home.html")

@app.route('/validates', methods=['POST'])
def validates():
    f = request.files["file"]
    buff = BufferedReader(f)
    df = pd.read_csv(
                buff,
                encoding='unicode_escape',
                sep=",", 
                header=None,
                skiprows=[0],
                on_bad_lines='skip',
                names=["Order Number","Customer Tel","Created At","Product SKU","Price","Quantity","Total"]
            )
    df.index = list(range(1, len(df) + 1))
    df_html = df.to_html(classes='table table-stripped')
    total_valid , total_invalid , list_invalid_dateformat = validate_date(df)
    return render_template("validates.html",
                           df_html = df_html,
                           total_valid_dateformat=total_valid,
                           total_invalid_dateformat=total_invalid,
                           list_invalid_dateformat=list_invalid_dateformat)

if __name__ == '__main__':
	app.run(debug=True)
