# take input
alph = input('enter alphabet:')

# check codition
if len(alph) == 1 and alph.isalpha():
    if alph in ['a', 'e', 'i', 'o', 'u']:
        print(f'{alph} is vowel.')
    else:
        print(f'{alph} is consonant.')
else:
    print("invalid input")
