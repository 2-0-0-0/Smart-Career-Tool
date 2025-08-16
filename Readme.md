JobScope – AI-Powered Career Intelligence Dashboard
ISSAI AI Internship Pre-Screening Challenge Submission

JobScope is a next-generation career search and company intelligence tool. It empowers users to move beyond traditional job boards by offering a robust system to search, enrich, validate, and score companies using web intelligence and generative AI models. Tailored for strategic career exploration and professional research, JobScope bridges the gap between raw search results and actionable insight.

Key Features
Domain + Location Based Company Search
Uses [SerpAPI] to fetch relevant company websites based on user-defined domain and location keywords. We parse top-ranked organic Google search results to prioritize relevance and visibility for career-focused queries.

Company Enrichment via Together.ai
We utilized Together.ai’s Mistral-7B model to extract structured information such as:

Company Name

Industry

Services/Products Offered

Contact Information

Though powerful, this method faced limitations due to non-uniform website structures. We flag this as a point for future enhancement (see below).

Fake Website Detection (Heuristic)
To filter out non-genuine or low-quality companies, we implemented:

SSL (HTTPS) check

Presence of Contact Us / About Us sections

Domain age and trust-based keywords (e.g., "established", "clients", "partners")

Minimum meaningful text threshold

This ensures that users engage only with credible organizations during their career research.

Company Scoring
Each company is assigned a score out of 100 based on the quality and completeness of extracted metadata, helping users prioritize which organizations to explore further or reach out to.

Tech Stack Overview
Area	Tools / Libraries
Frontend	Streamlit – rapid UI deployment
Scraping	requests, BeautifulSoup, SerpAPI
LLM Enrich	Together.ai (Mistral-7B)
Validation	SSL socket check, heuristics, keyword scans
Scoring	Custom logic based on metadata completeness

Limitations & Future Improvements
While LLMs are powerful in understanding unstructured text, relying solely on them for structured data extraction from varied websites can result in inconsistencies and sparse outputs. We propose the following improvements:

Hybrid Extraction: Combine LLM output with rule-based schema scraping for precision.

Career Platform Integration: Leverage APIs like Clearbit, Apollo, or Crunchbase to enrich company profiles with hiring signals.

ML-Based Scoring: Replace rule-based scoring with ML models trained on job relevance and career outcomes.

Data Cleanup: Use NLP pipelines to filter noise and extract cleaner metadata from webpages.


