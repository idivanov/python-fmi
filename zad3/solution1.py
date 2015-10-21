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
    generators_ = {"fibonacci": fibonacci(),
                    "primes": primes()}

    for generator in generators:
        arguments = dict([[key, value] for key, value in generator.items() if key != "sequence" and key != "length"])
        
        if generator["sequence"] == "alphabet":
            if generator["sequence"] not in generators_.keys():
                generators_[generator["sequence"]] = alphabet(**arguments)

        if kwargs is not None and "generator_definitions" in kwargs.keys() and generator["sequence"] in kwargs["generator_definitions"]:
            if generator["sequence"] not in generators_.keys():
                generators_[generator["sequence"]] = kwargs["generator_definitions"][generator["sequence"]](**arguments)
        
        for _ in range(generator["length"]):
            yield next(generators_[generator["sequence"]])

            
            
            
            
            
            
            
            