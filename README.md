<h1 align="center">NetNiche - Django Shop</h1>
<p align="center">
  <img width="350" height="auto" src="./doc/logo.png">
</p>

## Введення

NetNiche — це проект на Python / Django Framework, створений командою з 4 розробників як випускний іспит для курсу Full Stack Development. NetNiche — це, за своєю суттю, онлайн-магазин спортивних речей, написаний з нулю.

# Навігація файлом README.md
- [Введення](#введення)
- [Користь проекту](#користь)
- [Встановлення](#встановлення)
- [Figjma проект](#figma-проект)
- [Figjam проект](#figjam-проект)
- [Розробники](#розробники)
- [Структура](#структура)
- [Використані технології](#використані-технології)
- [Функції магазину](#функції-магазину)
  - [Авторизація та Реєстрація](#авторизаціяреєстрація)
  - [Каталог](#каталог)
  - [Сторінка каталогу](#сторінка-каталогу)
  - [Кошик](#кошик)
  - [Пошук](#поле-пошуку)
  - [Сторінка продукту](#сторінка-продукту)
  - [Сторінка оформлення замовлення](#сторінка-оформлення-замовлення)
  - [Відправка електронного листа](#відправка-електронного-листа)
  - [Адмін-панель](#адмін-панель)


## Користь 

Наш проект буде корисний усім, хто планує відкрити свій власний бізнес у сфері одягу, або вже має такий, але без веб-сайту.

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

## [Figma проект](https://www.figma.com/design/pvuPKtedz2IY0fawcZu3TG/InternetShop?node-id=0-1&t=vHebT1JBqN5veFWA-0)

## [Figjam проект](https://www.figma.com/board/TUPHhipvNfogpLZzD8m5E9/Untitled?node-id=0-1&t=L28bkHfqPddl2QUa-0)

## Розробники
+ [Ісхаков Марат](https://github.com/qrimosa)
+ [Андрій Бистров](https://github.com/AndriiBystrov)
+ [Іван Буряченко](https://github.com/ivanburyachenko)
+ [Мірошниченко Денис](https://github.com/Denisus-png)

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

## Використані технології

+ [HTML](https://en.wikipedia.org/wiki/HTML)
+ [CSS](https://en.wikipedia.org/wiki/CSS)
+ [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
+ [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
+ [Django](https://www.djangoproject.com/)
+ [MySQL](https://www.mysql.com/)
+ [Bootstrap](https://getbootstrap.com/)
+ [jQuery](https://jquery.com/)
+ [Figma](https://figma.com)
+ [Figjam](https://www.figma.com/figjam/)

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

### Сторінка каталогу
На сторінці каталогу представлено всі товари, що знаходяться у відповідній категорії. Доступні фільтри за двома параметрами, які також працюють без оновлення сторінки завдяки [AJAX](https://en.wikipedia.org/wiki/Ajax_(programming)).

### Кошик
Кошик реалізований як модальне вікно, де при кожному відкритті вміст оновлюється.

### Поле пошуку
За допомогою [JavaScript](https://en.wikipedia.org/wiki/JavaScript), при введенні тексту у поле пошуку з'являються підказки з перших 5 товарів, які було знайдено.

### Сторінка продукту
На сторінці продукту знаходяться всі дані про певний продукт.

### Сторінка оформлення замовлення
Після вибору товарів у кошик, можна перейти до сторінки оформлення замовлення.

### Відправка електронного листа
Після оформлення замовлення на електронну адресу, яку вказують у реєстрації, відбувається відправка електронного листа с ціною і товарами. 

### Адмін-панель
Реалізована кастомізація стандартної адмін-панелі Django під палітру нашого сайту та для кращого розуміння логіки її роботи.

## Сторінки

### base.html
Базовий шаблон, який використовувався в кожному наступному html-файлі.

```html
<div class="modal fade" id="catalogModal" tabindex="-1" aria-labelledby="catalogModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-xl">
            <div class="modal-content d-flex flex-row align-items-start">
                <div class="modal-body d-flex flex-column gap-15 catalogue-container">
                    {% for category in categorys %}
                    <a href="{% url 'categories' category.slug %}" role="button" data-category-id="{{category.id}}"
                        class="container width-100 category-name">
                        <div class="row align-items-center">
                            <div class="col">
                                <p class="h1 padding-margin-0 text-decoration-none">{{category.name}}</p>
                            </div>
                            <div class="col-auto">
                                <img src="{% static 'main/img/right-arrow.svg' %}" alt="">
                            </div>
                        </div>
                    </a>
                    {% endfor %}
                </div>
                <div class="modal-footer w-50">
                    {% for category in categorys %}
                    <div
                        class="d-flex w-100 justify-content-center d-none align-items-center category-image-{{category.id}}">
                        <img src="{{category.image.url}}" width="230px" alt="">
                    </div>
                    {% endfor %}
                </div>
            </div>
        </div>
    </div>
```
- В базовому шаблоні знаходиться код усіх модальних вікон/навбарів, які ми використовували. Написані на основі Bootstrap'y
- Тут можна побачити приклад модального вікна, наш каталог. Він отримує з датабази назви категорій та їх зображення. Потім ітерує і відображає Їх у циклі ```for```.

```html
<div class="modal fade" id="regModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5 h1" id="exampleModalLabel">Реєстрація</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form action="" class="form-reg-auth">
                        {% csrf_token %}
                        <p class="hello-user-register" name="error"></p>
                        <p class="register-error h1"></p>
                        <input type="text" name="email" class="reg-auth-field" placeholder="Email">
                        <input type="text" name="login" class="reg-auth-field" placeholder="Username">
                        <input type="password" name="password" class="reg-auth-field" placeholder="Password">
                        <input type="password" name="repeat-password" class="reg-auth-field"
                            placeholder="Repeat password">
                        <button type="button" id="btn-register" data-cart-url="{% url 'Registration' %}"
                            class="btn btn-primary btn-reg-auth">register</button>
                    </form>
                </div>
                <div class="modal-footer form-reg-auth">
                    <a href="#" class="h1" data-bs-toggle="modal" data-bs-target="#authModel">у мене вже є
                        аккаунт</a>
                </div>
            </div>
        </div>
    </div>
```
- Також у базовому шаблоні у нас прописані форми авторизації та реєстрації

```python
def Registration(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        login = request.POST.get('login')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        if login and password and email:
            if len(password) >= 8:
                if password == repeat_password:
                    try:
                        User.objects.create_user(username = login, email = email, password = password)
                        context['email'] = ''
                        context['login'] = ''
                        context['password']  = ''
                        response = JsonResponse({'isRegister': True, 'login':login})
                    except IntegrityError:
                        return JsonResponse({'error': 'Такий користувач вже існує!'})
                    return response
                else:
                    return JsonResponse({'error': 'Паролі не співпадають!'})
            else:
                return JsonResponse({'error': 'Пароль повинен бути більше ніж 7 символів!'})
        else:
            return JsonResponse({'error': 'Ви не заповнили усі поля!'})
    return render(request, 'main/register.html', context)
```
- У файлі views.py прописана робота реєстрації. 
- Присутня валідація кожної можливої помилки та відобрежння відповідного повідомлення.
- При натисканні користувача на кнопку "register" функція отримує ім'я, електронну пошту та пароль користувача та заносить ці дані у базу, які після цього використовуються для логіну.

### main.html
Головна сторінка

```html
<div id="carouselExampleIndicators" class="carousel slide main-carousel border border-3 border-black rounded-5" data-bs-ride="carousel">
    <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active"
            aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1"
            aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2"
            aria-label="Slide 3"></button>
    </div>
    <div class="carousel-inner">
        <a href="{% url 'categories' 'krosivki' %}" role="button" class="carousel-item active">
            <img src="{% static 'main/img/slider-1-1.svg' %}" class="d-block w-100" alt="...">
        </a>
        <a href="{% url 'categories' 'shorti' %}" role="button" class="carousel-item">
            <img src="{% static 'main/img/slider-1-2.svg' %}" class="d-block w-100" alt="...">
        </a>
        <a href="{% url 'categories' 'futbolki' %}" role="button" class="carousel-item">
            <img src="{% static 'main/img/slider-1-3.svg' %}" class="d-block w-100" alt="...">
        </a>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators"
        data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators"
        data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
    </button>
</div>
```
- На головній сторінці знаходиться слайдер, код якого вище. Він також реалізований за допомогою Bootstrap'y. 
- Реалізований індикатор слайдів та перехід між ними, також слайди клікабельні і переносять вас на вибрану категорію.

```html
<div class="under-slider padding-margin-0">
    {% for product in all_products %}
    {% if forloop.counter <= 12 %} 
    <div class="card border border-black border-opacity-50 border-2 rounded-2" data-price="{{product.price}}">
        <div class="card-item-img w-100">
            <img src="{{product.image.url}}" class="card-img-top" alt="...">
        </div>
        <div class="card-body">
            <p class="card-text h2">{{product.name}}</p>
            <div class="d-flex card-under-slider">
                <h1 class="h1">{{product.price}} грн.</h1>
                <a href="{% url 'product' product.slug %}" class="btn btn-primary montserrat-14">Детальніше</a>
            </div>
        </div>
</div>
```
- Під слайдером у нас відображаются товари за допомогою цикла ```for```. Прописана умова щодо кількості цих товарів, тобто їх не може бути більше 12. 
