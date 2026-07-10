import customtkinter as ctk
import random

variables = {
    "камень": "ножницы",
    "ножницы": "бумага",
    "бумага": "камень"
}

score = {
    "user": 0,
    "bot": 0
}

def user_play(user_choice):
    choice = ['камень', 'ножницы', 'бумага']
    bot_choice = random.choice(choice)

    if variables[user_choice] == bot_choice:
        score["user"] += 1
        label.configure(text=f"Вы выиграли!\nБот выбрал: {bot_choice}\n\nВаш счёт: {score['user']} / Счёт бота: {score['bot']}")
    elif user_choice == bot_choice:
        label.configure(text=f"Ничья!\nБот выбрал: {bot_choice}\n\nВаш счёт: {score['user']} / Счёт бота: {score['bot']}")
    else:
        score["bot"] += 1
        label.configure(text=f"Вы проиграли!\nБот выбрал: {bot_choice}\n\nВаш счёт: {score['user']} / Счёт бота: {score['bot']}")

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Камень, ножницы, бумага")
root.geometry("400x300")

label = ctk.CTkLabel(root, text="Добро пожаловать в игру\n'Камень, ножницы, бумага'!", font=("Sans-serif", 25))
label.pack(pady=20)

btn_rock = ctk.CTkButton(root, text="Камень", command=lambda: user_play("камень"))
btn_rock.pack(pady=10)
btn_scissors = ctk.CTkButton(root, text="Ножницы", command=lambda: user_play("ножницы"))
btn_scissors.pack(pady=10)
btn_paper = ctk.CTkButton(root, text="Бумага", command=lambda: user_play("бумага"))
btn_paper.pack(pady=10)

root.mainloop()