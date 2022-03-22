import os
import json

from flask import Flask ,jsonify
from pyairtable import Table

api_key = os.environ["AIRTABLE_API_KEY"]

app = Flask(__name__)

district_14 = Table(api_key, "app509gADynVIIgpa", "tblAFuETAyGakpAtR")

@app.route('/district-14')
def get_district_14():
	return jsonify(district_14.all())

if __name__ == "__main__":
	app.run()
