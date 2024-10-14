from mailing import Mailing
from address import Address

mailing = Mailing(
    to_address=Address("428000", "Канаш", "Мира", "66", "61"),
    from_address=Address("968354", "Москва", "Новая", "3а", "71"),
    cost=780,
    track="RN587946"
)

print(mailing)
