def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def primes():
    primes = []
    last = 1
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last


def alphabet(**kwargs):
    if 'letters' in kwargs.keys():
        return iter(kwargs['letters'])

    if kwargs['code'] == "lat":
        return iter("abcdefghijklmnopqrstuvwxz")

    if kwargs['code'] == "bg":
        return iter("абвгдежзийклмнопрстуфхцчшщъьюя")


def multiples_of(num):
    i = 1
    while True:
        yield num * i
        i += 1


def naturals():
    number = 1
    while True:
        yield number
        number += 1


def ones():
    while True:
        yield 1


def intertwined_sequences(generators, **kwargs):
    fibonacci_ = fibonacci()
    primes_ = primes()
    alphabet_ = None
    generators_ = {}

    for generator in generators:
        if generator["sequence"] == "fibonacci":
            for _ in range(generator["length"]):
                yield next(fibonacci_)

        if generator["sequence"] == "primes":
            for _ in range(generator["length"]):
                yield next(primes_)

        if generator["sequence"] == "alphabet":
            if alphabet_ is None:
                if "letters" in generator.keys():
                    alphabet_ = alphabet(letters=generator["letters"])
                if "code" in generator.keys():
                    alphabet_ = alphabet(code=generator["code"])
            for _ in range(generator["length"]):
                yield next(alphabet_)

        if kwargs is not None and\
            "generator_definitions" in kwargs.keys() and\
                generator["sequence"] in kwargs["generator_definitions"]:
            arguments = dict([[key, value] for key, value
                             in generator.items()
                             if key != "sequence" and key != "length"])
            if generator["sequence"] not in generators_.keys():
                if len(arguments) == 0:
                    generators_[generator["sequence"]] =\
                        kwargs["generator_definitions"]\
                        [generator["sequence"]]()
                else:
                    generators_[generator["sequence"]] =\
                        kwargs["generator_definitions"]\
                        [generator["sequence"]](**arguments)
            for _ in range(generator["length"]):
                yield next(generators_[generator["sequence"]])
