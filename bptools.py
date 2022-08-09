# BoxPile Tools

def formatStringList(string_list: list) -> str:
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


def formatIntegerList(integer_list: list) -> str:
    # TODO(Erton): Needs coding
    pass


def environmentEncryption(environment_variable) -> str:
    # TODO(Erton): Needs coding
    pass


def environmentDecryption(environment_variable) -> str:
    # TODO(Erton): Needs coding
    pass
