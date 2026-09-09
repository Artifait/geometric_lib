# Документация проекта Geometric Lib

## Общее описание решения
Проект **Geometric Lib** — это библиотека на Python для выполнения базовых геометрических расчетов. Она предоставляет модули для вычисления площади ($S$) и периметра ($P$) основных геометрических фигур: круга, прямоугольника, квадрата и треугольника. Проект разработан как учебное решение для демонстрации навыков модульного программирования, документирования кода и работы с Git.

## Модули и формулы
Ниже приведено краткое описание модулей. Для просмотра детальной документации и примеров вызова перейдите по ссылкам:

| Модуль | Описание и детальная справка | Формула площади ($S$) | Формула периметра ($P$) |
| :--- | :--- | :--- | :--- |
| **`circle.py`** | [Подробное описание модуля ↗](./circle.md) | $S = \pi R^2$ | $P = 2\pi R$ |
| **`rectangle.py`** | [Подробное описание модуля ↗](./rectangle.md) | $S = a \cdot b$ | $P = 2(a + b)$ |
| **`square.py`** | [Подробное описание модуля ↗](./square.md) | $S = a^2$ | $P = 4a$ |
| **`triangle.py`** | [Подробное описание модуля ↗](./triangle.md) | $S = \frac{1}{2} \cdot a \cdot h$ | $P = a + b + c$ |

## История изменений (Changelog)

* `c4c46e7` — fix(rectangle): correct formula in perimeter function
* `c20cde4` — feat: add triangle module with area and perimeter functions
* `a01f1f1` — feat: add rectangle module with area and perimeter functions
* `86edb1c` — L-05: Update Docs. Add user agreement info
* `438b89a` — L-05: Add user agreement
* `6adb962` — L-03: Docs added
* `3049431` — L-04: Add rectangle.py
* `b5b0fae` — L-04: Update docs for calculate.py
* `d76db2a` — L-04: Add calculate.py
* `51c40eb` — L-04: Doc updated for triangle
* `d080c78` — L-04: Triangle added
* `d078c8d` — L-03: Docs added
* `8ba9aeb` — L-03: Circle and square added
