# CSCI1133,Lab Section 004,lab06 Shanshan Zhong city_country
"""
Created on Thu Feb 28 13:04:18 2019
@author: shanshanzhong
"""
def city_country(city_name, country_name):
    print('%s, %s' % (city_name, country_name))

def main():
    num = int(input('How many times do you want to run the function: '))
    for i in [0,num]:
        city_name = input('Enter a city name: ')
        country_name = input('Enter a country name: ')
        city_country(city_name, country_name)
        print(city_country)
        
main()


def main():
    num = int(input('How many times do you want to run the function: '))
    i = 0 #i is used to control times loop
    while i < num:
        city_name = input('Enter a city name: ')
        country_name = input('Enter a country name: ')
        city_country(city_name, country_name)
        print(city_country)
        i += 1 #control times loop
        
main()
