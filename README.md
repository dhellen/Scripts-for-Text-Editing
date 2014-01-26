Scripts-for-Text-Editing
========================

Basically, if my text editor lacks a feature, I write a script to stand in for it.

Wordcount.py performs a word count for a text file.  If you have Python 2, and it's your default python version, copy the wordcount.py script and place the copy in the same directory as your textfile, then type the following into your console:

python wordcount.py filename.txt

If you have python 3, first change line 27 to

print(len(words))

and then use the above argument in your console.
