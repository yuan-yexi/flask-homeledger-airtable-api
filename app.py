import os
import json

from flask import Flask ,jsonify
from pyairtable import Table

api_key = os.environ["AIRTABLE_API_KEY"]

app = Flask(__name__)

base_id = "app509gADynVIIgpa"

district_14 = Table(api_key, base_id, "tblAFuETAyGakpAtR")
district_15 = Table(api_key, base_id, "tblMTEg8eUNngnBSS")
district_16 = Table(api_key, base_id, "tblAGBm5Uukc1J4GR")
district_bedok = Table(api_key, base_id, "tblgN0Rs9zWp2AApr")
district_yishun = Table(api_key, base_id, "tbluw6Y017VvxCouK")

@app.route('/district-14')
def get_district_14():
	return jsonify(district_14.all())

@app.route('/district-15')
def get_district_15():
	return jsonify(district_15.all())

@app.route('/district-16')
def get_district_16():
	return jsonify(district_16.all())

@app.route('/district-bedok')
def get_district_bedok():
	return jsonify(district_bedok.all())

@app.route('/district-yishun')
def get_district_yishun():
	return jsonify(district_yishun.all())

if __name__ == "__main__":
	app.run()
 