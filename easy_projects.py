inputs = []
for i in range (10):
    value = int(input(f"Enter value{i+1} :"))
    inputs.append(value)

even_count = 0
odd_count = 0 

for i in inputs:
    if i % 2 == 0:
        even_count +=1
    else:
        odd_count +=1

print("even_number :", even_count)
print("odd_number :", odd_count)
