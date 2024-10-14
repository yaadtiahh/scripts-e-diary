import random
from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation


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
    except Schoolkid.ObjectDoesNotExist:
        print("Учетной записи по такому имени не найдено!")
    except Schoolkid.MultipleObjectsReturned:
        print("Запрос вернул несколько объектов, хотя ожидался только один.")


def fix_marks(child):
    bad_child_marks = Mark.objects.filter(
        schoolkid=child,
        points__lt=4
    ).update(points=random.randint(4, 5))


def remove_chastisements(child):
    remarks = Chastisement.objects.filter(schoolkid=child)
    remarks.delete()


def create_commendation(child, subject):
    group_letter = child.group_letter
    year_of_study = child.year_of_study
    child_lesson = Lesson.objects.filter(
        group_letter=group_letter,
        year_of_study=year_of_study,
        subject__title=subject
    ).order_by('date').last()

    teacher = child_lesson.teacher
    date = child_lesson.date

    commendation_child = Commendation.objects.create(
        text=random.choice(COMMENDATIONS),
        schoolkid=child,
        subject=child_lesson.subject,
        teacher=teacher,
        created=date
    )
