from flask import Flask, render_template, request, jsonify
import requests
from duckduckgo_search import DDGS
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import spacy
from urllib.parse import urlparse
import time

app = Flask(__name__)

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading spaCy model...")
    import subprocess
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

class NLPSearcher:
    def __init__(self):
        self.ddgs = DDGS()
        self.stop_words = set(stopwords.words('english'))
    
    def search_duckduckgo(self, query, num_results=5):
        """Search using DuckDuckGo API"""
        try:
            results = []
            ddg_results = self.ddgs.text(query, max_results=num_results)
            
            for result in ddg_results:
                results.append({
                    'title': result.get('title', 'No Title'),
                    'url': result.get('href', ''),
                    'snippet': result.get('body', ''),
                    'source': self.extract_domain(result.get('href', ''))
                })
            return results
        except Exception as e:
            print(f"Error in DuckDuckGo search: {e}")
            return []
    
    def extract_domain(self, url):
        """Extract domain from URL"""
        try:
            return urlparse(url).netloc
        except:
            return "Unknown"
    
    def fetch_page_content(self, url):
        """Fetch and extract text content from webpage"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, timeout=5, headers=headers)
            response.encoding = 'utf-8'
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            text = soup.get_text(separator=' ', strip=True)
            return text[:1000]  # Limit to 1000 chars for summarization
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return ""
    
    def summarize_text(self, text, num_sentences=3):
        """Summarize text using NLP"""
        try:
            if not text or len(text) < 50:
                return text
            
            sentences = sent_tokenize(text)
            if len(sentences) <= num_sentences:
                return ' '.join(sentences)
            
            # Use spaCy for NLP processing
            doc = nlp(text)
            
            # Calculate sentence scores based on word frequency
            word_freq = {}
            for token in doc:
                if not token.is_stop and token.is_alpha:
                    word = token.text.lower()
                    word_freq[word] = word_freq.get(word, 0) + 1
            
            sentence_scores = {}
            for i, sent in enumerate(sentences):
                for word in sent.lower().split():
                    if word in word_freq:
                        sentence_scores[i] = sentence_scores.get(i, 0) + word_freq[word]
            
            # Get top sentences
            top_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)[:num_sentences]
            top_sentences = sorted(top_sentences, key=lambda x: x[0])
            
            summary = ' '.join([sentences[i] for i, _ in top_sentences])
            return summary
        except Exception as e:
            print(f"Error in summarization: {e}")
            return text[:200]
    
    def process_query(self, query, num_results=5):
        """Main processing function"""
        # Search with DuckDuckGo
        search_results = self.search_duckduckgo(query, num_results)
        
        processed_results = []
        for result in search_results:
            # Fetch full content
            content = self.fetch_page_content(result['url'])
            
            # Summarize
            summary = self.summarize_text(content, num_sentences=2)
            
            processed_results.append({
                'title': result['title'],
                'url': result['url'],
                'snippet': result['snippet'],
                'summary': summary if summary else result['snippet'],
                'source': result['source']
            })
            
            time.sleep(0.5)  # Rate limiting
        
        return processed_results

# Initialize searcher
searcher = NLPSearcher()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    try:
        data = request.json
        query = data.get('query', '').strip()
        
        if not query:
            return jsonify({'error': 'Please enter a search query'}), 400
        
        if len(query) < 2:
            return jsonify({'error': 'Query must be at least 2 characters'}), 400
        
        results = searcher.process_query(query, num_results=5)
        
        return jsonify({
            'success': True,
            'query': query,
            'results': results,
            'count': len(results)
        })
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'OK'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
