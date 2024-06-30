<h1 align="center">NetNiche - Django Shop</h1>
<p align="center">
  <img width="350" height="auto" src="./doc/logo.png">
</p>

## Введення

[NetNiche](https://netniche.pythonanywhere.com/) — це проект на Python / Django Framework, створений командою з 4 розробників як випускний іспит для курсу Full Stack Development. NetNiche — це, за своєю суттю, онлайн-магазин спортивних речей, написаний з нулю.

# Навігація файлом README.md
- [Введення](#введення)
- [Користь проекту](#користь)
- [Що таке база даних?](#що-таке-ба-даних)
- [Чому MySQL?](#чому-mysql)
- [Роль ID у таблицях бази даних](#роль-id-у-таблицях-бази-даних)
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
- [Шаблони](#шаблони)
  - [Базовий шаблон](#basehtml)
  - [Головна сторінка](#mainhtml)
  - [Оформлення замовлення](#checkouthtml)
  - [Сторінка продукту](#producthtml)
  - [Шаблон товарів у кошику](#cart_itemshtml)
  - [Персональний кабінет](#informationhtml)
  - [Сторінка категорій](#categorieshtml)
  - [Сторінка про нас](#abouthtml)
- [Функції відображення](#viewspy)
  - [product](#product)
  - [cart](#cart)
  - [about](#about)
  - [information](#information)
  - [cart_view](#cart_view)
  - [cart_remove](#cart_remove)
  - [log_out](#log_out)
  - [categories](#categories)
  - [checkout](#checkout)
- [script.js](#scriptjs)
  - [Реєстрація](#функція-реєстрації)
  - [Авторизація](#функція-авторизації)
  - [Додавання в кошик](#функція-додавання-в-кошик)
  - [Відображення товарів у кошику](#функція-відображення-товарів-у-кошику)
  - [Функція фільтрування](#функція-фільтрування)
- [script-cart.js](#script-cartjs)
- [search.js](#searchjs)


## Користь 

Наш проект буде корисний усім, хто планує відкрити свій власний бізнес у сфері одягу, або вже має такий, але без веб-сайту.

## Що таке база даних?
База даних - це організований збір даних, які можна легко отримати, управляти та оновлювати. Бази даних використовуються для зберігання інформації у структурованому вигляді, що дозволяє швидко отримувати необхідні дані, маніпулювати ними та забезпечувати їхню цілісність і безпеку. Бази даних можуть бути різних типів, включаючи реляційні, нереляційні, графові, документні тощо.

## Чому MySQL?
MySQL - це одна з найпопулярніших реляційних систем управління базами даних (РСУБД), яка використовується в багатьох веб-додатках та сервісах. Ось кілька причин, чому варто обрати MySQL:

1. Продуктивність та масштабованість: MySQL забезпечує високу швидкість роботи та може обробляти великі обсяги даних, що робить її ідеальною для великих проектів.
2. Безпека: MySQL підтримує різноманітні механізми безпеки, включаючи шифрування, контроль доступу користувачів та інші засоби для захисту даних.
3. Сумісність: MySQL є відкритим програмним забезпеченням та має велику спільноту користувачів і розробників, що забезпечує підтримку та розвиток.
4. Гнучкість: MySQL підтримує різні типи даних та індекси, що дозволяє адаптувати базу даних під специфічні потреби проекту.
5. Підтримка транзакцій: MySQL забезпечує атомарність, цілісність, ізоляцію та довговічність транзакцій (ACID), що є критичним для багатьох додатків.

## Роль ID у таблицях бази даних
ID (ідентифікатор) - це унікальний ключ, який використовується для однозначної ідентифікації записів у таблицях бази даних. Ось кілька причин, чому ID є важливим:

1. Унікальність: ID гарантує, що кожен запис у таблиці має унікальний ідентифікатор, що запобігає дублюванню даних.
2. Швидкий доступ: Використання індексів на полях ID дозволяє швидко здійснювати пошук та отримувати дані.
3. Зв’язки між таблицями: ID використовуються для створення зв’язків між таблицями (зовнішні ключі), що дозволяє організовувати дані у структурованому вигляді та забезпечувати їхню цілісність.
4. Маніпуляції з даними: Операції оновлення та видалення даних стають набагато простішими та ефективнішими при використанні унікальних ID.

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
7. Провести міграції
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
8. Натисніть Enter. Ваш локальний клон буде створено.

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

## Приступити до роботи з проектом
  
  ### Перелік необхідних модулів
   - Django - фреймворк для швидкої розробки веб-додатків.
   - jQuery - бібліотека для спрощення JavaScript коду.
   - Bootstrap - фреймворк для створення адаптивних інтерфейсів.
   - MySQL - реляційна база даних для зберігання даних.

## Запуск проекту локально
  - Клонуйте репозиторій: ```git clone https://github.com/qrimosa/diploma```
  - Перейдіть до папки проєкту: ```cd diploma```, потім до папки InternetShop: ```cd internetshop```
  - Запустіть сервер: ```python manage.py runserver```
  - У консолі натисніть ```ctrl + lkm``` на адрес локального сервера, щоб на нього перейти

## Запуск проекту віддалено 
  - Зареєструйтеся на PythonAnywhere.
  - Створіть новий веб-додаток.
  - Завантажте код проєкту на сервер через GitHub.
  - Налаштуйте базу даних.
  - Налаштуйте WSGI конфігурацію.
  - Запустіть веб-додаток.

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

### settings.py
```python
#Дозволені хости
ALLOWED_HOSTS = ['netniche.pythonanywhere.com']
#Налаштування віддаленої бази данних
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'netniche$default',
        'USER': 'netniche',
        'PASSWORD': 'n123123123',
        'HOST': 'netniche.mysql.pythonanywhere-services.com',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
#static файли
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#media файли
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#налаштування пошти
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'buryachenko.ivan2007@gmail.com'
EMAIL_HOST_PASSWORD = 'kokl pxfn hide hfmw'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```
### models.py
```python
class Category(models.Model):
    #текстове поле для збереження назви категорії
    name = models.CharField(max_length=255, verbose_name='Назва')
    #поле для збереження зображення категорії
    image = models.ImageField(verbose_name='Зображення')
    #поле для збереження слагу (короткий опис товару по якому він знаходиться на сайті, він використовується у URL)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, blank=True, null=True)
    #функція для відображення назви товару в адмін панелі
    def __str__(self):
        return f'{self.name}'
    #клас, за допомогою якого робиться переклад на українську
    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
```

## Шаблони

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


### checkout.html
Сторінка оформлення замовлення

```html
<ul id='delivery-form'>
            <li class="form-check courier-to-your-address">
                <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
                <label class="form-check-label" for="flexRadioDefault1">
                    Кур'єр на вашу адресу
                </label>
                <form id="payment-form" class="needs-validation courier-to-your-address-form d-none row g-3" action="">
                    <div class="col-md-4">
                        <label for="validationDefault01" class="form-label">Вулиця</label>
                        <input type="text" class="form-control" id="validationDefault01" value="" required>
                    </div>
                    <div class="col-md-4">
                        <label for="validationDefault02" class="form-label">Будинок</label>
                        <input type="text" class="form-control" id="validationDefault02" value="" required>
                    </div>
                    <div class="col-md-4">
                        <label for="validationDefault02" class="form-label">Квартира</label>
                        <input type="text" class="form-control" id="validationDefault02" value="" required>
                    </div>
                    <div class="col-md-4">
                        <label for="validationDefault02" class="form-label">Поверх</label>
                        <input type="text" class="form-control" id="validationDefault02" value="" required>
                    </div>
                    <div class="col-md-3">
                        <label for="validationDefault04" class="form-label">Ліфт</label>
                        <select class="form-select" id="validationDefault04" required>
                            <option selected disabled value="">Наявність важкого ліфта</option>
                            <option>Присутній</option>
                            <option>Відсутній</option>
                        </select>
                    </div>
                </form>
            </li>
            <li class="form-check pickup-from-nova-poshta">
                <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2">
                <label class="form-check-label" for="flexRadioDefault2">
                    Самовивіз з Нової Пошти
                </label>
                <form class="pickup-from-nova-poshta-form d-none" action="">
                    <div class="col-md-3">
                        <label for="validationDefault04" class="form-label">Відділення</label>
                        <select class="form-select" id="validationDefault04" required>
                            <option selected disabled value="">Виберіть ваше відділення</option>
                            {% for option in addresses %}
                            <option value="{{option}}">{{option}}</option>
                            {% endfor %}
                        </select>
                    </div>
                </form>
            </li>
        </ul>
```

- Працює вибір доставки: відділення Нової Пошти або доставку на вибрану адресу. 
- Також на сторінці оформлення замовлення відображаются товари, яки ви замовили, форма з ім'ям та прізвищем.

### product.html
Сторінка продукту

```html
<div class="container container-product">
    <div class="img">
        <img src="{{ product.image.url }}" alt="">
    </div>
    <div class="information d-flex flex-column gap-15">
        <h1 class="h1">{{product.name}}</h1>
        <hr>
        <div class="container d-flex justify-content-around">
            <p>{{product.article}}</p>
            {% if product.available %}
            <p>Товар в наявності</p>
            {% else %}
            <p>Товару немає в наявності</p>
            {% endif %}
        </div>
        <hr>
        <div class="container d-flex justify-content-around">
            <p>{{product.price}} грн.</p>
            <form action="" method="POST">
                {% csrf_token %}
                <input type="hidden" name="product_id" value="{{product.id}}">
                <button type="button" id="add-cart" data-cart-view-url="{% url 'cart_view' %}" data-cart-url="{% url 'cart' %}" class="btn btn-primary">Додати до
                    кошику</button>
            </form>
        </div>
        <p class="">{{product.description}}
            <br>
            <br>
            <b>Матеріал:</b>
            {{product.material}}
            <br>
            <br>
            <b>Країна виробник:</b>
            {{product.country}}
            <br>
            <br>
            <b>Характеристики:</b>
        <ul>
            {% for i in characteristics %}
            <li>{{i}}</li>
            {% endfor %}
        </ul>
        <b>Сезон:</b>
        Всесезонний;
        <br>
        <br>
        <b>Рекомендації щодо догляду:</b>
        <br>
        <ul>
            {% for i in guide %}
            <li>{{i}}</li>
            {% endfor %}
        </ul>
        </p>
    </div>
</div>
```

- На сторінці продукту відображаются усі його характеристики з бази даних: назва, зображення, розмір, сезон, опис, матеріал і тд. 

### cart_items.html
аблон товарів, які відображаются у кошику

```html
<div class="d-flex p-2 bg-white w-100 item-backet" style="width: 18rem;">
    <img src="{{product.product.image.url}}" width="120px" alt="...">
    <div class="card-body">
        <div class="d-flex justify-content-between ps-2">
            <h5 class="h2">{{product.product.name}}</h5>
            <form action="" method="POST">
                {% csrf_token %}
                <input type="hidden" name="product_in_cart_id" value="{{product.id}}">
                <div class="dropdown">
                    <img src="{% static 'main/img/three-dots.svg' %}" data-bs-toggle="dropdown" role='button'
                        width="30px" alt="">
                    <ul class="dropdown-menu">
                        <li><button type="button" data-product-id="{{product.id}}"
                                data-cart-url="{% url 'cart_remove' %}" class="dropdown-item delete-item-from-cart"
                                href="#">Видалити</button>
                        </li>
                    </ul>
                </div>
            </form>
        </div>
        <div class="d-flex align-items-end justify-content-end p-2 gap-15 h-50">
            <div class="d-flex align-items-center">
                <span class="minus" data-id="{{product.id}}" id="minus"><img src="{% static 'main/img/minus.svg' %}" width="20px" alt=""></span>
                <input type="number" class="count" data-id="{{product.id}}" id="count" name="qty" value="{{product.amount}}">
                <span class="plus" data-id="{{product.id}}" id="plus"><img src="{% static 'main/img/plus.svg' %}" width="20px" alt=""></span>
            </div>
        </div>
        <p class="h1 padding-margin-0 d-flex justify-content-end product-price">{{product.product.price}} грн</p>
    </div>
</div>
```

- Працює видалення товарів з кошика та зміна їх кількості.
- Відображається зображення та назва товару, також при збільшенні кількості ціна змінюється.

### information.html
Сторінка персонального кабінету користувача.

```html
<div class="container-fluid mt-5">
    <div class="accordion" id="accordionExample">
        <div class="accordion-item">
            <h2 class="accordion-header" id="headingOne">
                <button class="accordion-button btn-block" type="button" data-bs-toggle="collapse"
                    data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                    Особисті дані
                </button>
            </h2>
            <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne"
                data-bs-parent="#accordionExample">
                <div class="accordion-body">
                    <h6>Призвище:</h6>
                    <h6>Ім'я:</h6>
                </div>
            </div>
        </div>
        <div class="accordion-item">
            <h2 class="accordion-header" id="headingTwo">
                <button class="accordion-button collapsed btn-block" type="button" data-bs-toggle="collapse"
                    data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                    Мої замовлення
                </button>
            </h2>
            <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo"
                data-bs-parent="#accordionExample">
                <div class="accordion-body cart-wrap">
                    {% for product in products_in_cart %}
                    <div class="d-flex p-2 bg-white w-100 item-backet" style="width: 18rem;">
                        <img src="{{product.product.image.url}}" width="120px" alt="...">
                        <div class="card-body">
                            <div class="ml-1 d-flex justify-content-between">
                                <h5 class="h2">{{product.product.name}}</h5>
                                <form action="" method="POST">
                                    {% csrf_token %}
                                    <input type="hidden" name="product_in_cart_id" value="{{product.id}}">
                                    <div class="dropdown">
                                        <img src="{% static 'main/img/three-dots.svg' %}" data-bs-toggle="dropdown"
                                            role='button' width="30px" alt="">
                                        <ul class="dropdown-menu">
                                            <li><button type="button" data-product-id="{{product.id}}"
                                                    data-cart-url="{% url 'cart_remove' %}"
                                                    class="dropdown-item delete-item-from-cart"
                                                    href="#">Видалити</button>
                                            </li>
                                        </ul>
                                    </div>
                                </form>
                            </div>
                            <div class="d-flex align-items-end justify-content-end p-2 gap-15 h-50">
                                <div class="d-flex align-items-center">
                                    <span class="minus" data-id="{{forloop.counter}}" id="minus"><img
                                            src="{% static 'main/img/minus.svg' %}" width="20px" alt=""></span>
                                    <input type="number" data-id="{{forloop.counter}}" class="count" id="count"
                                        name="qty" value="{{product.amount}}">
                                    <span class="plus" data-id="{{forloop.counter}}" id="plus"><img
                                            src="{% static 'main/img/plus.svg' %}" width="20px" alt=""></span>
                                </div>
                            </div>
                            <p class="h1 padding-margin-0 d-flex justify-content-end">{{product.product.price}} грн</p>
                        </div>
                    </div>
                    <hr>
                    {% endfor %}
                </div>
            </div>
        </div>
        <div class="accordion-item">
            <h2 class="accordion-header" id="headingThree">
                <button class="accordion-button collapsed btn-block" type="button" data-bs-toggle="collapse"
                    data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                    Логін
                </button>
            </h2>
            <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree"
                data-bs-parent="#accordionExample">
                <div class="accordion-body">
                    <h6>Ім'я користувача: {{user.username}}</h6>
                    <h6>Електронна пошта: {{user.email}}</h6>
                    <a class='btn btn-outline-danger logout-button' href="{% url 'Logout' %}">Logout</a>
                </div>
            </div>
        </div>
    </div>
</div>
```

- Сторінка виконана за допомогою бутстраповського класу ```class = 'accordion'```. Присутнє відображення товарів, які знаходятся в кошику та інформація, яку користувач вводить при регістрації.
- Також для більшості стилів для елементів ми використовували Bootstrap.


### categories.html
Сторінка категорій

```html
<div class="filters desktop-filters" id="desktop-filters">
        <form id="filters-form" class='ms-2 border'>
            {% csrf_token %}
            <input type="hidden" id="category-url" data-category-url="{% url 'categories' category.slug %}">
            <div class="price-input">
                <div class="field">
                    <input type="number" class="input-min" value="{{min_price}}">
                </div>
                <div class="separator">-</div>
                <div class="field">
                    <input type="number" class="input-max" value="{{max_price}}">
                </div>
            </div>
            <div class="slider">
                <div class="progress"></div>
            </div>
            <div class="range-input">
                <input type="range" class="min-price-slider" min="{{min_price}}" max="{{max_price}}" step="10"
                    value="{{min_price}}">
                <input type="range" class="max-price-slider" min="{{min_price}}" max="{{max_price}}" step="10"
                    value="{{max_price}}">
            </div>
            <div class='pt-4'>
                <p class="h1">Колір</p>
                {% for color in colors %}
                <div class='d-flex flex-column'>
                    <div class='d-flex flex-row gap-2 desktop-filters'>
                        <label for="{{color.color}}">{{color.color}}</label>
                        <input type="checkbox" class="color-filter" name="colors-filter" id="{{color.color}}">
                    </div>
                </div>
                {% endfor %}
            </div>
            <div class='pt-4'>
                <p class="h1">Розмір</p>
                {% for size in sizes %}
                <div class='d-flex flex-column'>
                    <div class='d-flex flex-row gap-2 desktop-filters'>
                        <label for="{{size.size}}">{{size.size}}</label>
                        <input type="checkbox" class="size-filter" name="sizes-filter" id="{{size.size}}">
                    </div>
                </div>
                {% endfor %}
            </div>
            <div class='pt-4'>
                <p class="h1">Сезон</p>
                {% for season in seasons %}
                <div class='d-flex flex-column'>
                    <div class='d-flex flex-row gap-2 desktop-filters'>
                        <label for="{{season.season}}">{{season.season}}</label>
                        <input type="checkbox" class="season-filter" name="seasons-filter" id="{{season.season}}">
                    </div>
                </div>
                {% endfor %}
            </div>
        </form>
    </div>
```

- На цій сторінці ми прописували фільтри ціни, кольору, розміру і сезон. 

```html
<div id="product-list" class="under-slider border w-100">
        {% include 'main/categories_filter.html' %}
    </div>
```
- Також тут ми включаємо в цей шаблон ```categories_filter.html```, в якому прописане відображення товарів на сторінці:

```html
<div class="card-category padding-margin-0 d-flex justify-content-center align-items-center flex-column" data-price="{{product.price}}">
    <input type="hidden" name="product_id" value="{{product.id}}">
    <a href="{% url 'product' product.slug %}">
        <div class="card-item-img ">
            <img src="{{product.image.url}}" class="card-img-top" alt="...">
        </div>
    </a>
    <div class="card-body">
        <p class="card-text h2">{{product.name}}</p>
        <div class="d-flex card-under-slider">
            <h1 class="h1">{{product.price}} грн.</h1>
            <a class="add-cart" data-cart-url="{% url 'cart' %}" href="#">
                <div>
                    <img width="40px" src="{% static 'main/img/cart-add.svg' %}" alt="">
                </div>
            </a>
        </div>
    </div>
</div>
```

### about.html
Сторінка з інформацією про нас

```html
<div class="container-about">
    <div class="row">
        <div class="col-md-6 column_about_1">
            <img src="{% static 'main/img/logo.png' %}" alt="NetNiche Logo" class="img-fluid mb-4" style="width: 100%; max-width: 350px;">
            <h3>Ми завжди готові допомогти вам!</h3>
            <p class="contact-info">
                Зв'яжіться з нашою службою підтримки за наступним телефоном:<br>
                +38 (050) 084-97-20<br>
                Дякуємо за ваше розуміння та співпрацю!
            </p>
            <h2>Шановні клієнти!</h2>
            <p class="client-info">
                Ми завжди прагнемо забезпечити вам найкращий сервіс, але іноді можуть виникати непередбачені проблеми.
                Якщо у вас виникли будь-які питання або проблеми з нашим сервісом, будь ласка, не соромтеся звертатися до нас.
            </p>
            <h3>Якщо ви шукаєте роботу</h3>
            <div class="job-form bg-light p-4">
                <form action="#" method="POST">
                    {% csrf_token %}
                    <input type="text" placeholder="ПІБ" class="form-control mb-2">
                    <input type="email" placeholder="Електрона пошта" class="form-control mb-2">
                    <input type="tel" placeholder="Номер телефона" class="form-control mb-2">
                    <button type="submit" class="btn btn-primary">Надіслати</button>
                </form>
            </div>
        </div>
        <div class="col-md-6 column_about_2">
            <h1 class="netniche-title">Ми NetNiche</h1>
            <p class="netniche-info">
                1. Якість без компромісів: Ми ретельно добираємо матеріали та контролюємо кожен етап виробництва, щоб забезпечити найвищу якість нашого одягу. Кожен шов, кожна деталь – усе продумано до дрібниць.<br>
                2. Сучасний дизайн: Наші дизайнери постійно стежать за останніми модними тенденціями та створюють колекцію, яка поєднує стиль і комфорт. Ми прагнемо запропонувати вам найактуальніші та трендові моделі.<br>
                3. Індивідуальний підхід: Для нас кожен клієнт особливий. Ми готові допомогти вам знайти ідеальний образ, враховуючи ваші уподобання та особливості фігури. Наші консультанти завжди готові дати професійну пораду та допомогти з вибором.<br>
                4. Сталий розвиток: Ми піклуємось про майбутнє нашої планети та прагнемо мінімізувати вплив на навколишнє середовище. Наш одяг виготовляється з екологічно чистих матеріалів, і ми активно підтримуємо ініціативи із захисту природи.<br>
                5. Теплота та гостинність: Ми пишемося тим, що наш магазин – це не просто місце для покупок, а простір, де ви можете почуватися як вдома. Ми прагнемо створити атмосферу затишку та дружби, щоб кожна покупка приносила вам радість.
            </p>
        </div>
    </div>
</div>
```

- Присутня сторінка з інформацією про нас з нашими цілями і прагненнями.
- Також є форма для тих, хто шукає роботу в нашому магазині 

## views.py

### product
- У цій функції прописан динамічний slug-url, що дозволяє нам автоматично створювати url-адресу товару з його імені.

```python
def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {'product':product, 'characteristics': product.characteristics.get('name'), 'guide': product.guide.get('name')}
    return render(request, 'main/product.html', context)
```

### cart
- У функції ```cart``` ми додаємо товари до кошику за сессіоним ключем користувача

```python
def cart(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    if request.method == 'POST':
        session_key = request.session.session_key
        if not session_key:
            request.session.cycle_key()
            session_key = request.session.session_key
        product_id = request.POST.get('product_id')
        # product = Product.objects.get(id = product_id)
        # print(product)
        if product_id:
            try:
                product = ProductInCart.objects.get(product_id = product_id, session_key=session_key)
                product.amount += 1
                product.save()
            except:
                product = ProductInCart.objects.create(product_id=product_id,session_key=session_key, amount = 1)
            cart_count = ProductInCart.objects.filter(session_key=session_key).count()
            return JsonResponse({'cart_count': cart_count})
        # productsincart = ProductInCart.objects.filter(session_key=session_key)
    return render(request, "main/product.html", context=context)
```

### about
- Функція відображення сторінки ```about.html```

```python
def about(request):
    context = {}
    return render(request, 'main/about.html', context)
```

### information
- Функція відображення сторінки інформації, також відображається за сессіоним ключем.

```python
def information(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
        session_key = request.session.session_key
    context = {'products_in_cart': ProductInCart.objects.filter(session_key=session_key)}
    return render(request, 'main/information.html',context)
```

### cart_view
- Функція відображення товарів у кошику з фільтрацією за сессіоним ключем.

```python
def cart_view(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
        session_key = request.session.session_key
    productsincart = ProductInCart.objects.filter(session_key=session_key)
    context = {
        'incartproduct': productsincart,
    }
    html = render_to_string('main/cart_items.html', context)
    cart_count = ProductInCart.objects.filter(session_key=session_key).count()
    return JsonResponse({"html":html, 'cart_count':cart_count})
```

### cart_remove
- Функція видалення товару з кошику

```python
def cart_remove(request):
    context = {}
    if request.method == 'POST':
        product_in_cart_id = request.POST.get('product_in_cart_id')
        product = ProductInCart.objects.get(id = product_in_cart_id)
        product.delete()
    return render(request, "main/base.html",context)
```
### log_out
- Функція виходу з аккаунту 

```python
def log_out(request: HttpResponse):
    logout(request)
    return redirect('main')
```

### categories
- Функція категорій

```python
def categories(request, category):
    # отримуємо всі поля з бази даних 
    category_obj = Category.objects.get(slug=category)
    products_obj = Product.objects.filter(category=category_obj)
    colors = products_obj.values('color').distinct()
    products_list = products_obj.values_list('price')
    min_price = products_list.order_by('price').first()
    max_price = products_list.order_by('price').last()
    sizes = products_obj.values('size').distinct()
    seasons = products_obj.values('season').distinct()
    context = {'category': category_obj, 'products':products_obj, 'colors':colors, 'max_price': max_price[0], 'min_price': min_price[0], 'sizes': sizes, 'seasons': seasons}
    # умова для додавання фільтрів
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        category_obj = Category.objects.get(slug=category)
        products = Product.objects.filter(category = category_obj,price__range=(request.GET.get('min_price'), request.GET.get('max_price')))
        colors = request.GET.getlist('colors[]')
        sizes = request.GET.getlist('sizes[]')
        seasons = request.GET.getlist('seasons[]')
        # додаємо фільтри на сторінку
        if colors:
            products = products.filter(color__in = colors)
        if sizes:
            products = products.filter(size__in = sizes)
        if seasons:
            products = products.filter(season__in = seasons)
        html = render_to_string('main/categories_filter.html', {'products': products})
        return JsonResponse({"html":html})
    return render(request, 'main/categories.html', context)
```

### checkout
- Функція оформлення замовлення 

```python
def checkout(request):
    # отримуємо сессіоний ключ
    session_key = request.session.session_key
    products_in_cart = ProductInCart.objects.filter(session_key = session_key)
    sum_in_cart = 0
    for product in products_in_cart:
        sum_in_cart += product.product.price*product.amount
    context = {'products_in_cart':products_in_cart,'sum_in_cart':sum_in_cart}
    # умова, якщо користувач не додав товари до кошику, то його перекидує на головну сторінку
    if products_in_cart.exists():
        pass
    else:
        return redirect('main')
    # інтеграція API нової пошти 
    api_key = '8112617626b3a78db6c84bcc50a6d102'
    payload = {
        "apiKey": api_key,
        "modelName": "Address",
        "calledMethod": "getWarehouses",
        "methodProperties": {
            "CityName": "Днепр",
        }
    }
    response = requests.post('https://api.novaposhta.ua/v2.0/json/', json=payload)
    if response.status_code == 200:
        data = response.json()
        if data['success']:
            # отримання даних про відділення в місті Дніпро
            warehouses = data['data']
            addresses = [warehouse['Description'] for warehouse in warehouses if warehouse['TypeOfWarehouse']!='f9316480-5f2d-425d-bc2c-ac7cd29decf0']
            context['addresses'] = addresses
    # отримуємо дані з датабази
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        products = request.POST.getlist('products[]')
        sum_in_cart = request.POST.get('sum_in_cart')
        amount = request.POST.get('amount')
        delivery = request.POST.get('delivery')
        delivery_list = []
        if delivery == 'Кур\'єр на вашу адресу':
            street = request.POST.get('street')
            house = request.POST.get('house')
            flat = request.POST.get('flat')
            floor = request.POST.get('floor')
            elevator = request.POST.get('elevator')
            delivery_list.append([street, house, flat, floor, 'Ліфт:', elevator])
        elif delivery == 'Самовивіз з Нової Пошти':
            branch = request.POST.get('branch')
            delivery_list.append([branch])
        if name and surname and products and amount and delivery:
            products_in_checkout = ''
            message = ''
            for i in products:
                product = ProductInCart.objects.get(id=i)
                products_in_checkout+=f'{product.product.name} в кількості {amount}\n'
            message = f'Доброго дня, {name} {surname}, ви замовили: \n{products_in_checkout}\nЦіна за покупку: {sum_in_cart} грн.\nДоставка:\n{delivery}\n{" ".join(str(i)for i in delivery_list[0])}\nДякуємо вам за покупку!'
            # відправляємо електронний лист користувачу з його замовленням
            print(send_mail('Доставка одягу', message, settings.EMAIL_HOST_USER, [request.user.email]))
            result = {'success': True, 'message': 'Операция выполнена успешно!'}
            return JsonResponse(result)
    return render(request,'main/checkout.html', context)
```

## script.js
- Скрипт, який використовується майже на кожній сторінці, та є базовим.

### Функція реєстрації
```javascript
$('#btn-register').click(() => {
        var url = $('#btn-register').data('cart-url');
        $.ajax({
            url: url,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                email: $('input[name=email]').val(),
                login: $('input[name=login]').val(),
                password: $('input[name=password]').val(),
                repeat_password: $('input[name=repeat-password]').val(),
            },
            success: function (response) {
                if (response.isRegister) {
                    $('.hello-user-register').text(`Дякуємо за реєстрацію, ${response.login}!`)
                    $('input[name=login]').val('')
                    $('input[name=password]').val('')
                    $('input[name=email]').val('')
                    $('input[name=repeat-password]').val('')
                }
                if (response.error) {
                    $('.register-error').text(response.error)
                }
            }
        })
})
```
### Функція авторизації
```javascript
$('#btn-auth').click(() => {
        var url = $('#btn-auth').data('cart-url');
        $.ajax({
            url: url,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                username: $('input[name=username]').val(),
                password: $('input[name=loginPassword]').val(),
            },
            success: function (response) {
                console.log(response.isLogin)
                if (response.isLogin) {
                    $('.hello-user-login').text(`Вітаємо, ${response.username}!`)
                    $('input[name=username]').val('')
                    $('input[name=loginPassword]').val('')
                    localStorage.setItem('isAuthenticated', 'true')
                    $('.auth-link').removeClass('d-none')
                    $('.login-button').addClass('d-none')
                    $('.burger-auth').addClass('d-none')
                    $('.burger-profile').removeClass('d-none')
                }
                if (response.error) {
                    $('.login-error').text(response.error)
                }
            }
        })
    })
```
### Функція додавання в кошик
```javascript
$('.add-cart').click(function () {
        var cartUrl = $(this).data('cart-url')
        $.ajax({
            url: cartUrl,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                product_id: $(this).closest('.card-category').find('input[name=product_id]').val(),
            },
            success: function (data) {
                $('.badge').removeClass('d-none')
                $('.badge').text(data.cart_count)
            }
        })
    })
```

### Функція відображення товарів у кошику
```javascript
$('#backet-header').click(() => {
        var cartviewUrl = $('#backet-header').data('cart-url')
        $.ajax({
            url: cartviewUrl,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: (data) => {
                $('.cart-wrap').html(data.html);
                let total = 0
                $('.item-backet').each(function () {
                    let price = parseInt($(this).find('.product-price').text())
                    let count = $(this).find('.count').val()
                    total += price * count
                })
                $('.cart-footer-price').text(`Разом: ${total} грн`)
            }
        })
    })
```
### Функція фільтрування
```javascript
function updatePriceFilter() {
        //Перевірка if в одну строку, якщо вірно - у змінну activeForm буде записано '.mobile-filters', якщо невірно - '.desktop-filters'
        let activeForm = $(window).width() <= 768 ? '.mobile-filters' : '.desktop-filters'
        url = $('#category-url').data('category-url')
        minPrice = ($(`${activeForm} .min-price-slider`).val())
        maxPrice = ($(`${activeForm} .max-price-slider`).val())
        console.log($(`${activeForm} .min-price-slider`))
        colors = []
        seasons = []
        sizes = []
        $(`${activeForm} .color-filter:checked`).each(function () {
            colors.push($(this).attr('id'))
        })
        $(`${activeForm} .size-filter:checked`).each(function () {
            sizes.push($(this).attr('id'))
        })
        $(`${activeForm} .season-filter:checked`).each(function () {
            seasons.push($(this).attr('id'))
        })

        $.ajax({
            url: url,
            type: 'GET',
            data: {
                min_price: minPrice,
                max_price: maxPrice,
                colors: colors,
                sizes: sizes,
                seasons: seasons,
            },
            success: function (data) {
                $('#product-list').html(data.html);
                var newUrl = url + '?price_from=' + minPrice + '&price_to=' + maxPrice;
                if (colors.length > 0) {
                    newUrl += '&colors=' + colors.join(',')
                }
                if (seasons.length > 0) {
                    newUrl += '&seasons=' + seasons.join(',')
                }
                if (sizes.length > 0) {
                    newUrl += '&sizes=' + sizes.join(',')
                }
                //Зміна url адреси за допомогою History API
                history.pushState({}, '', newUrl)
            }
        })
    }
    let activeForm = $(window).width() <= 768 ? '.mobile-filters' : '.desktop-filters'
    $(`${activeForm} .min-price-slider,${activeForm} .max-price-slider,${activeForm} .color-filter,${activeForm} .size-filter,${activeForm} .season-filter`).on('change', updatePriceFilter);
    let priceGap = 0;
    function updateProgress() {
        let activeForm = $(window).width() <= 768 ? '.mobile-filters' : '.desktop-filters'
        let minVal = parseInt($(`${activeForm} .range-input input:eq(0)`).val()),
            maxVal = parseInt($(`${activeForm} .range-input input:eq(1)`).val())
        console.log($(`${activeForm} .range-input input:eq(0)`))
        let minRange = parseInt($(`${activeForm} .min-price-slider`).attr("min")),
            maxRange = parseInt($(`${activeForm} .max-price-slider`).attr("max"))
        let leftValue = ((minVal - minRange) / (maxRange - minRange)) * 100 + "%"
        let rightValue = ((maxRange - maxVal) / (maxRange - minRange)) * 100 + "%"
        $(`${activeForm} .progress`).css({
            "left": leftValue,
            "right": rightValue
        });
        $(`${activeForm} .input-min`).val(minVal);
        $(`${activeForm} .input-max`).val(maxVal);
    }
    updateProgress();
    $(".price-input input").each(function (index, input) {
        let activeForm = $(window).width() <= 768 ? '.mobile-filters' : '.desktop-filters'
        $(input).on("input", function (e) {
            let minPrice = parseInt($(`${activeForm} .price-input input:eq(0)`).val()),
                maxPrice = parseInt($(`${activeForm} .price-input input:eq(1)`).val())

            if ((maxPrice - minPrice >= priceGap) && maxPrice <= $(`${activeForm} .max-price-slider`).attr("max")) {
                if ($(this).hasClass("input-min")) {
                    $(`${activeForm} .min-price-slider`).val(minPrice)
                    updateProgress()
                } else {
                    $(`${activeForm} .max-price-slider`).val(maxPrice)
                    updateProgress()
                }
            }
        });
    });
    $(".range-input input").each(function (index, input) {
        let activeForm = $(window).width() <= 768 ? '.mobile-filters' : '.desktop-filters'
        $(input).on("input", function (e) {
            let minVal = parseInt($(`${activeForm} .range-input input:eq(0)`).val()),
                maxVal = parseInt($(`${activeForm} .range-input input:eq(1)`).val())
            if ((maxVal - minVal) < priceGap) {
                if ($(this).hasClass("range-min")) {
                    $(`${activeForm} .range-input input:eq(0)`).val(maxVal - priceGap)
                    updateProgress();
                } else {
                    $(`${activeForm} .range-input input:eq(1)`).val(minVal + priceGap)
                    updateProgress();
                }
            } else {
                updateProgress();
            }
        });
    });
```

## script-cart.js
- Скрипт, який використовується для відображення товарів у кошику.

```javascript
$('.delete-item-from-cart').click(function () {
        var cartUrl = $('.delete-item-from-cart').data('cart-url');
        var product_id = $(this).data('product-id');
        var cartviewUrl = $('#backet-header').data('cart-url');
        $.ajax({
            url: cartUrl,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                product_in_cart_id: product_id,
            },
            success: () => {
                $.ajax({
                    url: cartviewUrl,
                    type: 'POST',
                    data: {
                        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                        product_in_cart_id: $('input[name=product_in_cart_id]').val(),
                    },
                    success: (data) => {
                        if (data.cart_count == 0) {
                            $('.badge').addClass('d-none')
                        }
                        else {
                            $('.badge').text(data.cart_count)
                        }
                        $('.cart-wrap').html(data.html);
                        let total = 0;
                        $('.item-backet').each(function () {
                            let price = parseInt($(this).find('.product-price').text())
                            let count = $(this).find('.count').val()
                            total += price * count
                        })
                        $('.cart-footer-price').text(`Разом: ${total} грн`);
                    }
                })
            }
        })
    })
```

## search.js
- Скрипт, який використовується для поля пошуку в header

```javascript
    let availableProducts = [];
    const resultsBox = $(".result-box")
    const inputBox = $("#search-header")
    inputBox.on("keyup", function () {

        resultsBox.show()
        $('main').addClass('fade')
        $('main').css('opacity', 0.5)
        let input = inputBox.val().toLowerCase().trim();
        let result = availableProducts.filter((product) => {
            return product.name.toLowerCase().includes(input);
        });
        display(result.slice(0, 5));
        if (!result.length) {
            resultsBox.html('');
        }
    });
    function display(result) {
        const content = result.map((product) => {
            return `<li onclick="selectInput('${product.slug}')">${product.name}</li>`;
        });
        resultsBox.html("<ul>" + content.join('') + "</ul>");
    }
    window.selectInput = function (url) {
        window.location.href = `product/${url}`
    }
    inputBox.blur(() => {
        setTimeout(function () {
            resultsBox.html('');
        }, 200);
    })
    //отримуємо в масив availableProducts назви усіх продуктів
    $.ajax({
        url: $('#data-get-products-url').data('get-products-url'),
        method: 'GET',
        success: function (data) {
            availableProducts = data
        }
    });
```