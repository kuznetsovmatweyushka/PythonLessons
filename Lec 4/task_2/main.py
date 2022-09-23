# Идея: совместная разработка
# Система собирает информацию с датчиков, в ней есть
# модуль логирования, который заносит в журнал все
# обращения к датчикам.
# В системе есть модуль, выполняющий обращения для
# получения данных с датчиков и модуль генерации htmlпредставления.
# Запуск системы осуществляется из головного модуля.

import html_creator as hc
import xml_generator as xg
import data_provider as dp

# print(xg.create())
# print(hc.create())

hc.new_create(xg.new_create(dp.data_collection()))
