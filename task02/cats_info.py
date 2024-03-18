def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                cat_id, cat_name, cat_age = line.strip().split(',')
                cats_info.append({'id': cat_id.strip(), 'name': cat_name.strip(), 'age': cat_age.strip()})
    except FileNotFoundError as e:
        print(f"File not found {path}. Error: {e}")
        return None
    except ValueError as e:
        print(f"An error occurred while reading the file {path}. Error: {e}")
        return None

    return cats_info


path = 'cats_file.txt'
cats_info = get_cats_info(path)
print(f"Cats information: {cats_info}")

