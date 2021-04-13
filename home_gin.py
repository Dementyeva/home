def by_one(names):
    for i in names:
        yield i

names = by_one(['Sofi','Maria','Petia','Vasya'])
next_names = by_one(names)

print(next(names))
print(next_names.__next__())
next_names.send('nextone')


