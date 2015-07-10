__author__ = 'sajjadseyedsalehi'

import os
import sys

tweets = open('tweet_input/tweets.txt','r')
tw = tweets.readlines()  # read and save each line of tweets as a separate
#  element in tw

tw_uq = [None] * len(tw) # for storing number of unique words in each tweet
tw_md = [None] * len(tw) # for storing median of each set of tweets
tw_L = [None] * int(float(len(tw))//2 + 1) # lower half of tw_uq, tw_L will
#  contain half +/- 1 elements of tw_uq in a way that all elements be smaller than
# or equal to the elements of tw_H
tw_H = [None] * int(float(len(tw))//2 + 1) # upper half -/+ 1 of tw_uq,
tw_uq[0] = len(set(tw[0].split())) # number of unique words in the first tweet
tw_uq[1] = len(set(tw[1].split())) # number of unique words in the second tweet
tw_md[0] = tw_uq[0] # median of the first tweet
tw_md[1] =(tw_uq[0] + tw_uq[1])/2.0 # median of the first two tweets
if tw_uq[0] <= tw_uq[1]: # distributing the first two tweets between tw_L and tw_H
    tw_L[0] = tw_uq[0]
    tw_H[0] = tw_uq[1]
else:
    tw_L[0] = tw_uq[1]
    tw_H[0] = tw_uq[0]

i_L = 1  # index for tw_L
i_H = 1  # index for tw_H
tw_L_max = tw_L[0]  # maximum value in tw_L
tw_H_min = tw_H[0]  # minimum value in tw_H
for i in range(2, len(tw)):
    tw_uq[i] = len(set(tw[i].split())) # number of unique words in the i th tweet
    if tw_uq[i] <= tw_L_max:
        tw_L[i_L] = tw_uq[i]
        i_L += 1
    else:
        tw_H[i_H] = tw_uq[i]
        i_H += 1
        tw_H_min = min(tw_H_min,tw_uq[i])

    if i_H - i_L > 1:
        tw_L[i_L] = tw_H_min
        tw_L_max= tw_H_min
        i_L += 1
        i_H -= 1
    elif i_L - i_H > 1:
        tw_H[i_H] = tw_L_max
        tw_H_min = tw_L_max
        i_H += 1
        i_L -= 1

    if i_L == i_H:
        tw_md[i] = (tw_L_max+tw_H_min)/2.0
    elif i_L > i_H:
        tw_md[i] = tw_L_max
    else:
        tw_md[i] = tw_H_min

if not os.path.exists('tweet_output'): # check if the directory "tweet_output" exists
    os.makedirs('tweet_output')  # create the directory if it doesn't exist

ft2 = open("tweet_output/ft2.txt","w") # writing median to ft2.txt file
for y in tw_md:
    ft2.write("%s\n" % y)
ft2.close()