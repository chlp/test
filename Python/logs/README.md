# python test logs

# Первая часть

## Задача
Нужно написать скрипт на Python'е, описанный в примере разрабора проблемы в параграфе "Решение".

## Проблема
Клиент утверждает, что программа неправильно отображала изображения. Мы попросили его прислать нам все логи и он это сделал.

## Информация о программе
Мы знаем, что изображения, о которых говорит клиент программа загружает из интернета по полному URL'у вида "http://nordavind.ru/1234.png".
Мы знаем, что о каждом таком изображении программа оставляет запись в логах с полным путем до изображения вида "2018.10.24 10:15:23.192 can not load image http://nordavind.ru/1234.png".
Файлы с логами имеют имена вида 1540365795495.log и располагаются в папках с неограниченной вложенностью. Т.е. это может быть структура вида:
* logs/krasnodar/2017/01/22/1410365795491.log
* logs/krasnodar/2017/01/23/1410465795491.log
* logs/krasnodar/2017/01/23/1410465796543.log
* logs/sochi/komp1/2018/03/02/1450465796643.log
* logs/sochi/komp1/2018/03/02/1450465796644.log
* logs/sochi/komp1/2018/03/02/1450465796647.log
* logs/1450465791647.log

## Решение
Нужно написать скрипт на Python'е, который пройдется по всем файлам логов и вытащит из них все встретившиеся строчки, попадающие под шаблон "{date} {time} can not load image {url}" и составит файл, который на каждой строке выведет по одному полному URL'у до изображения - {url}.
Разработчику легче будет устранить проблему, если каждый {url} в результирующем файле будет встречаться только однажды.

Для генерации логов можно использовать скрипт generator.py.

# Вторая часть

Результат первой части - это файл со всеми URL'ами.
Во второй части нужно прочесть файл результат первой части и проверить каждый URL.
Пытаемся подключиться и если вернул не код 200, то складываем все эти пути в один файл.
Если 200, то пытаемся выкачать и проверяем изображение ли это. Если не изображение, то складываем во второй файл.
Все URL'ы, по которым отдается изображение складываем в третий файл.