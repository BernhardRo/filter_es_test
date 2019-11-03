# filter_es_test
just for testing around

Added algorithm #exp + average (correction)
Is exponential suppression with correction value, to prevent time lag
High suppression with p=0,2, r = 0,4, low suppression with  p=0.7, r=0.6

HOW TO use it:
install Python 3.x: https://www.python.org/downloads/
if not already available, install necessary dependencies: pim install numpy, pim install matplotlib
change the file secret.py to give the tool access to your nightscout data: update NS_URL and NS_SECRET (=API token) accordingly
to run it, simply run the run.bat file (only woks if Python is in your PATH)
