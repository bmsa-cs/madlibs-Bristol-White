"""
MadLibs
Author: Bristol White
Period/Core: 7


"""

import time

print("Let's play a really funny and awesome word game!!!!!!")
time.sleep(3)
word_one = input("Enter your name: ")
word_two = input("Pick an object: ")
word_three = input("Pick a place: ")
word_five = input("Pick a past tense verb: ")
word_six = input("Pick an adjective: ")
word_seven = input("Pick another name: ")
word_eight = input("Pick a food: ")
word_nine = input("Pick an emotion: ")

time.sleep(3)
print("Processing story... Processing story...")
time.sleep(10)

title = "The story of {fname}!".format(fname = word_one)
print(title)
print("Written by:\n You!",word_one,"!")
time.sleep(2)

print("Once upon a time,", word_one ,"was playing with their",word_six +' '+ word_two,".")
print("They sat there and played for a bit, when their friend", word_seven ,"came up to him.")
print("\"Hey buddy, how are you doing!?\"", word_seven ,"exclaimed.")
print("\"I'm feeling", word_nine,"\" said", word_one,".")
print("The two walked and talked for a while, and made their way to", word_three,".")
print("They", word_five,"around", word_three,"for a bit, before deciding it was time to eat.")
print("They feasted on some", word_six +' '+ word_eight,"until it was night.")
print("The two finished their food and", word_five,"for a while more, exchanging words.")
print("They said goodbye to each other, and left. It was a",word_six ,"day!")