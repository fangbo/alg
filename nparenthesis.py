

def compute(layer):

    values = set(['()'])

    i = 1
    while i < layer:
        new_values = set([])

        for item in values:
            new_values.add('(%s)' % item)
            new_values.add('()%s' % item)
            new_values.add('%s()' % item)

        i += 1

        values = new_values

    return values


if __name__ == "__main__":
    print compute(5)
