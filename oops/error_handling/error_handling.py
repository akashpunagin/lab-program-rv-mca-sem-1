existing_file_name = input("Enter existing file name: ")
new_file_name = input("Enter new file name: ")

try:
    existing_file = open(existing_file_name, "r")
    content = existing_file.read()

    print(f"\nContent of the file {existing_file_name} is:\n{content}")

    new_file = open(new_file_name, "w")
    new_file.write(content)
    print(f"Successfully copied content from {existing_file_name} to {new_file_name}\n")

    #print(1/0) # zero division error
    
    #dct = {"name": "Raju"} # key error
    #print(dct["age"])

except FileNotFoundError:
    print("The file was not found in present working directory")
except ValueError:
    print("Some value does not match with the key")
except NameError:
    print("Name error has occured")
except EOFError:
    print("End of flie error has occured")
except IOError:
    print("Some input/output error has occured")
except ZeroDivisionError:
    print("You are trying to divide a number by 0")
except KeyError:
    print("The key is not present in the dictionary")
except:
    print("An exception other than mentioned has occured")
finally:
    print("\nClosing the files")
    existing_file.close()
    new_file.close()
    print("File closed")
