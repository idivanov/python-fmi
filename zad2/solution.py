def extract_type(unextracted, type_):
    return ''.join([str(pair[0]) * pair[1] for pair in unextracted
                    if type(pair[0]) is type_])


def reversed_dict(_):
    return dict([[value, key] for key, value in _.items()])


def flatten_dict(unflattened):
    def expand(key_, value_):
        if isinstance(value_, dict):
            return [(key_ + '.' + key, value)
                    for key, value in flatten_dict(value_).items()]
        return [(key_, value_)]

    return dict([item for key, value in unflattened.items()
                for item in expand(key, value)])


def unflatten_dict(flattened, result=None):
    if result is None:
        result = {}

    for element in flattened:
        if '.' in element:
            if element.split('.')[0] in result:
                result[element.split('.')[0]] = unflatten_dict(
                    {element[len(element.split('.')[0]) + 1:]:
                        flattened[element]},
                    result[element.split('.')[0]])
            else:
                result[element.split('.')[0]] = unflatten_dict(
                    {element[len(element.split('.')[0]) + 1:]:
                        flattened[element]},
                    {})
        else:
            result[element] = flattened[element]

    return result


def reps(elements):
    return tuple([_ for _ in elements if elements.count(_) > 1])
