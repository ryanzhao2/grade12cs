def parse_braille_file(filename):
    with open(filename) as braille_file:
        for line in braille_file:
            py