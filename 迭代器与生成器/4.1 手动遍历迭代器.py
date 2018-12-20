def manual_iter():

    with open('test') as f:
        try:
            while True:
                line = next(f)
                print(line)
        except StopIteration:
            pass

manual_iter()

