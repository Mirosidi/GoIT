import os

def get_cats_info(path):
    cats_info = []
    file_path = os.path.join(os.path.dirname(__file__), path)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cats_info.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return cats_info

path = "path.txt"
cats_info = get_cats_info(path)
print(cats_info)
