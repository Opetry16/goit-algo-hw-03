import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)

def main():
    # Запитуємо користувача про рівень рекурсії
    recursion_level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))

    # Створюємо вікно та черепашку
    wn = turtle.Screen()
    wn.bgcolor("white")
    wn.title("Сніжинка Коха")

    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.speed(100)
    snowflake_turtle.color("blue")

    # Розміщуємо черепашку у відповідному місці
    snowflake_turtle.penup()
    snowflake_turtle.goto(-150, 90)
    snowflake_turtle.pendown()

    # Викликаємо функцію для малювання сніжинки Коха
    for _ in range(3):
        koch_snowflake(snowflake_turtle, recursion_level, 300)
        snowflake_turtle.right(120)

    turtle.done()

if __name__ == "__main__":
    main()


