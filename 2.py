a = int(input())
miles = (a * 38241) + 16637000000
km = miles * 1.609344
km = round(km)
astr_ed = km / (149597870700 * 0.01)
astr_ed = round(astr_ed, 3)
t = ((km * 100) / 299792458) / 360
t = round(t)
print('Расстояние до «Вояджера-1» от Солнца для указанной даты составит :', miles, 'миль,', km, ' километров,', astr_ed,
      'астрономических единиц. Задержка беспроводной связи составит :', t, 'часов')
