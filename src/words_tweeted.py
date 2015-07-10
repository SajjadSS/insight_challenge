__author__ = 'sajjadseyedsalehi'

import os
import sys
from collections import Counter

tweets = open('tweet_input/tweets.txt','r')
tw=tweets.read().splitlines()   # read and save each line of tweets as a separate
#  element in tw
tw_wd_all=' '.join(tw)  # joining all tweets, tw_wd_all contains all tweets as one string
tw_wd_all=tw_wd_all.split(" ")  # splitting all tweets' string to its words, " " indicates
#  that we want to split by space.
tw_ac=Counter(tw_wd_all) # number of times each word has been tweeted
tw_ac=sorted(tw_ac.items()) # sorting according to ASCII Code


if not os.path.exists('tweet_output'): # check if the directory "tweet_output" exists
    os.makedirs('tweet_output')  # create the directory if it does not exist

ft1=open("tweet_output/ft1.txt","w") # writing the results to the file ft1.txt
for i in range(0,len(tw_ac)):
    ft1.write(tw_ac[i][0] + '  ')  # word
    ft1.write('%s\n' % tw_ac[i][1]) # number of tweets
ft1.close()
