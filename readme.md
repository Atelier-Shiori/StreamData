# StreamData
Stream Data is a REST API that allows applications to retrieve a list of legal stream URLs for a given title. Database loading script and a Flask based REST API sever is written in Python.

The app uses legal stream link data [Because.moe](https://because.moe). The difference is that the whole stream data does not need to be downloaded completely and only need to retreive what you need. You will be able to use the title or MyAnimeList ID to look up links for a given title.

StreamData only supports Python 3.

# Why StreamData?
Providing stream links to your applications allows users to find where to watch a given show through legal streaming. Illegal/Pirated streams hurts the creators and animation studios that make an anime production possible. StreamData only provides legal sources where you can watch a given title (e.g. Crunchyroll, Funimation, Amazon, HiDive, etc) and not illegal sources.

This API enables you to obtain links where the user can watch a show legally through your app for a given title. StreamData only supports the following regions: United States, Canada, United Kingdom and Australia.

# How does StreamData works?
StreamData uses two different scripts. load.py is the script that is set to run as a cron job that refreshes the data in the database on a DBMS running MySQL/MariaDB. It performs some ETL (Extract, Transform, and Load). It downloads the stream data from the provider, load it to a staging table. The data is transformed and loaded to the data model. The ERD diagram for the database backend

![ERD](https://i.imgur.com/1wIYJnr.gif)

The frontend provides the rest API, allowing the user's apps to obtain stream data by title or MyAnimeList title id.

# How to use the API
TODO

# How to setup the API server
TODO

# License
StreamData is open source and licensed under Apache License 2.0
