animals=["ant","bear","cat","dog","elephant","fish","goat","hippo"]
print(f'list of animals: {animals}')
print(f'Number of animals: {len(animals)}')
while True: 
    animal = input('I want to find:\n')
    if animal in animals:
        print(f'there is {animal} in list of animals')
        break
    else:
        print(f'Con {animal} không có trong danh sách động vật của chúng tôi\nBạn chọn lại please!')
