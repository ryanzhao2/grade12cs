# import glob
# import csv
# dict = {}
# all_spotify_files = glob.glob('regional*.csv')
# for file in all_spotify_files:
#     with open(file) as spotify_file:
#         spotify_file.readline()
#         spotify_file.readline()
#         reader = csv.reader(spotify_file)
#         for line in reader:
#             #print(file[18:28])
#             str = f'{line[1]} by {line[2]}'
#             if str not in dict:
#                 dict[str] = {}
#                 dict[str][file[18:28]] = line[3]
#             else:
#                 dict[str][file[18:28]] = line[3]
# print(dict)
