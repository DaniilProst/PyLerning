def send_email(message, recipient, *, sender="university.help@gmail.com"):

    valid_domains = (".com", ".ru", ".net")
    if ("@" not in recipient or not recipient.endswith(valid_domains) or
            "@" not in sender or not sender.endswith(valid_domains)):
        return print("Невозможно отправить письмо с адреса ", sender, "На адрес ", recipient)
    if sender == recipient:
        return print("Нельзя отправить письмо самому себе!")
    if sender == "university.help@gmail.com":
        return print("Письмо успешно отправлено с адреса ", sender, " на адрес ", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ", sender, " на адрес ", recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


