from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iphone XS", "+79176775651"))
catalog.append(Smartphone("Honor", "Magic6 Pro 12", "+79175653596"))
catalog.append(Smartphone("Samsung", "Galaxy Tab 8", "+79274786378"))
catalog.append(Smartphone("Oppo", "Reno 10", "+79051977166"))
catalog.append(Smartphone("Sony", "Xperia 1V", "+79080023504"))

for smartphone in catalog:
    print(smartphone)
