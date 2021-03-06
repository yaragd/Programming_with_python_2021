##################################################
# Author: Hebah Qatanany
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Professor: Diego Pajarito
# Email: hebah.qatanany@studnets.iaac.net
# Course: MaCT precourse- Programming
##################################################

current_year= 2020

first_city_name= 'Yaffa'
first_country_name= 'Palestine'
first_city_area= 520 # units in km2
first_city_population= 460613 # units in millions
first_city_density= round(first_city_population/first_city_area) # units in millions/km2
first_year_of_establishment= 1902
first_city_age= current_year-first_year_of_establishment

second_city_name = 'Dubai'
second_country_name= 'UAE'
second_city_area= 4114 # units in km2
second_city_population= 3331420 # units in millions
second_city_density = round(second_city_population/second_city_area) # units in millions/km2
second_year_of_establishment= 1971
second_city_age= current_year-second_year_of_establishment

print('I come from the beautiful coastal city of ' + str(first_city_name)+ ' in '+ str(first_country_name))
print('The city is '+str(first_city_age)+' years old')
print('and has a population density of: ' + str(first_city_density))
print('However, for the past 20 years I have lived in '+ second_city_name)
print('a much younger city with a population density of '+ str(second_city_density))


##################################################
#This is the end of the code
##################################################


