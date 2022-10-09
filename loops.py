lst2=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
eng_rus_dict={
    "cat": "кот",
    "car": "машина "
}

for item in lst2:
    print(item)
print("-"*10)

print(range(10))
print(list(range(10)))
for i in range(10):
    if i==1:
        continue
    if i==5:
        break
    print(i)

cats= ["Barsik", "Murzic", "Vasilya"]
print(list(enumerate(cats)))
for idx,cat in enumerate(cats):
    print(f"{idx}.{cat}")


print(list(reversed(cats)))
print(list(sorted(cats)))

for key,value in eng_rus_dict.items():
    print("key", key, "value", value)
i=0
while i!=5:
    i+=1
print(i)

print("а", ord("а"))
symbol_number=ord("а")
while symbol_number <= ord("я"):
    print(symbol_number, chr(symbol_number))
    symbol_number+=1 

