from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation
import random


COMMENDATIONS = [
    "Молодец!",
    "Отлично!",
    "Хорошо!",
    "Гораздо лучше, чем я ожидал!",
    "Ты меня приятно удивил!",
    "Великолепно!", "Прекрасно!",
    "Ты меня очень обрадовал!",
    "Именно этого я давно ждал от тебя!",
    "Сказано здорово – просто и ясно!",
    "Ты, как всегда, точен!",
    "Очень хороший ответ!",
    "Талантливо!",
    "Ты сегодня прыгнул выше головы!",
    "Я поражен!",
    "Уже существенно лучше!",
    "Потрясающе!",
    "Замечательно!",
    "Прекрасное начало!",
    "Так держать!",
    "Ты на верном пути!",
    "Здорово!", "Это как раз то, что нужно!",
    "Я тобой горжусь!",
    "С каждым разом у тебя получается всё лучше!",
    "Мы с тобой не зря поработали!",
    "Я вижу, как ты стараешься!",
    "Ты растешь над собой!",
    "Ты многое сделал, я это вижу!",
    "Теперь у тебя точно все получится!"
    ]


def get_child():
    name = "Фролов Иван"
    try:
        child = Schoolkid.objects.get(full_name__contains=name)
        return child
    except:
        print("Учетной записи по такому имени не найдено!")


def fix_marks(child):
    bad_child_marks = Mark.objects.filter(schoolkid=child[0], points__lt=4)
    for bad_mark in bad_child_marks:
        bad_mark.points = random.randint(4, 5)
        bad_mark.save()


def remove_chastisements(child):
    remarks = Chastisement.objects.filter(schoolkid=child[0])
    remarks.delete()


def create_commendation(child, subject):
    group_letter = child.group_letter
    year_of_study = child.year_of_study
    child_lessons = Lesson.objects.filter(
        group_letter=group_letter,
        year_of_study=year_of_study,
        subject__title=subject
    )

    random_lesson = random.choice(child_lessons)
    teacher = random_lesson.teacher
    date = random_lesson.date

    commendation_child = Commendation.objects.create(
        text=random.choice(COMMENDATIONS),
        schoolkid=child,
        subject=random_lesson.subject,
        teacher=teacher,
        created=date
    )
