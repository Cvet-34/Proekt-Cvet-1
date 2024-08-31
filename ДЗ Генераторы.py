def all_variants(text):
    a = text
    for i in a:
        yield i
    for j in a:
        if j != i:
            yield j + i
    yield a


a = all_variants("abc")
for i in a:
    print(i)

