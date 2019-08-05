# Ahriman

def score(name):
    total = 0

    for char in name:
        total += (ord(char) - 64) # scale so A = 1, B = 2...

    return total

def main():
    # Open the names file for reading
    infile = open('names.txt', 'r')

    # Read the entire contents of the file
    file_contents = infile.read()

    # Close the file
    infile.close()

    # Convert file contents to a list of quoted names and sort them
    list_of_names = file_contents.split(',')
    list_of_names.sort()

    position = 1
    total = 0
    for name in list_of_names:
        name = name.strip('"') # strip the quotes from names individually
        total += score(name) * position
        position += 1

    print(total)

if __name__ == "__main__":
    main()