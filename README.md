# 🔍 NLP Web Crawler - Smart Search Engine

A Python-based web application that uses **Natural Language Processing (NLP)** and **DuckDuckGo API** to search the web and provide summarized, relevant results from top websites.

## 📋 Features

✅ **DuckDuckGo Integration** - Search across the entire web  
✅ **NLP Processing** - Advanced text analysis using spaCy and NLTK  
✅ **Smart Summarization** - Get condensed summaries of web content  
✅ **Web Crawler** - Fetch and extract text from webpages  
✅ **Beautiful Web UI** - Modern, responsive Flask-based interface  
✅ **Fast & Lightweight** - Quick search results with intelligent filtering  
✅ **BCA Minor Project Ready** - Complete documentation and code  

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/myworldcrazy65/Web-crawler-.git
cd Web-crawler-
```

2. **Create a virtual environment** (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download NLP models**
```bash
python -m spacy download en_core_web_sm
```

5. **Run the application**
```bash
python app.py
```

6. **Open in browser**
Navigate to: `http://localhost:5000`

## 📦 Project Structure

```
Web-crawler-/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Web UI
├── README.md             # This file
└── .gitignore           # Git ignore rules
```

## 🛠️ How It Works

### 1. **Search Processing**
- User enters a query in the web interface
- Flask backend receives the search request

### 2. **DuckDuckGo Search**
- Searches using DuckDuckGo API (no API key required!)
- Retrieves top 5 results with titles, URLs, and snippets

### 3. **Web Crawling**
- Fetches full webpage content from each result
- Extracts text using BeautifulSoup
- Removes scripts, styles, and unnecessary elements

### 4. **NLP Summarization**
- Uses NLTK for sentence tokenization
- Uses spaCy for named entity recognition and linguistic analysis
- Calculates word frequency and sentence importance scores
- Generates 2-3 sentence summaries

### 5. **Results Display**
- Returns organized results with:
  - Title and clickable URL
  - Source domain
  - Original snippet
  - AI-generated summary
  - Full webpage link

## 📝 API Endpoints

### POST /search
Search the web with NLP processing

**Request:**
```json
{
  "query": "your search query"
}
```

**Response:**
```json
{
  "success": true,
  "query": "your search query",
  "count": 5,
  "results": [
    {
      "title": "Result Title",
      "url": "https://example.com",
      "snippet": "Original snippet from search",
      "summary": "AI-generated summary",
      "source": "example.com"
    }
  ]
}
```

### GET /health
Health check endpoint

## 🎓 For BCA Project

### Project Components:

1. **Web Framework**: Flask (Python)
2. **NLP Libraries**: 
   - NLTK (Natural Language Toolkit)
   - spaCy (Industrial NLP)
3. **Web Scraping**: BeautifulSoup, Requests
4. **Search API**: DuckDuckGo Search
5. **Frontend**: HTML, CSS, JavaScript (Vanilla)

### Key Algorithms:

- **Text Summarization**: TF-IDF-based sentence scoring
- **Named Entity Recognition**: Using spaCy
- **Stopword Filtering**: NLTK stopwords
- **Web Crawling**: HTTP requests + HTML parsing

## 🔧 Configuration

Edit `app.py` to customize:
- Number of search results: Change `num_results=5` parameter
- Summarization length: Adjust `num_sentences=2` parameter
- Flask host/port: Modify the last line in `app.py`

## 📚 Dependencies

| Library | Purpose |
|---------|---------|
| Flask | Web framework |
| requests | HTTP requests |
| beautifulsoup4 | HTML parsing |
| duckduckgo-search | Search engine API |
| nltk | NLP toolkit |
| spacy | Advanced NLP |
| newspaper3k | Article extraction |

## 🐛 Troubleshooting

### spaCy model not found
```bash
python -m spacy download en_core_web_sm
```

### NLTK data not found
Models are auto-downloaded on first run, but if issues persist:
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

### Port 5000 already in use
Change the port in `app.py` (last line):
```python
app.run(debug=True, host='127.0.0.1', port=5001)
```

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

Created for BCA Minor Project - 2026

---

**Made with ❤️ using Python, Flask, and NLP**
