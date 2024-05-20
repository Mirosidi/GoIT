def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cats_info.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError:
        print(f"File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return cats_info

cats_info = get_cats_info("D:/Python/GoIT/path.txt")
print(cats_info)