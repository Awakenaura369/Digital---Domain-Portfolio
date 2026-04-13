import os
import json
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def run_engine():
    topics = [
        "The future of Domain Flipping in the AI era",
        "How LLaMA-3 is disrupting Digital Marketing agencies",
        "SEO strategies for voice search and AI assistants",
        "Top 5 high-value domain niches for 2027",
        "Building lightweight funnels with Python and Groq",
        "The role of blockchain in digital asset ownership",
        "Automating social media hooks with Large Language Models",
        "Why conversation-driven marketing beats influencer ads"
    ]
    
    generated_articles = []
    
    for topic in topics:
        try:
            print(f"Generating Long Article for: {topic}")
            completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system", 
                        "content": """You are an expert SEO strategist. 
                        Return ONLY a JSON object with:
                        - 'title': Catchy SEO title.
                        - 'category': One word (Marketing, AI, or Domains).
                        - 'snippet': A short 15-word preview.
                        - 'full_content': A detailed article (300+ words) formatted with HTML tags like <p> and <h3> for readability."""
                    },
                    {"role": "user", "content": f"Write a professional deep-dive article about: {topic}"}
                ],
                model="llama-3.3-70b-versatile",
                response_format={"type": "json_object"}
            )
            data = json.loads(completion.choices[0].message.content)
            generated_articles.append(data)
        except Exception as e:
            print(f"Error: {e}")

    with open('articles.json', 'w', encoding='utf-8') as f:
        json.dump(generated_articles, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    run_engine()
