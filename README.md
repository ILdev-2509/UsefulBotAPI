# UsefulBot API

## Это API для моего тг-бота.
## Функции:
- перевод текста с русского на код морзе
- перевод текста с кода морзе на русский
- перевод текста с одной раскладки клавиатуры на другую (определяется параметром direction)
- генератор паролей с заданной длиной
- проверка пароля на надежность
- конвертация числа в другую систему счисления
- конвертация арабских цифр в римские
- конвертация римских цифр в арабские
## В будущем планирую добавить: 
- заметки
- напоминалка
- менеджер финансов
- планировщик дел
- сервис с погодой
- сервис с конвертацией валюты
- сервис с конвертацией физических величин
- возможно что-то еще

## Ссылки для взаимодействия с API:
- `/translator/morse/to_morse-{text}`
- `/translator/morse/from_morse-{text}`
- `/translator/keyboard/keyboard-{text}-{direction}`  (direction: to_english или to_russian)
- `/password_manager/generator/generate-{length}`
- `/password_manager/checker/check-{password}`
- `/converter/bases/convert-{from_base}-{to_base}-{number}`
- `/converter/roman/to_roman-{number}`
- `/converter/roman/from_roman-{number}`

### - API пока нигде не развернута, все еще ищу бесплатные хостинги.