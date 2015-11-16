Times Tweets
===================

A website that lets you search for whatever you want, and shows you what the New York Times and Twitter had to say about it.

Created By:
----------
Caitlin Stanton --> Tweepy (Twitter scraping) API, UX  <br>
Alex Sosnovsky  --> New York Times API, Middleware <br>
Liam Daly       --> New York Times API, Middleware <br>

----------


How It Works
-------------
The user inputs a search term, which is what they would like to know about.
The website uses the New York Times and Twitter APIs to bring the user the results.

----------


Requirements
--------------
You must have the tweepy library installed (which can be done using 'pip install tweepy'). The csv, urllib2, json, sys, and datetime libraries are also necessary, but they should already be installed on your computer.

-----------


How to Run
--------------
Run 'python app.py' in your terminal. Go to localhost:8000 (or 0.0.0.0:8000) in whatever web browser you use, and enjoy Times Tweets!
