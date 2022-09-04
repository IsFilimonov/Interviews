def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "{} likes this".format(*names)
    elif len(names) == 2:
        return "{} and {} like this".format(*names)
    elif len(names) == 3:
        return "{}, {} and {} like this".format(*names)
    else:
        return "{}, {} and {} others like this".format(names[0], names[1], len(names)-2)