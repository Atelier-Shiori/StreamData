# StreamData
Stream Data is a REST API that allows applications to retrieve a list of legal stream URLs for a given title. Database loading script and a Flask based REST API sever is written in Python and works with Python 3, not 2.x.

The app uses legal stream link data [Because.moe](https://because.moe). The difference is that the whole stream data does not need to be downloaded completely and only need to retreive what you need. You will be able to use the title or MyAnimeList ID to look up links for a given title.

# Why StreamData?
Providing stream links to your applications allows users to find where to watch a given show through legal streaming. Illegal/Pirated streams hurts the creators and animation studios that make an anime production possible. StreamData only provides legal sources where you can watch a given title (e.g. Crunchyroll, Funimation, Amazon, HiDive, etc) and not illegal sources.

This API enables you to obtain links where the user can watch a show legally through your app for a given title. StreamData only supports the following regions: United States, Canada, United Kingdom and Australia.

StreamData is a free service and you do not need to be an active Patron to use it. If you want to help us keep the service running, feel free to [become a Patron](https://www.patreon.com/join/malupdaterosx) for as little as $1 a month.

# How does StreamData works?
StreamData uses two different scripts. load.py is the script that is set to run as a cron job that refreshes the data in the database on a DBMS running MySQL/MariaDB. It performs some ETL (Extract, Transform, and Load). It downloads the stream data from the provider, load it to a staging table. The data is transformed and loaded to the data model. The ERD diagram for the database backend

![ERD](https://i.imgur.com/1wIYJnr.gif)

The frontend provides the rest API, allowing the user's apps to obtain stream data by title or MyAnimeList title id.

# Requirements
* Apache with wsgi (libapache2-mod-wsgi-py3) module installed and enabled. The (libapache2-mod-wsgi module will not work.
* Python 3.x or later, the latest version is recommended.
* Following packages installed: mysql-connector-python, flask, and urllib. You can install these using `pip`. 

# How to use the API
## API Endpoints
```
GET http://streamdata.malupdaterosx.moe/search/(region)?q=(search term)
```
#### Parameters

| Parameter | Value | Required |
|:---|:---|:---|
| region| `us` or `ca` or `uk` or `au` | `true` |
| q | Title (URL Encoded) | `true` |

#### Example
```
[GET] http://streamdata.malupdaterosx.moe/search/us?q=Kandagawa%20Jet%20Girls
```

##### Response
```
{
  "data": [
    {
      "mal_id": 40196, 
      "regionname": "us", 
      "sitename": "vrv-hidive", 
      "title": "Kandagawa Jet Girls", 
      "url": "https://vrv.co/series/GYW4N30E6"
    }, 
    {
      "mal_id": 40196, 
      "regionname": "us", 
      "sitename": "hidive", 
      "title": "Kandagawa Jet Girls", 
      "url": "https://www.hidive.com/stream/kandagawa-jet-girls/s01e001"
    }
  ], 
  "meta": {
    "count": 2, 
    "query": "Kandagawa Jet Girls", 
    "region": "us"
  }
}

```

```
GET http://streamdata.malupdaterosx.moe/lookup/(region)/(MAL ID)
```
#### Parameters

| Parameter | Value | Required |
|:---|:---|:---|
| region| `us` or `ca` or `uk` or `au` | `true` |
| MAL ID| MyAnimeList Title ID | `true` |

#### Example
```
[GET] http://streamdata.malupdaterosx.moe/lookup/us/40196
```

##### Response
```
{
  "data": [
    {
      "mal_id": 40196, 
      "regionname": "us", 
      "sitename": "vrv-hidive", 
      "title": "Kandagawa Jet Girls", 
      "url": "https://vrv.co/series/GYW4N30E6"
    }, 
    {
      "mal_id": 40196, 
      "regionname": "us", 
      "sitename": "hidive", 
      "title": "Kandagawa Jet Girls", 
      "url": "https://www.hidive.com/stream/kandagawa-jet-girls/s01e001"
    }
  ], 
  "meta": {
    "count": 2, 
    "query": "Kandagawa Jet Girls", 
    "region": "us"
  }
}

```
# How to setup the API server
## 1. Install the necessary Python packages
```
pip3 install mysql-connector-python flask
```

## 2. Load the database schema by importing db.sql

## 3. Database configuration
Copy appconfig_sample.py and rename it to appconfig.py. Edit the dbconfig.py and specify the database user, password, server and database the app will use.

## 4. Adding the load.py script to the crontab
A cron job needs to be created so it can run the load.py, which updates the stream data in the database. Add the following to the crontab. You can edit the crontab by typing `crontab -e` into the terminal. Note that you need to replace "/path/to/StreamData" with the proper absolute path to the load.py script
```
0 0 1 * * python3 /path/to/StreamData/load.py > load.log
```

## 5. Configure Apache
Make sure wsgi is enabled. You can do this by running the following commands.
```
sudo a2enmod wsgi 
```

If it's not installed, run the following command:
```
sudo apt-get install libapache2-mod-wsgi-py3
```

In `/etc/apache2/sites-available`, create a site configuration file called hato.conf with the following. (Change the server name to the domain name where you will host the service)
```
WSGIDaemonProcess flask_streamdata user=www-data group=www-data threads=2
<VirtualHost *:80>
                ServerName streamdata.your-domain-here.com
                WSGIScriptAlias / /path/to/StreamData/streamdata.wsgi
                <Directory /path/to/StreamData/>
                        Require all granted
                </Directory>
                Alias /static /path/to/StreamData/static
                <Directory /path/to/StreamData/static/>
                        Require all granted
                </Directory>
                ErrorLog ${APACHE_LOG_DIR}/error.log
                LogLevel warn
                CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

In the StreamData directory, copy streamdata_sample.wsgi to streamdata.wsgi. Replace the "/path/to" to the absolute path of StreamData.

To enable the site, run the following
```
sudo a2ensite streamdata.conf
```

Go to your web browser and navigate to `http://(domain name)`. The domain dame is where you host the Hato service. If you see the Hato introduction page, the service is running correctly.


## 6. Securing StreamData (optional)
It's recommended to use HTTPS to do any requests between your application and DreamData. You can use the Let's Encrypt service to retrieve a free SSL certificate. You can do this by following [these instructions](https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-16-04).

## 7. Updating StreamData
You can update StreamData easily by performing a `git pull` as long you cloned the repo using Git. 

In the directory containing the StreamData application, run the following in the terminal:
```
git pull
```
# License
StreamData is open source and licensed under Apache License 2.0
