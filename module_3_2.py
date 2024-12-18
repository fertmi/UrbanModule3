#Функция проверки отправки письма
# Проверка на корректность e-mail отправителя и получателя.
# Проверка на отправку самому себе.
# Проверка на отправителя по умолчанию.
def send_email(message, recipient,*,sender = "university.help@gmail.com"):
    end_mail=[".com" , ".ru" , ".net"]
    def flag_end_mail(string, flag=True):    #Функция проверки окончания: ".com" , ".ru" , ".net" и наличие знака @
        for i in end_mail:
            if i in string and '@' in string:
                flag = False
                break
        return flag

    if flag_end_mail(recipient) or flag_end_mail(sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender=="university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

#Основная программа
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Это сообщение для проверки связи', 'vasyok1337gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teachermail.uk')