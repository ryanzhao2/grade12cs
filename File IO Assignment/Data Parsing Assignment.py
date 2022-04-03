import csv
from datetime import date


def dictionary_of_date_ranges():
    initial_ranges_dict = {'released after netflix': {'Movie': {}, 'TV Show': {}}, '0_10': {'Movie': {}, 'TV Show': {}},
                           '11_30': {'Movie': {}, 'TV Show': {}}, '31_90': {'Movie': {}, 'TV Show': {}},
                           '91_180': {'Movie': {}, 'TV Show': {}}, '181_365': {'Movie': {}, 'TV Show': {}},
                           '365+': {'Movie': {}, 'TV Show': {}}, 'unknown': {'Movie': {}, 'TV Show': {}}}
    for all_release_ranges in initial_ranges_dict:
        for type_of_film in initial_ranges_dict[all_release_ranges]:
            if 'amazon' not in initial_ranges_dict[all_release_ranges][type_of_film]:
                initial_ranges_dict[all_release_ranges][type_of_film]['amazon'] = []
                initial_ranges_dict[all_release_ranges][type_of_film]['disney'] = []
                initial_ranges_dict[all_release_ranges][type_of_film]['hulu'] = []
    return initial_ranges_dict


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


def netflix_to_app_date_difference(the_dictionary_ranges, app_dictionary, netflix_title, world_wide_release,
                                   netflix_date_difference,
                                   film_type):
    if netflix_title in app_dictionary and app_dictionary[netflix_title][3] == world_wide_release and \
            app_dictionary[netflix_title][0] == film_type:
        other_app_date_difference = app_dictionary[netflix_title][1]
        if app_dictionary[netflix_title][1] != 'unknown':
            rel_dates_between_apps = int(netflix_date_difference - other_app_date_difference)
        else:
            rel_dates_between_apps = 'unknown'
        app_dictionary[netflix_title].pop(1)
        app_dictionary[netflix_title].insert(1, rel_dates_between_apps)
        adding_lists_to_dict(the_dictionary_ranges, app_dictionary[netflix_title], rel_dates_between_apps)
    return the_dictionary_ranges


def streaming_programs(the_dictionary_ranges, file, streaming_app_name):
    with open(file, 'r', encoding='utf-8') as app:
        app_dictionary = {}
        app.readline()
        reader = csv.reader(app)
        for line in reader:
            movie_or_show = line[1]
            title = line[2]
            app_rel = line[6].split()
            global_rel = line[7]
            if len(app_rel) == 0:
                for i in range(3):
                    app_rel.append('unknown')

            date_difference = calculate_date_difference(app_rel, global_rel)
            if streaming_app_name == 'netflix':
                netflix_to_app_date_difference(the_dictionary_ranges, amazon_movies, title, global_rel, date_difference,
                                               movie_or_show)
                netflix_to_app_date_difference(the_dictionary_ranges, disney_plus_movies, title, global_rel,
                                               date_difference,
                                               movie_or_show)
                final_dict = netflix_to_app_date_difference(the_dictionary_ranges, hulu_movies, title, global_rel,
                                                            date_difference,
                                                            movie_or_show)
            else:
                app_dictionary[title] = []
                app_dictionary[title].append(movie_or_show)
                app_dictionary[title].append(date_difference)
                for index_of_data in column_list:
                    app_dictionary[title].append(line[index_of_data])
                app_dictionary[title].append(title)
                app_dictionary[title].append(streaming_app_name)
        if streaming_app_name == 'netflix':
            return final_dict
        return app_dictionary


def adding_lists_to_dict(the_dictionary_ranges, content_list, release_date_range):
    if '-' in str(release_date_range) and release_date_range < 0:
        the_dictionary_ranges['released after netflix'][content_list[0]][content_list[-1]].append(content_list)
    elif str(release_date_range).isdigit() and release_date_range >= 0 and release_date_range <= 10:
        the_dictionary_ranges['0_10'][content_list[0]][content_list[-1]].append(content_list)
    elif str(release_date_range).isdigit() and release_date_range >= 11 and release_date_range <= 30:
        the_dictionary_ranges['11_30'][content_list[0]][content_list[-1]].append(content_list)
    elif str(release_date_range).isdigit() and release_date_range >= 31 and release_date_range <= 90:
        the_dictionary_ranges['31_90'][content_list[0]][content_list[-1]].append(content_list)
    elif str(release_date_range).isdigit() and release_date_range >= 91 and release_date_range <= 180:
        the_dictionary_ranges['91_180'][content_list[0]][content_list[-1]].append(content_list)
    elif str(release_date_range).isdigit() and release_date_range >= 181 and release_date_range <= 365:
        the_dictionary_ranges['181_365'][content_list[0]][content_list[-1]].append(content_list)
    elif str(release_date_range).isdigit() and release_date_range >= 366:
        the_dictionary_ranges['365+'][content_list[0]][content_list[-1]].append(content_list)
    elif release_date_range == 'unknown':
        the_dictionary_ranges['unknown'][content_list[0]][content_list[-1]].append(content_list)
    return the_dictionary_ranges


column_list = [6, 7, 3, 5, 8, 9]
month_after = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
               'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

all_ranges_in_dict = dictionary_of_date_ranges()

amazon_movies = streaming_programs(all_ranges_in_dict, 'amazon_prime_titles.csv', 'amazon')
disney_plus_movies = streaming_programs(all_ranges_in_dict, 'disney_plus_titles.csv', 'disney')
hulu_movies = streaming_programs(all_ranges_in_dict, 'hulu_titles.csv', 'hulu')
netflix_and_other_app_date_comparison = streaming_programs(all_ranges_in_dict, 'netflix_titles.csv', 'netflix')

print(netflix_and_other_app_date_comparison)
