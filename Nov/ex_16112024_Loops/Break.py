count = 0

while True:
    count+=1
    print(f"This will print at least once. Count = {count}")

    if count == 5:
        continue
    if count >= 7:
        break

