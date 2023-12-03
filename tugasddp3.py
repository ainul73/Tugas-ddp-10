def filter_konsonan(input_string):
    konsonan = [char for char in input_string if char.isalpha() and char.lower() not in ['a', 'e', 'i', 'o', 'u']]
    return ''.join(konsonan)

# Penggunaan
hasil = filter_konsonan("Nurul Fikri")
print("Hasilnya:", hasil)