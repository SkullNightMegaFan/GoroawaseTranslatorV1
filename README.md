# Goroawase Translator V1

### REQUIREMENTS
Python version 3.14.2

## Packages

#### pentago

#### httpx

#### requests

### Why Did I Make This?
For this school assignment I was tasked with creating a decryption or encryption program. I initially wanted to opt for a Caesar cypher ,but I wanted to do something a little more interesting. My mind eventually drifted to the scene Yakuza 0 where the main protagoinst 

### Context For Goroawase
Kiryu is sent a message on his pager and is able to quickly decipher the meaning through understanding Goroawase or number puns.
![Kiryu is a funny guy.](/Images/YakuzaPagerExample.webp "Kiryu receiving a Goroawase message on his pager.")
Source:
https://www.reddit.com/r/yakuzagames/comments/1dynrnx/how_in_the_hell_did_kiryu_decipher_this/


Goroawase are a play on reading of numbers in Japanese as Japanese has two primary systems of numbers.
English pronounciation is also used for some puns as well making approxiamately 6 different ways to read each number in Japanese.
![Fun Fact: The japanese On'Yonmi pronounciation of four is considered bad luck as it can also be read as meaning death.](/Images/NumberSystemsChart.png "A list of the most common Japanese pronounciations")
Source:
https://www.tofugu.com/japanese/goroawase-japanese-numbers-wordplay/

This leads to some cool nmemonic puns that are pretty interesting.
![My Mom loves salt on her Rice.](/Images/GoroawaseExample.png "A delcious example of Goroawase in the wild.")
Source:
https://www.tofugu.com/japanese/goroawase-japanese-numbers-wordplay/

### How To Use and How It Works
The user is allowed to input a maximum of 6 characters, with each input being separate by an enter character. 
If you have a Goroawase combo that is under 6 characters, simply enter in a space or " " character to have the program finish input handling.

The user's input is then translated from a string into an int. 
Which is then used to reference a dictionary that contains a value for each number it correlates too. 
Each value contains an array of all the possible Japanese pronounciations of the number.

itertools does the hard work of taking each array and using each element as a possibility for each specific character index.
i.e if you enter in 825, the first Japanese character will always be taken from the 8 array.

After all possible combinations are stored in a new array, they are translated line by line. (maybe I should make this run desync?)
On the first line is the japanese text, the second the english translation and the last is a verbose line containing translation details.

## Special thanks
I would like to thank my Professor Dr.Rob Pettit and the team behind Yakuza 0 as serving as my inspiration for this project. 

### Super thank you!


## Maintainment
This project is only in it's infancy stages. I plan to continue working on this project and would like to utilize AI for choice selection,
thereby the user won't be presented with hundreds of options and will see closer to a dozen or fewer.
Truthfully, I hope to update this on a bi-monthly update schedule. (Grad school has me busy!)