import os
import json
from groq import Groq

# حط الـ API Key ديالك هنا
client = Groq(api_key="YOUR_GROQ_API_KEY")

def generate_articles(topics):
    articles = []
    
    for topic in topics:
        print(f"Generating article for: {topic}...")
        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional SEO content writer. Return ONLY a JSON object with 'title', 'category', and 'snippet' keys in Arabic."
                },
                {
                    "role": "user",
                    "content": f"Write a catchy SEO title and a 2-sentence summary about: {topic}",
                }
            ],
            model="llama-3.3-70b-versatile", # أحسن موديل فـ Groq حالياً
            response_format={"type": "json_object"}
        )
        
        # تحويل الاستجابة لـ Dictionary
        content = json.loads(chat_completion.choices[0].message.content)
        articles.append(content)

    # حفظ النتائج فملف JSON للموقع
    with open('articles.json', 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)
    
    print("Done! articles.json is ready.")

# جرب السكريبت بهاد المواضيع
my_topics = [
    "كيفاش تبيع دومينات فـ 2026",
    "أهمية Backlinks للسيو المحلي",
    "استخدام الذكاء الاصطناعي فـ التسويق"
]

generate_articles(my_topics)
