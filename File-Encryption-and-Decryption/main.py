#
# Jay 
# 4/26/2025
# File Encryption and Decryption Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

def process_file(input_file, output_file, key, mode):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                processed_line = ''.join(
                    chr((ord(char) + key) % 256) if mode == 'encrypt' else chr((ord(char) - key) % 256)
                    for char in line
                )
                outfile.write(processed_line)
        print(f"File '{input_file}' has been {mode}ed and saved as '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
def main():
    print("File Encryption and Decryption Program")
    while True:
        choice = input("1. Encrypt a file\n2. Decrypt a file\n3. Exit\nEnter your choice: ").strip()
        if choice in ['1', '2']:
            input_file = input("Enter the input file name: ").strip()
            output_file = input("Enter the output file name: ").strip()
            key = int(input("Enter the key (integer): ").strip())
            mode = 'encrypt' if choice == '1' else 'decrypt'
            process_file(input_file, output_file, key, mode)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
# Call the main function.
if __name__ == "__main__":
    main()
