OneTwoThree(300)
---------

One... Two... Three... Four?

Решение
------
Если долго смотреть на данную нам последовательность, пытаться провернуть над ее числами какие-нибудь действия, то можем получить довольно сильные хинты на решение задания. Сложение, вычитание и умножение чисел последовательности ничего полезного нам не выдает, с делением же другая история. Если мы попробуем делить попарно два последовательных числа последовательности (большее разделить на меньшее), то увидим, что частные таких пар стремятся к числу 1.839286755214… Загуглив данное число, получаем запросы, связанные с последовательностью чисел Трибоначчи, частное двух чисел которой также стремится к  данному числу. Сравнив числа данной нам последовательности с числами последовательности Трибоначчи (если написать код для выведения ее), можно заметить, что числа довольно схожи, если сместить числа нашей последовательности на +2 индекса. Попробуем что-нибудь сделать с этими двумя последовательностями. Операции типа сложение, деление ни к чему не приводят. Если же попарно (по индексам) находить разности чисел данной нам последовательности и чисел последовательности Трибоначчи, можно заметить, что все числа лежат в довольно разумных пределах. Также можно заметить, что довольно многие из получившихся чисел равны 32, что в ASCII соответствует пробелу. Пытаемся перевести каждое число по таблице ASCII, получаем текст с необходимым нам флагом.
