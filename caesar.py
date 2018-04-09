from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    a = ''
    b = (int(rot))
    for i in text:
        a = a + (rotate_character(i, b))
    return a
def main():
    d = input('Type a message:')
    g = input('Rotate by:')
    hh = int(g)
    print(encrypt(d, hh))

if __name__ == "__main__":
    main()
