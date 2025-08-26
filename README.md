# News_Summarizer_GUI
A Python desktop application with a graphical user interface (GUI) to quickly summarize news articles from any URL.

This project is a news summarizer application built with Python and the Tkinter library. It provides a user-friendly interface to help you quickly digest online articles. Users can simply paste the URL of a news article, specify a word limit, and receive a concise summary along with sentiment analysis. The tool is designed to save time and help users stay informed in a fast-paced world.

Features:
This application's key features include its intuitive graphical user interface for easy operation and the ability to summarize any online news article from a URL. It offers a customizable summary length, allowing users to set a specific word limit for the output. In addition to summarization, it performs sentiment analysis on the article's text, classifying it as positive, negative, or neutral. The application also extracts and displays key metadata, including the article's title, author(s), and publication date, and maintains a history of summarized articles for easy recall.

Software Requirements:
To run this project, you will need Python 3 installed on your system. The application also depends on several Python libraries which can be installed via pip: tkinter (usually included with Python), newspaper3k for article scraping and summarization, and textblob for sentiment analysis. The Natural Language Toolkit (nltk) is also required, specifically the 'punkt' tokenizer package.

Getting Started:
Follow these instructions to get the project set up and running on your local machine.

1. Installation:
First, ensure you have Python 3 installed. Then, open your terminal or command prompt and install the required libraries using pip by running the command: pip install newspaper3k textblob. After the installation, you need to download the necessary data for the NLTK library. Run Python from your terminal and enter the following commands: import nltk followed by nltk.download('punkt'). This will download the tokenizer models required for processing the articles.

2. Usage:
To run the application, navigate to the project directory in your terminal and execute the script with the command: python new.py. The application window will open, presenting you with an input field for a URL and another for a word limit. Paste the URL of the news article you wish to summarize, adjust the word limit if desired, and click the "Summarize" button. The application will fetch the article and display the title, author, publication date, summary, and sentiment analysis in the designated fields. You can also view previously summarized articles by clicking the "History" button.

How It Works:
The application's backend logic is powered by two main libraries. When a user provides a URL and clicks "Summarize," the newspaper3k library is used to download the webpage, parse the HTML, and extract key content like the article's full text, title, authors, and publication date. It also generates an initial summary using its built-in NLP capabilities. The full text of the article is then passed to the TextBlob library, which performs sentiment analysis to determine the polarity of the content. The final summary is truncated to the user-specified word limit and, along with all other extracted data, is displayed in the Tkinter GUI. To ensure the user interface remains responsive, the entire fetching and processing task is handled in a separate thread.

License:
This project is open source. Feel free to use, modify, and distribute it.
