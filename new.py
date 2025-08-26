import tkinter as tk
from tkinter import messagebox
from newspaper import Article
from textblob import TextBlob
import ssl
import nltk
import threading

ssl._create_default_https_context = ssl._create_unverified_context

nltk.download('punkt')

history = []

def summarize():
    url = utext.get().strip()
    word_limit = int(word_limit_entry.get().strip())
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL.")
        return

    def fetch_and_summarize():
        try:
            article = Article(url)
            article.download()
            article.parse()
            article.nlp()
            
            title_text = article.title
            author_text = ", ".join(article.authors) if article.authors else "N/A"
            publication_date_text = str(article.publish_date) if article.publish_date else "N/A"
            summary_text = ' '.join(article.summary.split()[:word_limit])
            analysis = TextBlob(article.text)
            polarity = analysis.polarity
            sentiment_text = f'Polarity: {polarity}, Sentiment: {"positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"}'

            history.append((title_text, author_text, publication_date_text, summary_text, sentiment_text))

            root.after(0, lambda: update_gui(title_text, author_text, publication_date_text, summary_text, sentiment_text))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    thread = threading.Thread(target=fetch_and_summarize)
    thread.start()

def update_gui(title_text, author_text, publication_date_text, summary_text, sentiment_text):
    title.config(state='normal')
    title.delete('1.0', 'end')
    title.insert('1.0', title_text)
    title.config(state='disabled')

    Author.config(state='normal')
    Author.delete('1.0', 'end')
    Author.insert('1.0', author_text)
    Author.config(state='disabled')

    publication.config(state='normal')
    publication.delete('1.0', 'end')
    publication.insert('1.0', publication_date_text)
    publication.config(state='disabled')

    summary.config(state='normal')
    summary.delete('1.0', 'end')
    summary.insert('1.0', summary_text)
    summary.config(state='disabled')

    sentiment.config(state='normal')
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', sentiment_text)
    sentiment.config(state='disabled')

def show_history():
    if not history:
        messagebox.showinfo("History", "No history available.")
        return

    history_window = tk.Toplevel(root)
    history_window.title("History")
    history_window.configure(bg='#2E2E2E')

    history_label = tk.Label(history_window, text="History", font=("Helvetica", 16, "bold"), bg='#2E2E2E', fg='#FFFFFF')
    history_label.pack(pady=10)

    for idx, item in enumerate(history, start=1):
        title_text, author_text, publication_date_text, _, _ = item
        article_frame = tk.Frame(history_window, bg='#3E3E3E', padx=10, pady=10)
        article_frame.pack(pady=5, fill='x')

        article_info = f"{idx}. Title: {title_text}\n   Author: {author_text}\n   Publication Date: {publication_date_text}\n\n"
        article_label = tk.Label(article_frame, text=article_info, justify='left', bg='#3E3E3E', fg='#FFFFFF', font=("Helvetica", 12))
        article_label.pack()

def about_page():
    about_window = tk.Toplevel(root)
    about_window.title("About")
    about_window.geometry("600x400")
    about_window.configure(bg='#2E2E2E')

    about_label = tk.Label(about_window, text="Welcome to News Summarizer, your ultimate tool for staying informed in today's fast-paced world. With the overwhelming amount of information available online, it can be challenging to keep up with the latest news and developments. News Summarizer is here to help you tackle this challenge head-on by providing quick and concise summaries of news articles from various sources.\n\nOur mission is to empower users with the ability to stay updated on current events efficiently, saving valuable time without compromising on the depth of information. Whether you're a busy professional trying to stay informed during your hectic schedule or simply looking for a convenient way to catch up on the news, News Summarizer is the perfect tool for you.\n\nPowered by advanced natural language processing techniques, News Summarizer extracts key information from news articles and presents it in an easily digestible format. It utilizes the Newspaper library for article extraction and TextBlob for sentiment analysis, ensuring accurate and informative summaries.\n\nExperience the convenience of News Summarizer today and elevate your news reading experience to a whole new level!\n\nIn addition to its powerful summarization capabilities, News Summarizer offers a user-friendly interface that allows users to quickly enter the URL of any news article they want to summarize. The application then retrieves the article, analyzes its content, and generates a concise summary along with sentiment analysis.\n\nMoreover, News Summarizer keeps track of your summarization history, enabling you to revisit previously summarized articles whenever you need them. This feature allows users to maintain a record of their reading habits and access important information conveniently.\n\nBut News Summarizer is more than just a summarization tool. It's a platform for knowledge discovery and exploration. Dive deep into the world of news and uncover hidden insights that can shape your understanding of the world around you. With News Summarizer, the possibilities are endless.\n\nJoin the thousands of users who have already embraced News Summarizer as their go-to tool for staying informed. Whether you're a student, a professional, or just someone who loves to stay updated on current events, News Summarizer has something for everyone.\n\nBut don't just take our word for it. Try News Summarizer today and see the difference for yourself. We're confident that once you experience the convenience and efficiency of News Summarizer, you'll wonder how you ever lived without it.\n\nOur team is dedicated to continuously improving News Summarizer based on user feedback. We're committed to providing you with the best possible experience and ensuring that News Summarizer remains a valuable tool for staying informed in today's fast-paced world.\n\nThank you for choosing News Summarizer. We look forward to serving you and helping you stay informed for years to come!", 
    font=("Helvetica", 12), bg='#2E2E2E', fg='#FFFFFF', justify="left", wraplength=600)
    about_label.pack(pady=20, padx=20)

