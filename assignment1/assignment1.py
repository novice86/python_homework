# Task1
def hello():
    return "Hello!"


# Task2
def greet(name):
    return f"Hello, {name}!"


# Task3
def addition(num1, num2):
    try:
        res = num1 + num2
    except TypeError:
        return "You can't add those values!"
    else:
        return res


def subtraction(num1, num2):
    try:
        res = num1 - num2
    except TypeError:
        return "You can't subtract those values!"
    else:
        return res


def multiplication(num1, num2):
    try:
        res = num1 * num2
    except TypeError:
        return "You can't multiply those values!"
    else:
        return res


def division(num1, num2, int_divide=False):
    try:
        if not int_divide:
            res = num1 / num2
        else:
            res = num1 // num2
    except ZeroDivisionError:
        return "You can't divide by 0!" # it is for the comparison with the test case, because the test case expects a string, not an exception
    except TypeError:
        raise TypeError(f"You can't divide those values: {num1} and {num2}")
    else:
        return res


def modulo(num1, num2):
    try:
        res = num1 % num2
    except ZeroDivisionError:
        return "You can't divide by 0!" # it is for the comparison with the test case, because the test case expects a string, not an exception
    except TypeError:
        raise TypeError(f"You can't modulo those values: {num1} and {num2}")
    else:
        return res


def power(num1, num2):
    try:
        res = num1 ** num2
    except TypeError:
        raise TypeError(f"You can't exponentiate those values: {num1} and {num2}")
    else:
        return res


def calc(num1, num2, operation="multiply"):
    match operation:
        case "add":
            return addition(num1, num2)
        case "subtract":
            return subtraction(num1, num2)
        case "multiply":
            return multiplication(num1, num2)
        case "divide":
            return division(num1, num2, int_divide=False)
        case "int_divide":
            return division(num1, num2, int_divide=True)
        case "modulo":
            return modulo(num1, num2)
        case "power":
            return power(num1, num2)


# Task4
def data_type_conversion(value, target_type):
    try:
        match target_type:
            case "int":
                res = int(value)
            case "float":
                res = float(value)
            case "str":
                res = str(value)
    except ValueError:
        return f"You can't convert {value} into a {target_type}."
    else:
        return res


# Task 5
def grade(*args):
    try:
        grades = [float(grade) for grade in args]
    except ValueError:
        return "Invalid data was provided."
    
    avg_grade = sum(grades) / len(grades)
    if avg_grade >= 90:
        return "A"
    elif avg_grade >= 80:
        return "B"
    elif avg_grade >= 70:
        return "C"
    elif avg_grade >= 60:
        return "D"
    else:
        return "F"
    
# Task 6
def repeat(string, times):
    print(f"Repeating {string} {times} times.")
    for i in range(times - 2):
        string += string
    return string


# Task 7
def student_scores(statistic, **kwargs):
   total_score = 0
   best_score = float('-inf')
   best_student = None
   for student, score in kwargs.items():
        total_score += score
        if score > best_score:
            best_score = score
            best_student = student
        
   if statistic == "mean":
         return total_score / len(kwargs)
   elif statistic == "best":
         return best_student
   else:
         return "Invalid statistic provided."
   
# Task 8
def titleize(string):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = string.split()
    titleized_words = []

    for i, word in enumerate(words):
        if i == 0:
            titleized_words.append(word.capitalize())
        elif i == len(words) - 1:
            titleized_words.append(word.capitalize())
        elif word.lower() in little_words:
            titleized_words.append(word.lower())
        else:
            titleized_words.append(word.capitalize())

    return " ".join(titleized_words)


# Task 9 
def hangman(secret, guess):
    result = ['_'] * len(secret)
    for i, letter in enumerate(secret):
        if letter in guess:
            result[i] = letter
    return "".join(result)


# Task 10
def find_consonants_cluster_index(word):
    consonants = "bcdfghjklmnpqrstvwxyz"
    i = 0
    while i < len(word):
        if word[i] in consonants:
            if word[i] == 'q' and i + 1 < len(word) and word[i+1] == 'u':
                i += 2
            else:
                i += 1

        else:
            break
    
    return i
    

def pig_latin(string):
    vowels = "aeiou"
    words = string.split()

    pig_latin_words = []
    for word in words:
        if word[0] in vowels:
            pig_latin_words.append(word + "ay")
        else:
            cc_idx = find_consonants_cluster_index(word)
            pig_latin_words.append(word[cc_idx:] + word[:cc_idx] + "ay")
    
    return " ".join(pig_latin_words)
    