# coding : utf-8

# 1) Implémenter extract_data()
# 2) Implémenter fizzbuzz()
# 3) Implémenter les autres fonctions

import math
import unittest


# Given a string and a non-negative int n, return a larger string
# that is n copies of the original string.
# Example: string_times("hey", 3) should return "heyheyhey"
def string_times(string, n):
    return string * n


# Write a function which returns True if a year is a leap year.
# A year is leap year if:
# - it is divisible by 4 AND indivisible by 100
# or if:
# - it is divisible by 400
def is_leap_year(year):
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)


# Given a list of ints, return True if one of the first 4 elements
# in the array is a 9. The list length may be less than 4.
def array_front9(nums):
    def check_existence(nums) :
            if 9 in nums : 
                return True 
            else : 
                return False
    if len(nums) < 4 : return check_existence(nums)
    else : 
       return check_existence(nums[:4])

# Given a list of ints, return the list of their square root.
def list_sqrt(nums):
    from math import sqrt
    return [math.sqrt(i) for i in nums]


# Write a function which return a dict containing the number of time each letter
# is present in the given text.
def occurences(text):
    dico = {}
    for l in text : 
        if l in dico:
            dico[l] += 1
        else:
            dico[l] = 1
    return dico


# Write a function that maps a list of words into a list of
# integers representing the lengths of the corresponding words.
def length_words(words):
    return [len(word) for word in words]


# Write a function that takes a number and returns a list of its digits.
def number_to_digits(number):
    return [int(x) for x in str(number)] 



# Write a function that translates a text from english to Pig Latin.
# English is translated to Pig Latin by taking the first letter of every word,
# moving it to the end of the word, and adding 'ay'.
def pig_latin(text):
    new_text = ""
    space = ""
    list_txt = text.split(" ")
    for word in  list_txt :
        first_letter = ''
        if  not (word == list_txt[-1]) : space = " "
        if  (word == list_txt[-1]) : space = ""
        first_letter = word[1].capitalize() if word[0].isupper() else word[1] 
        new_text +=  first_letter + word[2:] + word[0].lower() + "ay" + space
    return new_text


# Write a function which prints numbers from 1 to 100,
# but which prints "Fizz" instead of multiple of 3,
# "Buzz" instead of multiple of 5,
# and "FizzBuzz" instead of multiple of 15

def fizzbuzz_item(i) :
    a = (i % 3 == 0)
    b = (i % 5 == 0)
    res = 0
    if (not a and not b) : res = i
    else : res = ""
    if a : res += "Buzz"
    if b : res += "Fizz"
    print(res)

def fizzbuzz():
    [fizzbuzz_item(i) for i in range(1,101)]

weather_data = {
    "Paris": {
        "weather_list": [{
            "dt": 1569434400,
            "main": {"temp": 289.15, "humidity": 76},
            "dt_txt": "2019-09-25 18:00:00"
        }, {
            "dt": 1569445200,
            "main": {
                "temp": 289.62,
                "humidity": 87
            },
            "dt_txt": "2019-09-25 21:00:00"
        }],
        "metadata": {
            "coord": {"lat": 48.8566, "lon": 2.3515},
            "country": "FR",
        }
    },
    "London": {
        "weather_list": [{
            "dt": 1569434400,
            "main": {"temp": 289.52, "humidity": 77},
            "dt_txt": "2019-09-25 18:00:00"
        }, {
            "dt": 1569445200,
            "main": {"temp": 287.78, "humidity": 86},
            "dt_txt": "2019-09-25 21:00:00"
        }],
        "metadata": {
            "coord": {"lat": 51.5073, "lon": -0.1277},
            "country": "GB",
        }
    }
}


# Given the above data, write a function which return a list of dict,
# where each dict contains these fields:
# - name (str): the city name
# - country (str): the city country
# - date (str): the date
# - temp (float): the temperature in °celsius (not °kelvin)
def extract_data(data):
    list_dico = []
    for key, value in data.items():
        dico = {}
        dico.update({"name" : key , "country" : value["metadata"]["country"], "date" : value["weather_list"][0]["dt_txt"], "temp" : value["weather_list"][0]["main"]["temp"]-273.15})
        list_dico.append(dico)
    return list_dico


# End of exercices.


########################################################################
# Here's our "unit tests" (à quoi ça sert ? => https://huit.re/gMGd03vx)


class Lesson1Tests(unittest.TestCase):
    def test_01_string_times(self):
        self.assertEqual(string_times('Plop', 2), 'PlopPlop')
        self.assertEqual(string_times('Hey', 1), 'Hey')
        self.assertEqual(string_times('=', 4), '====')

    def test_02_is_leap_year(self):
        self.assertTrue(is_leap_year(2000))
        self.assertTrue(is_leap_year(2020))
        self.assertFalse(is_leap_year(1899))
        self.assertFalse(is_leap_year(1900))

    def test_03_array_front9(self):
        self.assertEqual(array_front9([1, 2, 9, 3, 4]), True)
        self.assertEqual(array_front9([1, 2, 3, 4, 9]), False)
        self.assertEqual(array_front9([1, 2, 3, 4, 5]), False)

    def test_04_list_sqrt(self):
        self.assertEqual(list_sqrt([]), [])
        self.assertEqual(
            list_sqrt([4, 9, 16, 81]),
            [2.0, 3.0, 4.0, 9.0]
        )

    def test_05_occurences(self):
        self.assertEqual(
            occurences("hello world"),
            {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
        )

    def test_06_length_words(self):
        self.assertEqual(length_words(['hello', 'world']), [5, 5])
        self.assertEqual(length_words(['hey']), [3])

    def test_07_number_to_digits(self):
        self.assertEqual(number_to_digits(2019), [2, 0, 1, 9])

    def test_08_pig_latin(self):
        self.assertEqual(pig_latin("Hello"), "Ellohay")
        self.assertEqual(
            pig_latin("The quick brown fox"),
            "Hetay uickqay rownbay oxfay"
        )

    def test_09_extract_data(self):
        result = extract_data(weather_data)
        self.assertEqual(
            result[0],
            {
                'name': 'Paris',
                'country': 'FR',
                'date': "2019-09-25 18:00:00",
                'temp': 16.0
            }
        )


def run_tests():
    test_suite = unittest.makeSuite(Lesson1Tests)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)



if __name__ == '__main__':
    run_tests()
