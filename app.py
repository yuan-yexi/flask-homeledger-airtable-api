from dis import dis
import os
import json

from flask import Flask, request, jsonify
from pyairtable import Table

api_key = os.environ["AIRTABLE_API_KEY"]

app = Flask(__name__)

base_id = "app509gADynVIIgpa"

district_14 = "tblAFuETAyGakpAtR"
district_15 = "tblMTEg8eUNngnBSS"
district_16 = "tblAGBm5Uukc1J4GR"
district_bedok = "tblgN0Rs9zWp2AApr"
district_yishun = "tbluw6Y017VvxCouK"

@app.route('/get-district-price', methods=['GET'])
def getAirTablePriceList():
    # List to store price list
    priceList = []
    
    table_id = request.args.get('table_id')
    
    response = Table(api_key, base_id, table_id)
    airTableData = response.all()
    
    for i in airTableData:
        tableRow = i['fields']
        tableRow = i['fields']
        tableRow['id'] = i['id']
        tableRow['createdTime'] = i['createdTime']
        priceList.append(tableRow)
    
    return jsonify(priceList) 
    
if __name__ == "__main__":
	app.run()
