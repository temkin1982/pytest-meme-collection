url = "http://localhost:3000/automation-lab/subscription"
promo = [
    ("BASIC199", "Промокод только для: Базовый"),
    ("WELCOME10", "Промокод истек 31.12.2024"),
]
ids = ["BASIC199-promo code only for: Basic", "WELCOME10-expired"]


test_card = [
    (
        "4111 1111 1111 1111",
        "1229",
        "123",
        '[class="success-title"]',
        "Успешно!",
    ),
    (
        "5555 5555 5555 4444",
        "1229",
        "234",
        '[class="success-title"]',
        "Успешно!",
    ),
    (
        "3782 822463 10005",
        "1229",
        "1234",
        '[class="success-title"]',
        "Успешно!",
    ),
    (
        "4000 0000 0000 0002",
        "1229",
        "123",
        "card-errors",
        "Карта отклонена. Попробуйте другую карту",
    ),
    (
        "4000 0000 0000 9995",
        "1229",
        "123",
        "card-errors",
        "Недостаточно средств на карте",
    ),
]

res = [
    "tc-01-Critical",
    "tc-02-Critical",
    "tc-03-Critical",
    "tc-04-Major",
    "tc-05-Major",
]
