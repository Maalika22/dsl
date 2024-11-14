import rpyc

def main():
    # Connect to the RPyC server
    conn = rpyc.connect("localhost", 18861)
    # Get input from the user
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    # Call the remote method
    result = conn.root.concatenate(str1, str2)
    print(f"The concatenated result is: {result}")

if _name_ == "_main_":
    main()
