# Электронный дневник школы

Этот скрипт предназначен для создания похвал, исправления оценок и удаления замечаний.

## Функции

1. Функция get_child() находит учетку ученика по имени.
В переменной *name*, указываете нужную Фамилию и Имя, например:
name = "Фролов Иван"
```
get_child()
```
1. Функция fix_marks(child) принимает на вход учетную запись ученика, и исправляет все его оценки на 4 и 5
```
fix_marks(child)
```
1. Функция remove_chastisements(child) принимает на вход учетную запись ученика и удаляет его замечания
```
remove_chastisements(child)
```
1. Функция create_commendation(child, subject) создает похвалу по выбранному предмету и выбраному ученику, принимает на вход *child* - учетку ученика, и *subject* - название предмета, например:
```
create_commendation(child, "Математика")
```

## Запуск

- Скачайте код
- Запустите shell командой `python3 manage.py shell`
- Импортируйте скрипты:
```
from scripts import *
```
- Запустите функцию get_child() и сохраните ее в переменную child

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
