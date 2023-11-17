from PIL import Image, ImageOps

#классы фильтров
class RedFilter:
    def apply(self, image):
        r, g, b = image.split()
        r = r.point(lambda x: x * 2) #подсмотрел реализацию в документации pillow
        new_image = Image.merge("RGB", (r, g, b))
        return new_image
class GreenFilter:
    def apply(self, image):
        r, g, b = image.split()
        g = g.point(lambda x: x * 2)
        new_image = Image.merge("RGB", (r, g, b))
        return new_image
class BlueFilter:
    def apply(self, image):
        r, g, b = image.split()
        b = b.point(lambda x: x * 2)
        new_image = Image.merge("RGB", (r, g, b))
        return new_image
class InversionFilter:
    def apply(self, image):
        new_image = ImageOps.invert(image)
        return new_image

#фильтры => словарь (отдельным файлом не удобно)
filters = {
    1: {"name": "Красный фильтр", "description": "Плавно усиливает красный оттенок на изображении.", "filter": RedFilter()},
    2: {"name": "Зелёный фильтр", "description": "Плавно усиливает зелёный оттенок на изображении.", "filter": GreenFilter()},
    3: {"name": "Синий фильтр", "description": "Плавно усиливает синий оттенок на изображении.", "filter": BlueFilter()},
    4: {"name": "Инверсия", "description": "Инвертирует цвета изображения.", "filter": InversionFilter()}
}

#функция меню фильтров
def printf():
    print("Меню фильтров:")
    for key, value in filters.items():
        print(f"{key}: {value['name']}")
    print("0: Выход")

#функция применения фильтров
def apply_filter(image, filter_info):
    print(filter_info["name"] + ":")
    print(filter_info["description"])
    apply_filter = input("Применить фильтр к картинке? (Да/Нет): ")
    if apply_filter.lower() == "да":
        image = filter_info["filter"].apply(image)
        save_path = input("Сохранить в: ")
        image.save(save_path)
    return image

#главная функция
def main():
    print("Добро пожаловать в консольный фоторедактор Никиты Курмачева!")
    while True:
        path = input("Введите путь к файлу: ")
        try:
            image = Image.open(path).convert("RGB")
            while True:
                printf()
                choose = input("Выберите фильтр (или 0 для выхода): ")
                if choose == "0":
                    break
                choose = int(choose)
                if choose in filters:
                    filter_info = filters[choose]
                    image = apply_filter(image, filter_info)
        except:
            print("Файл не найден. Попробуйте еще раз.")
        another_image = input("Ещё раз? (Да/Нет): ")
        if another_image.lower() == "нет":
            break
    print("До свидания!")

main() #можно еще через if __name__=="__main__": main()