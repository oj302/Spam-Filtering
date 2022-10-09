# Spam-Filtering
## Description
An algorithm that determines whether an e-mail is spam or ham based on what words and phrases are included

Data is input through csv files containing only 1's and 0's in the data directory.

The first collumn represents whether an email is spam (1) or ham (0). Other collumns represent specific words and whether theyre icluded in the email (1) or not (0).

A testing data set can also be put into the data directory and the accuracy of the program will be output when run.

## Algorithm Overview
The program first counts the total number of spam and ham emails, then counts the frequency of words in each type of email (e.g how many spam emails have the phrase "money" in them).

It then calculates probability of an email being spam / ham given it includes the word for each word using the calculation:

type_of_email = spam or ham depending on parameter

word          = word being looked at

probability   = number of type_of_email that includes word / total number of type_of_email

When training email data is given a value for the probability of the email being spam or ham is stored. These values are then multiplied by the probability of the  email being spam or ham given the words that are included / not included.
The email is then assumed to be whatever has the higher probability value.
