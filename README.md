**Термины**
>бд - база данных
> 
**Использование файлов**
>main.py - отправка запроса. 

>api.py - сам апи который нужно запустить.

>database.py - файл создания базы данных и обработки запросов.

>В файл main.bd сохраняем данные пользователя, а именно ссылка на гит(она будет использованна в профиле), id стороннего сервиса(телеграмм в нашем случае), и имя.

>В файл text.bd сохраняем текст и ссылку на репозиторий

**Функции**
>start_session используется для старта сессии бд, используется перед извлечением данных из дб.
> 
>**Пример**: users = start_session("users") запускает сессию для main.db