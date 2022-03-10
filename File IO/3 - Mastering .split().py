with open('university_programs.txt') as universities_file:
    main_list = []
    for line in universities_file:
        list = []
        strip_list = line.strip().split(', ')
        uni_name = strip_list[0].strip(' ')
        first_part = uni_name.split(' ')
        province = strip_list[2].split(':')
        province = province[0]
        province = province.replace(' ', '', 1)
        city = strip_list[1]
        city = city.replace(' ', '', 1)
        if first_part[0] != 'University':
            list.append(first_part[0])
        else:
            list.append(uni_name)
        list.append(city)
        list.append(province)
        list.append(strip_list[3])
        main_list.append(list)
    for char in main_list:
        print(char)




