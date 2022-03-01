def abbrev_name(name):
    names = name.split()
    initials = []
    for n in names:
        print(n)
        initials.append(n[0].upper())
    result = '.'.join(initials)
    print(result)


abbrev_name("Sam Harris")


def abbrev_name_2(name):
    return '.'.join(w[0] for w in name.split()).upper()


abbrev_name_2("Sam Harris")
