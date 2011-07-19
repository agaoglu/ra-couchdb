Result Announcer
================

A simple web application to be used as a tool to announce the results of an exam. Whole scenario is summarized in [this](http://agaoglu.tumblr.com/post/3764038619/examining-the-examination-results-warm-up) post. This project runs on [couchdb](http://couchdb.apache.org/) alone in a sense it is a [couchapp](http://couchapp.org/page/index). Blogged development experiences [here](http://agaoglu.tumblr.com/post/3896370525/announcing-results-with-of-couchdb).

Running
-------

You will need a running couchdb first. Although it is possible to use some other tool, default way of pushing the application to db is to use [couchapp command-line python tool](http://couchapp.org/page/couchapp-python). If your couchdb is located on localhost:5984 and you defined an admin with username:admin, password:admin all you have to do is

    couchapp push

This will define a database named `ra`, and install the application in design doc `app`. Navigate to `http://localhost:5984/ra/_design/app/_show/result/` to get to the login screen. If your couchdb installation is elsewhere you should define it as

    couchapp push http://<adminuser>:<adminpass>@<host>:<port>/<dbname>

Loading Data
------------

Getting to the login screen hardly means anything w/o data. In order to load some sample results into the db, you can supply your dbname to the script `load.py` as

    python load.py ra

After that you can use any number divisable by 3 between 1M and 10M as login and pass.

Demo
----

The app has been deployed [here](http://racouch.erdemagaoglu.com/). But it is not full with 3M records, there are only 90000. You should try any of the following username:password pairs

    1000002:1000002
    1000005:1000005
    ...
    1269999:1269999
