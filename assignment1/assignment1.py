# Write your code here.
# task 1
def hello():
    return "Hello!"
print(hello())

# task 2

def greet(name):
    return f"Hello, {name}!"
print (greet("Natalie"))

# task 3

def calc(a, b, operation="multiply"):
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b 
        elif operation == "modulo":
            return a % b 
        elif operation == "int_divide":
            return a // b 
        elif operation == "power":
            return a ** b
        else:
            return "Error: Invalid operation"   
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

print(calc(2, 5))  
print(calc(2, 5, "add")) 
print(calc(2, 5, "subtract"))  
print(calc(2, 5, "divide")) 
print(calc(2, 5, "modulo")) 
print(calc(2, 5, "int_divide"))  
print(calc(2, 5, "power"))  
print(calc(2, 0, "divide"))
print(calc("hello", 3, "multiply")) 
print(calc(5, "world", "add"))

# task 4

def data_type_conversion(value, data_type):
    try:
        if data_type == "int":
            return int(value)
        elif data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
        else:
            return f"Error: Invalid data type '{data_type}'"
    except ValueError:
        return f"You can't convert {value} into a {data_type}."


print(data_type_conversion("123", "int")) 
print(data_type_conversion("45.67", "float"))
print(data_type_conversion(89, "str")) 
print(data_type_conversion("nonsense", "int"))
print(data_type_conversion("ocean", "float"))
print(data_type_conversion(1.11, "unknown"))  

# task 5

def grade(*args):
    try:
        if not args:
            return "Invalid data was provided."
        
        avg = sum(args) / len(args)
        
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    
    except (TypeError, ValueError):
        return "Invalid data was provided."
    
print(grade(88, 90, 95, 88))
print(grade(80, 86, 83, 92))
print(grade(70, 71, 77, 80))
print(grade(70, 60, 61, 80))
print(grade(40, 50, 35, 65))
print(grade(40, "hi", 86))

# task 6

def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result
print(repeat("Hi", 4))

# task 7
  
def student_scores(mode, **kwargs):
    if not kwargs:  
        return "No scores available."
    
    if mode == "best":
        best_student = None
        highest_score = float('-inf') 
        for key, value in kwargs.items():
            if value > highest_score:
                highest_score = value
                best_student = key
        return best_student  
    
    elif mode == "mean":
        total_score = 0
        count = 0
        for key, value in kwargs.items():
            total_score += value
            count += 1
        return total_score / count 
    
    else:
        return "Invalid mode. Use 'best' or 'mean'."



print(student_scores("best", Alla=85, Bill=92, Charlie=88))  
print(student_scores("mean", Alla=85, Bill=92, Charlie=88))  


#task 8

def titleize(text):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    
    words = text.split() 
    
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word.lower() not in little_words:
            words[i] = word.capitalize()
        else:
            words[i] = word.lower()  
    
    return " ".join(words)  

print(titleize("a beginning of the story"))
print(titleize("on the table in the room"))
print(titleize("the end of night time"))

# task 9

def hangman(secret, guess):
    return "".join(letter if letter in guess else "_" for letter in secret)

print(hangman("alphabet", "ab")) 
print(hangman("approximately", "p"))  
print(hangman("individual", "di")) 

# task 10

def pig_latin(sentence):
    words = sentence.split()
    vowels = "aeiou"

    def convert_word(word):
        if word[0] in vowels:
            return word + "ay"
        elif word.startswith("qu"):
            return word[2:] + "quay"
        else:
            for i, letter in enumerate(word):
                if letter in vowels:
                    return word[i:] + word[:i] + "ay"
            return word + "ay"

    return " ".join(convert_word(word) for word in words)

print(pig_latin("monthly product update"))
print(pig_latin("quality best is not better"))
print(pig_latin("Better safe than sorry"))