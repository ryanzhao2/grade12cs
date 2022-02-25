from tkinter import *
import time, random


def convert_star_datatypes(line):
    '''Function returns a copy of given list with all values changed to float.'''
    temp = []
    for i in range(0, 6):
        temp.append(float(line[i]))
    return temp


def create_star_list(filename):
    '''Return a list of lists. Each list is a star from given file.'''
    star_list = []

    return star_list


def create_named_star_list(filename):
    '''Return a dictionary of lists. Each unique star name is key to star data as list.'''
    with open(filename) as star_file:
        named_stars_dict = {}
        for line in star_file:
            line = line.split(' ',6)
            if len(line) > 6:
                data = line[:6]
                names = line[6].split(',')

                for n in names:
                    named_stars_dict[n.strip()] = data

        return named_stars_dict


def create_constellations(filename):
    '''Return a dictionary of lists. Each unique constellation name is key to list of constellation star pairs.'''
    constellations = {}

    return constellations


def coordinates_to_pixels(x, y):
    '''Translates coordinates to pixels based on 700x700 canvas.'''
    newX = x * 350 + 350
    newY = y * (-350) + 350
    return newX, newY


def draw_stars_oncanvas(cv, star_list):
    for star in star_list:
        coords = coordinates_to_pixels(star[0], star[1])

        cv.create_oval(coords[0], coords[1], coords[0] + 1 * star[4] / 2, coords[1] + 1 * star[4] / 2, fill="white",
                       outline="white")

    cv.update()


def draw_constellation(cv, constellation, named_stars_dict):
    current_colour = random.choice(['coral', 'spring green', 'sky blue', 'ivory2', 'violet red', 'aquamarine'])

    for pair in constellation:
        fromStar = named_stars_dict[pair[0]]
        toStar = named_stars_dict[pair[1]]

        x1, y1 = fromStar[0], fromStar[1]
        x2, y2 = toStar[0], toStar[1]

        x1, y1 = coordinates_to_pixels(x1, y1)
        x2, y2 = coordinates_to_pixels(x2, y2)

        cv.create_oval(x1, y1, x1 + 3, y1 + 3, fill=current_colour, outline=current_colour)
        cv.create_oval(x2, y2, x2 + 3, y2 + 3, fill=current_colour, outline=current_colour)

        cv.create_line(x1, y1, x2, y2, width=2, fill=current_colour)
        cv.update()
        time.sleep(0.25)


def draw_all_constellations(cv, constellations_dict, named_stars, constellation_var):
    for name in constellations_dict:
        current_constellation = constellations_dict[name]
        constellation_var.set(f'Currently drawing ... {name}')

        draw_constellation(cv, current_constellation, named_stars)

    constellation_var.set(f'Done drawing all constellations')


def main():
    root = Tk()
    mainframe = Frame(root)

    star_canvas = Canvas(mainframe, width=700, height=700, bg="gray")
    constellation_var = StringVar()
    constellation_label = Label(mainframe, textvariable=constellation_var)

    mainframe.grid()
    constellation_label.grid(row=1, column=1)
    star_canvas.grid(row=2, column=1)

    # Create data structure for stars
    all_star_list = create_star_list("stars.txt")
    draw_stars_oncanvas(star_canvas, all_star_list)

    # Create data structure for drawing constellations
    named_stars = create_named_star_list("stars.txt")
    constellations_dict = create_constellations("constellations.txt")

    draw_all_constellations(star_canvas, constellations_dict, named_stars, constellation_var)

    root.mainloop()


main()