def open_file(my_year):
    """
    (str) -> list
    :param my_year: the year of films we want to be shown on the map
    :return: list of lists with movies of year we take as param
    """
    with open('locations.list', 'r', encoding='utf-8', errors="ignore") as f:
        contents = f.readlines()
        parser = set()
        for line in contents[15:]:
            #
            line = line.split('\t')
            if line[-1].startswith('('):
                line.remove(line[-1])
            del line[1:-1]
            if '(' in line[0]:
                x = line[0].index('(')
                line += ["".join(line[0][x + 1:x + 5])]
                line[0] = line[0].replace(line[0][x - 1:], "")
            if my_year in line:
                for i in range(line[0].count("'")):
                    line[0] = line[0].replace("'", "")
                parser.add(tuple(line))
        return parser


