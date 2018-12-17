text = 'hello world'
print(text.ljust(20))

print(text.rjust(20))

print(text.center(20))

print(text.ljust(20, '*'))

print(text.rjust(20, '*'))

print(text.center(20, '*'))

print(format(text, '>20'))

print(format(text, '<20'))

print(format(text, '=>20s'))

print(format(text, '*^20s'))

print(
    '{:>10s}{:>10s}'.format('hello', 'world')
)

