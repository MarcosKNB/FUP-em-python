a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    if a == b and a == c:
        print ('Triangulo equilatero')
    elif a == b or b == c or c == a:
        print ('Triangulo isosceles')
    elif a != b and b != c and a != c:
        print ('Triangulo escaleno')
else:
    print ('Nao triangulo')