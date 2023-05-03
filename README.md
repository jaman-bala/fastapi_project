# fastapi_project

Команда для миграции alimbic init migrations 
Там появится папка миграция и файл alembic.ini их надо отредактировать 

после пишем alembic revision --autogenerate -m "Название миграции"

после пишем alembic upgrade (62e589dc599d) код в скопке это в versions миграции revision = '94085a1c1ea6' если будет
ошибка  File "C:\Users\MrRobot\Desktop\FastAPI-Chat\migrations\versions\94085a1c1ea6_database_create.py", line 23, in upgrade
    sa.Column('url', sqlalchemy_utils.types.url.URLType(), nullable=False),
                     ^^^^^^^^^^^^^^^^
NameError: name 'sqlalchemy_utils' is not defined

нужно установить pip install sqlalchemy-utils
После этого нужно убедиться, что пакет импортируется в коде, который вызывает ошибку. В данном случае в файле "94085a1c1ea6_database_create.py". Для этого добавьте следующую строку в начало файла:
import sqlalchemy_utils
в мигарции
