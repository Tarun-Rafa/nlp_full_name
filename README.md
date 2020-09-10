# Full-Name-Predictor
Rule-based full name predictor

Person names in the English language typically consist of one or more forenames followed by one or more surnames (optionally preceded by zero or more titles and followed by zero or more suffixes). This situation can create ambiguity, as it is often unclear whether a particular name is a forename or a surname. For example, given the sequence Imogen and Andrew Lloyd Webber, it is not possible to tell what the full name of Imogen is, since that would depend on whether Lloyd is part of Andrew’s forename or surname (as it turns out, it is a surname: Imogen Lloyd Webber is the daughter of Andrew Lloyd Webber). This program explores ways of dealing with this kind of ambiguity.

This is a program that takes a string representing the names of two persons (joined by and), and tries to predict the full name of the first person in the string. 

# Data

A set of development and test data is available as a compressed ZIP archive on Blackboard. The uncompressed archive contains the following files:

1) A test file with a list of conjoined names.
2) A key file with the same list of conjoined names, and the correct full name of the first person for each example.
3) Three lists of name frequencies from U.S. census data (these lists are available on the web, and included in the package for your convenience).
4) Frequency of female first names from the 1990 census
5) Frequency of male first names from the 1990 census
6) Frequency of surnames from the 2010 census
