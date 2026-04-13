import os
import json
from groq import Groq

# الساروت كيجي من GitHub Secrets
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def generate_data():
    # المواضيع لي بغيتي تولد عليها مقالات
    topics = [
        "أهمية الدومينات المميزة في 2026",
        "كيف تبيع خدمات السيو للمقاولات الصغرى",
        "مستقبل التسويق بالذكاء الاصطناعي"
    ]
    
    results = []
    
    for t in topics:
        try:
            print(f"Generating: {t}")
            completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "Return ONLY a JSON object with 'title', 'snippet', and 'category' keys in Arabic."},
                    {"role": "user", "content": t}
                ],
                model="llama-3.3-70b-versatile",
                response_format={"type": "json_object"}
            )
            results.append(json.loads(completion.choices[0].message.content))
        except Exception as e:
            print(f"Error: {e}")

    # حفظ النتائج
    with open('articles.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    generate_data()
