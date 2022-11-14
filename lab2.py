#Utwórz funkcję, która otrzyma w parametrze listę 5 imion,
# a następnie wyświetli każde z nich.

def zad2a(imiona: list):
    for i in imiona:
        print(i)

if __name__ == '__main__':
    imiona = ['Olo', 'Bolo', 'Kolo', 'Ala', 'Ola']
    zad2a(imiona)

#Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5 dowolnych liczb,
#każdy jej element pomnoży przez 2, a na końcu ją zwróci.
#a Wykorzystując pętle for

def zad2ba(numbers: list):
    for n in range(len(numbers)):
        numbers[n] = numbers[n]*2
    return numbers

if __name__ == '__main__':
    lista = [1, 2, 5, 4, 6]
    print(zad2ba(lista))

#b wykorzystując listę składaną

def zad2bb (numbers: list):
    multiplication = [x*2 for x in numbers]
    return multiplication

if __name__ == '__main__':
    liczby = [1, 8, 3, 4, 6]
    print(zad2bb(liczby))

#Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
# a następnie wyświetli jedynie parzyste elementy.

def zad2c (numbers: list):

    for n in range(len(numbers)):
        if numbers[n] % 2 == 0:
            print(numbers[n])

if __name__ == '__main__':
    liczby = [1, 8, 3, 4, 6, 7, 10, 12, 1, 2]
    zad2c(liczby)

#Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
# a następnie wyświetli co drugi element.
def zad2d (numbers: list):

    for n in range(len(numbers)):
        if n % 2 == 0:
            co_druga_liczba.append(numbers[n])
    print(co_druga_liczba)

if __name__ == '__main__':
    co_druga_liczba = []
    liczby = [1, 8, 3, 4, 6, 7, 10, 12, 1, 2]
    zad2d(liczby)


