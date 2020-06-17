vector = []

command = "size"
while command != "end":
    command = input()
    if "push" in command:
        vector.append(int(input()))
        continue
    elif command == "size":
        print(len(vector))
        continue
    elif command == "pop":
        vector.pop
        continue
    elif command == "clear":
        vector.clear()
        continue
    elif command == "front":
        print(vector[0])
        continue
    elif command == "back":
        print(vector[-1])
        continue
    elif command == "end":
        break