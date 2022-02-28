with open('university_programs.txt') as universities_file:
    for line in universities_file:
        line = line.strip().split(', ')
        new_list = []
        #print(line[0].split())
        format_name = line[0].split()
        if format_name[0] not in 'University':
            new_list.append(format_name[0])
        elif format_name[0] in 'University':
            new_list.append(format_name[2])
        a = line[1].strip()
        new_list.append(a)
        b = line[2].strip().split(':  ')
        new_list.append(b[0])
        new_list.append(b[1])
        for i in range(3, len(line)):
            new_list.append(line[i].strip())
        new_list = ("[{}]".format(",".join(map(repr, new_list))))
        print(new_list)