def contact_page():
    contact_window = tk.Toplevel(root)
    contact_window.title("Contact")
    contact_window.geometry("400x200")
    contact_window.configure(bg='#2E2E2E')

    contact_label = tk.Label(contact_window, text="News Summariser Project\n By Dhruv Dhariwal", font=("Helvetica", 12), bg='#2E2E2E', fg='#FFFFFF')
    contact_label.pack(pady=20)

def on_enter(event):
    event.widget.config(fg='darkgreen', cursor='hand2', underline=True, font=("Helvetica", 16, "bold"))

def on_leave(event):
    event.widget.config(fg='white', underline=False)

root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x700')
root.configure(bg='#2E2E2E')

header_frame = tk.Frame(root, bg='#4E4E4E', relief='solid', borderwidth=2)
header_frame.pack(pady=20, fill='x', padx=20)

left_label = tk.Label(header_frame, text="News Summarizer", font=("Helvetica", 24, "bold"), bg='#4E4E4E', fg='white')
left_label.pack(side=tk.LEFT, padx=10)

middle_frame = tk.Frame(header_frame, bg='#4E4E4E')
middle_frame.pack(side=tk.LEFT, fill='x', padx=20)

home_button = tk.Label(middle_frame, text="Home", bg='#4E4E4E', fg="white", font=("Helvetica", 16))
home_button.pack(side=tk.LEFT, padx=(50, 10))
home_button.bind("<Enter>", on_enter)
home_button.bind("<Leave>", on_leave)

about_button = tk.Label(middle_frame, text="About", bg='#4E4E4E', fg="white", font=("Helvetica", 16))
about_button.pack(side=tk.LEFT, padx=10)
about_button.bind("<Enter>", on_enter)
about_button.bind("<Leave>", on_leave)
about_button.bind("<Button-1>", lambda event: about_page())

contact_button = tk.Label(middle_frame, text="Contact", bg='#4E4E4E', fg="white", font=("Helvetica", 16))
contact_button.pack(side=tk.LEFT, padx=10)
contact_button.bind("<Enter>", on_enter)
contact_button.bind("<Leave>", on_leave)
contact_button.bind("<Button-1>", lambda event: contact_page())

history_btn = tk.Button(header_frame, text="History", command=show_history, bg="lightgreen", fg="black", borderwidth=0, padx=10, pady=5, relief='flat')
history_btn.pack(side=tk.RIGHT)

frame = tk.Frame(root, bg='#2E2E2E')
frame.pack(pady=10)

url_label = tk.Label(frame, text="URL:", bg='#2E2E2E', fg='#FFFFFF', font=("Helvetica", 14))
url_label.grid(row=0, column=0, padx=(10, 0))

utext = tk.Entry(frame, width=70, relief='solid', bd=1, highlightthickness=0, bg='#CCCCCC', font=("Helvetica", 12))
utext.grid(row=0, column=1, padx=(0, 10), ipady=5)

word_limit_label = tk.Label(frame, text="Word Limit:", bg='#2E2E2E', fg='#FFFFFF', font=("Helvetica", 14))
word_limit_label.grid(row=0, column=2, padx=(10, 0))

word_limit_entry = tk.Entry(frame, width=10, relief='solid', bd=1, highlightthickness=0, bg='#CCCCCC', font=("Helvetica", 12))
word_limit_entry.grid(row=0, column=3, padx=(0, 10), ipady=5)
word_limit_entry.insert(0, "100")

btn = tk.Button(frame, text="Summarize", command=summarize, bg="lightgreen", fg="black", padx=10, pady=5, relief='flat', highlightthickness=0, borderwidth=0)
btn.grid(row=0, column=4, padx=(0, 10))
btn.config(border=5)

info_frame = tk.Frame(root, bg='#2E2E2E')
info_frame.pack(pady=10)

labels = ["Title:", "Author:", "Publication Date:", "Summary:", "Sentiment:"]
for i, label_text in enumerate(labels):
    label = tk.Label(info_frame, text=label_text, font=("Helvetica", 14, "bold"), bg='#2E2E2E', fg='#FFFFFF')
    label.grid(row=i, column=0, sticky="w", padx=(10, 0), pady=5)

title = tk.Text(info_frame, height=2, width=80, state='disabled', bg='#CCCCCC', font=("Helvetica", 12))
title.grid(row=0, column=1, columnspan=2, pady=5)

Author = tk.Text(info_frame, height=2, width=80, state='disabled', bg='#CCCCCC', font=("Helvetica", 12))
Author.grid(row=1, column=1, columnspan=2, pady=5)

publication = tk.Text(info_frame, height=2, width=80, state='disabled', bg='#CCCCCC', font=("Helvetica", 12))
publication.grid(row=2, column=1, columnspan=2, pady=5)

summary = tk.Text(info_frame, height=20, width=80, state='disabled', bg='#CCCCCC', font=("Helvetica", 12))
summary.grid(row=3, column=1, columnspan=2, pady=5)

sentiment = tk.Text(info_frame, height=2, width=80, state='disabled', bg='#CCCCCC', font=("Helvetica", 12))
sentiment.grid(row=4, column=1, columnspan=2, pady=5)

root.mainloop()
