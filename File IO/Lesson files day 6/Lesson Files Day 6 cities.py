import random
import datetime


def create_city_list(filename):
    city_list = []

    with open(filename, encoding='utf-8', errors='ignore') as citiesIn:

        citiesIn.readline()  ignore headers in file
        citiesIn.readline()

        for city in citiesIn:
            temp = []
            data = city.split("\t")

            temp.append(data[0])
            temp.append(data[1].strip())
            city_list.append(temp)

    return city_list
      
    

def create_sample_city_data(filename, city_list):

    with open(filename, "w", encoding='utf-8', errors='ignore') as citiesOut:

        for location in city_list:
                
            s = ""
            s += f'{location[0]:>15}\t'
            s += f'{location[1]:>15}\t'

            year = datetime.date.today().year
            
            generate 5 years of population data based on random growth
            growth = random.uniform(-1, 1)
            initialValue = random.randint(4, 30)
            for i in range(0, 5):
                year += 1
                pop = growth*i + initialValue

                s += f'{year}\t{pop:>5.1f}\t'

            s += '\n'

            citiesOut.write(s)
            print(s)


MAIN
location_list = create_city_list("cities.txt")

create_sample_city_data("sampleCityPopulation.txt", location_list)






import csv
import random
import datetime


def create_sample_city_data(filename, city_list):

    with open(filename, "w", encoding='utf-8', errors='ignore') as citiesOut:

        writer = csv.writer(citiesOut)
        
        for location in city_list:
                
            newCityData = []
            newCityData.append(location[0])
            newCityData.append(location[1])

            year = datetime.date.today().year
            
            #generate 5 years of population data based on random growth
            growth = random.uniform(-1, 1)
            initialValue = random.randint(4, 30)
            for i in range(0, 5):
                year += 1
                pop = growth*i + initialValue

                newCityData.append(year)
                newCityData.append(f'{pop:.1f}') 


            writer.writerow(newCityData)


MAIN
location_list = create_city_list("cities.txt")
create_sample_city_data("sampleCityPopulation.csv", location_list)




