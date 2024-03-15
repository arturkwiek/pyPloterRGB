import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Funkcja do konwersji wartości R, G, B
def remove_label_convert_int(value):
    return int(value.split(': ')[1])

# Ścieżka do pliku CSV z danymi
file_path = "2024_03_15.csv"

# Wczytanie danych, stosując funkcję konwersji do odpowiednich kolumn
data = pd.read_csv(
    file_path,
    converters={
        ' R': remove_label_convert_int,
        ' G': remove_label_convert_int,
        ' B': remove_label_convert_int
    }
)

# Zmiana nazw kolumn, usunięcie początkowych spacji
data.columns = ['Timestamp', 'R', 'G', 'B']

# Konwersja kolumny 'Timestamp' na typ datetime i ustawienie jej jako indeks DataFrame
data['Timestamp'] = pd.to_datetime(data['Timestamp'])
data.set_index('Timestamp', inplace=True)

# Rysowanie wykresów dla składowych R, G, B
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['R'], label='R', color='red')
plt.plot(data.index, data['G'], label='G', color='green')
plt.plot(data.index, data['B'], label='B', color='blue')

# Formatowanie osi X do wyświetlania daty i godziny
plt.gca().xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))

# Dodanie legendy, tytułu i etykiet osi
plt.legend()
plt.title('Zmiany wartości RGB w czasie' + file_path)
plt.xlabel('Czas')
plt.ylabel('Wartość składowych RGB')

# Obrócenie etykiet na osi X dla lepszej czytelności
plt.xticks(rotation=45)

# Wyświetlenie wykresu
plt.tight_layout()
plt.show()
