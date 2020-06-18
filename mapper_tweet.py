#!/usr/bin/env python3
import sys, json;
import fileinput
def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True
word_list = ["han", "hon", "den", "det", "denna", "denne","hen"]
count = 0
for line in fileinput.input():
    if not line.strip():
        continue
    tweets = line.split("^M")
    for tweet in tweets:
        #json_data = json.loads(tweet)
        isValid = validateJSON(tweet)
        #json_data = json.loads(tweet)
        if (isValid == True):
            json_data = json.loads(tweet)
	    #print (json_data["retweeted"])
            if (json_data["retweeted"] == False):
                count = count + 1
                #print (json_data["text"])
                tweet_words = json_data["text"].split()
                for search_word in word_list:
                    for tweet_word in tweet_words:
                        if (search_word == tweet_word.lower()):
                            print (("number of tweets mentioning pronoun %s\t%s") % (search_word,1))
                            break


