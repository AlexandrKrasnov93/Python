from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL базы данных
DATABASE_URL = "postgresql://postgres:admin@localhost:5432/DB"

# Проверяем, что DATABASE_URL установлен, иначе выбрасываем ошибку
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables")

# Создаем SQLAlchemy для подключения к базе данных
engine = create_engine(DATABASE_URL)

# Создаем фабрику сессий, привязанную к движку
Session = sessionmaker(bind=engine)

# Инициализируем сессию для взаимодействия с базой данных
session = Session()
