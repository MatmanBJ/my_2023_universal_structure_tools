# https://stackoverflow.com/questions/13437727/how-to-write-to-an-excel-spreadsheet-using-python
# https://stackoverflow.com/a/13437772
import xlwt
import enum
import sys

# https://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python
# https://stackoverflow.com/a/1319675
class MakeTypeError(Exception):
    pass

# https://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python
# https://stackoverflow.com/a/1319675
class ArgumentError(Exception):
    pass

# https://stackoverflow.com/questions/58608361/string-based-enum-in-python
class makeType(str, enum.Enum):
    movie = "movie"
    series = "series"

def fileRead(file_name):
    # https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html
    unordered_list = []

    # https://pythonz.net/references/named/file.read/
    # https://pythonz.net/references/named/file.readline/
    with open(file_name) as f:
        while True:
            str = f.readline()
            if not str:
                break
            unordered_list.append(str)
        #str = f.read(256) # read 256 symbols
    
    return unordered_list

def makeList(make_type, unordered_list):
    list_name = []
    list_season = []
    list_episode = []
    list_date = []

    if make_type == makeType.movie:
        for l in unordered_list:
            if l != "\n": # check if that's not just an empty string
                # https://stackoverflow.com/questions/69399503/how-to-return-the-last-character-of-a-string-in-python
                # https://stackoverflow.com/a/69399598
                z = 0 # special parameter, if the last real string has or hasn't the "\n" symbol
                if l[-1] == "\n": # has "\n" symbol
                    z = 0
                elif l[-1] != "\n": # hasn't  "\n" symbol
                    z = 1
                else: # default
                    z = 0
                # https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string
                # https://stackoverflow.com/a/7983848
                list_date.append(l[-11 + z:-2 + z] + l[-2 + z]) # if just "-10", it will be "x.xx.xxxx\n" (without 1st number and with "\n" in the end)
                list_name.append(l[0:-12 + z]) # if just "-11", it will be "name " (with space between date and name in the end)
    elif make_type == makeType.series:
        for l in unordered_list:
            if l != "\n": # check if that's not just an empty string
                # https://stackoverflow.com/questions/69399503/how-to-return-the-last-character-of-a-string-in-python
                # https://stackoverflow.com/a/69399598
                z = 0 # special parameter, if the last real string has or hasn't the "\n" symbol
                if l[-1] == "\n": # has "\n" symbol
                    z = 0
                elif l[-1] != "\n": # hasn't  "\n" symbol
                    z = 1
                else: # default
                    z = 0
                # https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string
                # https://stackoverflow.com/a/7983848
                list_date.append(l[-11 + z:-2 + z] + l[-2 + z])
                # https://stackoverflow.com/questions/642154/how-do-i-convert-all-strings-in-a-list-of-lists-to-integers
                # https://stackoverflow.com/a/642169
                list_episode.append(int(l[-14 + z:-12 + z]))
                list_season.append(int(l[-17 + z:-15 + z]))
                list_name.append(l[0:-19 + z])
    else:
        # https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python
        # https://stackoverflow.com/a/24065533
        raise MakeTypeError("No suitable type for making excel function!")

    #print(list_name)
    #print(list_season)
    #print(list_episode)
    #print(list_date)

    return list_name, list_season, list_episode, list_date

# https://stackoverflow.com/questions/13437727/how-to-write-to-an-excel-spreadsheet-using-python
# https://stackoverflow.com/a/13437772
def makeExcel(make_type, excel_name, sheet_name, list_name, list_season, list_episode, list_date):
    """
    :param make_type: type for making excel -- movie or series
    :param excel_name: excel file name
    :param sheet_name: excel sheet name (inside excel file)
    :param list_name: list with movie/series name (for all)
    :param list_season: list with series name (for series only)
    :param list_episode: list with series episode (for series only)
    :param list_date: list with movie/series viewing date (for all)
    :raises MakeTypeError: no suitable type for making excel function error
    """
    book = xlwt.Workbook()
    sh = book.add_sheet(sheet_name)

    column_list_name = "Name"
    column_list_season = "Season"
    column_list_episode = "Episode"
    column_list_date = "Date"

    n = 0 # initializing variable for numbering rows/columns
    
    if make_type == makeType.movie:
        sh.write(n, 0, column_list_name)
        sh.write(n, 1, column_list_date)

        for m, e1 in enumerate(list_name, n + 1):
            sh.write(m, 0, e1)

        for m, e2 in enumerate(list_date, n + 1):
            sh.write(m, 1, e2)
    elif make_type == makeType.series:
        sh.write(n, 0, column_list_name)
        sh.write(n, 1, column_list_season)
        sh.write(n, 2, column_list_episode)
        sh.write(n, 3, column_list_date)

        for m, e1 in enumerate(list_name, n + 1):
            sh.write(m, 0, e1)

        for m, e2 in enumerate(list_season, n + 1):
            sh.write(m, 1, e2)

        for m, e3 in enumerate(list_episode, n + 1):
            sh.write(m, 2, e3)

        for m, e4 in enumerate(list_date, n + 1):
            sh.write(m, 3, e4)
    else:
        # https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python
        # https://stackoverflow.com/a/24065533
        raise MakeTypeError("No suitable type for making excel function!")

    book.save(excel_name)

# https://stackoverflow.com/questions/4041238/why-use-def-main
# https://stackoverflow.com/a/4041253
def main():
    """
    :raises ArgumentError: incorrect argument error
    """
    # https://stackoverflow.com/questions/60224065/how-to-use-sys-argv
    # https://stackoverflow.com/a/60224680
    if len(sys.argv) >= 3:
        # https://stackoverflow.com/questions/1009860/how-can-i-read-and-process-parse-command-line-arguments
        # https://stackoverflow.com/a/1009879
        if sys.argv[1] == "-t" or sys.argv[1] == "--type":
            if sys.argv[2] == "movie":
                unordered_list = fileRead("movie.txt")
                list_name, list_season, list_episode, list_date = makeList(makeType.movie, unordered_list)
                makeExcel(makeType.movie, "list_to_excel_movie.xls", "list_to_excel_movie", list_name, None, None, list_date)
            elif sys.argv[2] == "series":
                unordered_list = fileRead("series.txt")
                list_name, list_season, list_episode, list_date = makeList(makeType.series, unordered_list)
                makeExcel(makeType.series, "list_to_excel_series.xls", "list_to_excel_series", list_name, list_season, list_episode, list_date)
            else:
                raise ArgumentError("Incorrect argument \"-t/--type\": expected \"movie\" or \"series\"!")
        else:
            raise ArgumentError("Incorrect argument: expected \"-t/--type\"!")
    else:
        raise ArgumentError("Incorrect argument: expected 3, got " + str(len(sys.argv)) + "!")

if __name__ == "__main__":
    main()
