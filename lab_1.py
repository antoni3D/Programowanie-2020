print('hello world')

a = float(input("Podaj liczbe 1"))
b = float(input("Podaj liczbe 2"))

print("Suma wynosi: ",a+b)
print("Roznica wynosi: ", a-b)
print("Iloczyn wynosi: ", a*b)
print("Iloraz wynosi: ", a/b)


print("1 - dodawanie 2 - odejmowanie 3- mnozenie 4 - dzielenie")
choice = int(input("Co wybierasz?"))
match(choice):
  case 1:print("Suma wynosi: ",a+b)
  case 2:print("roznica wynosi: ",a-b)
  case 3:print("Iloczyn wynosi: ",a*b)
  case 4:print("Iloraz wynosi: ",a/b)
  default:print("Zle podales")
