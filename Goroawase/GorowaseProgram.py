import itertools
from pentago import Pentago
from pentago.lang import *

import asyncio


output = open('output.txt', 'w',encoding="utf-8")

    #Potentially set up each number to have a dictionary for each number system
    #Systems being Kun'yomi, On'Yomi and English pronounciation
Gorowase = {
        0:["まる","ま", "れい", "れ","ォ","ゼ", "ゼロ"],
        1 :["ひとつ", "ひと", "ひ", "いち", "い","ワン"],
        2: ["ふたつ", "ふ","ふた", "に", "ツー", "トゥー"],
        3:["みつ", "み", "さん", "さ","スリー"],
        4:["よん", "よ", "よつ","し", "フォー"],
        5:["いつつ", "いつ" "ご", "こ",	"ファイブ"],
        6: ["むつ", "む","ろく", "ろ", "シックス"],
        7:["なな", "ななつ", "な","しち", "セブン"],
        8:["やつ", "や", "はち", "は", "ば" ,"エイト"],
        9:["ここのつ", "こ", "きゅう", "きゅ","く", "ナイン"],
        10: ["とお", "じゅう", "じ", "テ"]
    }


finalCombo = []
max_char = 6

def get_limited_input(prompt, limit):
    finalInput = []
    while len(finalInput) < limit:
        user_input = input(prompt)
        limited_input = user_input[:2]
        match limited_input:
            case "0":
                finalInput.append(limited_input)
                print(finalInput)
            case "1":
                finalInput.append(limited_input)
                print(finalInput)
            case "2":
                finalInput.append(limited_input)
                print(finalInput)
            case "3":
                finalInput.append(limited_input)
                print(finalInput)
            case "4":
                finalInput.append(limited_input)
                print(finalInput)
            case "5":
                finalInput.append(limited_input)
                print(finalInput)
            case "6":
                finalInput.append(limited_input)
                print(finalInput)
            case "7":
                finalInput.append(limited_input)
                print(finalInput)
            case "8":
                finalInput.append(limited_input)
                print(finalInput)
            case "9":
                finalInput.append(limited_input)
                print(finalInput)
            case "10":
                finalInput.append(limited_input)
                print(finalInput)
            case " ":
                print("You pressed space, ceasing input")
                break;
            case _:
                print("Invalid input detected. Please try again.")            
                
    return finalInput

async def main():
    #get input from user, they can choose up to max_char numbers.
    #Users can also enter in space to skip the rest of input, so they can have Goroawase less than 6.
    userInput = get_limited_input(f"Enter each number separately for the Gorowase:\n You are limited to {max_char} numbers ", max_char)
    print("The final list of numbers is",userInput)
    output.write(f"You have input {userInput} these numbers.\n\n\n")
    userInputNumbers = []
    iterator = 1
    #translate the input from string into ints.
    for i in userInput:
        userInputNumbers.append(int(i))
        
        kiryu = ""
        intermediateWords = []
        pentago = Pentago(JAPANESE, ENGLISH)
    #Use the userInput(now an int) to correlate to the dictionary with it's string values for each number.
    #Have the inputs for itertools be the lists contained in the dictionary instead of individual user input ints.
    for i in userInputNumbers:
        
        orderedWordPools = [Gorowase[num] for num in userInputNumbers]
        #Create all possible combinations in the order that they are given. "39", all values of three are in the first character slot.
        for combo in itertools.product(*orderedWordPools):
            intermediateWords.append("".join(combo))
            
            #We now have all the combination words, so now we translate into the chosen language and then save them to an output file. 
        for word in intermediateWords:
            
            result = await pentago.translate(word, honorific=False)
            translatedResult = result["translatedText"]
            
            print(f"{iterator}:{word}")
            print(f"{iterator}:{translatedResult}")
            print(f"{iterator}:{result}")
            
            output.write(f"{iterator}:{word}\n")
            output.write(f"{iterator}:{translatedResult}\n")
            output.write(f"{iterator}:{result}\n")
            iterator+=1
    
    #manually close the writing file.
    print("Writing to output.txt is finished")
    output.close()

if __name__ == "__main__":
    asyncio.run(main())
#main()