import os

def concatenate_data_files():
    
    files = os.listdir()

    
    with open("concatenated_data.bin", "wb") as output_file:
        
        for file_name in files:
            if file_name.endswith(".data"):  
                with open(file_name, "rb") as input_file:
                    
                    output_file.write(input_file.read())

    print("Data from .data files has been concatenated into concatenated_data.bin")


concatenate_data_files()