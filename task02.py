
import requests 
from collections import Counter
import matplotlib.pyplot as plt

# Задана URL-адреса для завантаження тексту
url = 'https://basket.com.ua/'

# Отримуємо вміст з URL-адреси
response = requests.get(url)
text = response.text

# Розділяємо текст на окремі слова (можливо, потрібно додатково обробити пунктуацію)
words = text.lower().split()

# Підраховуємо кількість входжень кожного слова
word_counts = Counter(words)

# Вибираємо топ N слів (наприклад, 10)
top_n = 10
top_words = word_counts.most_common(top_n)

# Візуалізуємо топ-слова
plt.figure(figsize=(10, 6))
plt.bar([word for word, count in top_words], [count for word, count in top_words])
plt.xlabel('Слова')
plt.ylabel('Частота використання')
plt.title(f'Топ-{top_n} слів у тексті')
plt.xticks(rotation=45)
plt.show()
