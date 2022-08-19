# BoxPile Tools
import cProfile
import pstats
import io



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
