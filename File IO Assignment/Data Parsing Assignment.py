import csv
from datetime import date

column_list = [6, 7, 3, 5, 8, 9]
month_after = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
                'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

def dict_ranges():
    the_ranges_dict = {'released after netflix': {'Movie': {}, 'TV Show': {}}, '0_10': {'Movie': {}, 'TV Show': {}},
                '11_30': {'Movie': {}, 'TV Show': {}}, '31_90': {'Movie': {}, 'TV Show': {}},
                '91_180': {'Movie': {}, 'TV Show': {}}, '181_365': {'Movie': {}, 'TV Show': {}},
                '365+': {'Movie': {}, 'TV Show': {}}, 'unknown': {'Movie': {}, 'TV Show': {}}}
    for ranges in the_ranges_dict:
        for type in the_ranges_dict[ranges]:
            if 'amazon' not in the_ranges_dict[ranges][type]:
                the_ranges_dict[ranges][type]['amazon'] = []
                the_ranges_dict[ranges][type]['disney'] = []
                the_ranges_dict[ranges][type]['hulu'] = []
    return the_ranges_dict

def calculate_date_difference(app_release, actual_release):
    if app_release[1] != 'unknown' and app_release[0] != 'unknown' and app_release[2] != 'unknown':
        month = int(month_after[app_release[0]])
        day = int(app_release[1].replace(',', ''))
        year = int(app_release[2])
        global_date_rel = date(int(actual_release), 1, 1)
        app_date_rel = date(year, month, day)
        date_difference = app_date_rel - global_date_rel
        return date_difference.days
    return 'unknown'

def streaming_programs(file, streaming_app_name):
    with open(file, 'r', encoding='utf-8') as app:
        dict = {}
        app.readline()
        reader = csv.reader(app)
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
            for char in column_list:
                dict[title].append(line[char])
            dict[title].append(title)
            dict[title].append(streaming_app_name)
        return dict

def ranges(netflix, amazon, disney, hulu, all_ranges):
    for char in netflix:
        netflix_date = netflix[char][1]
        netflix_release = netflix[char][3]
        netflix_type = netflix[char][0]
        if char in amazon and amazon[char][3] == netflix_release and amazon[char][0] == netflix_type:
            amazon_date = amazon[char][1]
            if amazon[char][1] != 'unknown':
                ama_dif = int(netflix_date - amazon_date)
            else:
                ama_dif = 'unknown'
            amazon[char].pop(1)
            amazon[char].insert(1, ama_dif)
            calculate_dict_for_ranges(all_ranges, amazon[char], ama_dif)
        if char in disney and disney[char][3] == netflix_release and disney[char][0] == netflix_type:
            disney_date = disney[char][1]
            if disney[char][1] != 'unknown':
                disney_dif = int(netflix_date - disney_date)
            else:
                disney_dif = 'unknown'
            disney[char].pop(1)
            disney[char].insert(1, disney_dif)
            calculate_dict_for_ranges(all_ranges, disney[char], disney_dif)

        if char in hulu and hulu[char][3] == netflix_release and hulu[char][0] == netflix_type:
            hulu_date = hulu[char][1]
            if hulu[char][1] != 'unknown':
                hulu_dif = int(netflix_date - hulu_date)
            else:
                hulu_dif = 'unknown'
            hulu[char].pop(1)
            hulu[char].insert(1, hulu_dif)
            calculate_dict_for_ranges(all_ranges, hulu[char], hulu_dif)
    return all_ranges

def calculate_dict_for_ranges(range_dict, content_list, range):
    if '-' in str(range) and range < 0:
        range_dict['released after netflix'][content_list[0]][content_list[-1]].append(content_list)
    elif str(range).isdigit() and range >= 0 and range <= 10:
        range_dict['0_10'][content_list[0]][content_list[-1]].append(content_list)
    elif str(range).isdigit() and range >= 11 and range <= 30:
        range_dict['11_30'][content_list[0]][content_list[-1]].append(content_list)
    elif str(range).isdigit() and range >= 31 and range <= 90:
        range_dict['31_90'][content_list[0]][content_list[-1]].append(content_list)
    elif str(range).isdigit() and range >= 91 and range <= 180:
        range_dict['91_180'][content_list[0]][content_list[-1]].append(content_list)
    elif str(range).isdigit() and range >= 181 and range <= 365:
        range_dict['181_365'][content_list[0]][content_list[-1]].append(content_list)
    elif str(range).isdigit() and range >= 366:
        range_dict['365+'][content_list[0]][content_list[-1]].append(content_list)
    elif range == 'unknown':
        range_dict['unknown'][content_list[0]][content_list[-1]].append(content_list)
    return range_dict

netflix_movies = streaming_programs('netflix_titles.csv', 'netflix')
amazon_movies = streaming_programs('amazon_prime_titles.csv', 'amazon')
disney_plus_movies = streaming_programs('disney_plus_titles.csv', 'disney')
hulu_movies = streaming_programs('hulu_titles.csv', 'hulu')
all_ranges = dict_ranges()
final_dict = ranges(netflix_movies, amazon_movies, disney_plus_movies, hulu_movies, all_ranges)
print(final_dict)
