def funkcia():
    while True:
        try:
          a=int(input('a '))
          b=int(input('b'))
          break
        except ValueError:
            print('Введите число')
    while b==0:
        b=int(input('b ne 0'))
    x=a**2/b
    print(x)
funkcia()