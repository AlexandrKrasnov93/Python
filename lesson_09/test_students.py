import pytest
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models import Base, Student
from db_config import DATABASE_URL


# Создаем сессию для тестов
@pytest.fixture(scope="module")
def db_session():
    engine = create_engine(DATABASE_URL)
    session_factory = sessionmaker(bind=engine)

    # Проверяем, существуют ли таблицы, чтобы избежать повторного их создания
    if not inspect(engine).has_table("students"):
        Base.metadata.create_all(engine)

    session = session_factory()
    yield session
    session.rollback()
    session.close()
    engine.dispose()


def test_add_student(db_session):
    # Добавление студента
    student = Student(name="Alex", age=25)
    db_session.add(student)
    db_session.commit()

    # Проверка, что студент добавлен
    added_student = db_session.query(Student).filter_by(name="Alex").first()
    assert added_student is not None, "Student was not added to the database."
    assert added_student.age == 25, f"Expected age 25, but got {added_student.age}"


def test_update_student(db_session):
    # Изменение студента
    student = db_session.query(Student).filter_by(name="Alex").first()
    student.age = 27
    db_session.commit()

    # Проверка, что возраст изменен
    updated_student = db_session.query(Student).filter_by(name="Alex").first()
    assert updated_student.age == 27, f"Expected age 27, but got {updated_student.age}"


def test_delete_student(db_session):
    # Удаление студента
    student = db_session.query(Student).filter_by(name="Alex").first()
    db_session.delete(student)
    db_session.commit()

    # Проверка, что студент удален
    deleted_student = db_session.query(Student).filter_by(name="Alex").first()
    assert deleted_student is None, "Student was not deleted from the database."
