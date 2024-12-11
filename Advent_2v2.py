def Report_Review():
    with open("Advent_2_input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line)

if __name__ == "__main__":
    Report_Review()  