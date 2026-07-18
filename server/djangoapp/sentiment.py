import re

POSITIVE_WORDS = {
    'amazing', 'awesome', 'best', 'clean', 'excellent', 'fantastic', 'fast',
    'friendly', 'good', 'great', 'helpful', 'honest', 'love', 'professional',
    'recommend', 'smooth', 'supportive', 'wonderful',
}
NEGATIVE_WORDS = {
    'awful', 'bad', 'delay', 'dishonest', 'horrible', 'poor', 'rude', 'slow',
    'terrible', 'unhelpful', 'worst',
}


def analyze_sentiment(text):
    words = set(re.findall(r"[a-z']+", (text or '').lower()))
    score = len(words & POSITIVE_WORDS) - len(words & NEGATIVE_WORDS)
    if score > 0:
        return 'positive'
    if score < 0:
        return 'negative'
    return 'neutral'
