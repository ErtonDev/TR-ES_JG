# BoxPile Tools
import cProfile
import pstats
import string
import io



alphabet = list(string.ascii_lowercase)



def profile(fnc):
    # Profiling decorator for optimization

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner


def format1DList(string_list: list) -> str:
    index_counter = 0
    max_index = len(string_list) - 1

    result = "'{"

    for i in string_list:
        if index_counter != max_index:
            result += '"' + i + '",'
        else:
            result += '"' + i + '"'

        index_counter += 1

    result += "}'"

    return result


def format2DList(string_list: list) -> str:
    super_counter = 0
    max_super = len(string_list) - 1

    result = "'{"

    for i in string_list:
        index_counter = 0
        max_index = len(i) - 1

        result += "{"

        for j in i:
            if index_counter != max_index:
                result += '"' + j + '",'
            else:
                result += '"' + j + '"'

            index_counter += 1

        if super_counter != max_super:
            result += "},"
        else:
            result += "}"

        super_counter += 1

    result += "}'"

    return result


def venvDecryption(venv: str) -> str:
    result = ""

    for char in venv:
        if char in alphabet:
            for item in alphabet:
                if char == item:
                    item_pos = alphabet.index(item)

                    if char == alphabet[0]:
                        new_pos = 24
                    elif char == alphabet[1]:
                        new_pos = 25
                    else:
                        new_pos = item_pos - 2

                    result += alphabet[new_pos]
        else:
            result += char

    return result
