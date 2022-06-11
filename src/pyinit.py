import os

print(os.getcwd())
path = input("Please enter the path\n")
project_name = input("Please enter project name\n")
project_name = project_name.replace(" ","-")  # Replaces spaces with dashes
os.chdir(path)  #Changes current working directory to the path provided
os.mkdir(project_name)  #Creates folder with project name
path = path+"/"+project_name
os.chdir(path)  #Changes current working directory to the folder created
os.system("git init")  #Initializes git repository
os.mkdir("assets")
print("Assets folder created")  #Creates assets folder
os.mkdir("src")
print("src folder created")  #Creates src folder
myfile = open("README.md","w")  #Creates README file
myfile.write(f"## {project_name.replace('-',' ')}")  #Writes project name in h2 in README file. Spaces are allowed.
myfile.close()
print("README file created")
myfile = open("requirements.txt","w")  #Creates requirements file
myfile.close()
print("requirements file created")
myfile = open(".gitignore","w")  #Creates gitignore file
myfile.close()
print("gitignore file created")
path = path+"/src"
os.chdir(path)  #Moves into the src folder
content = """#imports

def main():
    print("Main Begins")

if __name__ == "__main__":
    main()
 """

myfile = open(f"{project_name}.py","w")  #Creates empty python file with project name
myfile.write(content)
myfile.close()
print(f"{project_name}.py file created")
print("All Done!")
