# Приложение для кафе.

## Техническое задание:

1. Веб-приложение на Django для управления заказами в кафе.
2. Использовать базу данных SQLite для хранения информации о заказах, меню и пользователях.
3. Приложение должно позволять добавлять, удалять, искать, изменять и отображать заказы.
4. Реализуйте фронтенд с использованием Django templates для отображения меню и обработки заказов.
5. Для удобства работы персонала используется фронтенд с использованием Django templates.

----------------------------------------------------------------------
## Требования:

    Python==3.12
    Django==4.2.1
    asgiref==3.8.1
    sqlparse==0.5.3
    Pillow==11.1.0
    tzdata==2025.1
    и их зависимости (requirements.txt)

----------------------------------------------------------------------
## Запуск приложения

Создать виртуальное окружение:

    python -m venv venv

Активировать виртуальное окружение(Windows):

    .venv\Scripts\activate.bat

Скачать программу:

    git clone https://github.com/Liliya-Sh/order_management_system.git

При необходимости обновите: 

    python -m ensurepip --upgrade 

    python -m pip install --upgrade pip 

    pip install --upgrade setuptools 

Установить зависимости:

    pip install -r requirements.txt    

Супер-пользователь уже есть в БД, если не используется имеющаяся БД.
Создать супер-пользователя:

     python manage.py createsuperuser

Отметить директорию order_management_system как Sources Root, в PyCharm:
- Щелкните правой кнопкой мыши на директории.
- В контекстном меню выберите Mark Directory as (Отметить директорию как).
- Затем выберите Sources Root (Корень исходников).


Запустить программу в консоли PyCharm, подняться на уровень выше в order_managment_system:

    python manage.py runserver

Открыть в браузере(Google Chrome) страницу http://127.0.0.1:8000/
______________________________________________________________________

## Тестирование:

1. Страница Авторизации:

    http://127.0.0.1:8000/

    На самом верху сайта - Главное меню: Меню, Список заказов, Поиск заказа, Выручка.

    Необходимо авторизоваться, неавторизованным другие страницы будут недоступны. Ввести логин и пароль.

  
    По умолчанию 1 пользователь:
 
        - Администратор (username: root, Пароль: 12345)


2.  После авторизации попадаем на главную страницу, тут есть навигатор по разделам из меню: Пицца, Закуски, Напитки, Десерт.
    Можно просмотреть необходимый раздел без прокрутки страницы.

3. Есть Ссылка "Вверх", в правом нижнем углу, если необходимо прокрутить страницу сразу наверх.

4. Можно выбрать количество необходимого товара и добавить его в корзину. 
   Если нажать на изображение картинки, то переходишь на страницу продукта/блюда.

   http://127.0.0.1:8000/menu/product/<slug:product_slug>
 
   Например, если выбрать "Закуски": http://127.0.0.1:8000/menu/product/picca-italyanska/

   На данной странице можно выбрать необходимое количество товара и добавить его в корзину.

5. Корзина находится на главной странице, справа от меню. 
   Можно просмотреть, какие товары были добавлены в корзину, а также сумму заказа.
   Когда покупатель готов сделать заказ, нужно нажать на кнопку "Оформить заказ".

6. Оформление заказа. 
 
    http://127.0.0.1:8000/orders/create/

    В первой части представлен состав корзины, который можно поменять.
    Во второй части необходимо заполнить форму указав номер стола.(указано, что максимум 20 столов)  
    Если поле заполнено верно, нажать "Оформить заказ".
    Появится страница "Ваш заказ был успешно оформлен. Номер вашего заказа ...(id заказа)":

    http://127.0.0.1:8000/orders/create/

7. Можно просмотреть список заказов перейдя по "Список заказов" в главном меню:

    http://127.0.0.1:8000/orders/order_list/

   Будет представлен список всех заказов.
   Можно удалить заказ, нажав на кнопку, и подтвердив удаление.

8. Нажав на номер ID можно перейти в заказ:

   Пример: http://127.0.0.1:8000/orders/order_detail/5/

   На странице заказа можно поменять статус заказа выбрать: "В ожидании", "Готово", "Оплачено" -> Сохранить изменения
   Статус у заказа поменяется и перейдет к списку заказов.

9. Можно посмотреть выручку с заказов со статусом "Оплачено" через главное меню или:

    http://127.0.0.1:8000/orders/revenue/

   Представлена общая выручка и список заказов

10. Все данные можно просмотреть и изменить:

   - в программе SQLiteStudio(3.4.4)
   - http://127.0.0.1:8000/admin/
