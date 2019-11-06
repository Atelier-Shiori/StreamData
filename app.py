"""
    app.py
    This script runs the Rest API.
    ======

    Copyright 2019 Moy IT Solutions

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
import dbconfig
import mysql.connector
import json

from flask import Flask, request

app = Flask(__name__)


@app.route('/search/<region>', methods=['GET'])
def get_searchtitle(region):
    query = request.form['q']

def loadResultsByQuery(query, region) :
    mydb = openConnection()
    mycursor = mydb.cursor()
    sql = "SELECT "

def openConnection():
    mydb = mysql.connector.connect(
        host=dbconfig.db_host,
        user=dbconfig.db_user,
        password=dbconfig.db_user_password,
        database=dbconfig.db_name,
        auth_plugin='mysql_native_password'
    )
    return mydb