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
import appconfig
import mysql.connector

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/search/<region>', methods=['GET'])
def get_searchtitle(region):
    query = request.args['q']
    return loadResultsByQuery(query, region)

@app.route('/lookup/<region>/<int:malid>', methods=['GET'])
def get_mallookup(region, malid):
    return loadResultsByMALID(malid, region)

def loadResultsByQuery(query, region) :
    mydb = openConnection()
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT t.title, s.sitename, r.regionname, l.url, t.mal_id from region AS r, links AS l, sites AS s, titles AS t WHERE l.titleid = t.titleid AND l.siteid = s.id AND l.regionid = r.id AND r.regionname = %s AND t.title LIKE %s"
    val = [region, query]
    mycursor.execute(sql,val)
    results = mycursor.fetchall()
    fresults = type(dict);
    if len(results) > 0 :
        fresults = {"data" : results, "meta":{"query": query, "region":region, "count": len(results)}}
        return jsonify(fresults), 200
    else :
        fresults = {"data": None, "error" : "Not Found", "meta":{"query": query, "region":region}}
        return jsonify(fresults), 400

def loadResultsByMALID(malid, region) :
    mydb = openConnection()
    mycursor = mydb.cursor(dictionary=True)
    sql = "SELECT t.title, s.sitename, r.regionname, l.url, t.mal_id from region AS r, links AS l, sites AS s, titles AS t WHERE l.titleid = t.titleid AND l.siteid = s.id AND l.regionid = r.id AND r.regionname = %s AND t.mal_id = %s"
    val = [region, malid]
    mycursor.execute(sql,val)
    results = mycursor.fetchall()
    fresults = type(dict);
    if len(results) > 0 :
        fresults = {"data" : results, "count": len(results)}
        return jsonify(fresults), 200
    else :
        fresults = {"data": None, "error" : "Not Found"}
        return jsonify(fresults), 400

def openConnection():
    mydb = mysql.connector.connect(
        host=appconfig.db_host,
        user=appconfig.db_user,
        password=appconfig.db_user_password,
        database=appconfig.db_name,
        auth_plugin='mysql_native_password'
    )
    return mydb

if __name__ == '__main__':
    app.run(debug=True)
