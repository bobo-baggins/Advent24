def Report_Review():
    with open("Advent_2.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line)

if __name__ == "__main__":
    Report_Review()  