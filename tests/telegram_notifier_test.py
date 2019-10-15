from utils.notifiers import CodexTelegramNotifier

WORDPOOL = {
    "start": [
        "Давненько не было постов в телеге...",
        "Сегодня отличный день, чтобы сделать пост в телеграме ;)"
    ],
    "mid": [
        "Все еще жду...",
        "Не хочу показаться навязчивым, но поста все еще нет.",
        "Будет пост?",
        "Ребята, вы тут?",
        "Меня хоть кто-нибудь слушает? ПОСТОВ НЕ БЫЛО ДАВНО.",
        "Я знаю, вам это не нравится, но кто-то должен это сделать."
    ],
    "end": [
        "Ну наконец-то!",
        "Хорошая работа, парни.",
        "Так-то лучше.",
        "Молодцы, я доволен."
    ]
}

CHAT_ID = ""
notifier = CodexTelegramNotifier(f"https://notify.bot.codex.so/u/{CHAT_ID}", WORDPOOL)
notifier.start_notification()
notifier.send_message_with_delay(5)
notifier.end_notification()
