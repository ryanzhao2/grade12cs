import csv

month_after = {'January': 0, 'February': 1, 'March': 2, 'April': 3, 'May': 4, 'June': 5,
                'July': 6, 'August': 7, 'September': 8, 'October': 9, 'November': 10, 'December': 12}
#index 1 is the type of film(movie or show)
#index 2 is the title
#index 6 is release on app date
#index 7 is actual movie release date

def calculate_date_difference(app_release, actual_release):
    if app_release[0] != 'unknown':
        month_to_days = 30 * month_after[app_release[0]]
    else:
        month_to_days = 'unknown'
    if app_release[1] != 'unknown':
        days = int(app_release[1].replace(',', ''))
    else:
        days = 'unknown'
    if app_release[2].isdigit():
        years = int(app_release[2]) - int(actual_release)
        years_to_days = 365 * years
    else:
        years_to_days = 'unknown'
    total = month_to_days + days + years_to_days
    return total

def netflix_app(file):
    count = 0
    with open(file, 'r', encoding='utf-8') as netflix:
        dict = {}
        netflix.readline()
        reader = csv.reader(netflix)
        for line in reader:
            movie_or_show = line[1]
            title = line[2]
            app_rel = line[6].split()
            if len(app_rel) != 0:
                count += 1
            if len(app_rel) == 0:
                for i in range(3):
                    app_rel.append('unknown')
            actual_rel = line[7]
            difference = calculate_date_difference(app_rel, actual_rel)
            dict[title] = []
            dict[title].append(movie_or_show)
            dict[title].append(difference)
        print(count)
        #return dict

def amazon_prime(file):
    count = 0
    with open(file, 'r', encoding='utf-8') as amazon:
        dict = {}
        amazon.readline()
        reader = csv.reader(amazon)
        for line in reader:
            movie_or_show = line[1]
            title = line[2]
            app_rel = line[6].split()
            if len(app_rel) != 0:
                count += 1
            if len(app_rel) == 0:
                for i in range(3):
                    app_rel.append('unknown')
            actual_rel = line[7]
            difference = calculate_date_difference(app_rel, actual_rel)
            dict[title] = []
            dict[title].append(movie_or_show)
            dict[title].append(difference)
        print(count)
        #return dict


def disney_plus(file):
    count = 0
    with open(file, 'r', encoding='utf-8') as disney:
        dict = {}
        disney.readline()
        reader = csv.reader(disney)
        for line in reader:
            movie_or_show = line[1]
            title = line[2]
            app_rel = line[6].split()
            if len(app_rel) != 0:
                count += 1
            if len(app_rel) == 0:
                for i in range(3):
                    app_rel.append('unknown')
            actual_rel = line[7]
            difference = calculate_date_difference(app_rel, actual_rel)
            dict[title] = []
            dict[title].append(movie_or_show)
            dict[title].append(difference)

        print(count)
        #return dict

def hulu_app(file):
    count = 0
    with open(file, 'r', encoding='utf-8') as hulu:
        dict = {}
        hulu.readline()
        reader = csv.reader(hulu)
        for line in reader:
            movie_or_show = line[1]
            title = line[2]
            app_rel = line[6].split()
            if len(app_rel) != 0:
                count += 1
            if len(app_rel) == 0:
                for i in range(3):
                    app_rel.append('unknown')
            actual_rel = line[7]
            difference = calculate_date_difference(app_rel, actual_rel)
            dict[title] = []
            dict[title].append(movie_or_show)
            dict[title].append(difference)
        print(count)
        print(dict)
        return dict

def ranges(netflix, amazon, disney, hulu):
    zero_ten = {}
    eleven_thirty = {}
    thirty_90 = {}
    ninety_one_eighty = {}
    one_eighty_to_year = {}
    over_year = {}
    for char in netflix:
        netflix_date = netflix[char]
        amazon_date = amazon[char]

        if char in amazon:
            pass


netflix_movies = netflix_app('netflix_titles.csv')
amazon_movies = amazon_prime('amazon_prime_titles.csv')
disney_plus_movies = disney_plus('disney_plus_titles.csv')
hulu_movies = hulu_app('hulu_titles.csv')

#print(amazon_movies)