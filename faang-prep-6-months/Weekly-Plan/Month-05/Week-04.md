# Month 05 - Week 20 Plan – FAANG Prep

## 1. Motivation & Focus Reminder
- This 90-minute daily preparation is **non-negotiable**.
- Remember why you are doing this: building skills for **FAANG / top MNC**, mastering **DSA**, **system design**, and **AI fundamentals**.
- Focus on **small wins every day**, not the entire roadmap at once.
- Keep distractions away: phone on silent, no YouTube rabbit holes.

---

Week 20 – Month 5: System Design – Case Studies

Objective:

Apply all previous system design concepts to real-world case studies

Understand trade-offs, scalability, and bottlenecks

Hands-on coding + architecture diagram practice

Folder structure for code / examples:

Code/python/week-20/
├── day-01-url-shortener/
├── day-02-rate-limiter/
├── day-03-feed-system-part1/
├── day-04-feed-system-part2/
├── day-05-mini-project-integration/
└── day-06-week-review-postmortem/

Day 1: URL Shortener

Topics:

Problem requirements & constraints

Database choice & schema

Hashing vs Base62 encoding

Scaling considerations: sharding & replication

Dependencies:

Week 19 (Databases, Caching)

Code Folder: Code/python/week-20/day-01-url-shortener/
Documentation Link: 05-System-Design/case-studies/url-shortener.md

Hands-on Examples:

Implement Python URL shortener with basic persistence

Annotate hash collisions, performance bottlenecks

Day 2: Rate Limiter

Topics:

Rate limiting concepts: token bucket, leaky bucket

Distributed vs local rate limiting

Integration with API gateways / microservices

Dependencies:

Day 1 (URL Shortener)

Week 19 (Caching & Queues)

Code Folder: Code/python/week-20/day-02-rate-limiter/
Documentation Link: 05-System-Design/case-studies/rate-limiter.md

Hands-on Examples:

Implement Python token bucket rate limiter

Annotate trade-offs: memory, consistency, fairness

Day 3: Feed System – Part 1

Topics:

Problem statement: building a social feed

Data model & database choices (SQL vs NoSQL)

Pull-based vs push-based feed generation

Caching hot posts

Dependencies:

Day 2 (Rate Limiter)

Week 19 (Databases & Caching)

Code Folder: Code/python/week-20/day-03-feed-system-part1/
Documentation Link: 05-System-Design/case-studies/feed-system.md

Hands-on Examples:

Design basic feed system in Python

Annotate query patterns, latency issues

Day 4: Feed System – Part 2

Topics:

Scalability techniques: fan-out/fan-in, sharding

Real-time feed vs batch generation

Handling large number of users & updates

Dependencies:

Day 3 (Feed System Part 1)

Code Folder: Code/python/week-20/day-04-feed-system-part2/
Documentation Link: 05-System-Design/case-studies/feed-system.md

Hands-on Examples:

Simulate feed updates for multiple users

Annotate bottlenecks, trade-offs, caching strategy

Day 5: Mini Project Integration

Topics:

Integrate URL shortener + Rate Limiter + Feed System concepts

Discuss end-to-end architecture

Deployment & monitoring considerations

Dependencies:

Days 1–4

Code Folder: Code/python/week-20/day-05-mini-project-integration/
Documentation Link: 05-System-Design/case-studies/

Hands-on Examples:

Create mini-project skeleton linking all components

Annotate scalability, fault tolerance, caching, and queues

Day 6: Week Review & Postmortem

Topics:

Consolidate Week 20 case studies

Identify weak spots for revision

Update code → weekly MD → documentation links

Dependencies:

Days 1–5

Code Folder: Code/python/week-20/day-06-week-review-postmortem/
Documentation Link: Revision/weekly-review.md

Hands-on Examples:

Solve mock system design questions combining multiple components

Document trade-offs, bottlenecks, and improvements

Daily Execution Rules (Non-Negotiable)

90 minutes/day minimum

Concept → Diagram → Code → Documentation → Postmortem

Commit code + notes end of each day

Maintain links to weekly MD + documentation

✅ Outcome of Week 20:

Practical understanding of real-world system design problems

Hands-on mini-project integrating key components

Clear linkage of concepts → code → documentation → revision
