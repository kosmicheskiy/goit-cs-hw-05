import requests
from collections import Counter
import matplotlib.pyplot as plt

# Функція для відображення результатів
def visualize_top_words(word_counts, top_n=10):
    top_words = word_counts.most_common(top_n)
    plt.figure(figsize=(10, 6))
    plt.bar([word for word, count in top_words], [count for word, count in top_words])
    plt.xlabel('Слова')
    plt.ylabel('Частота використання')
    plt.title(f'Топ-{top_n} слів у тексті')
    plt.xticks(rotation=45)
    plt.show()

# Функція Map
def mapper(text):
    for line in text.split('\n'):
        for word in line.strip().split():
            yield word.lower(), 1

# Функція Reduce
def reducer(mapped_values):
    word_count = Counter()
    for word, count in mapped_values:
        word_count[word] += count
    return word_count

if __name__ == "__main__":
    # URL для завантаження тексту
    url = 'https://basket.com.ua/'

    # Отримуємо вміст з URL
    response = requests.get(url)
    text = response.text

    # Застосовуємо MapReduce
    mapped_values = list(mapper(text))
    word_counts = reducer(mapped_values)

    # Візуалізуємо топ-слова
    visualize_top_words(word_counts)
