# Week 19 – Month 5: System Design – Components & Caching

**Objective:**  
Understand key components of system design: databases, caching, queues. Learn caching strategies and how they improve performance. Develop ability to design scalable systems with proper component choice.

---

## Folder Structure for Code / Examples

```
Code/python/week-19/
├── day-01-databases/
├── day-02-advanced-database-queries/
├── day-03-caching-intro/
├── day-04-caching-strategies/
├── day-05-queues-and-messaging/
└── day-06-week-review-postmortem/
```

---

## Day 1: Databases – Basics

**Topics:**
- Relational vs Non-relational databases (SQL vs NoSQL)  
- ACID properties  
- Normalization vs Denormalization  
- Indexing & query optimization basics  

**Dependencies:** Week 17 (System Design Fundamentals)  
**Code Folder:** `Code/python/week-19/day-01-databases/`  
**Documentation Link:** `05-System-Design/components/databases.md`  

**Hands-on Examples:**
- Create sample SQL tables  
- Write queries with filtering, joins, and aggregates  
- Annotate how indexes affect query performance

---

## Day 2: Advanced Database Queries

**Topics:**
- Query optimization techniques  
- Use of caching hints  
- Partitioning & Sharding concepts  
- Transaction isolation levels  

**Dependencies:** Day 1 (Database Basics)  
**Code Folder:** `Code/python/week-19/day-02-advanced-database-queries/`  
**Documentation Link:** `05-System-Design/components/databases.md`  

**Hands-on Examples:**
- Write complex SQL queries  
- Test queries with sample dataset and analyze performance

---

## Day 3: Caching Introduction

**Topics:**
- Why caching is needed  
- In-memory caches: Redis, Memcached  
- Cache-aside, Read-through, Write-through strategies  

**Dependencies:** Day 2 (Database Queries)  
**Code Folder:** `Code/python/week-19/day-03-caching-intro/`  
**Documentation Link:** `05-System-Design/components/caching.md`  

**Hands-on Examples:**
- Simple Python + Redis caching example  
- Annotate when to cache and invalidation basics

---

## Day 4: Caching Strategies

**Topics:**
- Cache eviction policies: LRU, LFU, TTL  
- Hot data vs cold data caching  
- Trade-offs: memory vs latency  
- Avoiding cache stampede  

**Dependencies:** Day 3 (Caching Intro)  
**Code Folder:** `Code/python/week-19/day-04-caching-strategies/`  
**Documentation Link:** `05-System-Design/components/caching.md`  

**Hands-on Examples:**
- Implement LRU cache in Python  
- Annotate when to choose a strategy

---

## Day 5: Queues & Messaging

**Topics:**
- Introduction to queues: RabbitMQ, Kafka, SQS  
- Use-cases for asynchronous processing  
- Producer-consumer model  
- Fan-out / Fan-in patterns  

**Dependencies:** Day 4 (Caching Strategies)  
**Code Folder:** `Code/python/week-19/day-05-queues-and-messaging/`  
**Documentation Link:** `05-System-Design/components/queues.md`  

**Hands-on Examples:**
- Python example simulating queue processing  
- Annotate message ordering, retries, and throughput considerations

---

## Day 6: Week Review & Postmortem

**Topics:**
- Consolidate Week 19 topics: Databases, Caching, Queues  
- Identify weak spots & create revision notes  
- Link code → weekly MD → documentation  

**Dependencies:** Days 1–5  
**Code Folder:** `Code/python/week-19/day-06-week-review-postmortem/`  
**Documentation Link:** `Revision/weekly-review.md`  

**Hands-on Examples:**
- Solve 1–2 small system design scenarios applying databases, caching, queues  
- Document trade-offs, scalability, and bottlenecks

---

## Daily Execution Rules (Non-Negotiable)

- 90 minutes/day minimum  
- Concept → Diagram → Code → Documentation → Postmortem  
- Commit code + notes end of each day  
- Maintain links to weekly MD + documentation

---

## ✅ Outcome of Week 19

- Strong understanding of databases, caching, and queues in system design  
- Able to design scalable, low-latency systems using proper components  
- Clear linkage of code → documentation → revision notes
