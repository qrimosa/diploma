<h1 align="center">NetNiche - Django Shop</h1>
<p align="center">
  <img width="350" height="auto" src="./doc/logo.png">
</p>

## Введення

NetNiche — це проект на Python / Django Framework, створений командою з 4 розробників як випускний іспит для курсу Full Stack Development. NetNiche — це, по суті, онлайн-магазин, написаний з нуля.

## Структура
```mermaid
graph TD
  A[InternetShop] --> B(InternetShop)
  A[InternetShop] --> C(templates)
  C(templates) --> M(admin)
  A[InternetShop] --> D(main)
  D[main] --> E(static)
  D(main) --> F(templates)
  A(InternetShop) --> G(media)
  E(static) --> H(css)
  E(static) --> J(js)
  E(static) --> K(img)
  F(templates) --> L(main)
  B(InternetShop) --> N(settings)
  D(main) --> P(models)
  P(models) --> Q(category)
  Q(category) --> R(product)
  R(product) --> S(ProductInCart)
  ```

## Технології

### Мови програмування
+ [HTML](https://en.wikipedia.org/wiki/HTML)
+ [CSS](https://en.wikipedia.org/wiki/CSS)
+ [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
+ [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Використані фреймворки, бібліотеки та інструменти

+ [Django](https://www.djangoproject.com/)
+ [Bootstrap](https://getbootstrap.com/)
+ [jQuery](https://jquery.com/)
+ [AJAX](https://en.wikipedia.org/wiki/Ajax_(programming))

1. [Git](https://git-scm.com/)
    - Git використовувався для контролю версій.
2. [GitHub](https://github.com/)
    - GitHub використовувався для зберігання коду проекту після надсилання з Git.
3. [Google Fonts](https://fonts.google.com/)
    - Для імпорту шрифту «Montserrat» використовувалися шрифти Google.

## Функції магазину

### Авторизація/Реєстрація
Авторизація та реєстрація виконуються за допомогою запитів [AJAX](https://en.wikipedia.org/wiki/Ajax_(programming)), тобто сторінка не оновлюється.

### Каталог
Каталог реалізований у вигляді модального вікна. При наведенні на категорію у модальному вікні відображається приклад картинки товару.

#### Сторінка каталогу
На сторінці каталогу представлено всі товари, що знаходяться у відповідній категорії. Доступні фільтри за двома параметрами, які також працюють без оновлення сторінки завдяки [AJAX](https://en.wikipedia.org/wiki/Ajax_(programming)).

### Кошик
Кошик реалізований як модальне вікно, де при кожному відкритті вміст оновлюється.

### Поле пошуку
За допомогою [JavaScript](https://en.wikipedia.org/wiki/JavaScript), при введенні тексту у поле пошуку з'являються підказки з перших 5 товарів, які було знайдено.

### Сторінка продукту
На сторінці продукту знаходяться всі дані про певний продукт.

### Сторінка сплати
Після вибору товарів у кошик, можна перейти до сторінки сплати.

## Встановлення

1. Увійдіть на GitHub і знайдіть [GitHub Repository](https://github.com/qrimosa/diploma).
2. Під назвою сховища натисніть Code.
3. Щоб клонувати репозиторій за допомогою HTTPS, скопіюйте посилання в розділі «Клонувати за допомогою HTTPS».
4. Відкрийте Git Bash.
5. Змініть поточний робочий каталог на місце, де ви хочете створити клонований каталог.
6. Введіть `git clone`, а потім вставте URL-адресу, скопійовану на кроці 3.
    ```bash
    $ git clone https://github.com/qrimosa/diploma
    ```
7. Натисніть Enter. Ваш локальний клон буде створено.
## Контакти розробників
+ [Ісхаков Марат](https://github.com/qrimosa)
+ [Андрій Бистров](https://github.com/AndriiBystrov)
+ [Іван Буряченко](https://github.com/ivanburyachenko)
+ [Мірошниченко Денис](https://github.com/Denisus-png)
