import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        """Геттер для получения списка товаров в чеке."""
        return self.__name_items

    @property
    def number_items(self):
        """Геттер для получения количества товаров в чеке."""
        return self.__number_items

    def add_item_to_cheque(self, name):
        """Добавляет товар в чек."""
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        self.__name_items.append(name)
        self.__number_items += 1

    def delete_item_from_check(self, name):
        """Удаляет товар из чека."""
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        self.__name_items.remove(name)
        self.__number_items -= 1

    def check_amount(self):
        """Считает общую сумму покупок со скидкой при необходимости."""
        total = []
        for item in self.__name_items:
            total.append(self.__item_price[item])
        amount = sum(total)
        if self.__number_items > 10:
            amount *= 0.9  # скидка 10 %
        return amount

    def twenty_percent_tax_calculation(self):
        """Рассчитывает НДС для товаров со ставкой 20 % с учётом скидки."""
        twenty_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate.get(item) == 20:
                twenty_percent_tax.append(item)
                total.append(self.__item_price[item])
        base_amount = sum(total)
        # Применяем скидку, если товаров больше 10
        if self.__number_items > 10:
            base_amount *= 0.9
        return base_amount * 0.2

    def ten_percent_tax_calculation(self):
        """Рассчитывает НДС для товаров со ставкой 10 % с учётом скидки."""
        ten_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate.get(item) == 10:
                ten_percent_tax.append(item)
                total.append(self.__item_price[item])
        base_amount = sum(total)
        # Применяем скидку, если товаров больше 10
        if self.__number_items > 10:
            base_amount *= 0.9
        return base_amount * 0.1

    def total_tax(self):
        """Возвращает общую сумму НДС по чеку."""
        tax_20 = self.twenty_percent_tax_calculation()
        tax_10 = self.ten_percent_tax_calculation()
        return tax_20 + tax_10

    @staticmethod
    def get_telephone_number(telephone_number):
        """
        Возвращает номер телефона покупателя.

        Args:
            telephone_number: 10 цифр после +7

        Returns:
            str: полный номер телефона в формате +7XXXXXXXXXX

        Raises:
            ValueError: если передан нецелочисленный аргумент или длина не равна 10 символам
        """
        # Проверяем, что аргумент является числом
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')


        # Преобразуем в строку для подсчёта длины и форматирования
        telephone_str = str(telephone_number)

        # Проверяем длину — должно быть ровно 10 цифр
        if len(telephone_str) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')

        # Формируем полный номер в формате +7XXXXXXXXXX с помощью f‑строки
        full_number = f'+7{telephone_str}'
        return full_number
