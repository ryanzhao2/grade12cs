import glob
import csv
dict = {}
all_spotify_files = glob.glob('regional*.csv')

for file in all_spotify_files:
    with open(file) as spotify_file:
        spotify_file.readline()
        spotify_file.readline()
        reader = csv.reader(spotify_file)
        for line in reader:
            if line[1] not in dict:
                str = f'{line[1]} by {line[2]}'
                dict[str] = {}
            elif {line[1]} by {line[2]} in dict:
                str = f'{line[1]} by {line[2]}'

                print(dict[str])
print(dict)
