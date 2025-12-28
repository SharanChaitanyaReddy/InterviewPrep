# Week 22 – Month 6: RAG, LLM Prompting & ML System Design

**Objective:**  
Understand RAG workflows and prompt engineering for LLMs. Learn to design ML/AI systems in real-world scenarios. Hands-on coding with retrieval + LLM pipelines.

---

## Folder Structure for Code / Examples

```
Code/python/week-22/
├── day-01-rag-intro/
├── day-02-prompt-engineering/
├── day-03-embedding-retrieval/
├── day-04-llm-integration/
├── day-05-ml-system-design/
└── day-06-week-review-postmortem/
```

---

## Day 1: RAG Introduction

**Topics:**
- What is Retrieval-Augmented Generation (RAG)  
- Why RAG improves LLM outputs  
- Components: Retrieval, Indexing, LLM generation  

**Dependencies:** Week 21 (LLM basics, embeddings)  
**Code Folder:** `Code/python/week-22/day-01-rag-intro/`  
**Documentation Link:** `06-AI-Foundations/system-design-for-ai.md`  

**Hands-on Examples:**
- Implement basic document retrieval using Python  
- Index small corpus & retrieve top-k relevant docs  
- Annotate RAG flow: retrieval → embedding → generation

---

## Day 2: Prompt Engineering

**Topics:**
- Basics of prompt design for LLMs  
- Zero-shot, few-shot, chain-of-thought prompting  
- How prompts influence output quality  

**Dependencies:** Day 1  
**Code Folder:** `Code/python/week-22/day-02-prompt-engineering/`  
**Documentation Link:** `06-AI-Foundations/nlp-and-llms.md`  

**Hands-on Examples:**
- Experiment with different prompts in HuggingFace or OpenAI API  
- Measure effect of prompt variations on outputs  
- Annotate when to use zero-shot vs few-shot

---

## Day 3: Embedding & Retrieval Pipelines

**Topics:**
- Advanced embeddings for RAG  
- Vector stores & similarity search  
- Integrating retrieval into LLMs  

**Dependencies:** Day 1 & Day 2  
**Code Folder:** `Code/python/week-22/day-03-embedding-retrieval/`  
**Documentation Link:** `06-AI-Foundations/nlp-and-llms.md`  

**Hands-on Examples:**
- Use FAISS or Chroma for embedding storage & search  
- Retrieve relevant documents for a query and pass to LLM  
- Annotate why embeddings improve retrieval quality

---

## Day 4: LLM Integration

**Topics:**
- Integrating LLM with retrieval pipeline  
- Generating answers from retrieved context  
- Error handling & prompt tuning  

**Dependencies:** Day 3  
**Code Folder:** `Code/python/week-22/day-04-llm-integration/`  
**Documentation Link:** `06-AI-Foundations/system-design-for-ai.md`  

**Hands-on Examples:**
- Build mini RAG system: query → retrieval → LLM output  
- Test with multiple queries & tune prompts  
- Annotate end-to-end system flow

---

## Day 5: ML System Design

**Topics:**
- Designing AI/ML systems for scale  
- Components: data pipelines, training, inference  
- Real-world constraints: latency, throughput, cost  

**Dependencies:** Days 1–4  
**Code Folder:** `Code/python/week-22/day-05-ml-system-design/`  
**Documentation Link:** `05-System-Design/fundamentals.md`  

**Hands-on Examples:**
- Sketch ML system architecture diagram  
- Annotate trade-offs: batch vs real-time inference  
- Document how RAG/LLM integrates into system design

---

## Day 6: Week Review & Postmortem

**Topics:**
- Consolidate Week 22 AI concepts  
- Identify weak spots & revisit previous week’s concepts  
- Update code → weekly MD → documentation links  

**Dependencies:** Days 1–5  
**Code Folder:** `Code/python/week-22/day-06-week-review-postmortem/`  
**Documentation Link:** `Revision/weekly-review.md`  

**Hands-on Examples:**
- Implement mini end-to-end RAG demo  
- Document concept → code → application mapping

---

## Daily Execution Rules (Non-Negotiable)

- 90 minutes/day minimum  
- Concept → Diagram → Code → Documentation → Postmortem  
- Commit code + notes at end of each day  
- Maintain links to weekly MD + documentation

---

## ✅ Outcome of Week 22

- Strong foundation in RAG, prompt engineering, and ML system design  
- Hands-on coding with Python for retrieval + LLM pipelines  
- Clear linkage of concepts → code → documentation → revision
