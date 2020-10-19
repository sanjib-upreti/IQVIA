import feedparser
from datetime import datetime
from time import mktime
from disease_list import disease_list_all, disease_list_small
# disease list created for testing

# initializing the value of days by 2(for testing Module)
days=2
def disease_monitor(days):

    try:
        if 0 < days <= 30: # putting condition for input must between 1- 30
            for disease in disease_list_small: # iterting through the disease list, one by one
                # STRING URL OF RSS FEED...using string formatting
                feed_string = f'https://clinicaltrials.gov/ct2/results/rss.xml?rcv_d={days}&lup_d=&sel_rss=new14&cond={disease}'
                Feed = feedparser.parse(feed_string) # using parse funtion
                entries = Feed.entries # collecting the feed entries in dictionary format
                # PRINTING RESULTS
                if len(entries) == 0: # if dictionary item is absent
                    print(f'{len(entries)} cases of {disease}: in last {days} days')
        else:
            print('Please provide input in range 1-30 only')
    except:
        pass
# for calling the function
if __name__ == "__main__":
    try:
        days = int(input('Disease cases in last (enter days)\n'))
        # getting number of days from user
        disease_monitor(days) # calling the fucntion with days in parameter
    except ValueError:
        # passing the valueError if type is not integer 
        print("Please enter number between (1-30)")
