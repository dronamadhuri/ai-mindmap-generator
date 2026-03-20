from transformers import pipeline
import re

# summarizer
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# text generator (for smart explanations)
generator = pipeline("text-generation", model="gpt2")

def extract_keywords(text):
    words = re.findall(r'\b[A-Za-z]{4,}\b', text)
    return list(set(words))[:3]

def generate_ai_points(keyword, context):
    try:
        prompt = f"Explain {keyword} in simple terms:"

        result = generator(
            prompt,
            max_length=40,
            num_return_sequences=2
        )

        points = []
        for r in result:
            text = r['generated_text'].replace(prompt, "").strip()
            clean = text.split(".")[0]
            if clean:
                points.append(clean)

        return points if points else [f"{keyword} is an important concept"]

    except:
        return [f"{keyword} is important in the context"]

def process_text(text):
    text = text[:2000]

    summary = summarizer(
        text,
        max_length=120,
        min_length=40,
        do_sample=False
    )[0]['summary_text']

    sentences = [s.strip() for s in summary.split(".") if s.strip()]

    structured = {
        "main_topic": "Document",
        "categories": []
    }

    for sentence in sentences:
        keywords = extract_keywords(sentence)

        subtopics = []
        for key in keywords:
            points = generate_ai_points(key, text)

            subtopics.append({
                "name": key,
                "points": points
            })

        structured["categories"].append({
            "name": sentence[:25],
            "subtopics": subtopics
        })

    return {
        "summary": summary,
        "structure": structured
    }