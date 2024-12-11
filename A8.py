def ProcessGrid(FileName, AntennasLocations):
    grid_height = 0
    grid_width = 0
    
    with open(FileName, 'r') as file:
        lines = file.readlines()
        grid_height = len(lines)
        grid_width = len(lines[0].strip())  # Use first line's width
        
        for i, line in enumerate(lines):
            line = line.strip()  # Remove whitespace/newlines
            for j, char in enumerate(line):
                if char == ".":
                    continue
                if char not in AntennasLocations:
                    AntennasLocations[char] = []
                AntennasLocations[char].append((i+1, j+1))
#    print(AntennasLocations)
    return AntennasLocations, grid_height, grid_width

def CalcAntinode(AntennasLocations, height, width):
    #intialize Antinode dictionary with key from antennas dict, so each frequnecy will be a key with locations of antinodes as values
    AntinodeLocations = dict.fromkeys(AntennasLocations.keys(),[])

    for key in AntennasLocations.keys():
        #print(key)
        #Intialize or clear a list to record all possible antenna pairs for each frequency (key)
        AntennaPairs = []
        locations = AntennasLocations[key]
        for i in range(len(locations)):
            for j in range(i+1, len(locations)):
                AntennaPairs.append((locations[i], locations[j]))
        
        #Calc location for antinode, check if in grid and store in AntinodeLocation dict
        for Pair in AntennaPairs:
            print(Pair)
            dx = Pair[0][0]-Pair[1][0]
            dy = Pair[0][1]-Pair[1][1]
            print(f"Diff is , ({dx},{dy})") 
            #Calc both antinodes and make it's within the grid
            antinode1 = Pair[0][0] + dx, Pair[0][1] + dy
            if antinode1[0] > 0 and antinode1[0] <= height:
                if antinode1[1] >0 and antinode1[1] <= width:
                    AntinodeLocations[key].append(antinode1)
            
            antinode2 = Pair[1][0] - dx, Pair[1][1] - dy
            if antinode2[0] >0 and antinode2[0] <= height:
                if antinode2[1] >0 and antinode2[1] <= width:
                    AntinodeLocations[key].append(antinode2)
            print(f"Antinode locations are, {antinode1} & {antinode2}")
    return AntinodeLocations    

def Main():
    #FileName = "A8_Test.txt"
    FileName = "A8_Input.txt"
    AntennasLocations = {}
    AntinodeLocations = {}

    AntennasLocations, height, width = ProcessGrid(FileName, AntennasLocations)
    print(f"Grid size: {height}x{width}")
    print(AntennasLocations)

    AntinodeLocations = CalcAntinode(AntennasLocations, height, width)
    print(AntinodeLocations)
# Assuming your dictionary is AntinodeLocations
    all_tuples = []
    for value_list in AntinodeLocations.values():
        all_tuples.extend(value_list)
    
    unique_count = len(set(all_tuples))  
    print(unique_count)

if __name__ == "__main__":
    Main()


