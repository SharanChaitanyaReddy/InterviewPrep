# Week 23 – Month 6: Advanced RAG, LLM Fine-Tuning & Real-World AI Applications

**Objective:**  
Understand advanced retrieval and ranking strategies. Learn fine-tuning LLMs for domain-specific tasks. Apply AI/ML in real-world scenarios with performance considerations.

---

## Folder Structure for Code / Examples

```
Code/python/week-23/
├── day-01-advanced-retrieval/
├── day-02-ranking-and-augmentation/
├── day-03-llm-fine-tuning/
├── day-04-evaluation-metrics/
├── day-05-real-world-ai-system/
└── day-06-week-review-postmortem/
```

---

## Day 1: Advanced Retrieval Techniques

**Topics:**
- Dense vs sparse retrieval  
- Hybrid retrieval (BM25 + embeddings)  
- Semantic search improvements  

**Dependencies:** Week 22 (RAG introduction, embedding & retrieval pipelines)  
**Code Folder:** `Code/python/week-23/day-01-advanced-retrieval/`  
**Documentation Link:** `06-AI-Foundations/nlp-and-llms.md`  

**Hands-on Examples:**
- Implement hybrid retrieval combining BM25 + embeddings  
- Compare results with simple embedding-only search  
- Annotate impact on retrieval accuracy & latency

---

## Day 2: Ranking & Augmentation

**Topics:**
- Re-ranking retrieved documents  
- Using LLMs for contextual augmentation  
- Importance of top-k vs top-n retrieval  

**Dependencies:** Day 1  
**Code Folder:** `Code/python/week-23/day-02-ranking-and-augmentation/`  
**Documentation Link:** `06-AI-Foundations/system-design-for-ai.md`  

**Hands-on Examples:**
- Implement re-ranking using LLM scoring  
- Experiment with different top-k values and measure quality  
- Annotate why re-ranking improves generation

---

## Day 3: LLM Fine-Tuning

**Topics:**
- Domain adaptation via fine-tuning  
- Methods: full model, LoRA, adapters  
- Cost vs performance trade-offs  

**Dependencies:** Week 22 (LLM basics, prompt engineering)  
**Code Folder:** `Code/python/week-23/day-03-llm-fine-tuning/`  
**Documentation Link:** `06-AI-Foundations/nlp-and-llms.md`  

**Hands-on Examples:**
- Fine-tune a small LLM on domain-specific text  
- Test prompt + fine-tuning combination  
- Document accuracy improvements & latency effects

---

## Day 4: Evaluation Metrics

**Topics:**
- Retrieval metrics: precision, recall, F1  
- Generation metrics: BLEU, ROUGE, embedding-based similarity  
- Trade-offs between automated metrics and human evaluation  

**Dependencies:** Days 1–3  
**Code Folder:** `Code/python/week-23/day-04-evaluation-metrics/`  
**Documentation Link:** `06-AI-Foundations/ai-mental-models.md`  

**Hands-on Examples:**
- Compute retrieval + generation metrics for RAG system  
- Compare baseline vs fine-tuned LLM performance  
- Annotate which metrics matter in production

---

## Day 5: Real-World AI System Design

**Topics:**
- End-to-end RAG + LLM deployment  
- Scaling considerations: latency, throughput, memory  
- Monitoring & logging for AI systems  

**Dependencies:** Days 1–4  
**Code Folder:** `Code/python/week-23/day-05-real-world-ai-system/`  
**Documentation Link:** `05-System-Design/case-studies/feed-system.md`  

**Hands-on Examples:**
- Build mini AI service: query → retrieval → generation → response  
- Implement simple logging & monitoring  
- Document system trade-offs for production readiness

---

## Day 6: Week Review & Postmortem

**Topics:**
- Consolidate Week 23 AI concepts  
- Identify weak spots & revisit previous weeks’ concepts  
- Update code → weekly MD → documentation links  

**Dependencies:** Days 1–5  
**Code Folder:** `Code/python/week-23/day-06-week-review-postmortem/`  
**Documentation Link:** `Revision/weekly-review.md`  

**Hands-on Examples:**
- Test end-to-end RAG + fine-tuned LLM system  
- Document lessons learned, metrics, improvements

---

## Daily Execution Rules (Non-Negotiable)

- 90 minutes/day minimum  
- Concept → Diagram → Code → Documentation → Postmortem  
- Commit code + notes at end of each day  
- Maintain links to weekly MD + documentation

---

## ✅ Outcome of Week 23

- Advanced understanding of RAG, re-ranking, fine-tuning  
- End-to-end AI system ready for deployment experimentation  
- Clear linkage of concepts → code → documentation → revision
