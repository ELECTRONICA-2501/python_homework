# Write your code here.


#task 1
def hello():
    return "Hello!"

hello()



#task 2
def greet(name):
    return ("Hello, " + name + "!")

#greet("Sal")




#task 3
# def calc(x, y, operator):
#     try:
#         if operator == "+":
#             result = x+y
#         elif operator == "-":
#             result = x-y
#         elif operator == "*":
#             result = x*y
#         elif operator == "/":
#             result = x/y
#         elif operator == "^":
#             result = x**y
#         elif operator == "%":
#             result = x%y
#         elif operator == "//":
#             result = x//y
#         else:
#             return "Invalid op"
#     except ZeroDivisionError:
#             return "You can't divide by 0!"
#     except TypeError:
#             return "You can't multiply those values!"
        
#     return result



def calc(x,y,operator = "multiply"):
    result = None
    try:
        match operator:
            case "add":
                result = x+y
            case "subtract":
                result = x-y
            case "multiply":
                result = x*y
            case "divide":
                result = x/y
            case "power":
                result = x**y
            case "modulo":
                result = x%y
            case "int_divide":
                result = x//y
            case "_":
                return "Invalid op"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    return result




#task 4 

def data_type_conversion(val, data_type):
    try:
        match data_type:
            case "int":
                return int(val)
            case "float":
                return float(val)
            case "str":
                return str(val)
            case _:
                return "Invalid data type"
    except ValueError:
        return "You can't convert "+val+" into a " + data_type + "."
    


    
#task 5

def grade(*args):
    try:
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <0 or arg > 100:
                return "Invalid data was provided."
            
            average = sum(args) / len(args)

            if average >= 90:
                return "A"
            elif average >= 80:
                return "B"
            elif average >= 70:
                return "C"
            elif average >= 60:
                return "D"
            # elif arg < 0 or arg > 100 or type(arg) != int:
            #     print("Invalid data was provided")
            else:
                return "F"
    except (TypeError, ValueError):
        return "Invalid data was provided."
# print(grade(75, 85, 95))  # Expected: "B"




#task 6
def repeat(str, count):
    newString = ""
    for x in range(count):
        newString += str
    return newString
#repeat("Sal", 5)





#task 7
def student_scores(mode, **kwargs):
    if not kwargs:  
        return "No scores provided."
    
    if mode == "best":
        return max(kwargs, key=kwargs.get)
    elif mode == "mean":
        return sum(kwargs.values()) / len(kwargs)  # Return just the numeric mean

         
    
    else:
        return "Invalid mode."

# student_scores("best", best="Sal")
# student_scores("mean", mean="90")




#task 8
def titleize(str):
    
    # text[0].capitalize()
    # text[-1].capitalize()
    lilWords = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = str.lower().split()
        # this func would for example take "game of thrones" put it in a list called words
        # ["game" , "of" , "thrones"]

        # x is the index, word is the actual word at the index

    for x, word in enumerate(words):
        # first iteration examples
        # index = 0, word = game, condition check: First word = Capitalize, updated word = "Game"

        #2nd iteration
        # index = 1, word = of , condition check: word == lilWords, stay lower, update word = "of"
        if x == 0 or x == len(words)-1:
            words[x] = word.capitalize()
        elif word in lilWords:
            words[x] = word.lower()
        else:
            words[x] = word.capitalize()
    
    return " ".join(words)






# task 9

def hangman(secret_str, guess_str):
    #python strings are immutable so we cant modify them in place,
    # for edge case
    secret_str = secret_str.lower()
    guess_str = guess_str.lower()
    # use rolling sum to aggregate a letter or "_" as we iterate throu for loop
    output = ""
    for letter in secret_str:
        if letter in guess_str:
            output += letter
        else:
            output += "_"
    return output

#print(hangman("APIDTA", "ad"))




#task 10
def pig_latin(sentence):
    words = sentence.split()  # Split the sentence into words
    pig_latin_words = []  # List to store Pig Latin words

    for word in words:
        if word[0] in "aeiou":  
            pig_word = word + "ay"  # Rule 1: Starts with a vowel
        else:
            # Special handling for words containing "qu" at the start or inside a consonant cluster
            if "qu" in word:
                qu_index = word.index("qu")  # Find the first occurrence of "qu"
                if qu_index == 0 or all(c not in "aeiou" for c in word[:qu_index]):  
                    # Move everything before "qu" to the end
                    pig_word = word[qu_index + 2:] + word[:qu_index + 2] + "ay"
                else:
                    # Treat it as a normal consonant cluster if "qu" is not part of a leading cluster
                    pig_word = word[1:] + word[0] + "ay"
            else:
                # Normal consonant cluster handling
                for i, char in enumerate(word):
                    if char in "aeiou":
                        pig_word = word[i:] + word[:i] + "ay"
                        break
        
        pig_latin_words.append(pig_word)  # Store result

    return " ".join(pig_latin_words)  # Return transformed sentence



# def pig_latin(word):
#     words = word.split() # splits sentence apart and stores in list
#     pig_latin_word = [] # list 
#     #pigVowels = {"ay", "qu"}

#     for x in words: # we are at the first word
#         if x[0] in "aeiou": #checks the first letter of first word in list
#             pig_word = x + "ay"
#         # elif x.startswith("qu"):
#         elif "qu" in x[:2]:
#             pig_word = x[2:] + "quay" #x[2:] means start at array index 2, or 3rd element and index onward til end of string
#         else:
#             # Find the first vowel position
#             for i, char in enumerate(x):
#                 if char in "aeiou":
#                     pig_word = x[i:] + x[:i] + "ay"
#                     break

#         pig_latin_word.append(pig_word)  # Store result

        
#     return " ".join(pig_latin_word)


#print(pig_latin("whos calling my phone again"))


# calc1 = calc(2,0,"/")
# print(calc1)
# calc2 = calc("a","b", "*")
# print(calc2)

# calc_MatchCase1 = calc_MatchCase(2,0,"/")
# print(calc_MatchCase1)
# calc_MatchCase2 = calc_MatchCase("a","b", "*")
# print(calc_MatchCase2)
# calc_MatchCase3 = calc_MatchCase(2,3, "*")
# print(calc_MatchCase3)

# data_type_conversion1 = data_type_conversion(2, "int")
# print(data_type_conversion1)
# data_type_conversion2 = data_type_conversion("nonsense", "float")
# print(data_type_conversion2)

# grade_scale(90, 80, 70, 60, 50)
# grade_scale(-10)
# grade_scale(101)
# grade_scale("a")
