import json

def read_file():
    file_path = "in/ratings-movies.json"

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            print("File read with sucess")
        
    except FileNotFoundError:
        print("File not found")
        exit(1)
    except Exception as e:
        print(f"Something went wrong: {e}")
        exit(1)
        
def main():     
    read_file()

if __name__ == "__main__":
    main()
    
