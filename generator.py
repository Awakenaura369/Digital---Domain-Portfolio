import os
import json
from groq import Groq

# Ensure your secret GROQ_API_KEY is set in GitHub
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def run_engine():
    # Diversified SEO-friendly topics for 2026
    topics = [
        "The future of Domain Flipping in the AI era",
        "How Llama-3 is disrupting Digital Marketing agencies",
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
            print(f"Generating SEO content for: {topic}")
            completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system", 
                        "content": "You are an expert SEO content strategist. Return ONLY a JSON object with 'title' (catchy), 'snippet' (informative 2-sentence summary), and 'category' (e.g., Marketing, AI, Domains)."
                    },
                    {"role": "user", "content": f"Create a viral SEO post about: {topic}"}
                ],
                model="llama-3.3-70b-versatile",
                response_format={"type": "json_object"}
            )
            # Parse response
            data = json.loads(completion.choices[0].message.content)
            generated_articles.append(data)
        except Exception as e:
            print(f"Failed to generate {topic}: {e}")

    # Output to the JSON file that the website reads
    with open('articles.json', 'w', encoding='utf-8') as f:
        json.dump(generated_articles, f, ensure_ascii=False, indent=4)
    
    print("AI Articles successfully generated in English!")

if __name__ == "__main__":
    run_engine()
