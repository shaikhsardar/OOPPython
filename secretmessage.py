import os

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"F:\Docs\Udacity\Full Stack Web Developement\Python Fundamentals\Secret Message\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir(r"F:\Docs\Udacity\Full Stack Web Developement\Python Fundamentals\Secret Message\prank")
    #(2) for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
rename_files()
    
  #please find sprank folder for sample files original before renamed...
