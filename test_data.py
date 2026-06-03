memes = [
    ("Эффект Долиной", "ситуация", 5001, "Success"),
    ("Ты адекватная? А ниче тот факт, что…", "видео", 23233, "Success"),
    (111, "ситуация", 5001, "title должен быть строкой"),
    ("", 11, "s", "category должен быть строкой"),
    (111, 111, "5001", "title должен быть строкой"),
    (
        "Ты адекватная? А ниче тот факт, что…",
        "ситуация",
        -1,
        "likes не должен быть отрицательным",
    ),
    ("", "ситуация", 5001, "title не должен быть пустым"),
    ("Эффект Долиной!", "", 5001, "category не должен быть пустым"),
]

ids = [
    "valid-meme-success",
    "valid-meme-big-likes-success",
    "title-not-string-error",
    "category-not-string-error",
    "title-and-likes-wrong-type-error",
    "likes-negative-error",
    "title-empty-error",
    "category-empty-error",
]
