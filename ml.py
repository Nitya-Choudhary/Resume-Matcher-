from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = TfidfVectorizer(stop_words='english')

def match_resume_to_job(resume: str, jobDesc: str):
    documents = [resume, jobDesc]
    vectors = vectorizer.fit_transform(documents)
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    remark = "Excellent Fit 🔥" if similarity > 0.7 else "Moderate Fit ✅" if similarity > 0.4 else "Needs Improvement ⚠️"

    return [{
        "skillMatchScore": float(similarity),
        "remarks": remark
    }]
