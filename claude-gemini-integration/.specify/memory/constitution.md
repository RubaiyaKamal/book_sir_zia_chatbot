<!--
SYNC IMPACT REPORT
- Version: 1.0.0 (initial creation)
- Changes: Initial creation of the constitution from project specification.
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md (No updates needed, generic)
  - ✅ .specify/templates/spec-template.md (No updates needed, generic)
  - ✅ .specify_templates/tasks-template.md (No updates needed, generic)
- Follow-up TODOs: None
-->
# AI Agents: Building Autonomous Intelligent Systems Constitution

## Core Principles

### I. AI-Assisted, Spec-Driven Development
The project will demonstrate and rely on spec-driven and AI-driven development workflows. All development activity, from chapter generation to coding, will be guided by detailed specifications and executed with the assistance of AI agents (Claude Code with Gemini 2.5 Flash).

### II. Comprehensive and High-Quality Content
Every chapter must be substantive (2,500+ words), include runnable code examples, state clear learning objectives, and provide hands-on exercises. Content must be practical, encouraging, and and build in complexity gradually.

### III. Clean, Testable, and Documented Code
All code must adhere to PEP 8 standards for Python, use type hints, include error handling, and contain clear comments explaining the 'why'. Code examples must be complete, runnable, and well-tested. No hardcoded secrets.

### IV. Grounded, Functional, and Attributed AI
The RAG chatbot must provide answers grounded in the book's content, with clear source attribution linking back to chapters. It must be functional, with features like context selection and conversation memory, and avoid hallucinations.

### V. Reusability Through Agentic Components
The project will focus on creating reusable components in the form of Claude Code Subagents and Agent Skills. These components (e.g., `chapter-generator`, `code-example-creator`) should be modular and well-documented to demonstrate innovative and reusable AI patterns.

### VI. Success is Measured by Delivery and Innovation
The primary success of the project is measured by delivering on the "Must Achieve" goals: publishing 25 chapters, a functional RAG chatbot, and deploying the book. Bonus points are awarded for innovation in reusable AI components and advanced features.

## Technology Stack

### Book Infrastructure
- **Framework:** Docusaurus (TypeScript)
- **Hosting:** GitHub Pages
- **Documentation:** Markdown
- **Styling:** CSS/Tailwind (via Docusaurus themes)

### RAG Chatbot
- **Backend:** FastAPI (Python)
- **LLM:** OpenAI Agents SDK
- **UI:** OpenAI ChatKit SDK
- **Vector DB:** Qdrant Cloud (Free Tier)
- **Embeddings:** OpenAI text-embedding-3-small

### Development Tools
- **AI Assistant:** Claude Code with Gemini 2.5 Flash
- **Version Control:** Git + GitHub
- **Package Manager:** npm (Node.js), pip (Python)

## Development Workflow

### Phase 1: Setup (1 hour)
1. Initialize Docusaurus project
2. Configure GitHub repository
3. Set up Qdrant Cloud account
4. Create basic project structure

### Phase 2: Content Generation (5 hours)
1. Generate chapters 1-6 (Part 1)
2. Generate chapters 7-13 (Part 2)
3. Generate chapters 14-18 (Part 3)
4. Generate chapters 19-22 (Part 4)
5. Generate chapters 23-25 (Part 5)

### Phase 3: RAG Backend (4 hours)
1. Set up FastAPI server
2. Integrate Qdrant vector database
3. Implement OpenAI Agents SDK
4. Build context-selection feature
5. Add conversation memory

### Phase 4: Frontend Integration (2 hours)
1. Embed ChatKit widget in Docusaurus
2. Connect frontend to FastAPI backend
3. Test all chatbot features
4. Polish UI/UX

### Phase 5: Deployment & Polish (2 hours)
1. Deploy book to GitHub Pages
2. Deploy backend (Railway/Render/Vercel)
3. Final testing and bug fixes
4. Create demo video/screenshots
5. Prepare hackathon submission

## Governance

All development must adhere to the principles and quality standards outlined in this constitution. Any deviation requires justification and approval. Emergency fallbacks are defined for schedule or technical issues.

**Version**: 1.0.0 | **Ratified**: 2025-11-22 | **Last Amended**: 2025-11-22