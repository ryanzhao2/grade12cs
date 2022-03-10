import csv

month_after = {'January': 0, 'February': 1, 'March': 2, 'April': 3, 'May': 4, 'June': 5,
                'July': 6, 'August': 7, 'September': 8, 'October': 9, 'November': 10, 'December': 12}
#index 1 is the type of film(movie or show)
#index 2 is the title
#index 6 is release on app date
#index 7 is actual movie release date

def calculate_date_difference(app_release, actual_release):
    list = []
    if app_release[0] != 'unknown':
        months = month_after[app_release[0]]
    else:
        months = 'unknown'
    if app_release[1] != 'unknown':
        days = int(app_release[1].replace(',', ''))
    else:
        days = 'unknown'
    if app_release[2].isdigit():
        years = int(app_release[2]) - int(actual_release)
    else:
        years = 'unknown'
    list.append(days)
    list.append(months)
    list.append(years)
    return list

def netflix_app(file):
    with open(file, 'r') as netflix:
        dict = {}
        netflix.readline()
        reader = csv.reader(netflix)
        for line in reader:
            movie_or_show = line[1]
            title = line[2]
            app_rel = line[6].split()
            if len(app_rel) == 0:
                for i in range(3):
                    app_rel.append('unknown')
            actual_rel = line[7]
            difference = calculate_date_difference(app_rel, actual_rel)
            dict[title] = []
            dict[title].append(movie_or_show)
            dict[title].append(difference)

        return dict

def amazon_prime(file):
    with open(file, 'r') as amazon:
        dict = {}
        amazon.readline()
        reader = csv.reader(amazon)
        for line in reader:
            movie_or_show = line[1]
            title = line[2]
            app_rel = line[6].split()
            if len(app_rel) == 0:
                for i in range(3):
                    app_rel.append('unknown')
            actual_rel = line[7]
            difference = calculate_date_difference(app_rel, actual_rel)
            dict[title] = []
            dict[title].append(movie_or_show)
            dict[title].append(difference)

        return dict


def disney_plus(file):
    with open(file, 'r') as disney:
        dict = {}
        disney.readline()
        reader = csv.reader(disney)
        for line in reader:
            movie_or_show = line[1]
            title = line[2]
            app_rel = line[6].split()
            if len(app_rel) == 0:
                for i in range(3):
                    app_rel.append('unknown')
            actual_rel = line[7]
            difference = calculate_date_difference(app_rel, actual_rel)
            dict[title] = []
            dict[title].append(movie_or_show)
            dict[title].append(difference)

        return dict

def hulu_app(file):
    with open(file, 'r') as hulu:
        dict = {}
        hulu.readline()
        reader = csv.reader(hulu)
        for line in reader:
            movie_or_show = line[1]
            title = line[2]
            app_rel = line[6].split()
            if len(app_rel) == 0:
                for i in range(3):
                    app_rel.append('unknown')
            actual_rel = line[7]
            difference = calculate_date_difference(app_rel, actual_rel)
            dict[title] = []
            dict[title].append(movie_or_show)
            dict[title].append(difference)

        return dict

netflix_movies = netflix_app('netflix_titles.csv')
amazon_movies = amazon_prime('amazon_prime_titles.csv')
disney_plus_movies = disney_plus('disney_plus_titles.csv')
hulu_movies = hulu_app('hulu_titles.csv')

print(amazon_movies)