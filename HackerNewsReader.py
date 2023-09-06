import tkinter as tk
import requests

def get_top_hacker_news():
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    response = requests.get(url)
    top_story_ids = response.json()
    
    top_news_text.delete(1.0, tk.END)  # Lösche vorherige Top-Nachrichten
    for story_id in top_story_ids[:10]:  # Zeige die ersten 10 Top-Nachrichten
        story_url = f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json'
        story_response = requests.get(story_url)
        story_data = story_response.json()
        
        title = story_data.get('title')
        url = story_data.get('url')
        score = story_data.get('score')
        
        top_news_text.insert(tk.END, f'Titel: {title}\n')
        top_news_text.insert(tk.END, f'URL: {url}\n')
        top_news_text.insert(tk.END, f'Punktzahl: {score}\n')
        top_news_text.insert(tk.END, '-' * 30 + '\n')

# Erstelle das Hauptfenster
root = tk.Tk()
root.title("HN Top News Viewer")

# Schaltfläche zum Abrufen der Top-Nachrichten
get_top_news_button = tk.Button(root, text="Top-Nachrichten anzeigen", command=get_top_hacker_news)
get_top_news_button.pack()

# Textfeld für die Top-Nachrichten
top_news_text = tk.Text(root, wrap=tk.WORD, width=60, height=20)
top_news_text.pack()

# Starte die GUI-Schleife
root.mainloop()
