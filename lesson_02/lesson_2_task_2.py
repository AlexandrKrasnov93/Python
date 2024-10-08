def is_year_leap(year):
    # return year % 4 == 0
    return f"год {year}: {year % 4 == 0}"


print(is_year_leap(2024))
print(is_year_leap(2023))
print(is_year_leap(2022))
print(is_year_leap(2021))
print(is_year_leap(2020))
