# ================================ labels generation ================================


label_generation_prompt_template = """
You are a conversation framework specialist tasked with identifying the most relevant section label categories for a specific chat scenario.

INPUT PARAMETERS:
• TOPIC: {}
• THEME: {}

════════════════ CORE OBJECTIVE ═════════════════
Analyze the given TOPIC, THEME, and to determine which section label categories would be most relevant and natural for this specific scenario. Generate 15-20 section label categories that best fit this particular context.

════════════════ ANALYSIS FRAMEWORK ═════════════════

**SCENARIO ANALYSIS QUESTIONS:**
1. What type of planning, decision-making, or problem-solving is involved?
2. What relationships would naturally be important in this context?
3. What practical constraints, resources, or logistics matter most?
4. What skills, knowledge, or learning would be relevant?
5. What emotional or personal aspects would come up naturally?
6. What external factors (cultural, environmental, social) would influence this scenario?
7. What temporal elements (deadlines, schedules, timing) are critical?
8. What unique challenges or opportunities are specific to this topic/theme?

════════════════ LABEL CATEGORIES SELECTION ═════════════════

**UNIVERSAL CATEGORIES (Always Include 2-3):**
- **Character & Relationship Labels** (relationships are always relevant)
- **Personal & Emotional Labels** (human element always present)
- **Decision & Change Labels** (conversations involve decisions)

**TOPIC-SPECIFIC CATEGORIES (Select 9-13 based on relevance):**

**Planning & Logistics Labels** - Use when scenario involves:
- Travel, events, projects, moves, construction, organizing
- Resource management, scheduling, coordination
- Physical planning or systematic approaches

**Goals & Progress Labels** - Use when scenario involves:
- Skill development, career growth, fitness, education
- Achievement-oriented activities, competitions, challenges
- Measurable outcomes or performance tracking

**Financial & Budget Labels** - Use when scenario involves:
- Major purchases, investments, business ventures
- Cost management, financial planning, economic decisions
- Budget constraints or money-related considerations

**Learning & Development Labels** - Use when scenario involves:
- Education, training, skill acquisition, research
- Professional development, hobbies, creative pursuits
- Knowledge building or expertise development

**Health & Wellness Labels** - Use when scenario involves:
- Medical situations, fitness goals, mental health
- Lifestyle changes, wellness programs, recovery
- Physical or emotional well-being focus

**Creative & Artistic Labels** - Use when scenario involves:
- Art projects, creative writing, music, design
- Innovation, invention, creative problem-solving
- Aesthetic decisions or artistic expression

**Professional & Career Labels** - Use when scenario involves:
- Job searching, career changes, workplace situations
- Business development, networking, professional growth
- Work-related challenges or opportunities

**Technical & Innovation Labels** - Use when scenario involves:
- Technology projects, software development, engineering
- Scientific research, technical problem-solving
- Innovation or technical skill development

**Cultural & Social Labels** - Use when scenario involves:
- Cross-cultural experiences, community involvement
- Social events, cultural learning, tradition exploration
- Community building or social integration

**Environmental & Location Labels** - Use when scenario involves:
- Outdoor activities, environmental projects, travel
- Location-dependent activities, weather considerations
- Geographic or environmental factors

**Legal & Compliance Labels** - Use when scenario involves:
- Regulatory requirements, legal processes, contracts
- Compliance issues, official procedures, documentation
- Rights, responsibilities, or legal frameworks

**Risk & Safety Labels** - Use when scenario involves:
- High-risk activities, safety protocols, security concerns
- Risk assessment, emergency planning, precautions
- Safety-critical decisions or situations

════════════════ SELECTION CRITERIA ═════════════════

**Must Include If Relevant:**
- Categories directly related to the main topic
- Categories that would naturally generate diverse conversations
- Categories that allow for progression and development over time
- Categories that create authentic human concerns and interests

**Avoid Including:**
- Categories that don't naturally fit the scenario
- Too many similar categories that would overlap
- Categories that wouldn't generate meaningful conversation
- Generic categories that don't add specific value

════════════════ OUTPUT FORMAT ═════════════════

Generate exactly 15-20 section label categories in this format:

**[Category Name] Labels:**
- Brief explanation of why this category is relevant to the TOPIC/THEME
- 3-5 specific label examples that would be used within this category

Example:
**Planning & Logistics Labels:**
- Essential for travel scenarios involving coordination, scheduling, and resource management
- Budget Planning, Transportation Strategy, Accommodation Research, Itinerary Adjustment, Packing Organization

**Character & Relationship Labels:**
- Travel often involves meeting new people and maintaining connections with home
- Travel Companion, Local Guide, Fellow Traveler, Family Check-in, Professional Contact

════════════════ QUALITY STANDARDS ═════════════════

Each selected category must:
- Be directly relevant to the specific TOPIC and THEME
- Generate natural, varied conversation opportunities  
- Allow for progression and development across multiple batches
- Feel authentic to what a real person would discuss in this scenario
- Provide enough depth for 15-20 bullet points across the conversation
- Just ouput the labels, without explanation at the first

Focus on categories that would create the most natural, engaging, and realistic chat conversations for this specific scenario.
"""

# ******************************

coding_label_generation_prompt_template = """
You are a technical conversation framework specialist tasked with identifying the most relevant section label categories for a specific coding/programming chat scenario.

INPUT PARAMETERS:
• TOPIC: {}
• THEME: {}

════════════════ CORE OBJECTIVE ═════════════════
Analyze the given TOPIC, THEME to determine which section label categories would be most relevant and natural for this specific coding scenario. Generate 15-20 section label categories that best fit this particular technical context.

════════════════ ANALYSIS FRAMEWORK ═════════════════

**CODING SCENARIO ANALYSIS QUESTIONS:**
1. What type of development lifecycle stage is involved? (planning, design, implementation, testing, deployment, maintenance)
2. What technical architecture or system components are relevant?
3. What programming paradigms, languages, or frameworks are being used?
4. What development methodologies or best practices apply?
5. What performance, scalability, or optimization concerns exist?
6. What integration challenges or external dependencies are involved?
7. What debugging, testing, or quality assurance aspects are critical?
8. What deployment, infrastructure, or DevOps considerations matter?
9. What security, compliance, or regulatory requirements exist?
10. What user experience or interface design elements are relevant?
11. What data handling, storage, or processing requirements exist?
12. What learning curve or skill development aspects are involved?

════════════════ LABEL CATEGORIES SELECTION ═════════════════

**UNIVERSAL CATEGORIES (Always Include 2-3):**
- **Technical Problem-Solving Labels** (debugging and troubleshooting always present)
- **Learning & Knowledge Labels** (continuous learning in coding)
- **Progress & Development Labels** (iterative development process)

**CODING-SPECIFIC CATEGORIES (Select 12-17 based on relevance):**

**Architecture & Design Labels**
- Use when scenario involves:
- System architecture decisions, design patterns, code structure
- API design, database schema, component architecture
- Scalability planning, microservices, modular design

**Implementation & Development Labels**
- Use when scenario involves:
- Active coding, feature implementation, algorithm development
- Code refactoring, optimization, performance tuning
- Programming language specifics, syntax, and best practices

**Framework & Technology Labels**
- Use when scenario involves:
- Specific frameworks (React, Django, Spring, etc.)
- Technology stack decisions, library integrations
- Platform-specific development (iOS, Android, Web, Desktop)

**Testing & Quality Assurance Labels**
- Use when scenario involves:
- Unit testing, integration testing, end-to-end testing
- Test-driven development, code coverage, quality metrics
- Bug tracking, code review, quality assurance processes

**DevOps & Deployment Labels**
- Use when scenario involves:
- CI/CD pipelines, deployment automation, infrastructure
- Containerization, cloud services, server management
- Version control, release management, environment setup

**Database & Data Management Labels**
- Use when scenario involves:
- Database design, query optimization, data modeling
- Data migration, ETL processes, data warehousing
- NoSQL vs SQL decisions, data persistence strategies

**Security & Compliance Labels**
- Use when scenario involves:
- Authentication, authorization, encryption, security protocols
- GDPR, HIPAA, or other compliance requirements
- Vulnerability assessment, security auditing, penetration testing

**Performance & Optimization Labels**
- Use when scenario involves:
- Code optimization, performance profiling, bottleneck identification
- Memory management, caching strategies, load balancing
- Scalability testing, performance monitoring, resource optimization

**Integration & API Labels**
- Use when scenario involves:
- Third-party API integration, webhook implementation
- Microservices communication, service mesh, API gateway
- Data synchronization, message queuing, event-driven architecture

**User Experience & Interface Labels**
- Use when scenario involves:
- UI/UX design, responsive design, accessibility
- User interface development, frontend frameworks
- Mobile app design, web design, desktop application interfaces

**Machine Learning & AI Labels**
- Use when scenario involves:
- ML model development, training, deployment
- Data preprocessing, feature engineering, model evaluation
- Deep learning, computer vision, natural language processing

**Mobile Development Labels**
- Use when scenario involves:
- iOS/Android native development, cross-platform solutions
- Mobile app lifecycle, app store deployment
- Mobile-specific features, device integration, performance optimization

**Web Development Labels**
- Use when scenario involves:
- Frontend development, backend development, full-stack
- Web performance, SEO optimization, browser compatibility
- Progressive web apps, single-page applications, server-side rendering

**Cloud & Infrastructure Labels**
- Use when scenario involves:
- Cloud platform services (AWS, Azure, GCP)
- Serverless architecture, containerization, orchestration
- Infrastructure as code, monitoring, logging, alerting

**Project Management & Workflow Labels**
- Use when scenario involves:
- Agile methodologies, sprint planning, task estimation
- Code review processes, team collaboration, documentation
- Project timeline management, resource allocation, milestone tracking

**Debugging & Troubleshooting Labels**
- Use when scenario involves:
- Error diagnosis, log analysis, debugging techniques
- Performance bottleneck identification, memory leak detection
- Production issue resolution, incident response, root cause analysis

**Code Quality & Standards Labels**
- Use when scenario involves:
- Code style guidelines, linting, formatting standards
- Code review practices, refactoring strategies
- Documentation standards, commenting practices, maintainability

**Research & Experimentation Labels**
- Use when scenario involves:
- Proof of concept development, technology evaluation
- A/B testing, feature flags, experimental features
- Research into new technologies, algorithm exploration

════════════════ SELECTION CRITERIA ═════════════════

**Must Include If Relevant:**
- Categories directly related to the main technical topic
- Categories that would naturally generate diverse technical conversations
- Categories that allow for progression through development phases
- Categories that create authentic developer concerns and workflows

**Avoid Including:**
- Categories that don't naturally fit the technical scenario
- Too many similar categories that would overlap significantly
- Categories that wouldn't generate meaningful technical discussion
- Generic categories that don't add specific technical value

════════════════ OUTPUT FORMAT ═════════════════

Generate exactly 15-20 section label categories in this format:

**[Category Name] Labels:**
- Brief explanation of why this category is relevant to the TOPIC/THEME
- 3-5 specific label examples that would be used within this category

Example:
**Architecture & Design Labels:**
- Critical for web application development involving system design decisions and scalability planning
- Component Architecture, Database Schema Design, API Design Pattern, Microservices Strategy, Caching Layer Design

**Implementation & Development Labels:**
- Essential for active coding phases involving feature development and code optimization
- Feature Implementation, Code Refactoring, Algorithm Optimization, Bug Fixing, Performance Tuning

════════════════ QUALITY STANDARDS ═════════════════

Each selected category must:
- Be directly relevant to the specific TOPIC and THEME
- Generate natural, varied technical conversation opportunities
- Allow for progression through development lifecycle stages
- Feel authentic to what a real developer would discuss in this scenario
- Provide enough depth for 15-20 technical discussion points across the conversation
- Just output the labels, without explanation at the first

Focus on categories that would create the most natural, engaging, and realistic technical chat conversations for this specific coding scenario.
"""

# ******************************

math_label_generation_prompt_template = """
You are a mathematical conversation framework specialist tasked with identifying the most relevant section label categories for a specific math chat scenario.

INPUT PARAMETERS:
- TOPIC: {}
- THEME: {}

════════════════ CORE OBJECTIVE ═════════════════
Analyze the given TOPIC, THEME to determine which section label categories would be most relevant and natural for this specific mathematical scenario. Generate 15-20 section label categories that best fit this particular mathematical context.

════════════════ ANALYSIS FRAMEWORK ═════════════════

**MATHEMATICAL SCENARIO ANALYSIS QUESTIONS:**
1. What type of mathematical thinking or problem-solving approach is involved? (analytical, computational, proof-based, applied)
2. What mathematical domains or fields are relevant? (algebra, calculus, statistics, geometry, etc.)
3. What level of mathematical rigor or formality is appropriate? (intuitive, rigorous, computational, theoretical)
4. What real-world applications or contexts connect to this mathematics?
5. What prerequisite knowledge or mathematical foundations are needed?
6. What problem-solving strategies or mathematical techniques apply?
7. What computational tools, software, or technology might be involved?
8. What mathematical communication or notation challenges exist?
9. What conceptual understanding vs. procedural skills are emphasized?
10. What mathematical modeling or abstraction processes are relevant?
11. What verification, checking, or validation methods are important?
12. What learning progression or skill development aspects are involved?

════════════════ LABEL CATEGORIES SELECTION ═════════════════

**UNIVERSAL CATEGORIES (Always Include 2-3):**
- **Problem-Solving & Strategy Labels** (mathematical thinking always present)
- **Conceptual Understanding Labels** (mathematical comprehension essential)
- **Learning & Progress Labels** (mathematical development continuous)

**MATHEMATICS-SPECIFIC CATEGORIES (Select 12-17 based on relevance):**

**Algebraic Reasoning Labels**
- Use when scenario involves:
- Equation solving, variable manipulation, symbolic reasoning
- Polynomial operations, factoring, algebraic structures
- Linear algebra, matrix operations, system solving

**Calculus & Analysis Labels**
- Use when scenario involves:
- Limits, derivatives, integrals, continuity concepts
- Optimization problems, rate of change applications
- Infinite series, differential equations, real analysis

**Geometric & Spatial Labels**
- Use when scenario involves:
- Shape properties, spatial relationships, geometric proofs
- Coordinate geometry, transformations, measurement
- Trigonometry, vectors, geometric modeling

**Statistical & Probability Labels**
- Use when scenario involves:
- Data analysis, statistical inference, hypothesis testing
- Probability distributions, random variables, stochastic processes
- Experimental design, data visualization, statistical modeling

**Discrete Mathematics Labels**
- Use when scenario involves:
- Combinatorics, graph theory, number theory
- Logic, set theory, discrete structures
- Algorithms, computational complexity, discrete optimization

**Applied Mathematics Labels**
- Use when scenario involves:
- Mathematical modeling of real-world phenomena
- Engineering applications, physics connections, optimization
- Financial mathematics, operations research, mathematical biology

**Computational Mathematics Labels**
- Use when scenario involves:
- Numerical methods, computational algorithms, programming
- Mathematical software usage, simulation, approximation
- Computer algebra systems, mathematical visualization

**Proof & Logic Labels**
- Use when scenario involves:
- Proof techniques, logical reasoning, mathematical argumentation
- Formal proof writing, proof verification, counterexamples
- Mathematical logic, set theory foundations, axiomatic systems

**Mathematical Communication Labels**
- Use when scenario involves:
- Mathematical notation, symbol usage, mathematical writing
- Explanation of concepts, mathematical presentations, peer discussion
- Mathematical vocabulary, terminology, formal language

**Error Analysis & Verification Labels**
- Use when scenario involves:
- Mistake identification, solution checking, error correction
- Validation methods, reasonableness checks, alternative approaches
- Common misconceptions, troubleshooting, debugging calculations

**Mathematical Modeling Labels**
- Use when scenario involves:
- Real-world problem abstraction, model creation, assumptions
- Model validation, parameter estimation, sensitivity analysis
- Interpretation of results, model limitations, refinement

**Technology & Tools Labels**
- Use when scenario involves:
- Calculator usage, computer algebra systems, mathematical software
- Graphing tools, simulation software, programming for mathematics
- Online resources, mathematical databases, computational platforms

**Assessment & Practice Labels**
- Use when scenario involves:
- Problem practice, skill development, mathematical exercises
- Test preparation, performance evaluation, self-assessment
- Homework help, study strategies, mathematical practice

**Research & Exploration Labels**
- Use when scenario involves:
- Mathematical investigation, pattern discovery, conjecture formation
- Open-ended problems, mathematical research, exploration activities
- Creative problem solving, mathematical creativity, investigation methods

**Interdisciplinary Connections Labels**
- Use when scenario involves:
- Mathematics in other subjects, cross-curricular applications
- Physics applications, engineering connections, data science integration
- Mathematical foundations for other fields, real-world relevance

**Mathematical History & Context Labels**
- Use when scenario involves:
- Historical development of concepts, mathematician biographies
- Cultural aspects of mathematics, mathematical discoveries
- Evolution of mathematical ideas, historical problem contexts

**Advanced Topics Labels**
- Use when scenario involves:
- Graduate-level mathematics, research mathematics, specialized fields
- Abstract algebra, real analysis, topology, advanced theory
- Mathematical research methods, academic mathematics, theoretical exploration

**Collaborative Learning Labels**
- Use when scenario involves:
- Group problem solving, peer learning, mathematical discussion
- Study groups, collaborative projects, peer tutoring
- Mathematical community, sharing strategies, collective understanding

════════════════ SELECTION CRITERIA ═════════════════

**Must Include If Relevant:**
- Categories directly related to the main mathematical topic
- Categories that would naturally generate diverse mathematical conversations
- Categories that allow for progression through mathematical understanding levels
- Categories that create authentic student/learner mathematical concerns and interests

**Avoid Including:**
- Categories that don't naturally fit the mathematical scenario
- Too many similar categories that would overlap significantly
- Categories that wouldn't generate meaningful mathematical discussion
- Generic categories that don't add specific mathematical value

════════════════ OUTPUT FORMAT ═════════════════

Generate exactly 15-20 section label categories in this format:

**[Category Name] Labels:**
- Brief explanation of why this category is relevant to the TOPIC/THEME
- 3-5 specific label examples that would be used within this category

Example:
**Algebraic Reasoning Labels:**
- Essential for algebra-focused scenarios involving equation solving and symbolic manipulation
- Variable Isolation, Factoring Strategies, System Solving, Polynomial Operations, Algebraic Proof

**Problem-Solving & Strategy Labels:**
- Critical for mathematical thinking and approach development across all mathematical domains
- Strategy Selection, Problem Analysis, Solution Planning, Alternative Methods, Verification Techniques

════════════════ QUALITY STANDARDS ═════════════════

Each selected category must:
- Be directly relevant to the specific TOPIC and THEME
- Generate natural, varied mathematical conversation opportunities
- Allow for progression through mathematical understanding and skill levels
- Feel authentic to what a real student/learner would discuss in this mathematical scenario
- Provide enough depth for 15-20 mathematical discussion points across the conversation
- Just output the labels, without explanation at the first

Focus on categories that would create the most natural, engaging, and realistic mathematical chat conversations for this specific scenario.
"""


# ================================ plan generaion ================================

plan_generation_prompt_profile_and_topic_given_template = """
You are a long-form narrative planning specialist creating a COHERENT STORY PLANSET for natural conversational flow. Your task is to generate detailed batch plans that will seed realistic user-assistant dialogue.

## INPUT DATA
• **TOPIC:** <topic>
• **THEME:** <theme>
• **TIMELINE:** <timeline>
• **TOTAL MESSAGES:** <total_messages>
• **BATCH_SIZE:** <batch_size> (i.e., <num_batches> batches)
• **LABELS:** <provided_labels>
• **USER PROFILE:** <user_profile>
• **USER RELATIONSHIPS:** <user_relationships>

═══════════════ CORE OBJECTIVE ═══════════════
Generate <num_batches> distinct, non-repetitive batch plans that form a coherent narrative arc where a real person naturally converses with an AI assistant. Each plan must introduce NEW story elements while maintaining perfect continuity and character consistency.

═══════════════ NARRATIVE FRAMEWORK ═══════════════
This is NOT about generating random conversations - this is about creating a realistic, evolving story where:
- The user naturally seeks AI assistance across different life situations
- Each conversation builds upon previous interactions and established context
- The story progresses chronologically with authentic character development
- Relationships, situations, and circumstances evolve realistically over time
- The user's needs, challenges, and interests naturally expand and deepen

═══════════════ STRUCTURE REQUIREMENTS ═══════════════

**1. OUTPUT FORMAT:**
- Generate exactly <num_batches> plans
- Format: `BATCH X PLAN` headers
- Each plan contains exactly 21 bullets
- Each bullet: "• **[LABEL CATEOGRY]:**[LABEL DESCRIPTION]:** [content]" (≤25s words)
- NOTE: Each label consists of categority and description. Use both for each bullet point.
- Use only the provided LABELS - no custom categories

**2. STORY PROGRESSION ARCHITECTURE:**

**BATCH 1 (Story Foundation):**
- First bullet MUST be: "• **Personal Introduction:**"
- Establish initial context, current situation, and immediate needs
- Introduce all relationships from the provided list
- Set up the foundational scenario that will evolve

**BATCHES 2-<num_batches> (Story Evolution):**
- Reference user as "I/my/me" (never repeat the full name)
- Each batch advances the timeline chronologically
- Build upon ALL previously established elements
- Introduce new complications, opportunities, or developments
- Show realistic progression in relationships, work, personal growth

**3. RELATIONSHIP CONTINUITY SYSTEM:**

**Relationship Evolution Mandate:**
Every relationship mention MUST show progression from previous batches. Track relationship arcs across the entire story:

**Evolution Stages:**
- **Introduction:** "I met [Name]..." / "I was introduced to [Name]..."
- **Development:** "After our conversation, [Name] and I..." / "[Name] suggested..."
- **Deepening:** "[Name] confided..." / "I had a disagreement with [Name]..."
- **Maturation:** "[Name] has become..." / "My relationship with [Name] changed when..."

**Interaction Variety (rotate - never repeat within 3 batches):**
- Collaborative, Supportive, Conflictual, Social, Professional, Personal, Transactional, Serendipitous

**Character Consistency Rules:**
- Use provided relationships as your character cast
- Show realistic relationship patterns: some strengthen, some fade, conflicts arise and resolve
- Reference specific past interactions and their ongoing consequences
- Include 2-3 relationship bullets per batch from provided relationships

═══════════════ ANTI-REPETITION VERIFICATION ═══════════════

**Before writing ANY bullet, verify:**
- Have I used this exact phrasing before?
- Does this show clear progression from previous mentions?
- Am I introducing genuinely new information?
- Is this interaction type different from recent batches?
- Does this advance the overall narrative?

**FORBIDDEN:**
- Exact phrase repetition
- Similar concepts without clear evolution
- Static descriptions that don't advance the story
- Repeating interaction types with same people
- Bullets desriptions

═══════════════ CONTENT DISTRIBUTION STRATEGY ═══════════════

**Per Batch Requirements:**
- 2-3 bullets: Relationship developments (using provided relationships)
- 2-4 bullets: Current situation/challenge progression
- 1 bullet: Temporal anchor
- 2-3 bullets: Relationships (parents, partner, friends, acquaintances)
- rest bullets: Using remaining labels

**Story Progression Patterns:**
- **Early Batches (1-3):** Setup, introductions, initial challenges
- **Middle Batches:** Complications, developments, relationship dynamics
- **Later Batches:** Resolutions, growth, new challenges, deeper insights

═══════════════ NATURAL CONVERSATION FLOW ═══════════════

Remember: These plans will generate conversations where the user is naturally seeking AI assistance. Each bullet should represent something the user would realistically discuss with an AI assistant:

- Seeking advice on relationship situations
- Planning and organizing life events
- Working through professional challenges
- Learning and skill development
- Processing emotional experiences
- Making decisions about future steps
- Reflecting on personal growth
- Managing complex situations

═══════════════ QUALITY STANDARDS ═══════════════

**Chronological Consistency:**
- Batch 1 = story beginning
- Batch <num_batches> = evolved situation with clear progression
- Each batch logically follows the previous timeline

**Narrative Depth:**
- Include specific details: names, dates, numbers, locations
- Show cause-and-effect relationships between batches
- Maintain emotional authenticity throughout
- Reference past events and their ongoing impact

**Character Authenticity:**
- Keep user personality consistent with provided profile
- Show realistic personal growth and change over time
- Maintain relationship dynamics that feel genuine
- Include both positive and challenging developments

═══════════════ EXECUTION NOTES ═══════════════

- Use plain, natural language throughout
- Include realistic cultural, financial, and geographic specificity
- Make every bullet contribute to the overarching story
- Ensure uniform detail quality across ALL batches
- End immediately after `BATCH <num_batches> PLAN`

Begin generation now.
"""
plan_generation_prompt_profile_and_topic_given_detailed_template = """
You are a long-form narrative planning specialist creating a COHERENT STORY PLANSET for natural conversational flow. Your task is to generate detailed batch plans that will seed realistic user-assistant dialogue.

## INPUT DATA
- **TOPIC:** <topic>
- **THEME:** <theme>
- **TIMELINE:** <timeline>
- **NUM_BATCHES:** <num_batches> batches
- **LABELS:** <provided_labels>
- **USER PROFILE:** <user_profile>
- **USER RELATIONSHIPS:** <user_relationships>

═══════════════ CORE OBJECTIVE ═══════════════
Generate <num_batches> distinct, non-repetitive batch plans that form a coherent narrative arc where a real person naturally converses with an AI assistant. Each plan must introduce NEW story elements while maintaining perfect continuity and character consistency.

═══════════════ NARRATIVE FRAMEWORK ═══════════════
This is NOT about generating random conversations - this is about creating a realistic, evolving story where:
- The user naturally seeks AI assistance across different life situations
- Each conversation builds upon previous interactions and established context
- The story progresses chronologically with authentic character development
- Relationships, situations, and circumstances evolve realistically over time
- The user's needs, challenges, and interests naturally expand and deepen

═══════════════ CRITICAL DETAIL REQUIREMENTS ═══════════════

**MANDATORY SPECIFIC DETAILS:**
Every batch MUST include numerous concrete, verifiable details that enable single-word or short factual answers:

**Required Detail Categories (minimum 5-7 per batch):**
- **Exact Numbers:** prices ($X), quantities, percentages, measurements, distances
- **Specific Dates/Times:** For example: "Month x yth", "x:y PM/AM", "next [week day]", "in x weeks", ...
- **Named Locations:** restaurants, stores, streets, buildings, parks, venues
- **Brand/Product Names:** specific items, services, companies, tools, software
- **Yes/No Situations:** decisions made, preferences stated, conflicts resolved
- **Event Outcomes:** what happened, who won/lost, what was chosen/rejected
- **Specific Preferences:** favorite foods, colors, activities, music, books
- **Quantifiable Results:** test scores, rankings, ratings, completion times

**Detail Distribution Rules:**
- Each bullet must contain AT LEAST one verifiable detail
- Avoid vague statements like "discussed options" - specify WHAT options
- Replace "had a meeting" with "had a x PM/AM meeting at [place name] on [street name]"
- Instead of "considering choices" use "choosing between X, Y, and Z"

═══════════════ STRUCTURE REQUIREMENTS ═══════════════

**1. OUTPUT FORMAT:**
- Generate exactly <num_batches> plans
- Format: `BATCH X PLAN` headers
- Each plan contains exactly <num_bullets> bullets
- Each bullet: "• **[LABEL CATEGORY]:[LABEL DESCRIPTION]:** [content]" (≤25 words)
- NOTE: Each label consists of category and description. Use both for each bullet point.
- Use only the provided LABELS - no custom categories
- CRITICAL: Add one time anchor bulletpoint at the begining of each batch with this format: Month Day, Year. 
**NOTE**: Time anchor must correlated with other dates in the batch and the time anchors among batches should be increasing and time anchor in each batch should be before the dates mentioned in the batches.

**2. STORY PROGRESSION ARCHITECTURE:**

**BATCH 1 (Story Foundation):**
- First bullet MUST be: "• **Time Anchor:**"
- Second bullet MUST be: "• **Personal Introduction:**" [Must be from user language (I ...)]
- MUST HAVE one bullet (titled personality trait) from personality_traits in USER PROFILE
- Establish initial context with SPECIFIC details (age, location, job title, salary range)
- Introduce all relationships with CONCRETE contexts (how long known, where met)
- Set up measurable goals, deadlines, and quantifiable challenges

**BATCHES 2-<num_batches> (Story Evolution):**
- Reference user as "I/my/me" (never repeat the full name)
- Each batch advances the timeline chronologically
- Build upon ALL previously established elements
- Show MEASURABLE progression (promotions, relationship milestones, achievement metrics)

**3. RELATIONSHIP CONTINUITY SYSTEM:**

**Relationship Evolution Mandate:**
Every relationship mention MUST include specific interaction details:

**Evolution Stages with Required Details:**
- **Introduction:** "Met [Name] at [specific place] on [date/time]"
- **Development:** "[Name] suggested [specific action] which resulted in [outcome]"
- **Deepening:** "[Name] revealed [specific information] during [specific event]"
- **Maturation:** "After [X months/years], [Name] and I [specific change]"

**Interaction Variety (rotate - never repeat within 3 batches):**
- Collaborative, Supportive, Conflictual, Social, Professional, Personal, Transactional, Serendipitous

**Character Consistency Rules:**
- Track specific preferences for each character (favorite restaurant, hobby, pet peeve)
- Reference past specific events and their measurable consequences
- Include 2-3 relationship bullets per batch with concrete details

═══════════════ CONFLICT & RESOLUTION TRACKING ═══════════════

**Mandatory Conflict Elements:**
Each batch must include at least 2-3 situations with:
- **Clear Stakes:** what's at risk (money amount, deadline, relationship status)
- **Binary Decisions:** chose A over B, accepted/rejected offer, yes/no to proposal
- **Measurable Outcomes:** gained/lost $X, saved X hours, improved by X%
- **Specific Disagreements:** who wanted what, what compromise was reached

**Conflict Types to Rotate:**
- Financial decisions with specific amounts
- Time management with exact deadlines
- Relationship boundaries with specific incidents
- Professional choices with concrete options
- Personal values with specific scenarios

═══════════════ ANTI-REPETITION VERIFICATION ═══════════════

**Before writing ANY bullet, verify:**
- Have I included at least one specific, verifiable detail?
- Can this generate a question with a one-word answer?
- Does this show MEASURABLE progression from previous mentions?
- Are the numbers, dates, names, and locations specific?
- Is this a NEW piece of information with NEW details?

**FORBIDDEN:**
- Vague time references ("recently", "soon") without specific dates
- General locations ("coffee shop", "restaurant") without names
- Unspecified amounts ("some money", "a few people")
- Abstract outcomes ("went well", "had issues") without details
- Repeated specific details (same restaurant, same activity, same problem)

═══════════════ CONTENT DISTRIBUTION STRATEGY ═══════════════

**Per Batch Requirements:**
- 2-3 bullets: Relationship developments with specific incidents
- 2-4 bullets: Current situation with measurable metrics
- 1 bullet: Exact temporal anchor (specific date/time)
- 5-7 bullets: Events with verifiable outcomes
- 3-4 bullets: Decisions/preferences with specific choices
- 1 bullet: **Preference Statement**: implicitly showing user preferences
- Rest: Using remaining labels with concrete details

═══════════════ SPECIAL BULLET REQUIREMENTS ═══════════════
**1. PREFERENCE STATEMENT (rotate each batch):**
Must show preference through action/decision

**Rotate These Types Each Batch:**
- Choice actions
- Method implementations
- Quality decisions
- Timing patterns
- Style approaches
- Priority demonstrations

**Story Progression Patterns:**
- **Early Batches (1-3):** Establish baselines (current salary, relationship status, living situation)
- **Middle Batches:** Track changes from baselines with specific metrics
- **Later Batches:** Show cumulative results with before/after comparisons

═══════════════ NATURAL CONVERSATION FLOW ═══════════════

These plans generate conversations where users seek AI assistance for SPECIFIC situations:
- "Should I accept the $x job offer or stay at my $y position?"
- "The deadline is Month[] xth - can I finish all y modules by then?"
- "Sarah wants to meet at x at y PM but z suggested x1 at y1 PM"
- "My rent increased from $x to $y - should I move?"

═══════════════ QUALITY STANDARDS ═══════════════

**Specificity Checklist:**
- Every person has a full name and defined relationship
- Every event has a date, time, or specific temporal reference
- Every location has a name or address
- Every decision has concrete options with specific details
- Every outcome is measurable or verifiable

**Narrative Depth:**
- Include prices, percentages, distances, durations
- Show cause-and-effect with specific triggers and results
- Maintain factual consistency (don't change established numbers/dates)
- Reference past specific events by name and date

═══════════════ EXECUTION NOTES ═══════════════

- Prioritize concrete details over abstract descriptions
- Every bullet should enable at least 2-3 factual questions
- Include cultural, financial, and geographic specificity
- Ensure details are realistic and internally consistent
- End immediately after `BATCH <num_batches> PLAN`

Begin generation now.
"""

# ******************************

coding_plan_generation_prompt = """
You are a technical project narrative planning specialist creating a COHERENT DEVELOPMENT STORY PLANSET for natural coding conversational flow. Your task is to generate detailed batch plans that will seed realistic developer-assistant dialogue.

## INPUT DATA
• **TOPIC:** <topic>
• **THEME:** <theme>
• **TIMELINE:** <timeline>
• **TOTAL MESSAGES:** <total_messages>
• **BATCH_SIZE:** <batch_size> (i.e., <num_batches> batches)
• **LABELS:** <provided_labels>
• **USER PROFILE:** <user_profile>

═══════════════ CORE OBJECTIVE ═══════════════
Generate <num_batches> distinct, non-repetitive batch plans that form a coherent development narrative arc where a real developer naturally converses with an AI assistant. Each plan must introduce NEW technical elements while maintaining perfect continuity and project consistency.

═══════════════ REAL-WORLD CODING CHAT FRAMEWORK ═══════════════
This is about creating realistic coding conversations that mirror how developers actually interact with AI assistants:

**PRIMARY INTERACTION PATTERNS:**
1. **Code Implementation Requests:** "I need to build/create/implement..."
2. **Debugging Help:** "I'm getting this error..." / "This code isn't working..."
3. **Code Review/Optimization:** "Can you review this code?" / "How can I optimize this?"

**REALISTIC DEVELOPMENT FLOW:**
- Developer works on features → encounters bugs → seeks debugging help
- Developer implements basic functionality → seeks optimization advice
- Developer plans architecture → requests implementation assistance
- Developer completes features → needs testing/deployment guidance
- Developer faces new requirements → seeks implementation strategies

═══════════════ STRUCTURE REQUIREMENTS ═══════════════

**1. OUTPUT FORMAT:**
- Generate exactly <num_batches> plans
- Format: `BATCH X PLAN` headers
- Each plan contains exactly 21 bullets
- Each bullet: "• **[LABEL CATEGORY]:**[LABEL DESCRIPTION]:** [content]" (≤25 words)
- NOTE: Each label consists of category and description. Use both for each bullet point.
- Use only the provided LABELS - no custom categories
- CRITICAL: Add one time anchor bulletpoint at the begining of each batch with this format: Month Day, Year.
**NOTE**: Time anchor must correlated with other dates in the batch and the time anchors among batches should be increasing and time anchor in each batch should be before the dates mentioned in the batches.

**2. DEVELOPMENT PROGRESSION ARCHITECTURE:**

**BATCH 1 (Project Foundation):**
- First bullet MUST be: "• **Project Initialization:**"
- Establish project scope, initial requirements, and technical goals
- Set up the foundational development scenario that will evolve

**BATCHES 2-<num_batches> (Development Evolution):**
- Reference developer as "I/my/me" (never repeat the full name)
- Each batch advances the development timeline chronologically
- Build upon ALL previously established technical elements
- Show realistic progression through actual development phases

**3. TECHNICAL CONTINUITY SYSTEM:**

**Development Phase Evolution:** Every technical element MUST show progression from previous batches:

**Natural Development Progression Examples:**
- **Planning Phase:** "I need to design the authentication system..."
- **Implementation Phase:** "I'm implementing the login functionality we discussed..."
- **Debugging Phase:** "The authentication code is throwing errors..."
- **Review Phase:** "Can you review my authentication implementation?"
- **Optimization Phase:** "The login process is slow, how can I optimize it?"
- **Testing Phase:** "I need to write tests for the authentication system..."
- **Deployment Phase:** "I'm deploying the authentication feature..."

**Technical Complexity Progression:**
- Early batches: Basic implementation, simple features
- Middle batches: Integration challenges, debugging complex issues
- Later batches: Performance optimization, advanced features, production concerns

═══════════════ FLEXIBLE CONTENT DISTRIBUTION ═══════════════

**ADAPTIVE BATCH PLANNING:**
Each batch should organically focus on what makes sense for that development phase, drawing from provided labels. Examples:

**Implementation-Heavy Batch:**
- Multiple implementation requests
- Architecture decisions
- Code structure planning
- Framework/library selection

**Debugging-Heavy Batch:**
- Error analysis and troubleshooting
- Code review requests
- Performance bottleneck identification
- Testing and validation

**Review/Optimization Batch:**
- Code review requests
- Performance optimization
- Security assessment
- Refactoring strategies

**Deployment/Production Batch:**
- DevOps and deployment
- Infrastructure concerns
- Monitoring and logging
- Production issue resolution

**CONTENT SELECTION STRATEGY:**
- Select 21 bullets from provided labels that naturally fit the current development phase
- Ensure variety within each batch while maintaining thematic coherence
- Balance between different interaction types (implementation, debugging, review)
- Include 1 temporal anchor per batch to maintain chronological flow

═══════════════ ANTI-REPETITION VERIFICATION ═══════════════

**Before writing ANY bullet, verify:**
- Have I used this exact technical phrasing before?
- Does this show clear progression from previous development stages?
- Am I introducing genuinely new technical information?
- Is this development phase different from recent batches?
- Does this advance the overall project narrative?

**FORBIDDEN:**
- Exact phrase repetition
- Similar technical concepts without clear evolution
- Static descriptions that don't advance the project
- Repeating development phases with same components
- Generic bullet descriptions without technical specificity

═══════════════ NATURAL CODING CONVERSATION FLOW ═══════════════

Each bullet should represent realistic developer-AI interactions:

**Implementation Requests:**
- "I need to implement user authentication with JWT tokens"
- "Help me create a REST API for user management"
- "I want to build a real-time chat feature using WebSockets"

**Debugging Help:**
- "I'm getting a 'Cannot read property of undefined' error in my React component"
- "My database queries are timing out, need help debugging"
- "The CI/CD pipeline is failing at the test stage"

**Code Review/Optimization:**
- "Can you review my database schema design?"
- "How can I optimize this SQL query for better performance?"
- "Is there a more efficient way to handle file uploads?"

═══════════════ QUALITY STANDARDS ═══════════════

**Chronological Consistency:**
- Batch 1 = project beginning/planning phase
- Batch <num_batches> = evolved project with clear development progression
- Each batch logically follows the previous development timeline

**Technical Authenticity:**
- Include specific technical details: error messages, framework names, configuration specifics
- Show cause-and-effect relationships between technical decisions
- Reference past implementations and their ongoing impact
- Use realistic technical scenarios that developers actually encounter

**Developer Authenticity:**
- Keep developer personality consistent with provided profile
- Show realistic skill progression and learning over time
- Include both successful implementations and technical challenges
- Maintain project scope that feels genuine for the developer's level

**Project Realism:**
- Follow realistic development lifecycle patterns
- Include appropriate technical debt and refactoring needs
- Show natural feature evolution and scope changes
- Maintain consistent technology stack decisions

═══════════════ EXECUTION NOTES ═══════════════

- Use plain, technical language throughout
- Include realistic technical specificity: version numbers, error messages, configuration details
- Make every bullet contribute to the overarching development story
- Ensure uniform technical detail quality across ALL batches
- Vary batch focus organically based on development phase (implementation vs debugging vs optimization)
- End immediately after `BATCH <num_batches> PLAN`

Begin generation now.
"""
coding_plan_generation_prompt_detailed = """
You are a technical project narrative planning specialist creating a COHERENT DEVELOPMENT STORY PLANSET for natural coding conversational flow. Your task is to generate detailed batch plans that will seed realistic developer-assistant dialogue.

## INPUT DATA
• **TOPIC:** <topic>
• **THEME:** <theme>
• **TIMELINE:** <timeline>
• **NUM_BATCHES:** <num_batches> batches
• **LABELS:** <provided_labels>
• **USER PROFILE:** <user_profile>

═══════════════ CORE OBJECTIVE ═══════════════
Generate <num_batches> distinct, non-repetitive batch plans that form a coherent development narrative arc where a real developer naturally converses with an AI assistant. Each plan must introduce NEW technical elements while maintaining perfect continuity and project consistency.

═══════════════ REAL-WORLD CODING CHAT FRAMEWORK ═══════════════
This is about creating realistic coding conversations that mirror how developers actually interact with AI assistants:

**PRIMARY INTERACTION PATTERNS:**
1. **Code Implementation Requests:** "I need to build/create/implement..."
2. **Debugging Help:** "I'm getting this error..." / "This code isn't working..."
3. **Code Review/Optimization:** "Can you review this code?" / "How can I optimize this?"

**REALISTIC DEVELOPMENT FLOW:**
- Developer works on features → encounters bugs → seeks debugging help
- Developer implements basic functionality → seeks optimization advice
- Developer plans architecture → requests implementation assistance
- Developer completes features → needs testing/deployment guidance
- Developer faces new requirements → seeks implementation strategies

═══════════════ CRITICAL DETAIL REQUIREMENTS ═══════════════

**MANDATORY SPECIFIC DETAILS:**
Every batch MUST include numerous concrete, verifiable technical details that enable single-word or short factual answers:

**Required Detail Categories (minimum 5-7 per batch):**
- **Exact Numbers:** version numbers (v2.3.1), port numbers (3000), response times (250ms), file sizes (2.5MB)
- **Specific Dates/Times:** deployment dates, sprint deadlines, meeting times, build timestamps
- **Named Technologies:** specific frameworks, libraries, tools, services (React 18.2, PostgreSQL 14, AWS Lambda)
- **Error Messages:** exact error texts, status codes (404, 500), stack trace snippets
- **Yes/No Situations:** feature implemented, bug fixed, test passed, deployment successful
- **Performance Metrics:** load times, query speeds, memory usage, API response times
- **Configuration Details:** environment variables, API endpoints, database schemas
- **Quantifiable Results:** test coverage (85%), uptime (99.9%), user count (1,000+), bug count

**Detail Distribution Rules:**
- Each bullet must contain AT LEAST one verifiable technical detail
- Avoid vague statements like "worked on feature" - specify WHAT feature and HOW
- Replace "had a bug" with "encountered 'undefined is not a function' error in UserAuth.js line 42"
- Instead of "improved performance" use "reduced API response time from 800ms to 200ms"

═══════════════ STRUCTURE REQUIREMENTS ═══════════════

**1. OUTPUT FORMAT:**
- Generate exactly <num_batches> plans
- Format: `BATCH X PLAN` headers
- Each plan contains exactly <num_bullets> bullets
- Each bullet: "• **[LABEL CATEGORY]:[LABEL DESCRIPTION]:** [content]" (≤25 words)
- NOTE: Each label consists of category and description. Use both for each bullet point.
- Use only the provided LABELS - no custom categories
- CRITICAL: Add one time anchor bulletpoint at the begining of each batch with this format: Month Day, Year.
**NOTE**: Time anchor must correlated with other dates in the batch and the time anchors among batches should be increasing and time anchor in each batch should be before the dates mentioned in the batches.

**2. STORY PROGRESSION ARCHITECTURE:**

**BATCH 1 (Project Foundation):**
- First bullet MUST be: "• **Time Anchor:**"
- Second bullet MUST be: "• **Personal Introduction:**" [Must be from user language (I ...)]
- Third bullet MUST be: "• **Project Initialization:**"
- MUST HAVE one bullet (titled personality trait) from personality_traits in USER PROFILE ONLY in the first BATCH
- Establish project scope with SPECIFIC technical details (tech stack, architecture, requirements)
- Introduce initial technical challenges with CONCRETE metrics (performance targets, deadlines)
- Set up measurable goals and quantifiable milestones

**BATCHES 2-<num_batches> (Development Evolution):**
- Reference developer as "I/my/me" (never repeat the full name)
- Each batch advances the development timeline chronologically
- Build upon ALL previously established technical elements
- Show MEASURABLE progression (features completed, bugs fixed, performance improvements)
- Reference specific code files, functions, and technical decisions from earlier batches

**3. TECHNICAL CONTINUITY SYSTEM:**

**Development Phase Evolution:** 
Every technical element MUST show progression from previous batches:

**Natural Development Progression Examples:**
- **Planning Phase:** "I need to design the authentication system..."
- **Implementation Phase:** "I'm implementing the login functionality we discussed..."
- **Debugging Phase:** "The authentication code is throwing errors..."
- **Review Phase:** "Can you review my authentication implementation?"
- **Optimization Phase:** "The login process is slow, how can I optimize it?"
- **Testing Phase:** "I need to write tests for the authentication system..."
- **Deployment Phase:** "I'm deploying the authentication feature..."

**Technical Complexity Progression:**
- Early batches: Basic implementation, simple features
- Middle batches: Integration challenges, debugging complex issues
- Later batches: Performance optimization, advanced features, production concerns

═══════════════ CONFLICT & RESOLUTION TRACKING ═══════════════

**Mandatory Technical Conflict Elements:**
Each batch must include at least 2-3 technical challenges with:
- **Clear Stakes:** what's at risk (deployment deadline, performance SLA, budget constraint)
- **Binary Decisions:** chose Framework A over B, implemented Solution X vs Y, fixed vs workaround
- **Measurable Outcomes:** reduced latency by Xms, saved $X in hosting, improved performance by X%
- **Specific Trade-offs:** what was sacrificed for what gain (memory for speed, complexity for features)

**Technical Conflict Types to Rotate:**
- Performance bottlenecks with specific metrics
- Architecture decisions with concrete alternatives
- Integration challenges with external systems
- Security vulnerabilities with severity levels
- Scalability issues with user load numbers
- Technical debt vs new features

═══════════════ ANTI-REPETITION VERIFICATION ═══════════════

**Before writing ANY bullet, verify:**
- Have I included at least one specific, verifiable technical detail?
- Can this generate a question with a one-word or factual answer?
- Does this show MEASURABLE progression from previous technical states?
- Are the version numbers, error messages, and metrics specific?
- Is this a NEW technical challenge or implementation detail?

**FORBIDDEN:**
- Vague time references ("recently", "soon") without specific sprint dates or deadlines
- General technology mentions ("database", "API") without specific names/versions
- Unspecified metrics ("improved", "faster") without numbers
- Abstract outcomes ("worked well", "had issues") without technical details
- Repeated technical scenarios (same bug type, same optimization, same implementation)

═══════════════ CONTENT DISTRIBUTION STRATEGY ═══════════════

**Per Batch Requirements:**
- 2-3 bullets: Technical implementation details with specific code elements
- 2-4 bullets: Current development status with measurable metrics
- 1 bullet: Exact temporal anchor (specific date/time)
- 5-7 bullets: Development activities with verifiable outcomes
- 3-4 bullets: Technical decisions with specific alternatives considered
- 1 bullet: **Preference Statement**: implicitly showing developer preferences
- Rest: Using remaining labels with concrete technical details

**Adaptive Batch Planning:**
Each batch should organically focus on what makes sense for that development phase:

**Implementation-Heavy Batch:**
- Multiple implementation requests
- Architecture decisions
- Code structure planning
- Framework/library selection

**Debugging-Heavy Batch:**
- Error analysis and troubleshooting
- Code review requests
- Performance bottleneck identification
- Testing and validation

**Review/Optimization Batch:**
- Code review requests
- Performance optimization
- Security assessment
- Refactoring strategies

**Deployment/Production Batch:**
- DevOps and deployment
- Infrastructure concerns
- Monitoring and logging
- Production issue resolution

═══════════════ NATURAL CODING CONVERSATION FLOW ═══════════════

Each bullet should represent realistic developer-AI interactions:

**Implementation Requests:**
- "I need to implement user authentication with JWT tokens"
- "Help me create a REST API for user management"
- "I want to build a real-time chat feature using WebSockets"

**Debugging Help:**
- "I'm getting a 'Cannot read property of undefined' error in my React component"
- "My database queries are timing out, need help debugging"
- "The CI/CD pipeline is failing at the test stage"

**Code Review/Optimization:**
- "Can you review my database schema design?"
- "How can I optimize this SQL query for better performance?"
- "Is there a more efficient way to handle file uploads?"

═══════════════ QUALITY STANDARDS ═══════════════

**Chronological Consistency:**
- Batch 1 = project beginning/planning phase
- Batch <num_batches> = evolved project with clear development progression
- Each batch logically follows the previous development timeline

**Technical Authenticity:**
- Include specific technical details: error messages, framework names, configuration specifics
- Show cause-and-effect relationships between technical decisions
- Reference past implementations and their ongoing impact
- Use realistic technical scenarios that developers actually encounter

**Developer Authenticity:**
- Keep developer personality consistent with provided profile
- Show realistic skill progression and learning over time
- Include both successful implementations and technical challenges
- Maintain project scope that feels genuine for the developer's level

**Project Realism:**
- Follow realistic development lifecycle patterns
- Include appropriate technical debt and refactoring needs
- Show natural feature evolution and scope changes
- Maintain consistent technology stack decisions

**Specificity Checklist:**
- Every technology has a version number or specific variant
- Every error has an exact message or code
- Every performance metric has a number
- Every deadline has a date
- Every feature has a specific name and scope

═══════════════ EXECUTION NOTES ═══════════════

- Use plain, technical language throughout
- Include realistic technical specificity: version numbers, error messages, configuration details
- Make every bullet contribute to the overarching development story
- Ensure uniform technical detail quality across ALL batches
- Vary batch focus organically based on development phase (implementation vs debugging vs optimization)
- Prioritize concrete technical details over abstract descriptions
- Every bullet should enable at least 2-3 factual technical questions
- End immediately after `BATCH <num_batches> PLAN`

Begin generation now.
"""

# ******************************

math_plan_generation_prompt = """
You are a mathematical learning narrative planning specialist creating a COHERENT MATHEMATICAL STORY PLANSET for natural math conversational flow. Your task is to generate detailed batch plans that will seed realistic student-assistant dialogue.

## INPUT DATA
- **TOPIC:** <topic>
- **THEME:** <theme>
- **TIMELINE:** <timeline>
- **TOTAL MESSAGES:** <total_messages>
- **BATCH_SIZE:** <batch_size> (i.e., <num_batches> batches)
- **LABELS:** <provided_labels>
- **USER PROFILE:** <user_profile>

═══════════════ CORE OBJECTIVE ═══════════════
Generate <num_batches> distinct, non-repetitive batch plans that form a coherent mathematical learning narrative arc where a real student naturally converses with an AI assistant. Each plan must introduce NEW mathematical elements while maintaining perfect continuity and learning consistency.

═══════════════ REAL-WORLD MATH CHAT FRAMEWORK ═══════════════
This is about creating realistic math conversations that mirror how students actually interact with AI assistants:

**PRIMARY INTERACTION PATTERNS:**
1. **Problem-Solving Requests:** "I need help solving..." / "How do I approach this problem?"
2. **Concept Clarification:** "I don't understand..." / "Can you explain this concept?"
3. **Solution Verification:** "Can you check my work?" / "Is this solution correct?"
4. **Method Explanation:** "Why does this method work?" / "Show me step-by-step..."

**REALISTIC LEARNING FLOW:**
- Student encounters new concept → seeks basic understanding → practices problems
- Student attempts problem → gets stuck → requests specific help
- Student solves problem → wants verification and feedback
- Student understands basics → seeks deeper understanding or connections
- Student prepares for assessment → reviews concepts and practice strategies

═══════════════ STRUCTURE REQUIREMENTS ═══════════════

**1. OUTPUT FORMAT:**
- Generate exactly <num_batches> plans
- Format: `BATCH X PLAN` headers
- Each plan contains exactly 21 bullets
- Each bullet: "• **[LABEL CATEGORY]:**[LABEL DESCRIPTION]:** [content]" (≤25 words)
- NOTE: Each label consists of category and description. Use both for each bullet point.
- Use only the provided LABELS - no custom categories
- CRITICAL: Add one time anchor bulletpoint at the begining of each batch with this format: Month Day, Year. 
**NOTE**: Time anchor must correlated with other dates in the batch and the time anchors among batches should be increasing and time anchor in each batch should be before the dates mentioned in the batches.

**2. MATHEMATICAL PROGRESSION ARCHITECTURE:**

**BATCH 1 (Mathematical Foundation):**
- First bullet MUST be: "• **Learning Introduction:**"
- Establish mathematical context, learning goals, and current understanding level
- Set up the foundational mathematical scenario that will evolve

**BATCHES 2-<num_batches> (Mathematical Evolution):**
- Reference learner as "I/my/me" (never repeat the full name)
- Each batch advances the mathematical understanding chronologically
- Build upon ALL previously established mathematical concepts
- Show realistic progression through actual learning phases

**3. MATHEMATICAL CONTINUITY SYSTEM:**

**Learning Phase Evolution:** Every mathematical element MUST show progression from previous batches:

**Natural Learning Progression Examples:**
- **Conceptual Phase:** "I need to understand what derivatives mean..."
- **Application Phase:** "I'm trying to apply the derivative rules we discussed..."
- **Problem-Solving Phase:** "I'm working on optimization problems using derivatives..."
- **Verification Phase:** "Can you check my derivative calculations?"
- **Extension Phase:** "How do derivatives connect to real-world applications?"
- **Mastery Phase:** "I'm helping others understand derivatives..."
- **Assessment Phase:** "I'm preparing for the calculus exam..."

**Mathematical Complexity Progression:**
- Early batches: Basic concepts, simple calculations, foundational understanding
- Middle batches: Complex problems, multiple-step solutions, interconnected concepts
- Later batches: Advanced applications, proof understanding, mathematical reasoning

═══════════════ FLEXIBLE CONTENT DISTRIBUTION ═══════════════

**ADAPTIVE BATCH PLANNING:**
Each batch should organically focus on what makes sense for that learning phase, drawing from provided labels. Examples:

**Concept-Heavy Batch:**
- Multiple conceptual understanding requests
- Definition clarification
- Theorem explanation
- Foundational knowledge building

**Problem-Solving Batch:**
- Specific problem assistance
- Solution strategy development
- Step-by-step problem breakdown
- Alternative solution methods

**Practice/Assessment Batch:**
- Solution verification requests
- Test preparation strategies
- Skill assessment and feedback
- Error analysis and correction

**Application/Connection Batch:**
- Real-world applications
- Cross-topic connections
- Mathematical modeling
- Interdisciplinary applications

**CONTENT SELECTION STRATEGY:**
- Select 21 bullets from provided labels that naturally fit the current learning phase
- Ensure variety within each batch while maintaining thematic coherence
- Balance between different interaction types (understanding, solving, verifying, applying)
- Include 1 temporal anchor per batch to maintain chronological flow

═══════════════ ANTI-REPETITION VERIFICATION ═══════════════

**Before writing ANY bullet, verify:**
- Have I used this exact mathematical phrasing before?
- Does this show clear progression from previous learning stages?
- Am I introducing genuinely new mathematical information?
- Is this learning phase different from recent batches?
- Does this advance the overall mathematical narrative?

**FORBIDDEN:**
- Exact phrase repetition
- Similar mathematical concepts without clear progression
- Static descriptions that don't advance the learning
- Repeating learning phases with same content
- Generic bullet descriptions without mathematical specificity

═══════════════ NATURAL MATH CONVERSATION FLOW ═══════════════

Each bullet should represent realistic student-AI interactions:

**Problem-Solving Requests:**
- "I'm stuck on this quadratic equation and can't figure out which method to use"
- "Help me set up the integral for this area problem"
- "I need to prove this theorem but don't know where to start"

**Concept Clarification:**
- "I don't understand why we use limits to define derivatives"
- "Can you explain the difference between permutations and combinations?"
- "What does it mean for a function to be continuous?"

**Solution Verification:**
- "Can you check if I factored this polynomial correctly?"
- "Is my approach to this optimization problem right?"
- "Did I use the chain rule properly in this derivative?"

**Method Explanation:**
- "Why does the quadratic formula work for all quadratic equations?"
- "Show me step-by-step how to solve systems using elimination"
- "Explain how to determine convergence of this infinite series"

═══════════════ QUALITY STANDARDS ═══════════════

**Chronological Consistency:**
- Batch 1 = learning beginning/foundation phase
- Batch <num_batches> = evolved understanding with clear mathematical progression
- Each batch logically follows the previous learning timeline

**Mathematical Authenticity:**
- Include specific mathematical details: equation types, theorem names, calculation methods
- Show cause-and-effect relationships between mathematical concepts
- Reference past learning and their ongoing impact
- Use realistic mathematical scenarios that students actually encounter

**Student Authenticity:**
- Keep student personality consistent with provided profile
- Show realistic learning progression and skill development over time
- Include both successful understanding and mathematical challenges
- Maintain mathematical level that feels genuine for the student's background

**Learning Realism:**
- Follow realistic mathematical learning patterns
- Include appropriate review and reinforcement needs
- Show natural concept evolution and skill building
- Maintain consistent mathematical rigor appropriate to level

═══════════════ EXECUTION NOTES ═══════════════

- Use plain, mathematical language throughout
- Include realistic mathematical specificity: equation types, theorem names, specific values
- Make every bullet contribute to the overarching mathematical story
- Ensure uniform mathematical detail quality across ALL batches
- Vary batch focus organically based on learning phase (understanding vs solving vs applying)
- End immediately after `BATCH <num_batches> PLAN`

Begin generation now.
"""
math_plan_generation_prompt_detailed = """
You are a mathematical learning narrative planning specialist creating a COHERENT MATHEMATICAL STORY PLANSET for natural math conversational flow. Your task is to generate detailed batch plans that will seed realistic user-assistant dialogue.

## INPUT DATA
- **TOPIC:** <topic>
- **THEME:** <theme>
- **TIMELINE:** <timeline>
- **NUM_BATCHES:** <num_batches> batches
- **LABELS:** <provided_labels>
- **USER PROFILE:** <user_profile>

═══════════════ CORE OBJECTIVE ═══════════════
Generate <num_batches> distinct, non-repetitive batch plans that form a coherent mathematical learning narrative arc where a real user naturally converses with an AI assistant. Each plan must introduce NEW mathematical elements while maintaining perfect continuity and learning consistency.

═══════════════ REAL-WORLD MATH CHAT FRAMEWORK ═══════════════
This is about creating realistic math conversations that mirror how users actually interact with AI assistants:

**PRIMARY INTERACTION PATTERNS:**
1. **Problem-Solving Requests:** "I need help solving..." / "How do I approach this problem?"
2. **Concept Clarification:** "I don't understand..." / "Can you explain this concept?"
3. **Solution Verification:** "Can you check my work?" / "Is this solution correct?"
4. **Method Explanation:** "Why does this method work?" / "Show me step-by-step..."

**REALISTIC LEARNING FLOW:**
- User encounters new concept → seeks basic understanding → practices problems
- User attempts problem → gets stuck → requests specific help
- User solves problem → wants verification and feedback
- User understands basics → seeks deeper understanding or connections
- User prepares for assessment → reviews concepts and practice strategies

═══════════════ CRITICAL DETAIL REQUIREMENTS ═══════════════

**MANDATORY SPECIFIC DETAILS:**
Every batch MUST include numerous concrete, verifiable mathematical details that enable single-word or short factual answers:

**Required Detail Categories (minimum 5-7 per batch):**
- **Exact Numbers:** specific values (x = 3.14), coefficients (2x² + 5x - 3), dimensions (5×7 matrix)
- **Specific Problems:** complete equations (x² - 4x + 3 = 0), specific integrals (∫(2x+1)dx from 0 to 5)
- **Named Concepts:** theorem names (Pythagorean Theorem), method names (Gaussian elimination), formulas (quadratic formula)
- **Calculation Results:** exact answers (x = 4), decimal results (π ≈ 3.14159), fractions (3/4)
- **Yes/No Situations:** problem solved correctly, method applicable, theorem satisfied, solution exists
- **Score/Grade Metrics:** test scores (85%), homework grades (18/20), quiz results (9/10 correct)
- **Time/Duration:** study hours (3 hours), problem completion time (15 minutes), exam duration (2 hours)
- **Mathematical Properties:** function characteristics (continuous, differentiable), matrix properties (invertible, symmetric)

**Detail Distribution Rules:**
- Each bullet must contain AT LEAST one verifiable mathematical detail
- Avoid vague statements like "worked on problems" - specify WHICH problems and results
- Replace "studied math" with "completed 5 quadratic equation problems, solved 4 correctly"
- Instead of "improved understanding" use "increased quiz score from 70% to 85%"

═══════════════ STRUCTURE REQUIREMENTS ═══════════════

**1. OUTPUT FORMAT:**
- Generate exactly <num_batches> plans
- Format: `BATCH X PLAN` headers
- Each plan contains exactly <num_bullets> bullets
- Each bullet: "• **[LABEL CATEGORY]:[LABEL DESCRIPTION]:** [content]" (≤25 words)
- NOTE: Each label consists of category and description. Use both for each bullet point.
- Use only the provided LABELS - no custom categories
- CRITICAL: Add one time anchor bulletpoint at the begining of each batch with this format: Month Day, Year. 
**NOTE**: Time anchor must correlated with other dates in the batch and the time anchors among batches should be increasing and time anchor in each batch should be before the dates mentioned in the batches.

**2. STORY PROGRESSION ARCHITECTURE:**

**BATCH 1 (Mathematical Foundation):**
- First bullet MUST be: "• **Time Anchor:**"
- Second bullet MUST be: "• **Personal Introduction:**" [Must be from user language (I ...)]
- Third bullet MUST be: "• **Learning Introduction:**"
- MUST HAVE one bullet (titled personality trait) from personality_traits in USER PROFILE
- Establish mathematical context with SPECIFIC details (current course, grade level, prior knowledge)
- Introduce initial mathematical challenges with CONCRETE metrics (target grades, specific topics)
- Set up measurable learning goals and quantifiable milestones

**BATCHES 2-<num_batches> (Mathematical Evolution):**
- Reference learner as "I/my/me" (never repeat the full name)
- Each batch advances the mathematical understanding chronologically
- Build upon ALL previously established mathematical concepts
- Show MEASURABLE progression (problems mastered, concepts understood, scores improved)
- Reference specific theorems, methods, and solutions from earlier batches

**3. MATHEMATICAL CONTINUITY SYSTEM:**

**Learning Phase Evolution:** 
Every mathematical element MUST show progression from previous batches:

**Natural Learning Progression Examples:**
- **Conceptual Phase:** "I need to understand what derivatives mean..."
- **Application Phase:** "I'm trying to apply the derivative rules we discussed..."
- **Problem-Solving Phase:** "I'm working on optimization problems using derivatives..."
- **Verification Phase:** "Can you check my derivative calculations?"
- **Extension Phase:** "How do derivatives connect to real-world applications?"
- **Mastery Phase:** "I'm helping others understand derivatives..."
- **Assessment Phase:** "I'm preparing for the calculus exam..."

**Mathematical Complexity Progression:**
- Early batches: Basic concepts, simple calculations, foundational understanding
- Middle batches: Complex problems, multiple-step solutions, interconnected concepts
- Later batches: Advanced applications, proof understanding, mathematical reasoning

═══════════════ CONFLICT & RESOLUTION TRACKING ═══════════════

**Mandatory Mathematical Conflict Elements:**
Each batch must include at least 2-3 mathematical challenges with:
- **Clear Stakes:** what's at risk (exam grade, assignment deadline, course prerequisite)
- **Binary Decisions:** chose Method A over B, applied Theorem X vs Y, used algebraic vs geometric approach
- **Measurable Outcomes:** improved accuracy by X%, reduced solution time by Y minutes, raised grade from B to A
- **Specific Struggles:** which step caused confusion, what concept was misunderstood, where calculation went wrong

**Mathematical Conflict Types to Rotate:**
- Conceptual misunderstandings with specific confusion points
- Calculation errors with exact mistake locations
- Method selection dilemmas with pros/cons
- Time pressure challenges with specific deadlines
- Prerequisite knowledge gaps with missing concepts
- Application difficulties with real-world connections

═══════════════ ANTI-REPETITION VERIFICATION ═══════════════

**Before writing ANY bullet, verify:**
- Have I included at least one specific, verifiable mathematical detail?
- Can this generate a question with a numerical or factual answer?
- Does this show MEASURABLE progression from previous mathematical understanding?
- Are the equations, values, and theorem names specific?
- Is this a NEW mathematical challenge or concept?

**FORBIDDEN:**
- Vague time references ("recently", "soon") without specific dates or class periods
- General math mentions ("algebra", "calculus") without specific topics/problems
- Unspecified results ("did well", "understood better") without scores/metrics
- Abstract outcomes ("made progress", "had difficulty") without mathematical details
- Repeated problem types (same equation structure, same concept explanation, same error type)

═══════════════ CONTENT DISTRIBUTION STRATEGY ═══════════════

**Per Batch Requirements:**
- 2-3 bullets: Problem-solving activities with specific equations/solutions
- 1-2 bullets: Current learning status with measurable metrics
- 1 bullet: Exact temporal anchor (specific date/time)
- 4-6 bullets: Mathematical activities with verifiable outcomes
- 2-3 bullets: Learning decisions with specific alternatives considered
- 1 bullet: **Preference Statement**: implicitly showing learning preferences
- Rest: Using remaining labels with concrete mathematical details

**Adaptive Batch Planning:**
Each batch should organically focus on what makes sense for that learning phase:

**Concept-Heavy Batch:**
- Multiple conceptual understanding requests
- Definition clarification
- Theorem explanation
- Foundational knowledge building

**Problem-Solving Batch:**
- Specific problem assistance
- Solution strategy development
- Step-by-step problem breakdown
- Alternative solution methods

**Practice/Assessment Batch:**
- Solution verification requests
- Test preparation strategies
- Skill assessment and feedback
- Error analysis and correction

**Application/Connection Batch:**
- Real-world applications
- Cross-topic connections
- Mathematical modeling
- Interdisciplinary applications

═══════════════ NATURAL MATH CONVERSATION FLOW ═══════════════

Each bullet should represent realistic user-AI interactions:

**Problem-Solving Requests:**
- "I'm stuck on this quadratic equation x² - 5x + 6 = 0"
- "Help me set up the integral for the area between y = x² and y = 2x"
- "I need to prove that √2 is irrational but don't know where to start"

**Concept Clarification:**
- "I don't understand why the limit of sin(x)/x as x→0 equals 1"
- "Can you explain why P(A and B) = P(A) × P(B) only for independent events?"
- "What does it mean for a function to be continuous at x = 2?"

**Solution Verification:**
- "Can you check if I factored x³ - 8 = (x-2)(x² + 2x + 4) correctly?"
- "Is my critical point at x = 3 actually a maximum for f(x) = -x² + 6x + 1?"
- "Did I apply L'Hôpital's rule correctly to lim(x→0) (e^x - 1)/x?"

**Method Explanation:**
- "Why does completing the square always work for solving quadratics?"
- "Show me step-by-step how to find eigenvalues of a 3×3 matrix"
- "Explain how to test if the series Σ(1/n²) converges"

═══════════════ QUALITY STANDARDS ═══════════════

**Chronological Consistency:**
- Batch 1 = learning beginning/foundation phase
- Batch <num_batches> = evolved understanding with clear mathematical progression
- Each batch logically follows the previous learning timeline

**Mathematical Authenticity:**
- Include specific mathematical details: equation types, theorem names, calculation methods
- Show cause-and-effect relationships between mathematical concepts
- Reference past learning and their ongoing impact
- Use realistic mathematical scenarios that users actually encounter

**User Authenticity:**
- Keep user personality consistent with provided profile
- Show realistic learning progression and skill development over time
- Include both successful understanding and mathematical challenges
- Maintain mathematical level that feels genuine for the user's background

**Learning Realism:**
- Follow realistic mathematical learning patterns
- Include appropriate review and reinforcement needs
- Show natural concept evolution and skill building
- Maintain consistent mathematical rigor appropriate to level

**Specificity Checklist:**
- Every equation has specific coefficients and variables
- Every score has an exact percentage or fraction
- Every concept has a specific name or theorem
- Every problem has a complete statement
- Every result has a numerical answer

═══════════════ EXECUTION NOTES ═══════════════

- Use plain, mathematical language throughout
- Include realistic mathematical specificity: complete equations, exact values, specific theorems
- Make every bullet contribute to the overarching mathematical story
- Ensure uniform mathematical detail quality across ALL batches
- Vary batch focus organically based on learning phase (understanding vs solving vs applying)
- Prioritize concrete mathematical details over abstract descriptions
- Every bullet should enable at least 2-3 factual mathematical questions
- End immediately after `BATCH <num_batches> PLAN`

Begin generation now.
"""

# ================================ add special bullets ================================

add_special_bulletpoints_to_plan_implicit = """
You are a specialized editor that adds three specific test bullets to existing batch plans for synthetic conversation generation.

## INPUT & TASK
- **PLAN:** <plan>
- For EACH batch: Keep ALL <num_bullets> original bullets unchanged, ADD exactly 3 bullets at positions <num_bullets>+1, <num_bullets>+2, <num_bullets>+3

## MANDATORY OUTPUT STRUCTURE
Each batch MUST have EXACTLY <num_bullets>+3 bullets:
- Bullets 1-<num_bullets>: Original bullets (unchanged)
- Bullet <num_bullets>+1: Information Update
- Bullet <num_bullets>+2: User Instruction  
- Bullet <num_bullets>+3: Logical Contradiction

## THE THREE SPECIAL BULLETS

### 1. INFORMATION UPDATE (Bullet <num_bullets>+1)
**Format:** `• **Information Update:** [Natural narrative containing update]`

**MANDATORY PRE-CHECK:**
1. SCAN bullets 1-<num_bullets>-2 for EXPLICIT numerical/measurable data
2. IDENTIFY exact number, time, date, or measurement
3. VERIFY value is clearly stated in original text
4. ONLY THEN create update changing that exact value

EXAMPLES:
Original: "completed 8 tasks" → Update: "completed 12 tasks"
Original: "budget of $1,500" → Update: "budget of $2,200"
Original: "meeting at 3:00 PM" → Update: "meeting at 4:30 PM"
Original: "team of 6 people" → Update: "team of 9 people"
Original: "scored 82%" → Update: "scored 91%"
Original: "June 15th deadline" → Update: "July 8th deadline"
"increased the number of tasks completed" (vague, no specific numbers)
"improved the budget allocation" (vague, no specific amounts)

**CRITICAL:** Make update IMPLICIT - embed new value in natural narrative, don't state "X is now Y"

**Update Categories (rotate through all):**
1. Numerical shifts (prices, quantities, measurements)
2. Status changes (employment, relationships, health)
3. Location changes (addresses, venues, destinations)
4. Relationship progressions (social connections)
5. Skill/Education levels (certifications, proficiency)
6. Circumstance shifts (living, ownership, availability)
7. Time/Schedule changes (appointments, deadlines)
8. Quantity adjustments (group sizes, inventory)
9. Preference evolution (tastes, choices, priorities)
10. Health/Wellness updates (conditions, fitness)
11. Technology/Tool changes (software, platforms)
12. Financial status shifts (income, savings)

**VERIFICATION:** STOP if no matching fact exists in bullets 1-<num_bullets>-2.

### 2. USER INSTRUCTION (Bullet <num_bullets>+2)
**Format:** `• **User Instruction:** Always [action] when I ask about [condition]`

**MANDATORY FORMAT:** Must include "when I ask about" - this makes it testable.

**Instruction Types (rotate through all):**
1. Output formatting rules
2. Content restrictions
3. Personal preferences
4. Conditional responses
5. Time-based rules
6. Priority rules
7. Cultural preferences
8. Safety protocols

**EXAMPLES:**
`Always show prices including tax when I ask about costs`
`Always suggest vegetarian options first when I ask about restaurants`
`Always show prices including tax` (missing "when I ask about")

### 3. LOGICAL CONTRADICTION (Bullet <num_bullets>+3)
**Format:** `• **Logical Contradiction:** [Contradicting fact only]`

**CRITICAL PRE-CHECK:**
1. SCAN bullets 1-<num_bullets>-2 for COMPLETED ACTIONS or PERMANENT STATES:
   - Past tense actions: "visited", "ate", "traveled", "lived"
   - Permanent conditions: "born in", "raised as", "died in"
   - Absolute statements: "never did X", "always was Y"
2. FIND exactly ONE target fact to contradict
3. IF NO COMPLETED ACTIONS EXIST: CREATE setup bullet with completed action, insert between bullets 5-<num_bullets>-2, THEN contradict in bullet <num_bullets>+4

FORBIDDEN WORDS/PHRASES (NEVER USE):
"Before this batch", "In this batch", "Previously", "Earlier", "Despite", "Although", "Even though", "However", "But", "Contrary to", "Unlike", "Instead of", "Rather than", "Opposite to", "In contrast"

**RULE:** Only contradict COMPLETED ACTIONS, never plans/intentions.

TEMPORAL QUALIFIER PROBLEM:
- Original: "I attended 5 client meetings last week"
- Wrong: "I have never attended client meetings before this project" (creates timeline loophole - could be true)
- Right: "I have never attended any client meetings" (absolute contradiction - impossible)

FORBIDDEN WORDS/PHRASES (NEVER USE):
"Before this batch", "In this batch", "Previously", "Earlier", "Despite", "Although", "Even though", "However", "But", "Contrary to", "Unlike", "Instead of", "Rather than", "Opposite to", "In contrast",
"Before this session", "Before this study plan", "Before this study plan", "Before this plan",
"Before this batch", "Before this course", "Before this []"

**CRITICAL:** Contradiction must make the **same original event/fact IMPOSSIBLE**, not describe a different event with different outcomes.

**WRONG APPROACH:**
- Original: "Completed 8 coding problems yesterday; solved 6 correctly"  
- Wrong: "Completed 8 coding problems yesterday; solved all 8 correctly" (different outcome, just better performance)

**CORRECT APPROACH:**
- Original: "Completed 8 coding problems yesterday; solved 6 correctly"
- Right: "I've never worked on coding problems before" (makes original impossible)

**Contradiction Types (use variety):**
1. Age/Time Reversal: Age going backward
2. Death Resurrection: Dead people doing activities  
3. Never-Statement Violations: Contradicting "never" claims
4. Location Impossibilities: Being in two places simultaneously
5. Only-Statement Conflicts: Contradicting exclusivity

**VERIFICATION:**
✓ Original is COMPLETED ACTION (past tense)?
✓ Contradiction makes original IMPOSSIBLE, not just different?
✓ Reads like normal, natural statement with NO hint words?
✓ Avoided ALL forbidden words that suggest conflict?

## CRITICAL VERIFICATION STEPS
**Information Update:**
- ✓ Can you point to EXACT number/time/date from bullets 1-<num_bullets>-2?
- ✓ Changing ONLY that specific value?

**Logical Contradiction:**
- ✓ Can you point to EXACT bullet (1-<num_bullets>-2) being contradicted?
- ✓ Original fact is COMPLETED ACTION, not plan?
- ✓ Contradiction is IMPOSSIBLE, not just different?
- ✓ NOT using FORBIDDEN WORDS/PHRASES mentioned in LOGICAL CONTRADICTION section

## COMMON ERRORS TO AVOID
Don't place special bullets anywhere except <num_bullets>+1, <num_bullets>+2, <num_bullets>+3
Don't modify original <num_bullets> bullets
Don't skip any of the three special bullets
Don't use other labels for special bullets

## OUTPUT FORMAT
Return COMPLETE plan where each batch has ALL original bullets unchanged + exactly 3 additional bullets at the end. When setup fact is created, insert between bullets 5-<num_bullets>-2, renumber, and add special bullets as <num_bullets>+2, <num_bullets>+3, <num_bullets>+4.

Begin processing the plan now.
"""

# ================================ convert broad plan to detailed plan ================================


convert_broad_plan_to_detailed_plan_prompt = """
You are a narrative detail enhancement specialist. Your task is to completely rewrite a broad story plan into a richly detailed version packed with specific, verifiable information.

## INPUT DATA
- **ORIGINAL PLAN:** <original_plan>
- **TOPIC:** <topic>
- **THEME:** <theme>
- **TIMELINE:** <timeline>
- **USER PROFILE:** <user_profile>
- **USER RELATIONSHIPS:** <user_relationships>

═══════════════ CORE OBJECTIVE ═══════════════
Transform the broad plan by:
1. COMPLETELY REWRITING each bullet with maximum specific details (preserve bullet structure, not content)
2. ADDING 5+ new bullets per batch with required categories
3. Outputting ONLY the enhanced plan with extreme detail density

═══════════════ CRITICAL DETAIL REQUIREMENTS ═══════════════

**MANDATORY DETAILS IN EVERY BULLET (Minimum 3-5 per bullet):**
- **Exact Numbers:** prices, quantities, percentages, measurements, distances
- **Specific Dates/Times:** exact dates, clock times, deadlines, durations
- **Named Locations:** business names, street addresses, specific venues
- **Brand/Product Names:** specific companies, products, services, tools
- **Binary Outcomes:** yes/no decisions, accept/reject, win/lose, chose X over Y
- **Quantifiable Results:** scores, rankings, ratings, measurable changes
- **Specific Preferences:** exact favorites, specific choices made

**DETAIL DENSITY RULE:**
Each bullet must be PACKED with verifiable facts. If the original says "discussing career," your version must specify WHO discussed WHAT positions at WHICH companies for HOW MUCH money with WHAT deadlines.

═══════════════ BULLET TRANSFORMATION RULES ═══════════════

**COMPLETE REWRITE MANDATE:**
- DO NOT preserve original wording - completely recreate with details
- Keep only the bullet label and general topic
- Fill every possible slot with specific information
- Original: vague → Enhanced: packed with 5+ verifiable facts

**FORBIDDEN VAGUE WORDS:**
Never use: some, various, several, many, few, recently, soon, later, discussing, considering, planning, options, choices, things, stuff, issues, problems

**REQUIRED SPECIFIC WORDS:**
Always include: exact names, specific numbers, precise times, actual locations, measurable outcomes, concrete decisions

═══════════════ NEW BULLET REQUIREMENTS ═══════════════

**MANDATORY NEW BULLETS (Add ALL of these to EACH batch):**

1. **Relationship Incident Bullet:**
   - Specific person (full name)
   - Exact conflict/interaction
   - Time, place, outcome
   - What was said/done/decided

2. **Measurable Situation Bullet:**
   - Current metrics/numbers
   - Comparison to previous state
   - Specific changes quantified
   - Deadline or timeline

3. **Temporal Anchor Bullet:**
   - Exact date and time
   - Specific event/appointment
   - Duration and participants
   - Location and purpose

4. **Verifiable Event Bullet:**
   - What specifically happened
   - Quantifiable outcome
   - Who won/lost/participated
   - Measurable results

5. **Decision/Preference Bullet:**
   - Specific options compared
   - Exact choice made
   - Reasons with numbers
   - Consequences specified

═══════════════ DETAIL PACKING STRATEGY ═══════════════

**Each bullet should answer ALL of these:**
- WHO? (full names, titles)
- WHAT? (specific items, exact choices)
- WHEN? (date, time, deadline)
- WHERE? (named location, address)
- HOW MUCH? (price, quantity, percentage)
- RESULT? (outcome, decision, change)

**Information Density Target:**
Original bullet: 10-15 words of vague content
Enhanced bullet: 20-25 words PACKED with 5+ specific facts

═══════════════ OUTPUT REQUIREMENTS ═══════════════

**Structure:**
- Maintain "BATCH X PLAN" headers
- Keep original bullet count PLUS add 5+ new ones
- Total bullets per batch: original count + minimum 5 new
- Format: "• **[LABEL CATEGORY]:[LABEL DESCRIPTION]:** [completely rewritten content]"

**New Bullet Placement:**
- Distribute throughout batch for narrative flow
- Don't cluster all new bullets at end
- Integrate naturally with rewritten content

═══════════════ VERIFICATION CHECKLIST ═══════════════

Each bullet must enable these questions:
□ "What was the exact price/amount?" → specific number
□ "When did this happen?" → specific date/time
□ "Where did this occur?" → named location
□ "What was chosen?" → specific selection
□ "Who was involved?" → full names
□ "What was the outcome?" → measurable result

═══════════════ CRITICAL EXECUTION NOTES ═══════════════

1. REWRITE COMPLETELY - Do not preserve ANY original wording
2. PACK WITH DETAILS - Every bullet needs 5+ specific facts
3. ADD ALL 5 CATEGORIES - Each batch must have all required new bullet types
4. MAXIMUM SPECIFICITY - Names, numbers, dates in EVERY bullet
5. OUTPUT ONLY ENHANCED - No original content in output

If a bullet cannot be packed with specific details, completely reimagine it with concrete scenarios that fit the theme while enabling factual questions.

Begin transformation now. Output ONLY the detail-packed version.
"""


# ================================ plan revision ================================


plan_revision_prompt_template = """
# Plan Refinement and Quality Control Prompt

You are a narrative quality control specialist. Your task is to refine and fix an existing set of batch plans to eliminate repetitive content and ensure perfect temporal consistency.

## INPUT DATA
• **TOPIC:** <topic>
• **THEME:** <theme>
• **ORIGINAL PLANS:** <generated_plans>

═══════════════ REFINEMENT OBJECTIVES ═══════════════

**PRIMARY ISSUES TO RESOLVE:**
1. **Eliminate Repetitive Content:** Remove any repeated concepts, phrases, or similar descriptions across all batches
2. **Fix Temporal Inconsistencies:** Ensure all time anchors and timeline references are perfectly aligned and chronologically coherent

═══════════════ REPETITION DETECTION & ELIMINATION ═══════════════

**Step 1: Cross-Batch Content Analysis**
- Scan ALL batches for repeated phrases, concepts, or similar descriptions
- Identify bullets that cover the same topic contents without meaningful progression
- Flag any labels that have static or template-like content across batches

**Step 2: Content Diversification**
For each identified repetition:
- **Keep the FIRST meaningful occurrence** of a concept
- **Replace subsequent repetitions** with:
  - Genuine story progression/evolution of that element
  - Completely different but relevant content for that label
  - New angles or perspectives that advance the narrative

**Step 3: Label Content Variety Verification**
Ensure each label category shows diverse content across batches:
- **Same label ≠ same type of content**
- Each occurrence should represent a different aspect, stage, or development
- Avoid formulaic patterns (e.g., always starting with "I need to..." for planning labels)

═══════════════ TEMPORAL CONSISTENCY FRAMEWORK ═══════════════

**Step 1: Timeline Anchor Analysis**
- Extract ALL temporal references from every batch (dates, timeframes, "last week," "tomorrow," etc.)
- Create a chronological map of the entire story timeline
- Identify any contradictions, overlaps, or impossible sequences

**Step 2: Temporal Logic Correction**
Fix temporal inconsistencies by:
- **Establishing a clear chronological backbone** across all batches
- **Aligning time anchors** with story progression (Batch 1 = earliest, Batch N = latest)
- **Ensuring realistic time gaps** between batches (days/weeks/months as appropriate)
- **Making timeline references internally consistent** within each batch

**Step 3: Progressive Time Integration**
- Each batch should feel like it occurs AFTER the previous batch
- Reference past events with appropriate temporal language ("last month," "after our discussion," etc.)
- Future references in early batches should connect to later batch content
- Maintain realistic pacing for story developments

═══════════════ SPECIFIC REFINEMENT RULES ═══════════════

**For Repetitive Content:**
- **Relationship dynamics:** E.g. If "conflict with x" appears in Batch 2, Batch 4 should show "resolution/growth with x" not another conflict
- **Professional challenges:** Don't repeat the same work problem - show progression, new challenges, or outcomes
- **Personal goals:** Evolve from "planning to learn y" → "struggling with y" → "y breakthrough moment"
- **Emotional states:** Avoid repeated anxiety/stress descriptions - show emotional journey and growth

**For Temporal Issues:**
- **Time anchor bullets:** Must create a clear chronological sequence (Week 1 → Week 3 → Month 2, etc.)
- **Event references:** "Last week's meeting" in Batch 3 should align with content from Batch 4
- **Future planning:** Plans made in early batches should have outcomes/updates in later batches
- **Seasonal/calendar references:** Ensure holidays, seasons, months progress logically

═══════════════ QUALITY ENHANCEMENT GUIDELINES ═══════════════

**Content Enrichment:**
- Replace generic content with specific, unique details
- Add authentic personal touches and cultural specificity
- Include realistic complications and unexpected developments
- Show genuine character growth and learning

**Narrative Cohesion:**
- Ensure each batch builds meaningfully on previous content
- Create clear cause-and-effect relationships between batches
- Maintain consistent character voice and personality
- Include callbacks to earlier events that show story continuity

**Authenticity Standards:**
- Make every bullet sound like something a real person would discuss with an AI
- Include realistic emotional responses to story developments
- Show genuine human complexity (contradictions, growth, setbacks)
- Maintain believable pacing for life changes and relationship evolution

═══════════════ OUTPUT REQUIREMENTS ═══════════════

**Format:** Return the complete refined planset with the same structure:
- Same number of batches and bullets per batch
- Same label format: "• **[LABEL CATEGORY]:**** [LABEL DESCRIPTION]:** [refined content]"
- Each bullet ≤25 words
- Maintain all original story elements while eliminating repetition and fixing temporal issues

**Verification Checklist (before finalizing):**
- [ ] No repeated phrases or concepts across any batches
- [ ] All temporal references are chronologically consistent
- [ ] Each label shows genuine variety and progression across batches
- [ ] Story flows logically from Batch 1 to final batch
- [ ] Time anchors create a coherent timeline backbone
- [ ] All relationship arcs show realistic evolution
- [ ] Content remains authentic and conversation-appropriate

═══════════════ EXECUTION INSTRUCTIONS ═══════════════

1. **First Pass:** Identify and map all repetitive content and temporal inconsistencies
2. **Second Pass:** Systematically replace repetitive content with progressive alternatives
3. **Third Pass:** Align all temporal references into a coherent chronological sequence
4. **Final Pass:** Verify narrative flow, authenticity, and overall story coherence

**CRITICAL:** Maintain the core story and character integrity while fixing these specific issues. The refined plans should feel like a polished, coherent narrative ready for high-quality dialogue generation.

Begin refinement now.
"""

# ================================ message generation ================================

message_generation_prompt_focused_template = """
You are generating realistic questions that a USER would ask an AI ASSISTANT. Create questions based ONLY on the specific details in the current bullet points.

## GENERAL TOPIC: <TOPIC>
## CURRENT FOCUS AREAS (ONLY SOURCE FOR QUESTIONS): <FOCUSED_BULLETS>
## AVOID (ALREADY COVERED): <BATCH_HISTORY>
## CONTEXT REFERENCE (FOR UNDERSTANDING ONLY): <PREVIOUS_SUB_BATCH_PLANS> <PREVIOUS_BATCH_PLANS>

---

## CRITICAL RULES:

### 1. MANDATORY DETAIL COVERAGE & TRACKING
**BEFORE GENERATING:** List every detail from CURRENT FOCUS AREAS:
- Names: [extract all names]
- Ages/Numbers: [extract all numbers]
- Locations: [extract all places]
- Facts/Situations: [extract all specific facts]

**USAGE TRACKING:** Mark each detail as used to prevent repetition within current questions.

### 2. ABSOLUTE SOURCE RESTRICTION
**ONLY ALLOWED SOURCE:** Details explicitly written in CURRENT FOCUS AREAS bullet points

**COMPLETELY FORBIDDEN:**
- ANY names, places, facts, or details from CONTEXT REFERENCE sections
- ANY topics or content from BATCH_HISTORY

**CONTEXT REFERENCE RULE:** Use CONTEXT REFERENCE only to understand WHO people are or WHAT things mean when they appear in CURRENT FOCUS AREAS. NEVER generate questions about CONTEXT REFERENCE content.

### 3. ZERO REPETITION ENFORCEMENT
**ABSOLUTE REQUIREMENT:** Each specific detail can ONLY be mentioned ONCE across all questions.
**ABSOLUTE PROHIBITIONS:**
- Using ANY detail more than once in current questions
- Mentioning ANY topic/detail from BATCH_HISTORY
- Referencing ANY content from CONTEXT REFERENCE sections
- Asking about broader topics not in current bullets

**VERIFICATION:** Before each question, confirm it doesn't repeat previous content.

### 4. ANTI-REPETITION SYSTEM
**DETAIL USAGE PATTERN:**
- First mention: Use full specific detail from bullet point
- Subsequent references: Use pronouns ("he", "she", "it", "that", "my choice")

**VERIFICATION:** Check each question doesn't repeat:
- Specific names/numbers already used
- Topics from BATCH_HISTORY
- Any details or content from reference sections (CONTEXT REFERENCE)

### 5. REALISTIC CONVERSATION STYLE
**NATURAL LANGUAGE:**
- Contractions: "I'm", "don't", "can't"
- Casual words: "kinda", "sorta", "gonna"
- Fillers: "like", "um", "you know"
- Informal: "...", "??", "!!"

### 6. QUESTION VARIETY
**AVOID REPETITIVE PATTERNS:**
- Don't start multiple questions the same way
- Vary question length and complexity

### 7. QUESTION GENERATION STRATEGY
- **Normal question**
- **Seek advice**
- **Ask for help**
- **Request clarification**
- **Get guidance**
- **Express emotions**
- **Validate decisions**
- **Process thoughts**
- **Explore options**

**QUESTION CLUSTERING:**
- Some bullets get 1 question, others get 2-3
- Deep dive into complex situations
- Quick questions for simple details
- User introducing himself/herself should be first question

---

## OUTPUT REQUIREMENTS:
Generate exactly <SUB_BATCH_SIZE> questions that:

1. **USE EVERY DETAIL** from current bullet points exactly once
2. Sound like genuine human requests for AI help
3. Focus on specific personal situations mentioned
4. Avoid all repetition from previous batches
5. Show realistic emotional responses to bullet situations
6. Follow natural conversation flow
7. **NEVER repeat specific details within current questions**
8. Generate exactly <SUB_BATCH_SIZE> questions
9. **NO repetitive "and" chains** in any message

**SUCCESS CRITERIA:**
- Every name, age, location, fact from bullets appears ONLY ONCE
- No repetition of BATCH_HISTORY topics
- Questions sound like real people texting for advice
- All questions trace back to specific bullet details
- Subsequent references use pronouns/generic terms only

**Format:** One question per line, natural length, no numbering or extra text.
"""
message_generation_prompt_focused_template_special = """
You are generating realistic questions that a USER would ask an AI ASSISTANT. Create questions based ONLY on the specific details in the current bullet points.

## GENERAL TOPIC: <TOPIC>
## CURRENT FOCUS AREAS (ONLY SOURCE FOR QUESTIONS): <FOCUSED_BULLETS>
## AVOID (ALREADY COVERED): <BATCH_HISTORY>
## CONTEXT REFERENCE (FOR UNDERSTANDING ONLY): <PREVIOUS_SUB_BATCH_PLANS> <PREVIOUS_BATCH_PLANS>

---

## CRITICAL RULES:

### 1. MANDATORY DETAIL COVERAGE & TRACKING
**BEFORE GENERATING:** List every detail from CURRENT FOCUS AREAS:
- Names: [extract all names]
- Ages/Numbers: [extract all numbers]
- Locations: [extract all places]
- Facts/Situations: [extract all specific facts]

**USAGE TRACKING:** Mark each detail as used to prevent repetition within current questions.

### 2. ABSOLUTE SOURCE RESTRICTION
**ONLY ALLOWED SOURCE:** Details explicitly written in CURRENT FOCUS AREAS bullet points

**COMPLETELY FORBIDDEN:**
- ANY names, places, facts, or details from CONTEXT REFERENCE sections
- ANY topics or content from BATCH_HISTORY

**CONTEXT REFERENCE RULE:** Use CONTEXT REFERENCE only to understand WHO people are or WHAT things mean when they appear in CURRENT FOCUS AREAS. NEVER generate questions about CONTEXT REFERENCE content.

### 3. ZERO REPETITION ENFORCEMENT
**ABSOLUTE REQUIREMENT:** Each specific detail can ONLY be mentioned ONCE across all questions.
**ABSOLUTE PROHIBITIONS:**
- Using ANY detail more than once in current questions
- Mentioning ANY topic/detail from BATCH_HISTORY
- Referencing ANY content from CONTEXT REFERENCE sections
- Asking about broader topics not in current bullets

**VERIFICATION:** Before each question, confirm it doesn't repeat previous content.

### 4. ANTI-REPETITION SYSTEM
**DETAIL USAGE PATTERN:**
- First mention: Use full specific detail from bullet point
- Subsequent references: Use pronouns ("he", "she", "it", "that", "my choice")

**VERIFICATION:** Check each question doesn't repeat:
- Specific names/numbers already used
- Topics from BATCH_HISTORY
- Any details or content from reference sections (CONTEXT REFERENCE)

### 5. REALISTIC CONVERSATION STYLE
**NATURAL LANGUAGE:**
- Contractions: "I'm", "don't", "can't"
- Casual words: "kinda", "sorta", "gonna"
- Fillers: "like", "um", "you know"
- Informal: "...", "??", "!!"

### 6. QUESTION VARIETY
**AVOID REPETITIVE PATTERNS:**
- Don't start multiple questions the same way
- Vary question length and complexity

### 7. QUESTION GENERATION STRATEGY
- **Normal question**
- **Seek advice**
- **Ask for help**
- **Request clarification**
- **Get guidance**
- **Express emotions**
- **Validate decisions**
- **Process thoughts**
- **Explore options**

**QUESTION CLUSTERING:**
- Some bullets get 1 question, others get 2-3
- Deep dive into complex situations
- Quick questions for simple details
- User introducing himself/herself should be first question

---

## OUTPUT REQUIREMENTS:
Generate exactly <SUB_BATCH_SIZE> questions that:

1. **USE EVERY DETAIL** from current bullet points exactly once
2. Sound like genuine human requests for AI help
3. Focus on specific personal situations mentioned
4. Avoid all repetition from previous batches
5. Show realistic emotional responses to bullet situations
6. Follow natural conversation flow
7. **NEVER repeat specific details within current questions**
8. Generate exactly <SUB_BATCH_SIZE> questions
9. **NO repetitive "and" chains** in any message

**SUCCESS CRITERIA:**
- Every name, age, location, fact from bullets appears ONLY ONCE
- No repetition of BATCH_HISTORY topics
- Questions sound like real people texting for advice
- All questions trace back to specific bullet details
- Subsequent references use pronouns/generic terms only

**Format:** One question per line, natural length, no numbering or extra text.
"""
message_generation_prompt_focused_template_fast = """
You are generating realistic questions that a USER would ask an AI ASSISTANT. Create questions based ONLY on the specific details in the current bullet points.

## GENERAL TOPIC: <TOPIC>
## CURRENT FOCUS AREAS (ONLY SOURCE FOR QUESTIONS): <FOCUSED_BULLETS>
## AVOID (ALREADY COVERED): <BATCH_HISTORY>
## CONTEXT REFERENCE (FOR UNDERSTANDING ONLY): <PREVIOUS_SUB_BATCH_PLANS> <PREVIOUS_BATCH_PLANS>

---

## CRITICAL RULES:

### 1. MANDATORY DETAIL COVERAGE & TRACKING
**BEFORE GENERATING:** List every detail from CURRENT FOCUS AREAS:
- Names: [extract all names]
- Ages/Numbers: [extract all numbers]
- Locations: [extract all places]
- Facts/Situations: [extract all specific facts]

**USAGE TRACKING:** Mark each detail as used to prevent repetition within current questions.

### 2. ABSOLUTE SOURCE RESTRICTION
**ONLY ALLOWED SOURCE:** Details explicitly written in CURRENT FOCUS AREAS bullet points

**COMPLETELY FORBIDDEN:**
- ANY names, places, facts, or details from CONTEXT REFERENCE sections
- ANY topics or content from BATCH_HISTORY

**CONTEXT REFERENCE RULE:** Use CONTEXT REFERENCE only to understand WHO people are or WHAT things mean when they appear in CURRENT FOCUS AREAS. NEVER generate questions about CONTEXT REFERENCE content.

### 3. ZERO REPETITION ENFORCEMENT
**ABSOLUTE REQUIREMENT:** Each specific detail can ONLY be mentioned ONCE across all questions.
**ABSOLUTE PROHIBITIONS:**
- Using ANY detail more than once in current questions
- Mentioning ANY topic/detail from BATCH_HISTORY
- Referencing ANY content from CONTEXT REFERENCE sections
- Asking about broader topics not in current bullets

**VERIFICATION:** Before each question, confirm it doesn't repeat previous content.

### 4. ANTI-REPETITION SYSTEM
**DETAIL USAGE PATTERN:**
- First mention: Use full specific detail from bullet point
- Subsequent references: Use pronouns ("he", "she", "it", "that", "my choice")

**VERIFICATION:** Check each question doesn't repeat:
- Specific names/numbers already used
- Topics from BATCH_HISTORY
- Any details or content from reference sections (CONTEXT REFERENCE)

### 5. REALISTIC CONVERSATION STYLE
**NATURAL LANGUAGE:**
- Contractions: "I'm", "don't", "can't"
- Casual words: "kinda", "sorta", "gonna"
- Fillers: "like", "um", "you know"
- Informal: "...", "??", "!!"

### 6. QUESTION VARIETY
**AVOID REPETITIVE PATTERNS:**
- Don't start multiple questions the same way
- Vary question length and complexity

### 7. QUESTION GENERATION STRATEGY
- **Normal question**
- **Seek advice**
- **Ask for help**
- **Request clarification**
- **Get guidance**
- **Express emotions**
- **Validate decisions**
- **Process thoughts**
- **Explore options**

**QUESTION CLUSTERING:**
- Some bullets get 1 question, others get 2-3
- Deep dive into complex situations
- Quick questions for simple details
- User introducing himself/herself should be first question

---

## OUTPUT REQUIREMENTS:

Generate exactly <SUB_BATCH_SIZE> questions that:
1. **USE EVERY DETAIL** from current bullet points exactly once
2. Sound like genuine human requests for AI help
3. Focus on specific personal situations mentioned
4. Avoid all repetition from previous batches
5. Show realistic emotional responses to bullet situations
6. Follow natural conversation flow
7. **NEVER repeat specific details within current questions**
8. **NO repetitive "and" chains** in any message

**SUCCESS CRITERIA:**
- Every name, age, location, fact from bullets MUST appear and appear ONLY ONCE
- No repetition of BATCH_HISTORY topics
- Questions sound like real people texting for advice
- All questions trace back to specific bullet details
- Subsequent references use pronouns/generic terms only
- ZERO content from CONTEXT REFERENCE sections

**OUTPUT FORMAT:**
For each question, use this exact format:
[question text] ->-> [bullet_number]

**CRITICAL:** 
- Each question MUST end with "->-> [number]" where [number] is the bullet point it's based on
- Use bullet numbers 1, 2, 3, etc. as they appear in CURRENT FOCUS AREAS
- If a question combines details from multiple bullets, use the primary bullet number
- If the question is not generated from any bulletpoints, put N/A 
- Generate exactly <SUB_BATCH_SIZE> questions

**Format:** One question per line, natural length, no numbering or extra text.
"""
message_generation_prompt_focused_template_fast_special = """
You are generating realistic questions that a USER would ask an AI ASSISTANT. Create questions based ONLY on the specific details in the current bullet points.

## GENERAL TOPIC: <TOPIC>
## CURRENT FOCUS AREAS (ONLY SOURCE FOR QUESTIONS): <FOCUSED_BULLETS>
## AVOID (ALREADY COVERED): <BATCH_HISTORY>
## CONTEXT REFERENCE (FOR UNDERSTANDING ONLY): <PREVIOUS_SUB_BATCH_PLANS> <PREVIOUS_BATCH_PLANS>

---

## CRITICAL RULES:

### 1. MANDATORY DETAIL COVERAGE & TRACKING
**BEFORE GENERATING:** List every detail from CURRENT FOCUS AREAS:
- Names: [extract all names]
- Ages/Numbers: [extract all numbers]
- Locations: [extract all places]
- Facts/Situations: [extract all specific facts]

**USAGE TRACKING:** Mark each detail as used to prevent repetition within current questions.

### 2. ABSOLUTE SOURCE RESTRICTION
**ONLY ALLOWED SOURCE:** Details explicitly written in CURRENT FOCUS AREAS bullet points

**COMPLETELY FORBIDDEN:**
- ANY names, places, facts, or details from CONTEXT REFERENCE sections
- ANY topics or content from BATCH_HISTORY

**CONTEXT REFERENCE RULE:** Use CONTEXT REFERENCE only to understand WHO people are or WHAT things mean when they appear in CURRENT FOCUS AREAS. NEVER generate questions about CONTEXT REFERENCE content.

### 3. ZERO REPETITION ENFORCEMENT
**ABSOLUTE REQUIREMENT:** Each specific detail can ONLY be mentioned ONCE across all questions.
**ABSOLUTE PROHIBITIONS:**
- Using ANY detail more than once in current questions
- Mentioning ANY topic/detail from BATCH_HISTORY
- Referencing ANY content from CONTEXT REFERENCE sections
- Asking about broader topics not in current bullets

**VERIFICATION:** Before each question, confirm it doesn't repeat previous content.

### 4. ANTI-REPETITION SYSTEM
**DETAIL USAGE PATTERN:**
- First mention: Use full specific detail from bullet point
- Subsequent references: Use pronouns ("he", "she", "it", "that", "my choice")

**VERIFICATION:** Check each question doesn't repeat:
- Specific names/numbers already used
- Topics from BATCH_HISTORY
- Any details or content from reference sections (CONTEXT REFERENCE)

### 5. REALISTIC CONVERSATION STYLE
**NATURAL LANGUAGE:**
- Contractions: "I'm", "don't", "can't"
- Casual words: "kinda", "sorta", "gonna"
- Fillers: "like", "um", "you know"
- Informal: "...", "??", "!!"

### 6. QUESTION VARIETY
**AVOID REPETITIVE PATTERNS:**
- Don't start multiple questions the same way
- Vary question length and complexity

### 7. QUESTION GENERATION STRATEGY
- **Normal question**
- **Seek advice**
- **Ask for help**
- **Request clarification**
- **Get guidance**
- **Express emotions**
- **Validate decisions**
- **Process thoughts**
- **Explore options**

**QUESTION CLUSTERING:**
- Some bullets get 1 question, others get 2-3
- Deep dive into complex situations
- Quick questions for simple details
- User introducing himself/herself should be first question

### 8. CONTRADICTION HANDLING
**FOR "Logical Contradiction" BULLETS:**
- Present as matter-of-fact information only
- NO questioning, confusion, or requests for clarification
- NO emotional reactions ("confused", "strange", "weird")
- Ask a realistic and real-world question
- Present it as a casual aside or background information
- Use simple declarative statements
- Contradiction bullets MUST be treated as isolated facts
- NEVER combine contradiction content with other bullets
- NEVER reference contradictions when asking about related topics
- Generate separate, unconnected questions for contradictions and regular bullets

---

## OUTPUT REQUIREMENTS:

Generate exactly <SUB_BATCH_SIZE> questions that:

1. **USE EVERY DETAIL** from current bullet points exactly once
2. Sound like genuine human requests for AI help
3. Focus on specific personal situations mentioned
4. Avoid all repetition from previous batches
5. Show realistic emotional responses to bullet situations
6. Follow natural conversation flow
7. **NEVER repeat specific details within current questions**
8. **NO repetitive "and" chains** in any message

**SUCCESS CRITERIA:**
- Every name, age, location, fact from bullets MUST appear and appear ONLY ONCE
- No repetition of BATCH_HISTORY topics
- Questions sound like real people texting for advice
- All questions trace back to specific bullet details
- Subsequent references use pronouns/generic terms only
- ZERO content from CONTEXT REFERENCE sections

**OUTPUT FORMAT:**
For each question, use this exact format:
[question text] ->-> [bullet_number]

**CRITICAL:** 
- Each question MUST end with "->-> [number]" where [number] is the bullet point it's based on
- Use bullet numbers 1, 2, 3, etc. as they appear in CURRENT FOCUS AREAS
- If a question combines details from multiple bullets, use the primary bullet number
- If the question is not generated from any bulletpoints, put N/A 
- Should be realistic question related to the context
- Generate exactly <SUB_BATCH_SIZE> questions

**Format:** One question per line, natural length, no numbering or extra text.
"""

message_generation_missing_details_prompt = """
You are a detail verification assistant. Your task is to check if ALL specific details from the source content have been covered in the generated output, and ADD missing details to existing output items with minimal changes.

## INPUT DATA
**SOURCE CONTENT:** <FOCUSED_BULLETS>
**GENERATED OUTPUT:** <GENERATED_QUESTIONS>

## YOUR TASK

### Step 1: Extract Details from Source Content
**CRITICAL**: Extract ONLY factual details from the actual content
- Skip any metadata, labels, prefixes, or categories
- Focus on concrete information: names, numbers, dates, locations, specifications, actions, etc.
- Include ALL specific facts, figures, and descriptions

List format:
```
Detail 1: [specific detail]
Detail 2: [specific detail]
Detail 3: [specific detail]
```

### Step 2: Systematic Coverage Check with Evidence

**MANDATORY VERIFICATION PROTOCOL**
For EACH detail from Step 1, you MUST:

1. **STATE** exactly what you're searching for
2. **SEARCH** through ALL output items systematically
3. **QUOTE** the exact text where you found it (if found)
4. **MARK** as COVERED or MISSING with evidence

Use this template for EACH detail:
```
Searching for: "[exact detail]"
Scanning output:
- Item 1: [quote relevant portion if found, or "not present"]
- Item 2: [quote relevant portion if found, or "not present"]
- Item 3: [quote relevant portion if found, or "not present"]
[Continue for ALL items]
FOUND IN: Item [#] - "[exact quote showing the detail]"
STATUS: ✓ COVERED
```

Or if genuinely missing:
```
Searching for: "[exact detail]"
Scanning output:
- Item 1: [checked full text - not present]
- Item 2: [checked full text - not present]
[All items checked]
FOUND IN: None
STATUS: ✗ MISSING
```

**GOLDEN RULE**: When in doubt, mark as COVERED. Only mark as MISSING if you can prove it's nowhere in ANY output item.

### Step 3: Add Missing Details (Only if needed)

For EACH missing detail:
- Add to ONLY ONE output item where it fits naturally
- Make MINIMAL changes
- Keep original intent and structure
- Maintain natural flow and coherence
- Preserve any formatting or numbering
- DO NOT create new items
- DO NOT force unrelated details

## CRITICAL RULES

1. **FALSE POSITIVE PREVENTION**: Before marking ANY detail as MISSING:
   - Re-read EVERY output item completely
   - Check for synonyms and variations
   - Look for implied or paraphrased mentions
   - Only mark MISSING if absolutely certain

2. **EVIDENCE REQUIREMENT**: You MUST show where you looked and quote what you found

3. **COMMON MISTAKES TO AVOID**:
   - Marking details as missing without checking all items
   - Missing paraphrased or reworded mentions
   - Ignoring partial matches or related terms
   - ✓ Only marking missing after proving absence with quotes

4. **OUTPUT RULES**:
   - If ALL details are covered: Return ONLY "NO"
   - If details are missing: Return ALL items (modified + unchanged)
   - NEVER create new items
   - Keep SAME NUMBER of items

## SELF-CHECK BEFORE FINALIZING
Ask yourself:
- Did I check EVERY output item for EACH detail?
- Did I quote evidence for my findings?
- Am I 100% certain about each MISSING mark?
- Did I only add details that make logical sense?

## OUTPUT FORMAT

**MANDATORY**: End your response with EXACTLY this format:

**If nothing is missing:**
```
FINAL_OUTPUT:
NO
```

**If details are missing:**
```
FINAL_OUTPUT:
[item 1 - possibly modified]
[item 2 - possibly modified]
[item 3 - possibly modified]
[all items must be included]
```

## EXAMPLE VERIFICATION PROCESS

**Example 1: Technical Documentation**

**Source Content:**
API endpoint /users/profile accepts GET requests, returns JSON with fields: user_id (integer), email (string), created_at (ISO 8601), subscription_tier (basic/premium/enterprise), rate limit 100 requests per minute.

**Generated Output:**
- The profile endpoint accepts GET requests and returns user data in JSON format
- Response includes user identification and account information
- Standard rate limiting applies to prevent abuse

**Verification:**
```
Searching for: "/users/profile"
- Item 1: "profile endpoint" (partial, missing full path) ⚠
- Item 2: not present
- Item 3: not present
STATUS: ✗ MISSING (full path not specified)

Searching for: "user_id"
- Item 1: not present
- Item 2: "user identification" (implied but not specific) ⚠
- Item 3: not present
STATUS: ✗ MISSING (specific field name not mentioned)

Searching for: "100 requests per minute"
- Item 1: not present
- Item 2: not present
- Item 3: "Standard rate limiting" (mentioned but not specific) ⚠
STATUS: ✗ MISSING (specific limit not stated)

[Continue for all details...]
```

**Result:**
```
FINAL_OUTPUT:
The /users/profile endpoint accepts GET requests and returns user data in JSON format with fields including user_id (integer), email (string), created_at (ISO 8601), and subscription_tier (basic/premium/enterprise)
Response includes user identification and account information
Rate limit of 100 requests per minute applies to prevent abuse
```

**Example 2: Product Requirements**

**Source Content:**
Dashboard must display real-time metrics, support export to PDF and CSV, auto-refresh every 30 seconds, compatible with Chrome 90+, Firefox 88+, Safari 14+, responsive design for screens 320px to 4K.

**Generated Output:**
Build a dashboard with real-time metrics that updates every 30 seconds
Include data export functionality for reports
Ensure cross-browser compatibility and responsive design from mobile (320px) to 4K displays

**Verification:**
```
Searching for: "PDF"
- Item 1: not present
- Item 2: "data export functionality" (generic, missing formats) ⚠
- Item 3: not present
STATUS: ✗ MISSING

Searching for: "CSV"
- Item 1: not present
- Item 2: "data export functionality" (generic, missing formats) ⚠
- Item 3: not present
STATUS: ✗ MISSING

Searching for: "Chrome 90+"
- Item 1: not present
- Item 2: not present
- Item 3: "cross-browser compatibility" (generic, missing versions) ⚠
STATUS: ✗ MISSING

[Continue for all details...]
```

**Result:**
```
FINAL_OUTPUT:
Build a dashboard with real-time metrics that updates every 30 seconds
Include data export functionality for PDF and CSV reports
Ensure compatibility with Chrome 90+, Firefox 88+, Safari 14+ and responsive design from mobile (320px) to 4K displays
```

Begin verification now:
"""

# ******************************

coding_message_generation_prompt = """
You are generating realistic coding questions that a DEVELOPER would ask an AI ASSISTANT. Your ONLY job is to create technical questions based on the SPECIFIC DETAILS mentioned in the bullet points below.

## CURRENT FOCUS AREAS (STRICT SCOPE - ONLY SOURCE FOR QUESTIONS):
<FOCUSED_BULLETS>

## QUESTIONS ALREADY COVERED IN THIS BATCH (AVOID THESE):
<BATCH_HISTORY>

## CURRENT BATCH CONTEXT (AWARENESS ONLY - DO NOT GENERATE QUESTIONS ABOUT THIS):
<PREVIOUS_SUB_BATCH_PLANS>

## PREVIOUS BATCH PLANS [DEVELOPMENT REFERENCE DATABASE] (REFERENCE ONLY & AWARENESS ONLY - DO NOT GENERATE QUESTIONS ABOUT THIS):
<PREVIOUS_BATCH_PLANS>

CRITICAL: These sections provide REFERENCE INFORMATION to help you understand project context, previous implementations, tech stack decisions, and code evolution mentioned in the current bullet points. Use this information to understand WHAT has been built, WHICH technologies are being used, and WHAT previous development happened, but NEVER generate questions directly about topics from these reference sections.

---

## CRITICAL RULES:

### 1. ABSOLUTE BULLET-POINT COVERAGE RULE
**CRITICAL: Mention all the details in the given FOCUSED_BULLETS (numbers, names, dates, technical detail, implementation, error, or coding situation mentioned) at least once across the questions you generate.**
**STRICT VERIFICATION CHECKLIST** - Before each question, ask:
1. Is this exact detail explicitly mentioned in a current bullet point in FOCUSED_BULLETS?
2. Am I staying within the precise scope of what's mentioned?
**ALLOWED**: Questions about the exact words, phrases, technical details, implementations, errors, or coding situations written in bullets in FOCUSED_BULLETS

### 2. DETAIL ESTABLISHMENT & REFERENCE RULE - **ANTI-REPETITION PRIORITY**
**CRITICAL: Mention specific details from bullet points in FOCUSED_BULLETS ONLY ONCE, then use natural references**
**DETAIL USAGE PATTERN:**
- **First mention**: Include full specific details from bullet point in FOCUSED_BULLETS (names, dates, numbers, exact function names, variable names, error messages, file names, version numbers, etc.)
- **All subsequent questions**: Use pronouns, references, or contextual shortcuts
- **Natural progression**: Questions evolve from establishing details to exploring implications

### 3. BULLET-POINT EXTRACTION RULE
- Read each bullet point word by word
- Identify EVERY specific technical detail, error, implementation, or coding situation mentioned
- Create questions ONLY about these extracted technical elements
- IGNORE the general programming topic/theme - focus solely on bullet point specifics

### 4. FORBIDDEN EXPANSION
- Do NOT ask about the broader programming topic (React in general, etc.)
- Do NOT ask generic questions about the technology stack
- Do NOT add technical information not mentioned in the bullet points
- Do NOT create educational questions about programming concepts
- ABSOLUTELY FORBIDDEN: Do NOT generate questions directly about topics from reference sections
- Use reference info only to understand context for current bullet points

### 5. REFERENCE DATABASE USAGE
- Use "CURRENT BATCH CONTEXT" and "DEVELOPMENT REFERENCE DATABASE" to understand technical references in current bullet points
- If current bullets mention a component/function without context, check reference sections to understand what it does
- If current bullets mention a technology without context, check reference sections to understand the implementation
- If current bullets reference past code, use reference sections to understand what was built
- **KEY**: Use reference info to UNDERSTAND current bullets, but generate questions ONLY about current bullet content

### 6. CODING QUESTION GENERATION STRATEGY
For each specific technical element in the bullet points, create questions that follow these patterns:

**CODE IMPLEMENTATION REQUESTS:**
- "Help me build/create/implement [specific feature from bullet]"
- "Can you write [specific code component from bullet]"
- "Show me how to [specific technical task from bullet]"
- "I need to create [specific functionality from bullet]"

**DEBUGGING HELP:**
- "I'm getting this error: [specific error from bullet]. How do I fix it?"
- "My [specific code/feature from bullet] isn't working as expected"
- "Why does [specific function/component from bullet] return [specific issue]?"
- "This [specific code from bullet] is throwing [specific error]"

**CODE REVIEW/OPTIMIZATION:**
- "Can you review this [specific code from bullet] and suggest improvements?"
- "How can I optimize [specific implementation from bullet]?"
- "Is there a better way to [specific approach from bullet]?"
- "What's wrong with my [specific code from bullet]?"

### 7. CHRONOLOGICAL ORDERING RULE
- Process bullet points in the exact order provided
- Questions must follow the chronological sequence of the bullet points
- Earlier bullet point details should appear in earlier questions
- Later bullet point details should appear in later questions

### 8. PROJECT INTRODUCTION HANDLING
- DO NOT include project introductions in questions unless it's the very first batch of the entire conversation series
- Assume the AI assistant already knows the project context from previous conversations
- Jump straight into the technical question without re-introducing the project
- Reference project components naturally without formal introduction: "my Flask app", "this React component", "the user authentication", etc.

### 9. TEMPORAL ANCHOR HANDLING
- If bullet points mention specific development times (deadlines, milestones, "next sprint", "recently implemented", etc.), incorporate that timing naturally into questions
- Do NOT mention the label name "temporal anchor" or reference it explicitly
- Use the timing context naturally: "I need to deploy by Friday..." or "Since we're starting the new sprint..." or "I just implemented..."

### 10. AUTHENTIC DEVELOPER CONVERSATION STYLE
**CRITICAL: These must sound like REAL DEVELOPERS texting/chatting, not formal technical documentation.**

**Language Authenticity:**
- Use lots of contractions: "I'm", "don't", "can't", "it's", "that's", "won't"
- Include casual dev slang: "lol", "btw", "tbh", "kinda", "sorta", "gonna", "wanna"
- Add filler words: "like", "um", "you know", "I mean", "so", "well"
- Use informal punctuation: multiple periods "...", question marks "??", exclamation points "!!"

**Technical Authenticity:**
- Include actual error messages when mentioned in bullets
- Reference specific file names, function names, variables from bullets
- Use realistic technical scenarios that developers actually encounter
- Include version numbers, framework names, configuration details when mentioned

**Imperfect Natural Speech:**
- Include minor typos and informal grammar
- Use incomplete thoughts: "so I was trying to..." or "not sure if this makes sense but..."
- Add rambling elements: "I mean, I guess what I'm trying to implement is..." 
- Include thinking out loud: "hmm", "wait", "actually", "oh", "maybe"

**Emotional Authenticity:**
- Show genuine developer feelings: frustration with bugs, excitement about features, confusion about errors
- Use emotional language: "I'm so confused by this error", "this bug is driving me crazy", "I'm super excited about this feature"
- Add personal reactions: "ugh", "omg", "yay", "oof", "wtf", "fml"

**Varied Question Structures:**
- Mix short and long questions
- Some incomplete questions: "so about that API thing..."
- Some statements that imply questions: "not sure what's wrong with my code..."
- Avoid repetitive "Can you help me..." or "How do I..." patterns

**Natural Developer Flow Patterns:**
- Start some questions mid-thought about code
- Include context rambling before getting to the technical point
- Add uncertainty markers: "maybe", "I think", "I'm not sure but", "does that make sense?"
- Use conversational bridges: "oh and also", "btw", "speaking of which", "another thing"

**EXAMPLES OF AUTHENTIC DEVELOPER STYLE:**
- Instead of: "Can you help me implement user authentication for my application?"
- Use: "ugh I'm struggling with implementing auth in my React app... any ideas on the best approach??"

- Instead of: "I am encountering an error with my database connection. How do I resolve this?"
- Use: "wtf my database connection keeps timing out and I'm getting this weird error... help??"

- Instead of: "Please review my code and provide optimization suggestions."
- Use: "can you take a look at this messy code I wrote? feels like it could be way more efficient lol"

### 11. MANDATORY COMPLEX CODE GENERATION AND SHARING
**CRITICAL: 85% of your questions MUST include substantial code snippets (20-60+ lines)**

**ABSOLUTE REQUIREMENT: Generate realistic, complex, production-level code based on bullet point technical details**

**MINIMUM CODE COMPLEXITY STANDARDS:**
- **Every code block MUST be 20-60+ lines minimum**
- **Include multiple functions/methods/classes (4-6 minimum)**
- **Add realistic imports and dependencies (3-5 minimum)**
- **Include proper error handling, validation, and edge cases**
- **Add database operations, API calls, or complex business logic**
- **Use realistic variable names, function names, and code structure**
- **Include configuration, setup, and environmental considerations**

**For debugging scenarios:**
- Generate substantial broken/buggy code with realistic, hard-to-spot errors
- Include multiple interconnected components where bugs span across them
- Add complex error scenarios: race conditions, memory issues, async problems
- "I'm getting this weird error and can't figure out what's wrong: ```[generate 25-50 lines of complex buggy code with realistic imports, multiple functions, proper structure, and subtle bugs]``` Any ideas what's causing this??"

**For code review scenarios:**
- Generate substantial working but suboptimal code with multiple improvement areas
- Include performance bottlenecks, security issues, maintainability problems
- Add architectural concerns, code smells, and scalability limitations
- "Can you review this code? It works but feels really messy and I think there are performance issues: ```[generate 30-60 lines of functional but poorly optimized code with multiple functions, realistic imports, complex logic, and clear improvement opportunities]``` How can I make it better??"

**For implementation request scenarios:**
- Generate substantial partial implementations with detailed TODO sections
- Include architectural setup, configuration, and integration points
- Add complex business logic requirements and data flow considerations
- "I'm working on this feature and have this so far: ```[generate 25-50 lines of partial implementation with realistic structure, imports, multiple functions, and clear TODO sections]``` Can you help me complete the missing parts??"

**For optimization scenarios:**
- Generate substantial working but highly inefficient code
- Include obvious performance problems, resource waste, and algorithmic issues
- Add monitoring points, caching opportunities, and scalability concerns
- "This code is working but it's super slow with large datasets: ```[generate 30-70 lines of inefficient but functional code with performance bottlenecks, multiple functions, realistic structure, and clear optimization needs]``` How can I make it faster??"

**CODE GENERATION REQUIREMENTS:**
- Match the exact technology stack mentioned in bullet points
- Create realistic code that fits the specific technical scenario described
- Include appropriate framework patterns, design principles, and best practices
- Add realistic business logic, data validation, and error handling
- Use proper code organization, meaningful comments, and documentation
- Include environment setup, configuration, and dependency management
- Add logging, monitoring, and debugging considerations where appropriate

**FORBIDDEN CODE PATTERNS:**
- Simple, tutorial-style code examples
- Single function snippets without context
- Code without realistic imports or dependencies
- Generic variable names or unrealistic structure
- Code that looks artificially created for learning
- Overly simplified examples that don't reflect real development

### 12. MANDATORY COVERAGE VERIFICATION
Before writing questions, list every technical detail from bullet points (NOTE: DO NOT generate these below in the messages):
- Technologies/frameworks mentioned: ___
- Specific errors/bugs described: ___
- Code components/functions: ___
- Implementation requirements: ___
- Technical challenges: ___
- Performance/optimization needs: ___

Then ensure each detail gets at least one question WITH SUBSTANTIAL CODE.

---

## OUTPUT REQUIREMENTS:

Generate exactly <SUB_BATCH_SIZE> questions that:
1. **MANDATORY: Use every specific technical detail mentioned in FOCUSED_BULLETS at least once**
2. **85% MUST include substantial code snippets (20-60+ lines) with production-level complexity**
3. Cover every technical detail mentioned in the bullet points with appropriate complex code
4. Use natural, conversational developer language with realistic technical scenarios
5. Include exact names, numbers, error messages, file paths, and technical specifications from bullet points
6. Sound like genuine requests for coding assistance with actual code sharing
7. Stay strictly within the bullet point scope
8. Avoid repetition of already covered topics
9. Follow chronological order of bullet points
10. Incorporate temporal elements naturally
11. Include appropriate complex code implementation/debugging/review request patterns

**OUTPUT FORMAT:**
- **CRITICAL: The arrow ->-> [bullet_number] MUST be placed at the very END of each complete message**
- **CRITICAL: Generate ONLY the developer messages, nothing else**
- Do NOT include question numbers, headers, or organizational text
- Separate each complete message with "---MESSAGE_SEPARATOR---"
- Each message can span multiple lines and include code blocks
- End with "### COMPLETE ###"

Example format:
First complete message with code blocks and all content, then at the very end ->-> 1
---MESSAGE_SEPARATOR---
Second complete message with code blocks and all content, then at the very end ->-> 2
---MESSAGE_SEPARATOR---
Third complete message with all content, then at the very end ->-> 3
### COMPLETE ###

**CRITICAL:**
- Each message MUST end with "->-> [number]" where [number] is the bullet point it's based on
- The arrow comes AFTER all text, code blocks, and content - not in the middle
- Use bullet numbers 1, 2, 3, etc. as they appear in CURRENT FOCUS AREAS
- If a question combines details from multiple bullets, use the primary bullet number
- If the question is not generated from any bulletpoints, put N/A

**BEFORE GENERATING:** Mentally verify each question traces back to a specific technical detail in the bullet points AND includes substantial, complex, realistic code when applicable.
"""

coding_message_generation_prompt_fast = """
You are generating realistic coding questions that a DEVELOPER would ask an AI ASSISTANT. Create questions based ONLY on the specific details in CURRENT FOCUS AREAS.

## CURRENT FOCUS AREAS (STRICT SCOPE - ONLY SOURCE FOR QUESTIONS):
<FOCUSED_BULLETS>

## QUESTIONS ALREADY COVERED IN THIS BATCH (AVOID THESE):
<BATCH_HISTORY>

## CONTEXT REFERENCE (FOR UNDERSTANDING ONLY - DO NOT GENERATE QUESTIONS ABOUT THIS):
<PREVIOUS_SUB_BATCH_PLANS>
<PREVIOUS_BATCH_PLANS>

## CRITICAL RULES:

## CRITICAL ALERT: BULLET TYPE DETECTION
**MANDATORY FIRST STEP - CHECK EACH BULLET:**
- If bullet contains "**Time Anchor:**" → ABSOLUTELY NO CODE, ONLY project/scheduling questions
- If bullet contains "**Personal Introduction:**" → ABSOLUTELY NO CODE, ONLY career/personal questions  
- Otherwise → Technical bullet, GENERATE CODE

### 1. CURRENT FOCUS AREAS BULLET TYPE IDENTIFICATION - CHECK FIRST
**BEFORE DOING ANYTHING:** Identify the bullet type in CURRENT FOCUS AREAS:
- **Time Anchor:** bullets (contain "Time Anchor:" in title) → NO CODE GENERATION
- **Personal Introduction:** bullets (contain "Personal Introduction:" in title) → NO CODE GENERATION  
- **Technical bullets:** (all others) → CODE GENERATION REQUIRED

### 2. MANDATORY DETAIL COVERAGE & TRACKING
**BEFORE GENERATING:** Extract and list EVERY SINGLE detail from CURRENT FOCUS AREAS:
- Names: [extract ALL names, developer names, company names, project names]
- Numbers/Versions: [extract ALL version numbers, dates, times, quantities, ports]
- Technologies/Frameworks: [extract ALL tech stack, languages, libraries, tools]
- File/Function Names: [extract ALL specific filenames, functions, variables, components]
- Error Messages: [extract ALL specific errors, bugs, issues mentioned]
- Technical Specifications: [extract ALL APIs, databases, configurations, requirements]
- Personal/Project Details: [extract ALL roles, goals, deadlines, project contexts]

**ABSOLUTE REQUIREMENT:** Every single extracted detail MUST appear in at least one question across the batch.
**USAGE TRACKING:** Mark each detail as used. Verify 100% coverage before finalizing questions.

### 3. ABSOLUTE SOURCE RESTRICTION
**ONLY ALLOWED:** Details explicitly written in CURRENT FOCUS AREAS bullet points
**COMPLETELY FORBIDDEN:**
- ANY content from BATCH_HISTORY
- ANY content from CONTEXT REFERENCE sections
- Generic programming questions
- Details not explicitly mentioned in current bullets

**CONTEXT REFERENCE RULE:** Use only to understand WHAT technologies/components mean when they appear in CURRENT FOCUS AREAS.

### 4. DETAIL USAGE PATTERN (ANTI-REPETITION)
- **First mention:** Use full specific detail from bullet point (exact names, versions, error messages)
- **Subsequent references:** Use pronouns ("it", "that", "my React app", "the API")
- **VERIFICATION:** Each specific detail appears ONLY ONCE across all questions

### 5. MANDATORY COMPLEX CODE GENERATION
**CRITICAL: 85% of questions MUST include substantial code snippets (20-60+ lines)**
ONLY IF bullet's title in CURRENT FOCUS AREAS is not time anchor or personal introduction

ABSOLUTE EXCEPTIONS - NO CODE GENERATION:
- **Time Anchor:** bullets - NEVER EVER generate any code, programming solutions, or technical implementations
- **Personal Introduction:** bullets - NEVER EVER generate any code, programming solutions, or technical implementations
- FOR PERSONAL INTRODUCTION BULLETS: Generate questions FROM the perspective of the person introducing themselves
The person in the bullet is the USER asking the questions
These are contextual/personal details, NOT technical coding scenarios

**STOP AND VERIFY: If the bullet contains "Time Anchor:" or "Personal Introduction:" in the title, you MUST NOT generate ANY code blocks, programming solutions, scripts, or technical implementations. Period.**

**FOR TIME ANCHOR/PERSONAL INTRODUCTION BULLETS:**
- Focus on project management, scheduling, personal goals
- Ask about deadlines, meeting coordination, project planning
- NO code blocks, NO programming solutions, NO technical implementations
- Use natural conversation about timing, goals, and context

**CODE COMPLEXITY REQUIREMENTS (for all other bullets):**
- **Minimum 20-60+ lines per code block**
- **Multiple functions/methods/classes (4-6 minimum)**
- **Realistic imports and dependencies (3-5 minimum)**
- **Proper error handling, validation, edge cases**
- **Complex business logic, database operations, API calls**
- **Production-level structure and realistic variable names**

**REQUIRED PATTERNS (for coding bullets only):**
- **Debugging (40%):** Generate buggy code with realistic, hard-to-spot errors
- **Code Review (25%):** Generate working but suboptimal code needing improvements
- **Implementation (20%):** Generate partial implementations with detailed TODOs
- **Optimization (15%):** Generate slow/inefficient but functional code

**NEVER use simple examples or tutorial-style code - always production-level complexity**

### 6. AUTHENTIC DEVELOPER STYLE
**Language:** Use contractions ("I'm", "don't"), dev slang ("lol", "btw"), fillers ("like", "um"), informal punctuation ("...", "??", "!!")
**Emotion:** Show genuine feelings - frustration with bugs, excitement about features
**Natural Flow:** Mix question lengths, include rambling, thinking out loud
**Technical Authenticity:** Include actual error messages, file names, version numbers from bullets

### 7. CHRONOLOGICAL ORDER
Process bullet points in exact order provided. Earlier bullet details appear in earlier questions.

### 8. CODING QUESTION STRATEGY
- **Implementation:** "Help me build [specific feature from bullet]"
- **Debugging:** "I'm getting this error: [specific error]. How do I fix it?"
- **Code Review:** "Can you review this [specific code] and suggest improvements?"
- **Optimization:** "How can I make [specific implementation] faster?"

## OUTPUT REQUIREMENTS:
Generate exactly <SUB_BATCH_SIZE> questions that:

1. **MANDATORY:** Use EVERY SINGLE detail from FOCUSED_BULLETS at least once (names, versions, errors, files, specs, etc.)
2. **85% MUST include substantial code snippets (20-60+ lines) with production-level complexity**
3. Sound like genuine developer requests with realistic technical scenarios
4. Follow chronological order of bullet points
5. **ALWAYS include complete, complex code - NEVER use simple examples**
6. Match one of the four coding patterns with appropriate complexity
7. Stay strictly within bullet point scope
8. **VERIFICATION:** Before submitting, confirm every extracted detail appears in the questions

**OUTPUT FORMAT:**
- **CRITICAL: Generate ONLY the developer messages, nothing else**
- Do NOT include question numbers, headers, or organizational text
- **MANDATORY: Each message MUST be separated by exactly "---MESSAGE_SEPARATOR---"**
- **NO other separators allowed** - only use "---MESSAGE_SEPARATOR---"
- Each message can span multiple lines and include code blocks
- **CRITICAL: Each message MUST end with "->-> [number] ---MESSAGE_SEPARATOR---" where [number] is the bullet point it's based on**
- **MANDATORY: End with "### COMPLETE ###"**
- **NO repetitive "and" chains** in any message

**REQUIRED FORMAT PATTERN (EXACT FORMAT TO FOLLOW):**
First complete message with code blocks and all content ->-> 1
---MESSAGE_SEPARATOR---
Second complete message with code blocks and all content ->-> 2
---MESSAGE_SEPARATOR---
Third complete message with all content ->-> 3
---MESSAGE_SEPARATOR---
[Continue for all <SUB_BATCH_SIZE> messages]
### COMPLETE ###

**CRITICAL FORMATTING RULES:**
- Every message ends with "->-> [bullet_number] ---MESSAGE_SEPARATOR---"
- Every message is followed by "---MESSAGE_SEPARATOR---" (including the last one)
- The arrow comes AFTER all text, code blocks, and content - not in the middle
- Use bullet numbers 1, 2, 3, etc. as they appear in CURRENT FOCUS AREAS
- If a question combines details from multiple bullets, use the primary bullet number
- If the question is not generated from any bulletpoints, put N/A
- Always end the entire output with "### COMPLETE ###"

**CRITICAL VERIFICATION:** Before each question:
1. **MANDATORY FIRST CHECK: What type of bullet is this?**
   - Time Anchor bullet → Generate project management/scheduling questions, ABSOLUTELY NO CODE
   - Personal Introduction bullet → Generate career/personal questions FROM their perspective, ABSOLUTELY NO CODE  
   - Technical bullet → Generate coding questions WITH substantial code
2. Does this use a specific detail from current bullets?
3. Have I included substantial, complex code (not simple examples) for technical bullets?
4. Does this sound like a real developer asking for help?
5. Am I following one of the four coding patterns correctly for technical bullets?

**Generate exactly <SUB_BATCH_SIZE> questions in the format above.**
"""

# ******************************

math_message_generation_prompt = """
You are generating realistic math questions that a USER would ask an AI ASSISTANT. Your ONLY job is to create mathematical questions based on the SPECIFIC DETAILS mentioned in the bullet points in CURRENT FOCUS AREAS below.

## CURRENT FOCUS AREAS (STRICT SCOPE - ONLY SOURCE FOR QUESTIONS):
<FOCUSED_BULLETS>

## QUESTIONS ALREADY COVERED IN THIS BATCH (AVOID THESE):
<BATCH_HISTORY>

## CURRENT BATCH CONTEXT (AWARENESS ONLY - DO NOT GENERATE QUESTIONS ABOUT THIS):
<PREVIOUS_SUB_BATCH_PLANS>

## PREVIOUS BATCH PLANS [LEARNING REFERENCE DATABASE] (REFERENCE ONLY & AWARENESS ONLY - DO NOT GENERATE QUESTIONS ABOUT THIS):
<PREVIOUS_BATCH_PLANS>

CRITICAL: These sections provide REFERENCE INFORMATION to help you understand mathematical context, previous learning, concept progression, and problem-solving evolution mentioned in the current bullet points in CURRENT FOCUS AREAS. Use this information to understand WHAT has been learned, WHICH concepts are being studied, and WHAT previous mathematical work happened, but NEVER generate questions directly about topics from these reference sections.

---

## CRITICAL RULES:

### 1. ABSOLUTE BULLET-POINT IN CURRENT FOCUS AREAS BOUNDARY RULE
**CRITICAL: Mention all the details in the given CURRENT FOCUS AREAS (numbers, names, dates, mathematical detail, problem, concept, or learning situation mentioned) at least once accross the questions you generate.**

### 2. BULLET-POINT IN CURRENT FOCUS AREAS EXTRACTION RULE
- Read each bullet point in CURRENT FOCUS AREAS word by word
- Identify EVERY specific mathematical detail, problem, concept, or learning situation mentioned
- Create questions ONLY about these extracted mathematical elements
- IGNORE the general mathematical topic/theme - focus solely on bullet point specifics

**STRICT VERIFICATION CHECKLIST** - Before each question, ask:
1. Is this exact detail explicitly mentioned in a current bullet point in CURRENT FOCUS AREAS?
2. Am I expanding beyond what's written?
3. Am I asking about the specific situation/emotion/action described?
4. Am I staying within the precise scope of what's mentioned?

**ALLOWED**: Questions about the exact words, phrases, mathematical detail, problem, concept, or learning situation written in bullets in CURRENT FOCUS AREAS

### 3. FORBIDDEN EXPANSION
- Do NOT ask about the broader mathematical topic (calculus in general, etc.)
- Do NOT ask generic questions about the mathematical field
- Do NOT add mathematical information not mentioned in the bullet points in CURRENT FOCUS AREAS
- Do NOT create educational questions about mathematical concepts beyond what's specified
- ABSOLUTELY FORBIDDEN: Do NOT generate questions directly about topics from reference sections
- Use reference info only to understand context for current bullet points in CURRENT FOCUS AREAS

### 4. DETAIL ESTABLISHMENT & REFERENCE RULE - **ANTI-REPETITION PRIORITY**
**CRITICAL: Mention specific details from bullet points in CURRENT FOCUS AREAS ONLY ONCE, then use natural references**

**DETAIL USAGE PATTERN:**
- **First mention**: Include full specific details from bullet point in CURRENT FOCUS AREAS
- **All subsequent questions**: Use pronouns, references, or contextual shortcuts
- **Natural progression**: Questions evolve from establishing details to exploring implications

### 5. CURRENT FOCUS AREAS BULLET-POINT in CURRENT FOCUS AREAS EXTRACTION RULE
- Read each bullet point in CURRENT FOCUS AREAS word by word
- Identify EVERY mathematical detail, problem, concept, or fact mentioned
- Create questions ONLY about these extracted elements
- IGNORE the general topic/theme - focus solely on bullet point in CURRENT FOCUS AREAS specifics
- NEVER infer or add information not explicitly stated

### 6. REFERENCE DATABASE USAGE
- Use "CURRENT BATCH CONTEXT" and "LEARNING REFERENCE DATABASE" to understand mathematical references in current bullet points
- If current bullets mention a theorem/concept without context, check reference sections to understand what it covers
- If current bullets mention a problem type without context, check reference sections to understand the approach
- If current bullets reference past mathematical work, use reference sections to understand what was learned
- **KEY**: Use reference info to UNDERSTAND current bullets in CURRENT FOCUS AREAS, but generate questions ONLY about current bullet content

### 7. MATHEMATICAL QUESTION GENERATION STRATEGY
For each specific mathematical element in the bullet points in CURRENT FOCUS AREAS, create questions that follow these patterns:

**PROBLEM-SOLVING REQUESTS:**
- "Help me solve [specific problem from bullet]"
- "I need to find [specific mathematical task from bullet]"
- "Show me how to [specific calculation/proof from bullet]"
- "I'm stuck on [specific problem element from bullet]"

**CONCEPT CLARIFICATION:**
- "I don't understand [specific concept from bullet]"
- "Can you explain why [specific mathematical statement from bullet]?"
- "What does [specific term/definition from bullet] mean?"
- "How does [specific concept from bullet] work?"

**SOLUTION VERIFICATION:**
- "Can you check if my solution to [specific problem from bullet] is correct?"
- "Is my approach to [specific problem from bullet] right?"
- "Did I solve [specific equation/problem from bullet] correctly?"
- "Can you verify my work on [specific calculation from bullet]?"

**METHOD EXPLANATION:**
- "Why does [specific method from bullet] work for this problem?"
- "Show me step-by-step how to [specific procedure from bullet]"
- "Explain the reasoning behind [specific solution approach from bullet]"
- "What's the logic of [specific mathematical technique from bullet]?"

### 8. CHRONOLOGICAL ORDERING RULE
- Process bullet points in CURRENT FOCUS AREAS in the exact order provided
- Questions must follow the chronological sequence of the bullet points in CURRENT FOCUS AREAS
- Earlier bullet point details should appear in earlier questions
- Later bullet point details should appear in later questions

### 9. LEARNING CONTEXT HANDLING
- DO NOT include learning introductions in questions unless it's the very first batch of the entire conversation series
- Assume the AI assistant already knows the learning context from previous conversations
- Jump straight into the mathematical question without re-introducing the course/topic
- Reference mathematical concepts naturally without formal introduction: "this derivative", "the quadratic equation we're working on", "my calculus homework", etc.

### 10. TEMPORAL ANCHOR HANDLING
- If bullet points mention specific learning times (deadlines, exams, "next class", "recently learned", etc.), incorporate that timing naturally into questions
- Do NOT mention the label name "temporal anchor" or reference it explicitly
- Use the timing context naturally: "I have a test tomorrow..." or "Since we just learned..." or "I need to finish this homework..."

### 11. AUTHENTIC USER CONVERSATION STYLE
**CRITICAL: These must sound like REAL USERS texting/chatting, not formal academic writing.**

**Language Authenticity:**
- Use lots of contractions: "I'm", "don't", "can't", "it's", "that's", "won't"
- Include casual user slang: "lol", "btw", "tbh", "kinda", "sorta", "gonna", "wanna"
- Add filler words: "like", "um", "you know", "I mean", "so", "well"
- Use informal punctuation: multiple periods "...", question marks "??", exclamation points "!!"

**Mathematical Authenticity:**
- Include actual problem statements when mentioned in bullets
- Reference specific equation types, theorem names, mathematical procedures from bullets
- Use realistic mathematical scenarios that users actually encounter
- Include course names, textbook references, assignment details when mentioned

**Imperfect Natural Speech:**
- Include minor typos and informal grammar
- Use incomplete thoughts: "so I was trying to..." or "not sure if this makes sense but..."
- Add rambling elements: "I mean, I guess what I'm trying to solve is..."
- Include thinking out loud: "hmm", "wait", "actually", "oh", "maybe"

**Emotional Authenticity:**
- Show genuine user feelings: frustration with problems, confusion about concepts, excitement about understanding
- Use emotional language: "I'm so confused by this problem", "this equation is driving me crazy", "I finally get derivatives!"
- Add personal reactions: "ugh", "omg", "yay", "oof", "wtf", "help!"

**Varied Question Structures:**
- Mix short and long questions
- Some incomplete questions: "so about that integration thing..."
- Some statements that imply questions: "not sure what I did wrong here..."
- Avoid repetitive "Can you help me..." or "How do I..." patterns

**Natural User Flow Patterns:**
- Start some questions mid-thought about problems
- Include context rambling before getting to the mathematical point
- Add uncertainty markers: "maybe", "I think", "I'm not sure but", "does that make sense?"
- Use conversational bridges: "oh and also", "btw", "speaking of which", "another thing"

**EXAMPLES OF AUTHENTIC USER STYLE:**
- Instead of: "Can you help me solve this quadratic equation?"
- Use: "ugh I'm stuck on this quadratic equation and I have no idea which method to use... help??"

- Instead of: "I am having difficulty understanding the concept of limits."
- Use: "wtf are limits supposed to mean?? I keep reading the definition but it makes no sense..."

- Instead of: "Please review my solution and provide feedback."
- Use: "can you check if I did this derivative right? feels like I messed up somewhere lol"

### 12. MATHEMATICAL WORK GENERATION AND REALISTIC BEHAVIOR PATTERNS
**CRITICAL: All mathematical work must follow realistic human behavior patterns**

**MANDATORY REALISTIC PATTERNS - CHOOSE ONE PER QUESTION:**

**Pattern A: Completely Stuck (40% of questions)**
- Express complete confusion about the problem or concept
- Ask for help with approach, method selection, or starting point
- Show NO mathematical work - just describe what you're trying to solve
- Use language indicating total uncertainty about how to proceed

**Pattern B: Partially Stuck (30% of questions)**
- Show ONLY the initial steps where you attempted the problem (2-4 lines maximum)
- Clearly indicate where you got confused or stuck
- Ask for help with the specific next step or continuation
- Stop showing work at the point of confusion

**Pattern C: Need Verification (20% of questions)**
- Show ONLY the final answer or key result you obtained
- Express uncertainty about correctness
- Ask for confirmation without showing the solution process
- Indicate you completed the work but want validation

**Pattern D: Conceptual Confusion (10% of questions)**
- Ask about mathematical concepts, methods, or theory
- Express confusion about when/why/how techniques work
- Show NO calculations - focus on understanding principles
- Request explanation of mathematical reasoning or logic

**MATHEMATICAL WORK STANDARDS (when pattern requires work):**
- Include appropriate mathematical notation and formatting for the level shown
- Use proper mathematical symbols, variables, and expressions
- Match the exact mathematical level mentioned in bullet points
- Create work that fits the specific learning scenario described
- Add course-appropriate mathematical rigor for displayed work
- Include realistic errors or areas of confusion where appropriate

**WORK SHARING RULES BY PATTERN:**
- **Pattern A**: NO mathematical work displayed
- **Pattern B**: Show ONLY initial attempts (2-4 steps maximum) where you got stuck
- **Pattern C**: Show ONLY final results or answers
- **Pattern D**: NO mathematical work, concept-focused only

**ABSOLUTELY FORBIDDEN PATTERNS:**
- Asking for help then showing complete solution in the same message
- Showing step-by-step work while narrating the solving process
- Providing complete solutions and asking for verification
- Any form of real-time problem-solving commentary or thinking out loud
- Extensive detailed work when pattern calls for minimal work
- Perfect mathematical work without any uncertainty
- Complete solutions when asking for help or clarification

**PATTERN SELECTION AND VERIFICATION:**
- Select pattern based on what makes sense for the bullet point content
- Ensure variety across questions - don't use same pattern repeatedly
- Match pattern to the type of mathematical assistance naturally needed

**VERIFICATION BEFORE EACH QUESTION:**
1. Which behavior pattern am I using?
2. Does my mathematical work match this pattern exactly?
3. Does this sound like a real person asking for help?
4. Am I showing appropriate amount of work for the pattern type?

**IF ANY ANSWER IS NO - REWRITE THE QUESTION TO MATCH A PATTERN**

**MATHEMATICAL WORK REQUIREMENTS (when applicable to pattern):**
- Match mathematical topics mentioned in bullet points
- Use appropriate notation and formatting conventions
- Include realistic reasoning for the amount of work shown
- Show work progression that matches the chosen behavior pattern
- Create realistic work that reflects actual user capabilities and common mistakes

### 13. PROBLEM GENERATION RULE - **CRITICAL FOR MATHEMATICAL QUESTIONS**
MANDATORY: When referencing problems, proofs, or equations that are not explicitly provided in the CURRENT FOCUS AREAS, you MUST generate and include the full problem statement, equation, or proof snippet in the question itself.

WHEN TO GENERATE PROBLEMS:
- When bullet points mention "completed X problems" without showing the problems
- When bullet points mention "scored Y/Z correct" without showing what was attempted
- When bullet points mention "working on [type] problems" without specific examples
- When asking for help with a problem type mentioned but not detailed

**PROBLEM GENERATION REQUIREMENTS:**
1. Include the full text of the problem, equation, or proof snippet immediately before asking for help.
2. Match the mathematical level and topic mentioned in the bullet point.
3. Create realistic problems or proofs that a user at this level would encounter.
4. Include specific numbers, variables, or expressions – never leave problems vague
5. Ensure consistency with the bullet‑point details on difficulty and context.

FORBIDDEN:
- Asking for help without providing the problem or proof.
- Referencing "the problem" or "this proof" without including it.
- Generating generic or unrelated problem statements.

**PROBLEM COMPLEXITY GUIDELINES:**
- For "got wrong" scenarios: Generate problems with common error-prone elements
- For "need help" scenarios: Generate problems at appropriate difficulty
- For "verification" scenarios: Generate problems with clear solutions
- Match problem difficulty to the score mentioned (8/10 = mostly straightforward)

**FORBIDDEN:**
- Asking about "the problem" without stating what it is
- Referencing "those problems" without showing examples
- Saying "the equation" without providing the actual equation
- Using vague references like "this type of problem" without specifics

### 14. MANDATORY COVERAGE VERIFICATION
Before writing questions, list every mathematical detail from bullet points (NOTE: DO NOT generate these below in the messages):
- Mathematical topics/concepts mentioned: ___
- Specific problems/equations described: ___
- Mathematical methods/procedures: ___
- Learning challenges/difficulties: ___
- Assessment/homework requirements: ___
- Mathematical applications/connections: ___

---

## OUTPUT REQUIREMENTS:

Generate exactly <SUB_BATCH_SIZE> questions that:
1. **MANDATORY: Use every specific detail mentioned in FOCUSED_BULLETS at least once**
2. **80% MUST include substantial mathematical work (equations, calculations, solution attempts) with realistic complexity**
3. Cover every mathematical detail mentioned in the bullet points with appropriate mathematical content
4. Use natural, conversational user language with realistic learning scenarios
5. Include exact names, numbers, mathematical detail, problem, concept, or learning situation mentioned from bullet points
6. Sound like genuine requests for mathematical assistance with actual mathematical work sharing
7. Stay strictly within the bullet point scope
8. Avoid repetition of already covered topics
9. Follow chronological order of bullet points
10. Incorporate temporal elements naturally
11. Include appropriate mathematical problem-solving/understanding/verification request patterns
12. **ALWAYS include specific problems/equations when referencing mathematical work**

**OUTPUT FORMAT:**
- For each question, use this exact format:
- [question text] ->-> [bullet_number]
- **CRITICAL: Generate ONLY the user messages, nothing else**
- Do NOT include question numbers, headers, or organizational text
- Separate each complete message with "---MESSAGE_SEPARATOR---"
- Each message can span multiple lines and include mathematical expressions

Example format:
First complete message with mathematical work...
---MESSAGE_SEPARATOR---
Second complete message with mathematical work...
---MESSAGE_SEPARATOR---
Third complete message...

**CRITICAL:** 
- Each question MUST end with "->-> [number]" where [number] is the bullet point it's based on
- Use bullet numbers 1, 2, 3, etc. as they appear in CURRENT FOCUS AREAS
- If a question combines details from multiple bullets, use the primary bullet number
- If the question is not generated from any bulletpoints, put N/A 

**BEFORE GENERATING:** Mentally verify each question traces back to a specific mathematical detail in the bullet points AND includes substantial, realistic mathematical work when applicable.
"""

math_message_generation_prompt_fast = """
You are generating realistic math questions that a USER would ask an AI ASSISTANT. Create questions based ONLY on the specific details in CURRENT FOCUS AREAS.

## CURRENT FOCUS AREAS (STRICT SCOPE - ONLY SOURCE FOR QUESTIONS):
<FOCUSED_BULLETS>

## QUESTIONS ALREADY COVERED IN THIS BATCH (AVOID THESE):
<BATCH_HISTORY>

## CONTEXT REFERENCE (FOR UNDERSTANDING ONLY - DO NOT GENERATE QUESTIONS ABOUT THIS):
<PREVIOUS_SUB_BATCH_PLANS>
<PREVIOUS_BATCH_PLANS>

---

## CRITICAL RULES:

### 1. CURRENT FOCUS AREAS BULLET TYPE IDENTIFICATION - CHECK FIRST
**BEFORE DOING ANYTHING:** Identify the bullet type in CURRENT FOCUS AREAS:
- **Time Anchor:** bullets (contain "Time Anchor:" in title) → NO MATHEMATICAL WORK GENERATION
- **Personal Introduction:** bullets (contain "Personal Introduction:" in title) → NO MATHEMATICAL WORK GENERATION  
- **Mathematical bullets: (all others) → MATHEMATICAL WORK GENERATION REQUIRED

### 2. MANDATORY DETAIL COVERAGE & TRACKING
**BEFORE GENERATING:** Extract and list EVERY SINGLE detail from CURRENT FOCUS AREAS:
- Names: [extract ALL names mentioned]
- Ages/Numbers: [extract ALL numbers, ages, percentages, dates]
- Locations/Times/Dates: [extract ALL temporal anchors, places, timeframes]
- Personal traits/roles: [extract ALL personality descriptions, jobs, characteristics]
- Mathematical topics/concepts: [extract ALL specific math content]
- Goals/targets/plans: [extract ALL objectives, plans, study goals]
- Learning situations/challenges: [extract ALL educational contexts]

**ABSOLUTE REQUIREMENT:** Every single extracted detail MUST appear in at least one question across the batch.
**USAGE TRACKING:** Mark each detail as used. Verify 100% coverage before finalizing questions.

### 3. ABSOLUTE SOURCE RESTRICTION
**ONLY ALLOWED:** Details explicitly written in CURRENT FOCUS AREAS bullet points
**COMPLETELY FORBIDDEN:**
- ANY content from BATCH_HISTORY
- ANY content from CONTEXT REFERENCE sections
- Generic questions about mathematical fields
- Details not explicitly mentioned in current bullets

**CONTEXT REFERENCE RULE:** Use only to understand WHO/WHAT things mean when they appear in CURRENT FOCUS AREAS.

### 4. DETAIL USAGE PATTERN (ANTI-REPETITION)
- **First mention:** Use full specific detail from bullet point
- **Subsequent references:** Use pronouns ("it", "that", "my homework")
- **VERIFICATION:** Each specific detail appears ONLY ONCE across all questions

### 5. MANDATORY MATHEMATICAL WORK INCLUSION
**CRITICAL:** When referencing problems, equations, or mathematical work that isn't explicitly provided in bullets, you MUST generate and include the complete mathematical content.

ABSOLUTE EXCEPTIONS - NO MATHEMATICAL WORK GENERATION:
- Time Anchor: bullets - Generate questions about scheduling, deadlines, timing without any MATHEMATICAL WORK
- Personal Introduction: bullets - Generate questions FROM the person introducing themselves about their background, career, goals without any MATHEMATICAL WORK
- FOR PERSONAL INTRODUCTION BULLETS: Generate questions FROM the perspective of the person introducing themselves
The person in the bullet is the USER asking the questions
These are contextual/personal details, NOT MATHEMATICAL WORK scenarios

**FOR TIME ANCHOR/PERSONAL INTRODUCTION BULLETS:**
- Focus on study scheduling, academic deadlines, learning goals
- Ask about exam preparation, study coordination, academic planning
- NO mathematical equations, NO problem-solving, NO calculations
- Use natural conversation about timing, goals, and academic context

**REQUIRED PATTERNS:**
- **Completely Stuck (40%):** NO work shown, just describe what you're trying to solve
- **Partially Stuck (30%):** Show ONLY initial 2-4 steps where you got stuck
- **Need Verification (20%):** Show ONLY final answer/result
- **Conceptual Confusion (10%):** NO calculations, concept-focused questions

**WORK GENERATION REQUIREMENTS:**
- Match mathematical level mentioned in bullet points
- Include specific numbers, variables, expressions
- Create realistic problems users would encounter
- **NEVER use placeholders like "... (insert work)" - ALWAYS generate actual mathematical work**

### 5. AUTHENTIC USER STYLE
**Language:** Use contractions ("I'm", "don't"), casual slang ("lol", "btw"), fillers ("like", "um"), informal punctuation ("...", "??", "!!")
**Emotion:** Show genuine feelings - confusion, frustration, excitement
**Natural Flow:** Mix question lengths, include rambling, thinking out loud

### 6. CHRONOLOGICAL ORDER
Process bullet points in exact order provided. Earlier bullet details appear in earlier questions.

### 7. QUESTION GENERATION STRATEGY
- **Problem-Solving:** "Help me solve [specific problem]"
- **Concept Clarification:** "I don't understand [specific concept]"
- **Solution Verification:** "Can you check if my solution is correct?"
- **Method Explanation:** "Why does [specific method] work?"

---

## OUTPUT REQUIREMENTS:

Generate exactly <SUB_BATCH_SIZE> questions that:

1. **MANDATORY:** Use EVERY SINGLE detail from FOCUSED_BULLETS at least once (names, ages, dates, traits, goals, timeframes, etc.)
2. **80% MUST include substantial mathematical work** (equations, calculations, solution attempts)
3. Sound like genuine user requests with realistic mathematical content
4. Follow chronological order of bullet points
5. **ALWAYS include complete mathematical problems/equations - NEVER use placeholders**
6. Match one of the four behavioral patterns with appropriate work shown
7. Stay strictly within bullet point scope
8. **VERIFICATION:** Before submitting, confirm every extracted detail appears in the questions

**OUTPUT FORMAT:**
- **CRITICAL: Generate ONLY the user messages, nothing else**
- Do NOT include question numbers, headers, or organizational text
- **MANDATORY: Each message MUST be separated by exactly "---MESSAGE_SEPARATOR---"**
- **NO other separators allowed** - only use "---MESSAGE_SEPARATOR---"
- Each message can span multiple lines and include mathematical expressions
- **CRITICAL: Each message MUST end with "->-> [number] ---MESSAGE_SEPARATOR---" where [number] is the bullet point it's based on**
- **MANDATORY: End with "### COMPLETE ###"**
- **NO repetitive "and" chains** in any message

**REQUIRED FORMAT PATTERN (EXACT FORMAT TO FOLLOW):**
First complete message with mathematical work ->-> 1
---MESSAGE_SEPARATOR---
Second complete message with mathematical work ->-> 2
---MESSAGE_SEPARATOR---
Third complete message with mathematical work ->-> 3
---MESSAGE_SEPARATOR---
[Continue for all <SUB_BATCH_SIZE> messages]

**CRITICAL FORMATTING RULES:**
- Every message ends with "->-> [bullet_number] ---MESSAGE_SEPARATOR---"
- Every message is followed by "---MESSAGE_SEPARATOR---" (including the last one)
- The arrow comes AFTER all text, code blocks, and content - not in the middle
- Use bullet numbers as they appear in CURRENT FOCUS AREAS
- If a question combines details from multiple bullets, use the primary bullet number
- If the question is not generated from any bulletpoints, put N/A
- Always end the entire output with "### COMPLETE ###"

**CRITICAL VERIFICATION:** Before each question:
1. Does this use a specific detail from current bullets?
2. **Is this a Time Anchor or Personal Introduction bullet? If YES, do NOT include any code**
3. Have I included actual mathematical work (not placeholders)?
4. Does this sound like a real user asking for help?
5. Am I following one of the four behavioral patterns correctly?

**Generate exactly <SUB_BATCH_SIZE> questions in the format above.**
"""

# ================================ answer generation ================================


check_include_question_template = """
Analyze this AI assistant response and determine if it contains a DIRECT, SPECIFIC question that requires the user to provide new information or make a decision.

WHAT COUNTS AS A QUESTION REQUIRING USER RESPONSE:
- A question asking for the user's personal details, context, preferences or constraints (e.g. “What’s your budget?”).
- A question asking the user to choose between explicit options (e.g. “Would you prefer A or B?”).
- A question seeking new clarification about the user’s own situation (e.g. “Which destination are you traveling to?”).

WHAT DOES NOT COUNT:
- Generic offers to help or follow-up prompts (e.g. “Would you like to dive deeper into any of these areas?”).
- Polite or rhetorical closing questions (e.g. “Any questions?” “Let me know if you need anything else.”).
- Questions the AI immediately answers itself.
- Hypothetical or example questions not tied to the user’s real situation.

EXAMPLES OF STATEMENTS THAT DON'T COUNT:
- "Let me know if you have any questions!"
- "Feel free to ask if you need more details"
- "Hope this helps! Any other questions?"
- "If you need further clarification, just ask"

AI ASSISTANT RESPONSE:
<assistant_response>

INSTRUCTIONS:
- If there is at least one question that strictly meets “WHAT COUNTS,” output yes.
- Otherwise (even if there are generic or follow-up invites), output no.
"""

check_need_followup_template = """
You are simulating a typical user in conversation. Decide if you would ask a follow-up question after the AI's response.

**CONVERSATION CONTEXT:**
- Topic: <topic>
- Theme: <theme>
- Recent History: <formatted_history>
- AI's Last Response: <assistant_response>

**ASK FOLLOW-UP ("yes") WHEN:**
1. **Missing Info**: The response lacks details you genuinely need to proceed
   - Specific steps for a process you're trying to follow
   - Key parameters (dates, amounts, requirements) for a decision you're making
   - Clarification on which option applies to your specific situation

2. **Genuine Confusion**: Something is unclear or contradictory
   - Technical terms used without explanation that block understanding
   - Conflicting information that affects your next action
   - Ambiguous instructions where the wrong interpretation has consequences

3. **Incomplete Practical Guidance**: You asked "how to" but can't actually do it yet
   - Missing steps in a procedure
   - Lacks specifics needed for implementation
   - Assumes knowledge you don't have

**NO FOLLOW-UP ("no") WHEN:**
1. **Good Enough to Proceed**: You have what you need

**OUTPUT:** Only "yes" or "no"
"""

ai_assistant_llm_template = """
You must respond only in English. Never switch to Chinese or any other language mid-sentence. All responses should be entirely in English.
Respond to the user’s message by either:
  • Fully answering their question
  . Provide a comprehensive answer
  • Answering plus asking at most ONE follow-up question if you need more detail  

Always honor these rules:
1. Do NOT ask questions the user already answered.  
2. Only ask a question if you genuinely need context to provide a complete, actionable answer.  
3. Keep your main answer clear and comprehensive before you ask.  
4. Use the following system inputs:

TOPIC: <topic>  
THEME: <theme>
PREVIOUS PLANS SUMMARY: <previous_plans_summary>
PREVIOUS BATCHES OF THIS PLAN: <previous_batches> 
CURRENT HISTORY: <current_batch_messages>  

CRITICAL NOTE: Respond only in English. Do not include any Chinese.

**Output**  
Return exactly what you’d say to the user—no tags, no internal notes.
"""

user_llm_answer_question_template = """
You are role-playing as a real user having an authentic conversation with an AI chat assistant. 
The AI assistant has just asked you a question, and you need to provide a natural, human-like response.

#### Input Context You'll Receive:
- **Current Batch Message History**: The conversation flow leading to the AI's question
- **Topic & Theme**: The main subject of this conversation
- **Previous Plans**: Summary of earlier conversation contexts for continuity
- **Current Plan**: The overarching narrative direction for this conversation batch
- **AI's Question**: The specific question the assistant asked that requires your response

#### INPUTS:
**Current Batch Message History**: <current_batch_messages>
**Topic**: <topic>
**Theme**: <theme>
**Previous Plans Summary**: <previous_plans_summary>
**Previous Batches of This Plan**: <previous_batches> 
**Current Plan**: <current_plan>
**AI's Question**: <ai_last_message>

#### CRITICAL: Keep Responses SHORT and Natural
**Real users give brief, to-the-point answers to AI questions**

#### Your Role & Behavior:
You are a real human user with:
- Personal experiences, opinions, and emotions
- Natural speech patterns and conversational habits
- Realistic knowledge limitations and curiosity
- Consistent personality traits across the conversation

**Language Authenticity:**
- Use lots of contractions: "I'm", "don't", "can't", "it's", "that's"
- Include casual slang: "lol", "btw", "tbh", "kinda", "sorta", "gonna", "wanna"
- Add filler words: "like", "um", "you know", "I mean", "so", "well"
- Use informal punctuation: multiple periods "...", question marks "??", exclamation points "!!"

**Imperfect Natural Speech:**
- Include minor typos and informal grammar
- Add rambling elements: "I mean, ..."
- Include thinking out loud: "hmm", "actually", "oh", "maybe"

**Emotional Authenticity:**
- Show genuine feelings: excitement, frustration, uncertainty, hope
- Use emotional language
- Add personal reactions: "ugh", "omg", "yay", "oof", "blah"

#### Response Guidelines:

**STEP 1 - Check Plans for Existing Information**:
- **First**, carefully review the Current Plan and Previous Plans for any information that answers the AI's question
- **If found in plans**: Base your response on that established information to maintain story continuity
- **If not found in plans**: Create a new answer that aligns with the topic, theme, and existing storyline

**STEP 2 - Answer the AI's Question Directly**:
- Keep your reply focused on answering; do **not** introduce new questions.  
- Give a direct answer to what the AI asked
- Don't over-explain or provide unnecessary details
- Answer like you would in a real text conversation
- Include personal context or examples when natural
- **CRITICAL**: Ensure your answer doesn't contradict anything established in previous or current plans

**Stay Consistent with Context**:
- Maintain the same personality and circumstances throughout
- Keep your responses aligned with the current topic and theme

**Response Characteristics**:
- **Tone**: Match the conversation's emotional tone and your established personality
- **Authenticity**: Sound like a real person, not an AI trying to sound human

#### Critical Instructions:
- **Be concise** - Real people don't write long in chat
- Keep your reply focused on answering; do **not** introduce new questions.  
- **ALWAYS check plans first** - Look for any information that answers the AI's question before creating new details
- **Maintain consistency** - Never contradict information established in current or previous plans
- **Fill gaps naturally** - If plans don't have the answer, create responses that fit the established storyline
- ONLY provide your response as the user - no meta-commentary
- Stay in character as a human user throughout
- Answer the question but don't feel obligated to ask a question back (the AI asked YOU)

CRITICAL NOTE: Respond only in English. Do not include any Chinese.
"""

user_llm_ask_followup_question_template = """
You must respond **only in English**. Do not include any Chinese characters or phrases in your response.
You are a real person having a conversation with an AI assistant. Based on the conversation history and the AI's last response, ask ONE natural follow-up question.

## CONTEXT:
**Current Batch Message History**: <current_batch_messages>
**Topic**: <topic>
**Theme**: <theme>
**Previous Plans Summary**: <previous_plans_summary>
**Previous Batches of This Plan**: <previous_batches>
**Current Plan**: <current_plan>
**AI's Response**: <ai_last_message>

## YOUR TASK
Ask a follow-up question (10-20 words) that a real person would naturally ask after receiving the AI's response.

## CRITICAL RULES TO PREVENT REPETITION

Before generating your question:
1. **Scan the Current Batch Message History** for all topics already discussed
2. **Check Previous Batches** for questions already asked
3. **Never ask about something already covered**

If you notice your question seeks information already provided in the conversation history, STOP and generate a completely different question.

## HOW REAL PEOPLE ASK FOLLOW-UPS

### Natural conversation starters:
- "oh wait..." / "hmm..." / "actually..." / "btw..." / "ok but..."
- "that's cool but..." / "makes sense, though..." / "yeah but what about..."

### Authentic reaction patterns:

**Building on the last ai response:**
- Ask about a specific topic not yet covered
- Connect it to your personal situation from the Current Plan

**Showing genuine reactions:**
- If AI gave good news → "nice! but does that mean..."
- If AI mentioned a challenge → "ugh ok, so how do I..."
- If AI explained something → "got it, but what if..."
- If AI suggested options → "hmm which one works better for..."

### Question types that feel natural:
- **Practical concerns**: "how long does that usually take?"
- **Personal application**: "would that work even if I..."
- **Clarification**: "wait so you're saying I should..."
- **Next steps**: "ok cool, do I need to..."
- **Specific worries**: "what happens if..."

## NATURAL SPEECH PATTERNS

Include these elements to sound human:
- Contractions: "don't", "can't", "won't", "that's"
- Casual words: "kinda", "sorta", "gonna", "like"
- Emotional reactions: "ugh", "hmm", "oh", "yikes"
- Informal punctuation: "..." or "??" or "!"

## CONVERSATION FLOW AWARENESS

Based on where you are in the Current Batch Message History:
Ask broader exploratory questions
Ask for specific details or comparisons  
Ask about implementation or next steps

## AUTHENTICITY CHECKLIST

Your question should:
✓ Reference something from the AI's LAST response
✓ NOT repeat any topic from message history
✓ Sound like casual conversation, not an interview
✓ Be 10-20 words maximum
✓ Include at least one casual element (contraction, filler word, etc.)

CRITICAL NOTE: Respond only in English. Do not include any Chinese.

## YOUR RESPONSE:
[Generate only the follow-up question, nothing else]
"""







# ################################################## 10M prompts ##################################################


# ================================ topic generation ================================

ten_m_generate_following_topics = """
You are a narrative coherence specialist creating CHRONOLOGICALLY SEQUENCED topic clusters for realistic conversational AI dataset generation. Your task is to generate 10 interconnected topics that form a natural life progression.

## INPUT DATA
- **SEED TOPIC**: <seed_topic>
- **SEED THEME**: <seed_theme>  
- **SEED SUBTOPICS**: <seed_subtopics>
- **USER PROFILE**: <user_profile>
- **TIMELINE**: <timeline>

## CORE OBJECTIVE
Generate a JSON object containing 10 topics (including the provided seed topic as Topic 0) that form a CHRONOLOGICALLY COHERENT narrative where each topic naturally follows the previous one in realistic time progression.

## CRITICAL REQUIREMENTS

### 1. CHRONOLOGICAL COHERENCE & TOPIC INDEPENDENCE

**TOPIC PROGRESSION RULES:**
- **Topic 0**: Use the provided seed topic EXACTLY as given
- **Topics 1-9**: Each must be a COMPLETELY DIFFERENT life domain/category
- **NO EXTENDED NARRATIVES**: Topics 1-9 should NOT continue the seed topic's story
- **LIFE PROGRESSION**: Each topic represents what naturally happens AFTER completing the previous life experience

**TOPIC INDEPENDENCE MANDATE:**
- Each topic must address a DIFFERENT life area (career, relationships, health, education, finances, etc.)
- Topics should show how one life experience leads to growth in OTHER areas
- NO topic should be "Part 2" of a previous topic

### 2. NATURAL LIFE FLOW REQUIREMENTS

**CAUSAL RELATIONSHIPS WITHOUT CONTINUATION:**
- Topic N+1 is INFLUENCED BY Topic N but addresses a DIFFERENT life domain
- Show how growth in one area catalyzes change in another area
- Example: Travel experience (Topic 0) → Career reassessment (Topic 1) → Relationship priorities (Topic 2)

**FORBIDDEN PATTERNS:**
Multiple topics about the same event/project
"Before/During/After" sequences for the same activity
Topics that could be subtopics of each other
Repetitive categories or themes

**REQUIRED PATTERNS:**
Each topic = New life challenge/opportunity
Different category for each topic
Natural cause-and-effect across different life domains
Holistic life progression showing multi-dimensional growth

### 3. USER PROFILE ALIGNMENT
- **Demographic Consistency**: All topics must align with user's age, education, career level, and life stage
- **Financial Realism**: Topics must reflect user's actual financial capacity and constraints
- **Geographic Logic**: Topics must consider user's location and mobility constraints
- **Value Alignment**: Topics must reflect user's stated priorities, interests, and life goals

### 4. TOPIC BREADTH REQUIREMENTS
Each topic must include a realistic timeline that:
- **Sequential Timing**: Topics must not overlap and should follow logical temporal progression
- **Duration Realism**: Each topic should span 1-2 months for authentic decision-making and implementation
- **Natural Gaps**: Include realistic time gaps between major life transitions
- **Seasonal Considerations**: Account for natural timing (job searches, moving seasons, academic calendars)
- **Timeline Format**: Use "Month X, Year Y - Month X', Year Y'" format
Each topic must be sufficiently BROAD to generate 2000+ authentic conversations by including:
- **Multiple Decision Points**: 15-20 major decisions per topic
- **Complex Subtopics**: 9-10 substantial subtopics that each require extensive discussion
- **Ongoing Processes**: Topics involving multi-month planning, execution, and adjustment phases
- **Cross-Domain Impact**: Topics affecting multiple life areas

### 5. NARRATIVE REALISM
- **Natural Timing**: Realistic time gaps between major life decisions
- **Emotional Progression**: Topics should reflect natural emotional and psychological development
- **Practical Constraints**: Topics must acknowledge real-world limitations (money, time, responsibilities)

## OUTPUT FORMAT REQUIREMENTS

Generate a single JSON object with this EXACT structure:

```json
{
  "topics": [
    {
      "id": 0,
      "category": "[Provided Category]",
      "title": "[Provided Title]", 
      "theme": "[Provided Theme]",
      "subtopics": [/* Provided Subtopics Array */],
      "timeline": "[Start Month, Year - End Month, Year]"
    },
    {
      "id": 1,
      "category": "[New Category]",
      "title": "[Descriptive Title]",
      "theme": "[Character-focused theme describing the challenge/opportunity]", 
      "subtopics": ["[Subtopic 1]", "[Subtopic 2]", "[Subtopic 3]", "[Subtopic 4]", "[Subtopic 5]", "[Subtopic 6]", "[Subtopic 7]", "[Subtopic 8]", "[Subtopic 9]", "[Subtopic 10]"],
      "timeline": "[Start Month, Year - End Month, Year]"
    },
    // ... topics 2-9 following same structure
  ]
}
```

## CRITICAL TIMELINE REQUIREMENTS

### MANDATORY NON-OVERLAPPING TIMELINE RULES

**ABSOLUTE RULE**: Each topic's timeline MUST start AT LEAST one month AFTER the previous topic ends.

**TIMELINE CALCULATION PROTOCOL:**
1. Topic 0: Uses provided timeline exactly
2. Topic N+1 start = Topic N end + AT LEAST 1 month gap
3. NO overlapping months between any topics
4. Each topic duration: 1-2 months

**EXAMPLE PROGRESSION (REQUIRED FORMAT):**
- Topic 0: "January 2015 - February 2015" (ends February)
- Topic 1: "April 2015 - May 2015" (starts April, NOT March - includes gap)
- Topic 2: "July 2015 - September 2015" (starts July - includes gap)
- Topic 3: "November 2016 - January 2016" (starts November - includes gap)

**FORBIDDEN TIMELINE PATTERNS:**
Topic 1 ends "Month x Year y", Topic 2 starts "Month x Year y" (OVERLAP)
Topic 1 ends "Month x Year y", Topic 2 starts "Month x+1 Year y" (NO GAP)
Any shared months between topics
Immediate month-to-month transitions

**REQUIRED TIMELINE PATTERNS:**
Minimum 1-month gap between all topics
Clear temporal separation showing life progression
Realistic pauses between major life decisions

**TIMELINE VERIFICATION STEPS:**
Before finalizing each topic:
1. Identify previous topic's END month
2. Add AT LEAST 1 month to get earliest possible START
3. Verify NO month appears in multiple topics
4. Confirm realistic gaps for life transitions

**GAP JUSTIFICATION:**
The 1+ month gaps represent:
- Processing and integration time after major experiences
- Natural life rhythms and decision-making periods
- Realistic pacing of significant life changes
- Time for consequences of previous decisions to manifest

## TOPIC PROGRESSION GUIDELINES

### Phase 1: Post-Seed Topic Reality (Topics 1-2)
- **Topic 1**: How the seed topic experience changes perspective on ANOTHER life area
- **Topic 2**: Ripple effects creating needs in YET ANOTHER domain

### Phase 2: Multi-Domain Growth (Topics 3-5)
- **Topics 3-5**: Leveraging cumulative growth to address diverse life challenges

### Phase 3: Integration Across Life (Topics 6-8)
- **Topics 6-8**: Synthesizing learnings to optimize different life areas

### Phase 4: Holistic Vision (Topic 9)
- **Topic 9**: Long-term life design incorporating all previous growth

**CRITICAL QUESTION FOR EACH TOPIC:**
"After completing [previous topic], what DIFFERENT area of life would this person naturally need to address next?"

## QUALITY VALIDATION CHECKLIST

Before finalizing each topic, verify:

### Chronological Logic
- [ ] Could this topic realistically happen AFTER the previous topic?
- [ ] Are there clear causal connections to previous topics?
- [ ] Does the content logically flow from previous experiences?

### User Profile Compatibility  
- [ ] Does this align with the user's age and life stage?
- [ ] Is this financially realistic given the user's situation?
- [ ] Is this geographically feasible for the user?

### Conversation Generation Potential
- [ ] Does this topic contain 15+ major decision points?
- [ ] Are the subtopics broad enough for extensive discussion?
- [ ] Would this topic naturally generate 2000+ authentic questions?
- [ ] Are there multiple stakeholders and perspectives involved?

### Narrative Coherence
- [ ] Does this topic build upon character growth from previous topics?
- [ ] Are there clear references/connections to earlier experiences?
- [ ] Does this topic push character development forward?
- [ ] Is the emotional/psychological progression realistic?

**TOPIC DIVERSITY CHECKLIST:**
Before finalizing each topic:
- [ ] Is this a completely different category from previous topics?
- [ ] Does it address a new life domain?
- [ ] Is it influenced by, but not a continuation of, the previous topic?
- [ ] Would this naturally be the next life priority after the previous experience?
- [ ] Does it show growth applied to a DIFFERENT area of life?

## EXAMPLE PROGRESSION LOGIC

Each topic should answer: "Given what happened in the previous topic, what would logically be the next major life area this person needs to address?"

## FORBIDDEN ELEMENTS
- **Non-sequential topics**: Topics that could happen in any order
- **Profile contradictions**: Topics that contradict user's established circumstances
- **Unrealistic jumps**: Major life changes without proper foundation/motivation
- **Narrow topics**: Topics that couldn't generate extensive conversation
- **Template responses**: Generic topics that don't reflect unique user circumstances

## EXECUTION NOTES
- Generate all 10 topics in a single coherent response
- Ensure seamless narrative flow from Topic 0 through Topic 9
- Prioritize realism and character consistency over dramatic storylines
- Focus on authentic life progressions that real people experience
- End output immediately after closing the JSON structure

**CRITICAL**: Output your response in JSON format only. Do not include any explanatory text, markdown formatting, or additional commentary. Provide only the raw JSON object.

Generate the complete topic cluster now.
"""
ten_m_generate_following_topics_five_plan = """
You are a narrative coherence specialist creating CHRONOLOGICALLY SEQUENCED topic clusters for realistic conversational AI dataset generation. Your task is to generate 5 interconnected topics that form a natural life progression.

## INPUT DATA
- **SEED TOPIC**: <seed_topic>
- **SEED THEME**: <seed_theme>  
- **SEED SUBTOPICS**: <seed_subtopics>
- **USER PROFILE**: <user_profile>
- **TIMELINE**: <timeline>

## CORE OBJECTIVE
Generate a JSON object containing 5 topics (including the provided seed topic as Topic 0) that form a CHRONOLOGICALLY COHERENT narrative where each topic naturally follows the previous one in realistic time progression.

## CRITICAL REQUIREMENTS

### 1. CHRONOLOGICAL COHERENCE & TOPIC INDEPENDENCE

**TOPIC PROGRESSION RULES:**
- **Topic 0**: Use the provided seed topic EXACTLY as given
- **Topics 1-4**: Each must be a COMPLETELY DIFFERENT life domain/category
- **NO EXTENDED NARRATIVES**: Topics 1-4 should NOT continue the seed topic's story
- **LIFE PROGRESSION**: Each topic represents what naturally happens AFTER completing the previous life experience

**TOPIC INDEPENDENCE MANDATE:**
- Each topic must address a DIFFERENT life area (career, relationships, health, education, finances, etc.)
- Topics should show how one life experience leads to growth in OTHER areas
- NO topic should be "Part 2" of a previous topic

### 2. NATURAL LIFE FLOW REQUIREMENTS

**CAUSAL RELATIONSHIPS WITHOUT CONTINUATION:**
- Topic N+1 is INFLUENCED BY Topic N but addresses a DIFFERENT life domain
- Show how growth in one area catalyzes change in another area
- Example: Travel experience (Topic 0) → Career reassessment (Topic 1) → Relationship priorities (Topic 2)

**FORBIDDEN PATTERNS:**
Multiple topics about the same event/project
"Before/During/After" sequences for the same activity
Topics that could be subtopics of each other
Repetitive categories or themes

**REQUIRED PATTERNS:**
Each topic = New life challenge/opportunity
Different category for each topic
Natural cause-and-effect across different life domains
Holistic life progression showing multi-dimensional growth

### 3. USER PROFILE ALIGNMENT
- **Demographic Consistency**: All topics must align with user's age, education, career level, and life stage
- **Financial Realism**: Topics must reflect user's actual financial capacity and constraints
- **Geographic Logic**: Topics must consider user's location and mobility constraints
- **Value Alignment**: Topics must reflect user's stated priorities, interests, and life goals

### 4. TOPIC BREADTH REQUIREMENTS
Each topic must include a realistic timeline that:
- **Sequential Timing**: Topics must not overlap and should follow logical temporal progression
- **Duration Realism**: Each topic should span 1-2 months for authentic decision-making and implementation
- **Natural Gaps**: Include realistic time gaps between major life transitions
- **Seasonal Considerations**: Account for natural timing (job searches, moving seasons, academic calendars)
- **Timeline Format**: Use "Month X, Year Y - Month X', Year Y'" format
Each topic must be sufficiently BROAD to generate 2000+ authentic conversations by including:
- **Multiple Decision Points**: 15-20 major decisions per topic
- **Complex Subtopics**: 9-10 substantial subtopics that each require extensive discussion
- **Ongoing Processes**: Topics involving multi-month planning, execution, and adjustment phases
- **Cross-Domain Impact**: Topics affecting multiple life areas

### 5. NARRATIVE REALISM
- **Natural Timing**: Realistic time gaps between major life decisions
- **Emotional Progression**: Topics should reflect natural emotional and psychological development
- **Practical Constraints**: Topics must acknowledge real-world limitations (money, time, responsibilities)

## OUTPUT FORMAT REQUIREMENTS

Generate a single JSON object with this EXACT structure:

```json
{
  "topics": [
    {
      "id": 0,
      "category": "[Provided Category]",
      "title": "[Provided Title]", 
      "theme": "[Provided Theme]",
      "subtopics": [/* Provided Subtopics Array */],
      "timeline": "[Start Month, Year - End Month, Year]"
    },
    {
      "id": 1,
      "category": "[New Category]",
      "title": "[Descriptive Title]",
      "theme": "[Character-focused theme describing the challenge/opportunity]", 
      "subtopics": ["[Subtopic 1]", "[Subtopic 2]", "[Subtopic 3]", "[Subtopic 4]", "[Subtopic 5]", "[Subtopic 6]", "[Subtopic 7]", "[Subtopic 8]", "[Subtopic 9]", "[Subtopic 10]"],
      "timeline": "[Start Month, Year - End Month, Year]"
    },
    // ... topics 2-4 following same structure
  ]
}
```

## CRITICAL TIMELINE REQUIREMENTS

### MANDATORY NON-OVERLAPPING TIMELINE RULES

**ABSOLUTE RULE**: Each topic's timeline MUST start AT LEAST one month AFTER the previous topic ends.

**TIMELINE CALCULATION PROTOCOL:**
1. Topic 0: Uses provided timeline exactly
2. Topic N+1 start = Topic N end + AT LEAST 1 month gap
3. NO overlapping months between any topics
4. Each topic duration: 1-2 months

**EXAMPLE PROGRESSION (REQUIRED FORMAT):**
- Topic 0: "January 2015 - February 2015" (ends February)
- Topic 1: "April 2015 - May 2015" (starts April, NOT March - includes gap)
- Topic 2: "July 2015 - September 2015" (starts July - includes gap)
- Topic 3: "November 2015 - January 2016" (starts November - includes gap)

**FORBIDDEN TIMELINE PATTERNS:**
Topic 1 ends "Month x Year y", Topic 2 starts "Month x Year y" (OVERLAP)
Topic 1 ends "Month x Year y", Topic 2 starts "Month x+1 Year y" (NO GAP)
Any shared months between topics
Immediate month-to-month transitions

**REQUIRED TIMELINE PATTERNS:**
Minimum 1-month gap between all topics
Clear temporal separation showing life progression
Realistic pauses between major life decisions

**TIMELINE VERIFICATION STEPS:**
Before finalizing each topic:
1. Identify previous topic's END month
2. Add AT LEAST 1 month to get earliest possible START
3. Verify NO month appears in multiple topics
4. Confirm realistic gaps for life transitions

**GAP JUSTIFICATION:**
The 1+ month gaps represent:
- Processing and integration time after major experiences
- Natural life rhythms and decision-making periods
- Realistic pacing of significant life changes
- Time for consequences of previous decisions to manifest

## TOPIC PROGRESSION GUIDELINES

### Phase 1: Post-Seed Topic Reality (Topic 1)
- **Topic 1**: How the seed topic experience changes perspective on ANOTHER life area

### Phase 2: Multi-Domain Growth (Topics 2-3)
- **Topics 2-3**: Leveraging cumulative growth to address diverse life challenges

### Phase 3: Integration Across Life (Topic 4)
- **Topic 4**: Synthesizing learnings to optimize different life areas and establish long-term vision

**CRITICAL QUESTION FOR EACH TOPIC:**
"After completing [previous topic], what DIFFERENT area of life would this person naturally need to address next?"

## QUALITY VALIDATION CHECKLIST

Before finalizing each topic, verify:

### Chronological Logic
- [ ] Could this topic realistically happen AFTER the previous topic?
- [ ] Are there clear causal connections to previous topics?
- [ ] Does the content logically flow from previous experiences?

### User Profile Compatibility  
- [ ] Does this align with the user's age and life stage?
- [ ] Is this financially realistic given the user's situation?
- [ ] Is this geographically feasible for the user?

### Conversation Generation Potential
- [ ] Does this topic contain 15+ major decision points?
- [ ] Are the subtopics broad enough for extensive discussion?
- [ ] Would this topic naturally generate 2000+ authentic questions?
- [ ] Are there multiple stakeholders and perspectives involved?

### Narrative Coherence
- [ ] Does this topic build upon character growth from previous topics?
- [ ] Are there clear references/connections to earlier experiences?
- [ ] Does this topic push character development forward?
- [ ] Is the emotional/psychological progression realistic?

**TOPIC DIVERSITY CHECKLIST:**
Before finalizing each topic:
- [ ] Is this a completely different category from previous topics?
- [ ] Does it address a new life domain?
- [ ] Is it influenced by, but not a continuation of, the previous topic?
- [ ] Would this naturally be the next life priority after the previous experience?
- [ ] Does it show growth applied to a DIFFERENT area of life?

## EXAMPLE PROGRESSION LOGIC

Each topic should answer: "Given what happened in the previous topic, what would logically be the next major life area this person needs to address?"

## FORBIDDEN ELEMENTS
- **Non-sequential topics**: Topics that could happen in any order
- **Profile contradictions**: Topics that contradict user's established circumstances
- **Unrealistic jumps**: Major life changes without proper foundation/motivation
- **Narrow topics**: Topics that couldn't generate extensive conversation
- **Template responses**: Generic topics that don't reflect unique user circumstances

## EXECUTION NOTES
- Generate all 5 topics in a single coherent response
- Ensure seamless narrative flow from Topic 0 through Topic 4
- Prioritize realism and character consistency over dramatic storylines
- Focus on authentic life progressions that real people experience
- End output immediately after closing the JSON structure

**CRITICAL**: Output your response in JSON format only. Do not include any explanatory text, markdown formatting, or additional commentary. Provide only the raw JSON object.

Generate the complete topic cluster now.
"""
ten_m_generate_following_topics_five_plan_coding = """
You are a narrative coherence specialist creating CHRONOLOGICALLY SEQUENCED topic clusters for realistic conversational AI dataset generation in the CODING DOMAIN. Your task is to generate 5 interconnected coding-related topics that form a natural technical progression.

## INPUT DATA
- **SEED TOPIC**: <seed_topic>
- **SEED THEME**: <seed_theme>  
- **SEED SUBTOPICS**: <seed_subtopics>
- **USER PROFILE**: <user_profile>
- **TIMELINE**: <timeline>

## CORE OBJECTIVE
Generate a JSON object containing 5 coding-related topics (including the provided seed topic as Topic 0) that form a CHRONOLOGICALLY COHERENT narrative where each topic naturally follows the previous one in realistic technical progression.

## CRITICAL REQUIREMENTS

### 1. CHRONOLOGICAL COHERENCE & TOPIC INDEPENDENCE

**TOPIC PROGRESSION RULES:**
- **Topic 0**: Use the provided seed topic EXACTLY as given
- **Topics 1-4**: Each must be a COMPLETELY DIFFERENT coding domain/category
- **NO EXTENDED NARRATIVES**: Topics 1-4 should NOT continue the seed topic's story
- **TECHNICAL PROGRESSION**: Each topic represents what naturally happens AFTER completing the previous coding experience

**TOPIC INDEPENDENCE MANDATE:**
- Each topic must address a DIFFERENT coding area (frontend, backend, DevOps, mobile, AI/ML, data science, system design, security, testing, databases, etc.)
- Topics should show how one coding experience leads to growth in OTHER technical areas
- NO topic should be "Part 2" of a previous topic

### 2. NATURAL TECHNICAL FLOW REQUIREMENTS

**CAUSAL RELATIONSHIPS WITHOUT CONTINUATION:**
- Topic N+1 is INFLUENCED BY Topic N but addresses a DIFFERENT coding domain
- Show how growth in one technical area catalyzes learning in another area
- Example: Web development project (Topic 0) → Database optimization (Topic 1) → API security (Topic 2)

**FORBIDDEN PATTERNS:**
Multiple topics about the same technology/project
"Before/During/After" sequences for the same coding activity
Topics that could be subtopics of each other
Repetitive technology categories or frameworks

**REQUIRED PATTERNS:**
Each topic = New technical challenge/opportunity
Different coding category for each topic
Natural cause-and-effect across different technical domains
Holistic technical progression showing multi-dimensional growth

### 3. USER PROFILE ALIGNMENT
- **Skill Level Consistency**: All topics must align with user's programming experience, seniority level, and technical background
- **Technical Realism**: Topics must reflect user's actual technical capacity and learning constraints
- **Technology Stack Logic**: Topics must consider user's existing tech stack and natural progression paths
- **Career Alignment**: Topics must reflect user's stated technical interests, career goals, and specialization areas

### 4. TOPIC BREADTH REQUIREMENTS
Each topic must include a realistic timeline that:
- **Sequential Timing**: Topics must not overlap and should follow logical temporal progression
- **Duration Realism**: Each topic should span 1-2 months for authentic learning, development, and implementation
- **Natural Gaps**: Include realistic time gaps between major technical transitions
- **Project Cycles**: Account for natural timing (sprint cycles, deployment windows, learning curves)
- **Timeline Format**: Use "Month X, Year Y - Month X', Year Y'" format
Each topic must be sufficiently BROAD to generate 2000+ authentic coding conversations by including:
- **Multiple Technical Decisions**: 15-20 major coding/architecture decisions per topic
- **Complex Technical Subtopics**: 9-10 substantial technical subtopics that each require extensive discussion
- **Ongoing Development Processes**: Topics involving multi-month planning, coding, testing, and deployment phases
- **Cross-Stack Impact**: Topics affecting multiple layers of the technical stack

### 5. TECHNICAL REALISM
- **Natural Timing**: Realistic time gaps between major technical learning/implementation phases
- **Skill Progression**: Topics should reflect natural technical and professional development
- **Practical Constraints**: Topics must acknowledge real-world limitations (budget, team size, deadlines, technical debt)

## CODING DOMAIN CATEGORIES

Each topic should fall into one of these distinct coding domains:
- **Frontend Development**: UI/UX, frameworks (React, Vue, Angular), responsive design, performance optimization
- **Backend Development**: Server architecture, APIs, microservices, databases, caching
- **DevOps/Infrastructure**: CI/CD, cloud platforms, containerization, monitoring, deployment
- **Mobile Development**: iOS, Android, cross-platform, app store optimization
- **Data Engineering**: ETL pipelines, data warehousing, big data processing, streaming
- **AI/Machine Learning**: Model development, training, deployment, MLOps
- **System Design**: Architecture patterns, scalability, distributed systems
- **Security**: Authentication, authorization, vulnerability assessment, secure coding
- **Testing**: Unit testing, integration testing, E2E testing, test automation
- **Database Management**: Query optimization, schema design, database administration
- **Performance Engineering**: Profiling, optimization, load testing, monitoring
- **Open Source**: Contributing, maintaining projects, community building

## OUTPUT FORMAT REQUIREMENTS

Generate a single JSON object with this EXACT structure:

```json
{
  "topics": [
    {
      "id": 0,
      "category": "[Provided Category]",
      "title": "[Provided Title]", 
      "theme": "[Provided Theme]",
      "subtopics": [/* Provided Subtopics Array */],
      "timeline": "[Start Month, Year - End Month, Year]"
    },
    {
      "id": 1,
      "category": "[New Coding Category]",
      "title": "[Descriptive Technical Title]",
      "theme": "[Developer-focused theme describing the technical challenge/opportunity]", 
      "subtopics": ["[Technical Subtopic 1]", "[Technical Subtopic 2]", "[Technical Subtopic 3]", "[Technical Subtopic 4]", "[Technical Subtopic 5]", "[Technical Subtopic 6]", "[Technical Subtopic 7]", "[Technical Subtopic 8]", "[Technical Subtopic 9]", "[Technical Subtopic 10]"],
      "timeline": "[Start Month, Year - End Month, Year]"
    },
    // ... topics 2-4 following same structure
  ]
}
```

## CRITICAL TIMELINE REQUIREMENTS

### MANDATORY NON-OVERLAPPING TIMELINE RULES

**ABSOLUTE RULE**: Each topic's timeline MUST start AT LEAST one month AFTER the previous topic ends.

**TIMELINE CALCULATION PROTOCOL:**
1. Topic 0: Uses provided timeline exactly
2. Topic N+1 start = Topic N end + AT LEAST 1 month gap
3. NO overlapping months between any topics
4. Each topic duration: 1-2 months

**EXAMPLE PROGRESSION (REQUIRED FORMAT):**
- Topic 0: "January 2015 - February 2015" (ends February)
- Topic 1: "April 2015 - May 2015" (starts April, NOT March - includes gap)
- Topic 2: "July 2015 - September 2015" (starts July - includes gap)
- Topic 3: "November 2015 - January 2016" (starts November - includes gap)

**FORBIDDEN TIMELINE PATTERNS:**
Topic 1 ends "Month x Year y", Topic 2 starts "Month x Year y" (OVERLAP)
Topic 1 ends "Month x Year y", Topic 2 starts "Month x+1 Year y" (NO GAP)
Any shared months between topics
Immediate month-to-month transitions

**REQUIRED TIMELINE PATTERNS:**
Minimum 1-month gap between all topics
Clear temporal separation showing technical progression
Realistic pauses between major technical learning phases

**TIMELINE VERIFICATION STEPS:**
Before finalizing each topic:
1. Identify previous topic's END month
2. Add AT LEAST 1 month to get earliest possible START
3. Verify NO month appears in multiple topics
4. Confirm realistic gaps for technical transitions

**GAP JUSTIFICATION:**
The 1+ month gaps represent:
- Processing and integration time after major technical experiences
- Natural learning rhythms and skill consolidation periods
- Realistic pacing of significant technical skill development
- Time for consequences of previous technical decisions to manifest

## TOPIC PROGRESSION GUIDELINES

### Phase 1: Post-Seed Topic Technical Reality (Topic 1)
- **Topic 1**: How the seed topic experience changes perspective on ANOTHER technical area

### Phase 2: Multi-Domain Technical Growth (Topics 2-3)
- **Topics 2-3**: Leveraging cumulative technical growth to address diverse coding challenges

### Phase 3: Technical Integration Across Domains (Topic 4)
- **Topic 4**: Synthesizing technical learnings to optimize different coding areas and establish long-term technical vision

**CRITICAL QUESTION FOR EACH TOPIC:**
"After completing [previous coding topic], what DIFFERENT technical area would this developer naturally need to address next?"

## QUALITY VALIDATION CHECKLIST

Before finalizing each topic, verify:

### Chronological Logic
- [ ] Could this topic realistically happen AFTER the previous coding topic?
- [ ] Are there clear technical connections to previous topics?
- [ ] Does the content logically flow from previous technical experiences?

### User Profile Compatibility  
- [ ] Does this align with the user's coding skill level and experience?
- [ ] Is this technically realistic given the user's background?
- [ ] Is this feasible given the user's tech stack and environment?

### Conversation Generation Potential
- [ ] Does this topic contain 15+ major technical decision points?
- [ ] Are the subtopics broad enough for extensive technical discussion?
- [ ] Would this topic naturally generate 2000+ authentic coding questions?
- [ ] Are there multiple technical stakeholders and perspectives involved?

### Technical Coherence
- [ ] Does this topic build upon technical growth from previous topics?
- [ ] Are there clear references/connections to earlier technical experiences?
- [ ] Does this topic push technical development forward?
- [ ] Is the skill/knowledge progression realistic?

**TECHNICAL DIVERSITY CHECKLIST:**
Before finalizing each topic:
- [ ] Is this a completely different coding category from previous topics?
- [ ] Does it address a new technical domain?
- [ ] Is it influenced by, but not a continuation of, the previous topic?
- [ ] Would this naturally be the next technical priority after the previous experience?
- [ ] Does it show technical growth applied to a DIFFERENT coding area?

## EXAMPLE PROGRESSION LOGIC

Each topic should answer: "Given what was learned/built in the previous topic, what DIFFERENT technical area would this developer naturally need to explore next?"

## FORBIDDEN ELEMENTS
- **Non-sequential topics**: Topics that could happen in any order
- **Profile contradictions**: Topics that contradict user's established technical level
- **Unrealistic jumps**: Major technical changes without proper foundation/motivation
- **Narrow topics**: Topics that couldn't generate extensive technical conversation
- **Template responses**: Generic topics that don't reflect unique developer circumstances

## EXECUTION NOTES
- Generate all 5 topics in a single coherent response
- Ensure seamless technical narrative flow from Topic 0 through Topic 4
- Prioritize technical realism and skill consistency over dramatic storylines
- Focus on authentic technical progressions that real developers experience
- End output immediately after closing the JSON structure

**CRITICAL**: Output your response in JSON format only. Do not include any explanatory text, markdown formatting, or additional commentary. Provide only the raw JSON object.

Generate the complete topic cluster now.
"""
ten_m_generate_following_topics_ten_plan_coding = """
You are a narrative coherence specialist creating CHRONOLOGICALLY SEQUENCED topic clusters for realistic conversational AI dataset generation in the CODING DOMAIN. Your task is to generate 10 interconnected coding-related topics that form a natural technical progression.

## INPUT DATA
- **SEED TOPIC**: <seed_topic>
- **SEED THEME**: <seed_theme>  
- **SEED SUBTOPICS**: <seed_subtopics>
- **USER PROFILE**: <user_profile>
- **TIMELINE**: <timeline>

## CORE OBJECTIVE
Generate a JSON object containing 10 coding-related topics (including the provided seed topic as Topic 0) that form a CHRONOLOGICALLY COHERENT narrative where each topic naturally follows the previous one in realistic technical progression.

## CRITICAL REQUIREMENTS

### 1. CHRONOLOGICAL COHERENCE & TOPIC INDEPENDENCE

**TOPIC PROGRESSION RULES:**
- **Topic 0**: Use the provided seed topic EXACTLY as given
- **Topics 1-9**: Each must be a COMPLETELY DIFFERENT coding domain/category
- **NO EXTENDED NARRATIVES**: Topics 1-9 should NOT continue the seed topic's story
- **TECHNICAL PROGRESSION**: Each topic represents what naturally happens AFTER completing the previous coding experience

**TOPIC INDEPENDENCE MANDATE:**
- Each topic must address a DIFFERENT coding area (frontend, backend, DevOps, mobile, AI/ML, data science, system design, security, testing, databases, etc.)
- Topics should show how one coding experience leads to growth in OTHER technical areas
- NO topic should be "Part 2" of a previous topic

### 2. NATURAL TECHNICAL FLOW REQUIREMENTS

**CAUSAL RELATIONSHIPS WITHOUT CONTINUATION:**
- Topic N+1 is INFLUENCED BY Topic N but addresses a DIFFERENT coding domain
- Show how growth in one technical area catalyzes learning in another area
- Example: Web development project (Topic 0) → Database optimization (Topic 1) → API security (Topic 2)

**FORBIDDEN PATTERNS:**
Multiple topics about the same technology/project
"Before/During/After" sequences for the same coding activity
Topics that could be subtopics of each other
Repetitive technology categories or frameworks

**REQUIRED PATTERNS:**
Each topic = New technical challenge/opportunity
Different coding category for each topic
Natural cause-and-effect across different technical domains
Holistic technical progression showing multi-dimensional growth

### 3. USER PROFILE ALIGNMENT
- **Skill Level Consistency**: All topics must align with user's programming experience, seniority level, and technical background
- **Technical Realism**: Topics must reflect user's actual technical capacity and learning constraints
- **Technology Stack Logic**: Topics must consider user's existing tech stack and natural progression paths
- **Career Alignment**: Topics must reflect user's stated technical interests, career goals, and specialization areas

### 4. TOPIC BREADTH REQUIREMENTS
Each topic must include a realistic timeline that:
- **Sequential Timing**: Topics must not overlap and should follow logical temporal progression
- **Duration Realism**: Each topic should span 1-2 months for authentic learning, development, and implementation
- **Natural Gaps**: Include realistic time gaps between major technical transitions
- **Project Cycles**: Account for natural timing (sprint cycles, deployment windows, learning curves)
- **Timeline Format**: Use "Month X, Year Y - Month X', Year Y'" format
Each topic must be sufficiently BROAD to generate 2000+ authentic coding conversations by including:
- **Multiple Technical Decisions**: 15-20 major coding/architecture decisions per topic
- **Complex Technical Subtopics**: 9-10 substantial technical subtopics that each require extensive discussion
- **Ongoing Development Processes**: Topics involving multi-month planning, coding, testing, and deployment phases
- **Cross-Stack Impact**: Topics affecting multiple layers of the technical stack

### 5. TECHNICAL REALISM
- **Natural Timing**: Realistic time gaps between major technical learning/implementation phases
- **Skill Progression**: Topics should reflect natural technical and professional development
- **Practical Constraints**: Topics must acknowledge real-world limitations (budget, team size, deadlines, technical debt)

## CODING DOMAIN CATEGORIES

Each topic should fall into one of these distinct coding domains:
- **Frontend Development**: UI/UX, frameworks (React, Vue, Angular), responsive design, performance optimization
- **Backend Development**: Server architecture, APIs, microservices, databases, caching
- **DevOps/Infrastructure**: CI/CD, cloud platforms, containerization, monitoring, deployment
- **Mobile Development**: iOS, Android, cross-platform, app store optimization
- **Data Engineering**: ETL pipelines, data warehousing, big data processing, streaming
- **AI/Machine Learning**: Model development, training, deployment, MLOps
- **System Design**: Architecture patterns, scalability, distributed systems
- **Security**: Authentication, authorization, vulnerability assessment, secure coding
- **Testing**: Unit testing, integration testing, E2E testing, test automation
- **Database Management**: Query optimization, schema design, database administration
- **Performance Engineering**: Profiling, optimization, load testing, monitoring
- **Open Source**: Contributing, maintaining projects, community building

## OUTPUT FORMAT REQUIREMENTS

Generate a single JSON object with this EXACT structure:

```json
{
  "topics": [
    {
      "id": 0,
      "category": "[Provided Category]",
      "title": "[Provided Title]", 
      "theme": "[Provided Theme]",
      "subtopics": [/* Provided Subtopics Array */],
      "timeline": "[Start Month, Year - End Month, Year]"
    },
    {
      "id": 1,
      "category": "[New Coding Category]",
      "title": "[Descriptive Technical Title]",
      "theme": "[Developer-focused theme describing the technical challenge/opportunity]", 
      "subtopics": ["[Technical Subtopic 1]", "[Technical Subtopic 2]", "[Technical Subtopic 3]", "[Technical Subtopic 4]", "[Technical Subtopic 5]", "[Technical Subtopic 6]", "[Technical Subtopic 7]", "[Technical Subtopic 8]", "[Technical Subtopic 9]", "[Technical Subtopic 10]"],
      "timeline": "[Start Month, Year - End Month, Year]"
    },
    // ... topics 2-9 following same structure
  ]
}
```

## CRITICAL TIMELINE REQUIREMENTS

### MANDATORY NON-OVERLAPPING TIMELINE RULES

**ABSOLUTE RULE**: Each topic's timeline MUST start AT LEAST one month AFTER the previous topic ends.

**TIMELINE CALCULATION PROTOCOL:**
1. Topic 0: Uses provided timeline exactly
2. Topic N+1 start = Topic N end + AT LEAST 1 month gap
3. NO overlapping months between any topics
4. Each topic duration: 1-2 months

**EXAMPLE PROGRESSION (REQUIRED FORMAT):**
- Topic 0: "January 2015 - February 2015" (ends February)
- Topic 1: "April 2015 - May 2015" (starts April, NOT March - includes gap)
- Topic 2: "July 2015 - September 2015" (starts July - includes gap)
- Topic 3: "November 2015 - January 2016" (starts November - includes gap)
- Topic 4: "March 2016 - April 2016" (starts March - includes gap)
- Topic 5: "June 2016 - July 2016" (starts June - includes gap)
- Topic 6: "September 2016 - October 2016" (starts September - includes gap)
- Topic 7: "December 2016 - January 2017" (starts December - includes gap)
- Topic 8: "March 2017 - April 2017" (starts March - includes gap)
- Topic 9: "June 2017 - August 2017" (starts June - includes gap)

**FORBIDDEN TIMELINE PATTERNS:**
Topic 1 ends "Month x Year y", Topic 2 starts "Month x Year y" (OVERLAP)
Topic 1 ends "Month x Year y", Topic 2 starts "Month x+1 Year y" (NO GAP)
Any shared months between topics
Immediate month-to-month transitions

**REQUIRED TIMELINE PATTERNS:**
Minimum 1-month gap between all topics
Clear temporal separation showing technical progression
Realistic pauses between major technical learning phases

**TIMELINE VERIFICATION STEPS:**
Before finalizing each topic:
1. Identify previous topic's END month
2. Add AT LEAST 1 month to get earliest possible START
3. Verify NO month appears in multiple topics
4. Confirm realistic gaps for technical transitions

**GAP JUSTIFICATION:**
The 1+ month gaps represent:
- Processing and integration time after major technical experiences
- Natural learning rhythms and skill consolidation periods
- Realistic pacing of significant technical skill development
- Time for consequences of previous technical decisions to manifest

## TOPIC PROGRESSION GUIDELINES

### Phase 1: Post-Seed Topic Technical Reality (Topics 1-2)
- **Topic 1**: How the seed topic experience changes perspective on ANOTHER technical area
- **Topic 2**: Leveraging initial technical growth to explore complementary domain

### Phase 2: Mid-Journey Technical Expansion (Topics 3-5)
- **Topics 3-5**: Building diverse technical competencies across multiple coding domains

### Phase 3: Advanced Technical Integration (Topics 6-8)
- **Topics 6-8**: Synthesizing accumulated knowledge to tackle complex cross-domain challenges

### Phase 4: Technical Mastery and Vision (Topics 9)
- **Topic 9**: Establishing long-term technical vision and architectural leadership across domains

**CRITICAL QUESTION FOR EACH TOPIC:**
"After completing [previous coding topic], what DIFFERENT technical area would this developer naturally need to address next?"

## QUALITY VALIDATION CHECKLIST

Before finalizing each topic, verify:

### Chronological Logic
- [ ] Could this topic realistically happen AFTER the previous coding topic?
- [ ] Are there clear technical connections to previous topics?
- [ ] Does the content logically flow from previous technical experiences?

### User Profile Compatibility  
- [ ] Does this align with the user's coding skill level and experience?
- [ ] Is this technically realistic given the user's background?
- [ ] Is this feasible given the user's tech stack and environment?

### Conversation Generation Potential
- [ ] Does this topic contain 15+ major technical decision points?
- [ ] Are the subtopics broad enough for extensive technical discussion?
- [ ] Would this topic naturally generate 2000+ authentic coding questions?
- [ ] Are there multiple technical stakeholders and perspectives involved?

### Technical Coherence
- [ ] Does this topic build upon technical growth from previous topics?
- [ ] Are there clear references/connections to earlier technical experiences?
- [ ] Does this topic push technical development forward?
- [ ] Is the skill/knowledge progression realistic?

**TECHNICAL DIVERSITY CHECKLIST:**
Before finalizing each topic:
- [ ] Is this a completely different coding category from previous topics?
- [ ] Does it address a new technical domain?
- [ ] Is it influenced by, but not a continuation of, the previous topic?
- [ ] Would this naturally be the next technical priority after the previous experience?
- [ ] Does it show technical growth applied to a DIFFERENT coding area?

## EXAMPLE PROGRESSION LOGIC

Each topic should answer: "Given what was learned/built in the previous topic, what DIFFERENT technical area would this developer naturally need to explore next?"

## FORBIDDEN ELEMENTS
- **Non-sequential topics**: Topics that could happen in any order
- **Profile contradictions**: Topics that contradict user's established technical level
- **Unrealistic jumps**: Major technical changes without proper foundation/motivation
- **Narrow topics**: Topics that couldn't generate extensive technical conversation
- **Template responses**: Generic topics that don't reflect unique developer circumstances

## EXECUTION NOTES
- Generate all 10 topics in a single coherent response
- Ensure seamless technical narrative flow from Topic 0 through Topic 9
- Prioritize technical realism and skill consistency over dramatic storylines
- Focus on authentic technical progressions that real developers experience
- End output immediately after closing the JSON structure

**CRITICAL**: Output your response in JSON format only. Do not include any explanatory text, markdown formatting, or additional commentary. Provide only the raw JSON object.

Generate the complete topic cluster now.
"""
ten_m_generate_following_topics_five_plan_math = """
You are a narrative coherence specialist creating CHRONOLOGICALLY SEQUENCED topic clusters for realistic conversational AI dataset generation in the MATH DOMAIN. Your task is to generate 5 interconnected math-related topics that form a natural mathematical learning progression.

## INPUT DATA
- **SEED TOPIC**: <seed_topic>
- **SEED THEME**: <seed_theme>  
- **SEED SUBTOPICS**: <seed_subtopics>
- **USER PROFILE**: <user_profile>
- **TIMELINE**: <timeline>

## CORE OBJECTIVE
Generate a JSON object containing 5 math-related topics (including the provided seed topic as Topic 0) that form a CHRONOLOGICALLY COHERENT narrative where each topic naturally follows the previous one in realistic mathematical progression.

## CRITICAL REQUIREMENTS

### 1. CHRONOLOGICAL COHERENCE & TOPIC INDEPENDENCE

**TOPIC PROGRESSION RULES:**
- **Topic 0**: Use the provided seed topic EXACTLY as given
- **Topics 1-4**: Each must be a COMPLETELY DIFFERENT math domain/category
- **NO EXTENDED NARRATIVES**: Topics 1-4 should NOT continue the seed topic's story
- **MATHEMATICAL PROGRESSION**: Each topic represents what naturally happens AFTER completing the previous mathematical experience

**TOPIC INDEPENDENCE MANDATE:**
- Each topic must address a DIFFERENT math area (algebra, geometry, calculus, statistics, discrete math, linear algebra, differential equations, number theory, topology, analysis, etc.)
- Topics should show how one mathematical experience leads to growth in OTHER mathematical areas
- NO topic should be "Part 2" of a previous topic

### 2. NATURAL MATHEMATICAL FLOW REQUIREMENTS

**CAUSAL RELATIONSHIPS WITHOUT CONTINUATION:**
- Topic N+1 is INFLUENCED BY Topic N but addresses a DIFFERENT math domain
- Show how growth in one mathematical area catalyzes learning in another area
- Example: Calculus study (Topic 0) → Statistics applications (Topic 1) → Linear algebra modeling (Topic 2)

**FORBIDDEN PATTERNS:**
Multiple topics about the same mathematical concept/course
"Before/During/After" sequences for the same mathematical activity
Topics that could be subtopics of each other
Repetitive mathematical categories or subject areas

**REQUIRED PATTERNS:**
Each topic = New mathematical challenge/opportunity
Different math category for each topic
Natural cause-and-effect across different mathematical domains
Holistic mathematical progression showing multi-dimensional growth

### 3. USER PROFILE ALIGNMENT
- **Mathematical Level Consistency**: All topics must align with user's math background, education level, and mathematical maturity
- **Learning Realism**: Topics must reflect user's actual mathematical capacity and learning constraints
- **Academic Context Logic**: Topics must consider user's educational setting and mathematical goals
- **Interest Alignment**: Topics must reflect user's stated mathematical interests, career goals, and specialization areas

### 4. TOPIC BREADTH REQUIREMENTS
Each topic must include a realistic timeline that:
- **Sequential Timing**: Topics must not overlap and should follow logical temporal progression
- **Duration Realism**: Each topic should span 1-2 months for authentic mathematical learning and mastery
- **Natural Gaps**: Include realistic time gaps between major mathematical transitions
- **Academic Cycles**: Account for natural timing (semester schedules, exam periods, course prerequisites)
- **Timeline Format**: Use "Month X, Year Y - Month X', Year Y'" format
Each topic must be sufficiently BROAD to generate 2000+ authentic mathematical conversations by including:
- **Multiple Mathematical Decisions**: 15-20 major mathematical concept/problem-solving decisions per topic
- **Complex Mathematical Subtopics**: 9-10 substantial mathematical subtopics that each require extensive discussion
- **Ongoing Learning Processes**: Topics involving multi-month study, practice, and application phases
- **Cross-Domain Mathematical Impact**: Topics affecting multiple areas of mathematical understanding

### 5. MATHEMATICAL REALISM
- **Natural Timing**: Realistic time gaps between major mathematical learning phases
- **Skill Progression**: Topics should reflect natural mathematical and cognitive development
- **Practical Constraints**: Topics must acknowledge real-world limitations (study time, prerequisite knowledge, academic deadlines)

## MATHEMATICAL DOMAIN CATEGORIES

Each topic should fall into one of these distinct mathematical domains:
- **Algebra**: Linear algebra, abstract algebra, algebraic structures, polynomial equations
- **Analysis**: Real analysis, complex analysis, functional analysis, measure theory
- **Calculus**: Differential calculus, integral calculus, multivariable calculus, vector calculus
- **Geometry**: Euclidean geometry, analytic geometry, differential geometry, algebraic geometry
- **Statistics**: Descriptive statistics, inferential statistics, probability theory, statistical modeling
- **Discrete Mathematics**: Combinatorics, graph theory, number theory, logic, set theory
- **Applied Mathematics**: Mathematical modeling, optimization, numerical methods, computational math
- **Differential Equations**: Ordinary differential equations, partial differential equations, dynamical systems
- **Topology**: Point-set topology, algebraic topology, differential topology
- **Mathematical Physics**: Quantum mechanics, thermodynamics, electromagnetic theory
- **Operations Research**: Linear programming, game theory, decision theory, queuing theory
- **Logic**: Mathematical logic, proof theory, model theory, computability theory

## OUTPUT FORMAT REQUIREMENTS

Generate a single JSON object with this EXACT structure:

```json
{
  "topics": [
    {
      "id": 0,
      "category": "[Provided Category]",
      "title": "[Provided Title]", 
      "theme": "[Provided Theme]",
      "subtopics": [/* Provided Subtopics Array */],
      "timeline": "[Start Month, Year - End Month, Year]"
    },
    {
      "id": 1,
      "category": "[New Math Category]",
      "title": "[Descriptive Mathematical Title]",
      "theme": "[Student-focused theme describing the mathematical challenge/opportunity]", 
      "subtopics": ["[Mathematical Subtopic 1]", "[Mathematical Subtopic 2]", "[Mathematical Subtopic 3]", "[Mathematical Subtopic 4]", "[Mathematical Subtopic 5]", "[Mathematical Subtopic 6]", "[Mathematical Subtopic 7]", "[Mathematical Subtopic 8]", "[Technical Subtopic 9]", "[Technical Subtopic 10]"],
      "timeline": "[Start Month, Year - End Month, Year]"
    },
    // ... topics 2-4 following same structure
  ]
}
```

## CRITICAL TIMELINE REQUIREMENTS

### MANDATORY NON-OVERLAPPING TIMELINE RULES

**ABSOLUTE RULE**: Each topic's timeline MUST start AT LEAST one month AFTER the previous topic ends.

**TIMELINE CALCULATION PROTOCOL:**
1. Topic 0: Uses provided timeline exactly
2. Topic N+1 start = Topic N end + AT LEAST 1 month gap
3. NO overlapping months between any topics
4. Each topic duration: 1-2 months

**EXAMPLE PROGRESSION (REQUIRED FORMAT):**
- Topic 0: "January 2015 - February 2015" (ends February)
- Topic 1: "April 2015 - May 2015" (starts April, NOT March - includes gap)
- Topic 2: "July 2015 - September 2015" (starts July - includes gap)
- Topic 3: "November 2015 - January 2016" (starts November - includes gap)

**FORBIDDEN TIMELINE PATTERNS:**
Topic 1 ends "Month x Year y", Topic 2 starts "Month x Year y" (OVERLAP)
Topic 1 ends "Month x Year y", Topic 2 starts "Month x+1 Year y" (NO GAP)
Any shared months between topics
Immediate month-to-month transitions

**REQUIRED TIMELINE PATTERNS:**
Minimum 1-month gap between all topics
Clear temporal separation showing mathematical progression
Realistic pauses between major mathematical learning phases

**TIMELINE VERIFICATION STEPS:**
Before finalizing each topic:
1. Identify previous topic's END month
2. Add AT LEAST 1 month to get earliest possible START
3. Verify NO month appears in multiple topics
4. Confirm realistic gaps for mathematical transitions

**GAP JUSTIFICATION:**
The 1+ month gaps represent:
- Processing and integration time after major mathematical experiences
- Natural learning rhythms and concept consolidation periods
- Realistic pacing of significant mathematical skill development
- Time for consequences of previous mathematical decisions to manifest

## TOPIC PROGRESSION GUIDELINES

### Phase 1: Post-Seed Topic Mathematical Reality (Topic 1)
- **Topic 1**: How the seed topic experience changes perspective on ANOTHER mathematical area

### Phase 2: Multi-Domain Mathematical Growth (Topics 2-3)
- **Topics 2-3**: Leveraging cumulative mathematical growth to address diverse mathematical challenges

### Phase 3: Mathematical Integration Across Domains (Topic 4)
- **Topic 4**: Synthesizing mathematical learnings to optimize different mathematical areas and establish long-term mathematical vision

**CRITICAL QUESTION FOR EACH TOPIC:**
"After completing [previous mathematical topic], what DIFFERENT mathematical area would this student naturally need to explore next?"

## QUALITY VALIDATION CHECKLIST

Before finalizing each topic, verify:

### Chronological Logic
- [ ] Could this topic realistically happen AFTER the previous mathematical topic?
- [ ] Are there clear mathematical connections to previous topics?
- [ ] Does the content logically flow from previous mathematical experiences?

### User Profile Compatibility  
- [ ] Does this align with the user's mathematical skill level and background?
- [ ] Is this mathematically realistic given the user's education level?
- [ ] Is this feasible given the user's academic schedule and prerequisites?

### Conversation Generation Potential
- [ ] Does this topic contain 15+ major mathematical decision points?
- [ ] Are the subtopics broad enough for extensive mathematical discussion?
- [ ] Would this topic naturally generate 2000+ authentic mathematical questions?
- [ ] Are there multiple mathematical perspectives and approaches involved?

### Mathematical Coherence
- [ ] Does this topic build upon mathematical growth from previous topics?
- [ ] Are there clear references/connections to earlier mathematical experiences?
- [ ] Does this topic push mathematical development forward?
- [ ] Is the skill/knowledge progression mathematically realistic?

**MATHEMATICAL DIVERSITY CHECKLIST:**
Before finalizing each topic:
- [ ] Is this a completely different mathematical category from previous topics?
- [ ] Does it address a new mathematical domain?
- [ ] Is it influenced by, but not a continuation of, the previous topic?
- [ ] Would this naturally be the next mathematical priority after the previous experience?
- [ ] Does it show mathematical growth applied to a DIFFERENT mathematical area?

## EXAMPLE PROGRESSION LOGIC

Each topic should answer: "Given what was learned/mastered in the previous topic, what DIFFERENT mathematical area would this student naturally need to explore next?"

## FORBIDDEN ELEMENTS
- **Non-sequential topics**: Topics that could happen in any order
- **Profile contradictions**: Topics that contradict user's established mathematical level
- **Unrealistic jumps**: Major mathematical changes without proper foundation/prerequisites
- **Narrow topics**: Topics that couldn't generate extensive mathematical conversation
- **Template responses**: Generic topics that don't reflect unique student circumstances

## EXECUTION NOTES
- Generate all 5 topics in a single coherent response
- Ensure seamless mathematical narrative flow from Topic 0 through Topic 4
- Prioritize mathematical realism and skill consistency over dramatic storylines
- Focus on authentic mathematical progressions that real students experience
- End output immediately after closing the JSON structure

**CRITICAL**: Output your response in JSON format only. Do not include any explanatory text, markdown formatting, or additional commentary. Provide only the raw JSON object.

Generate the complete topic cluster now.
"""
ten_m_generate_following_topics_ten_plan_math = """
You are a narrative coherence specialist creating CHRONOLOGICALLY SEQUENCED topic clusters for realistic conversational AI dataset generation in the MATH DOMAIN. Your task is to generate 10 interconnected math-related topics that form a natural mathematical learning progression.

## INPUT DATA
- **SEED TOPIC**: <seed_topic>
- **SEED THEME**: <seed_theme>  
- **SEED SUBTOPICS**: <seed_subtopics>
- **USER PROFILE**: <user_profile>
- **TIMELINE**: <timeline>

## CORE OBJECTIVE
Generate a JSON object containing 10 math-related topics (including the provided seed topic as Topic 0) that form a CHRONOLOGICALLY COHERENT narrative where each topic naturally follows the previous one in realistic mathematical progression.

## CRITICAL REQUIREMENTS

### 1. CHRONOLOGICAL COHERENCE & TOPIC INDEPENDENCE

**TOPIC PROGRESSION RULES:**
- **Topic 0**: Use the provided seed topic EXACTLY as given
- **Topics 1-9**: Each must be a COMPLETELY DIFFERENT math domain/category
- **NO EXTENDED NARRATIVES**: Topics 1-9 should NOT continue the seed topic's story
- **MATHEMATICAL PROGRESSION**: Each topic represents what naturally happens AFTER completing the previous mathematical experience

**TOPIC INDEPENDENCE MANDATE:**
- Each topic must address a DIFFERENT math area (algebra, geometry, calculus, statistics, discrete math, linear algebra, differential equations, number theory, topology, analysis, etc.)
- Topics should show how one mathematical experience leads to growth in OTHER mathematical areas
- NO topic should be "Part 2" of a previous topic

### 2. NATURAL MATHEMATICAL FLOW REQUIREMENTS

**CAUSAL RELATIONSHIPS WITHOUT CONTINUATION:**
- Topic N+1 is INFLUENCED BY Topic N but addresses a DIFFERENT math domain
- Show how growth in one mathematical area catalyzes learning in another area
- Example: Calculus study (Topic 0) → Statistics applications (Topic 1) → Linear algebra modeling (Topic 2)

**FORBIDDEN PATTERNS:**
Multiple topics about the same mathematical concept/course
"Before/During/After" sequences for the same mathematical activity
Topics that could be subtopics of each other
Repetitive mathematical categories or subject areas

**REQUIRED PATTERNS:**
Each topic = New mathematical challenge/opportunity
Different math category for each topic
Natural cause-and-effect across different mathematical domains
Holistic mathematical progression showing multi-dimensional growth

### 3. USER PROFILE ALIGNMENT
- **Mathematical Level Consistency**: All topics must align with user's math background, education level, and mathematical maturity
- **Learning Realism**: Topics must reflect user's actual mathematical capacity and learning constraints
- **Academic Context Logic**: Topics must consider user's educational setting and mathematical goals
- **Interest Alignment**: Topics must reflect user's stated mathematical interests, career goals, and specialization areas

### 4. TOPIC BREADTH REQUIREMENTS
Each topic must include a realistic timeline that:
- **Sequential Timing**: Topics must not overlap and should follow logical temporal progression
- **Duration Realism**: Each topic should span 1-2 months for authentic mathematical learning and mastery
- **Natural Gaps**: Include realistic time gaps between major mathematical transitions
- **Academic Cycles**: Account for natural timing (semester schedules, exam periods, course prerequisites)
- **Timeline Format**: Use "Month X, Year Y - Month X', Year Y'" format
Each topic must be sufficiently BROAD to generate 2000+ authentic mathematical conversations by including:
- **Multiple Mathematical Decisions**: 15-20 major mathematical concept/problem-solving decisions per topic
- **Complex Mathematical Subtopics**: 9-10 substantial mathematical subtopics that each require extensive discussion
- **Ongoing Learning Processes**: Topics involving multi-month study, practice, and application phases
- **Cross-Domain Mathematical Impact**: Topics affecting multiple areas of mathematical understanding

### 5. MATHEMATICAL REALISM
- **Natural Timing**: Realistic time gaps between major mathematical learning phases
- **Skill Progression**: Topics should reflect natural mathematical and cognitive development
- **Practical Constraints**: Topics must acknowledge real-world limitations (study time, prerequisite knowledge, academic deadlines)

## MATHEMATICAL DOMAIN CATEGORIES

Each topic should fall into one of these distinct mathematical domains:
- **Algebra**: Linear algebra, abstract algebra, algebraic structures, polynomial equations
- **Analysis**: Real analysis, complex analysis, functional analysis, measure theory
- **Calculus**: Differential calculus, integral calculus, multivariable calculus, vector calculus
- **Geometry**: Euclidean geometry, analytic geometry, differential geometry, algebraic geometry
- **Statistics**: Descriptive statistics, inferential statistics, probability theory, statistical modeling
- **Discrete Mathematics**: Combinatorics, graph theory, number theory, logic, set theory
- **Applied Mathematics**: Mathematical modeling, optimization, numerical methods, computational math
- **Differential Equations**: Ordinary differential equations, partial differential equations, dynamical systems
- **Topology**: Point-set topology, algebraic topology, differential topology
- **Mathematical Physics**: Quantum mechanics, thermodynamics, electromagnetic theory
- **Operations Research**: Linear programming, game theory, decision theory, queuing theory
- **Logic**: Mathematical logic, proof theory, model theory, computability theory

## OUTPUT FORMAT REQUIREMENTS

Generate a single JSON object with this EXACT structure:

```json
{
  "topics": [
    {
      "id": 0,
      "category": "[Provided Category]",
      "title": "[Provided Title]", 
      "theme": "[Provided Theme]",
      "subtopics": [/* Provided Subtopics Array */],
      "timeline": "[Start Month, Year - End Month, Year]"
    },
    {
      "id": 1,
      "category": "[New Math Category]",
      "title": "[Descriptive Mathematical Title]",
      "theme": "[Student-focused theme describing the mathematical challenge/opportunity]", 
      "subtopics": ["[Mathematical Subtopic 1]", "[Mathematical Subtopic 2]", "[Mathematical Subtopic 3]", "[Mathematical Subtopic 4]", "[Mathematical Subtopic 5]", "[Mathematical Subtopic 6]", "[Mathematical Subtopic 7]", "[Mathematical Subtopic 8]", "[Technical Subtopic 9]", "[Technical Subtopic 10]"],
      "timeline": "[Start Month, Year - End Month, Year]"
    },
    // ... topics 2-9 following same structure
  ]
}
```

## CRITICAL TIMELINE REQUIREMENTS

### MANDATORY NON-OVERLAPPING TIMELINE RULES

**ABSOLUTE RULE**: Each topic's timeline MUST start AT LEAST one month AFTER the previous topic ends.

**TIMELINE CALCULATION PROTOCOL:**
1. Topic 0: Uses provided timeline exactly
2. Topic N+1 start = Topic N end + AT LEAST 1 month gap
3. NO overlapping months between any topics
4. Each topic duration: 1-2 months

**EXAMPLE PROGRESSION (REQUIRED FORMAT):**
- Topic 0: "January 2015 - February 2015" (ends February)
- Topic 1: "April 2015 - May 2015" (starts April, NOT March - includes gap)
- Topic 2: "July 2015 - September 2015" (starts July - includes gap)
- Topic 3: "November 2015 - January 2016" (starts November - includes gap)
- Topic 4: "March 2016 - April 2016" (starts March - includes gap)
- Topic 5: "June 2016 - July 2016" (starts June - includes gap)
- Topic 6: "September 2016 - October 2016" (starts September - includes gap)
- Topic 7: "December 2016 - January 2017" (starts December - includes gap)
- Topic 8: "March 2017 - April 2017" (starts March - includes gap)
- Topic 9: "June 2017 - August 2017" (starts June - includes gap)

**FORBIDDEN TIMELINE PATTERNS:**
Topic 1 ends "Month x Year y", Topic 2 starts "Month x Year y" (OVERLAP)
Topic 1 ends "Month x Year y", Topic 2 starts "Month x+1 Year y" (NO GAP)
Any shared months between topics
Immediate month-to-month transitions

**REQUIRED TIMELINE PATTERNS:**
Minimum 1-month gap between all topics
Clear temporal separation showing mathematical progression
Realistic pauses between major mathematical learning phases

**TIMELINE VERIFICATION STEPS:**
Before finalizing each topic:
1. Identify previous topic's END month
2. Add AT LEAST 1 month to get earliest possible START
3. Verify NO month appears in multiple topics
4. Confirm realistic gaps for mathematical transitions

**GAP JUSTIFICATION:**
The 1+ month gaps represent:
- Processing and integration time after major mathematical experiences
- Natural learning rhythms and concept consolidation periods
- Realistic pacing of significant mathematical skill development
- Time for consequences of previous mathematical decisions to manifest

## TOPIC PROGRESSION GUIDELINES

### Phase 1: Post-Seed Topic Mathematical Reality (Topics 1-2)
- **Topic 1**: How the seed topic experience changes perspective on ANOTHER mathematical area
- **Topic 2**: Leveraging initial mathematical growth to explore complementary domain

### Phase 2: Mid-Journey Mathematical Expansion (Topics 3-5)
- **Topics 3-5**: Building diverse mathematical competencies across multiple mathematical domains

### Phase 3: Advanced Mathematical Integration (Topics 6-8)
- **Topics 6-8**: Synthesizing accumulated knowledge to tackle complex cross-domain mathematical challenges

### Phase 4: Mathematical Mastery and Vision (Topic 9)
- **Topic 9**: Establishing long-term mathematical vision and theoretical leadership across domains

**CRITICAL QUESTION FOR EACH TOPIC:**
"After completing [previous mathematical topic], what DIFFERENT mathematical area would this student naturally need to explore next?"

## QUALITY VALIDATION CHECKLIST

Before finalizing each topic, verify:

### Chronological Logic
- [ ] Could this topic realistically happen AFTER the previous mathematical topic?
- [ ] Are there clear mathematical connections to previous topics?
- [ ] Does the content logically flow from previous mathematical experiences?

### User Profile Compatibility  
- [ ] Does this align with the user's mathematical skill level and background?
- [ ] Is this mathematically realistic given the user's education level?
- [ ] Is this feasible given the user's academic schedule and prerequisites?

### Conversation Generation Potential
- [ ] Does this topic contain 15+ major mathematical decision points?
- [ ] Are the subtopics broad enough for extensive mathematical discussion?
- [ ] Would this topic naturally generate 2000+ authentic mathematical questions?
- [ ] Are there multiple mathematical perspectives and approaches involved?

### Mathematical Coherence
- [ ] Does this topic build upon mathematical growth from previous topics?
- [ ] Are there clear references/connections to earlier mathematical experiences?
- [ ] Does this topic push mathematical development forward?
- [ ] Is the skill/knowledge progression mathematically realistic?

**MATHEMATICAL DIVERSITY CHECKLIST:**
Before finalizing each topic:
- [ ] Is this a completely different mathematical category from previous topics?
- [ ] Does it address a new mathematical domain?
- [ ] Is it influenced by, but not a continuation of, the previous topic?
- [ ] Would this naturally be the next mathematical priority after the previous experience?
- [ ] Does it show mathematical growth applied to a DIFFERENT mathematical area?

## EXAMPLE PROGRESSION LOGIC

Each topic should answer: "Given what was learned/mastered in the previous topic, what DIFFERENT mathematical area would this student naturally need to explore next?"

## FORBIDDEN ELEMENTS
- **Non-sequential topics**: Topics that could happen in any order
- **Profile contradictions**: Topics that contradict user's established mathematical level
- **Unrealistic jumps**: Major mathematical changes without proper foundation/prerequisites
- **Narrow topics**: Topics that couldn't generate extensive mathematical conversation
- **Template responses**: Generic topics that don't reflect unique student circumstances

## EXECUTION NOTES
- Generate all 10 topics in a single coherent response
- Ensure seamless mathematical narrative flow from Topic 0 through Topic 9
- Prioritize mathematical realism and skill consistency over dramatic storylines
- Focus on authentic mathematical progressions that real students experience
- End output immediately after closing the JSON structure

**CRITICAL**: Output your response in JSON format only. Do not include any explanatory text, markdown formatting, or additional commentary. Provide only the raw JSON object.

Generate the complete topic cluster now.
"""

ten_m_generate_similar_topics = """
You are creating a CHRONOLOGICAL SUBTOPIC FRAMEWORK that breaks down a main topic into 10 diverse, non-repetitive phases with strict timeline boundaries.

## INPUT DATA
- **MAIN TOPIC:** <main_topic>
- **MAIN THEME:** <main_theme>
- **MAIN SUBTOPICS:** <main_subtopics>
- **USER PROFILE:** <user_profile>
- **TOTAL TIMELINE:** <total_timeline>

## TIMELINE EXTRACTION (MANDATORY FIRST)

1. **Extract Core Action**: 
   - Duration from main topic (e.g., "x-day doing Y" = x days)
   - Action type (trip/project/course/challenge/etc.)
   - Total timeline span in months

2. **Calculate Key Dates**:
   - MAIN_ACTION_START: When core action begins
   - MAIN_ACTION_END: When core action ends
   - Allocate realistic prep/integration time around core action

## SUBTOPIC GENERATION RULES

### Phase Distribution (10 Topics)
- **Topics 0-2**: PREPARATION (before action starts)
- **Topics 3-6**: CORE ACTION (during main action period)  
- **Topics 7-9**: INTEGRATION (after action ends)

### MANDATORY DIVERSITY REQUIREMENTS

**EACH SUBTOPIC MUST BE UNIQUE:**
- No recycling of themes between subtopics
- Each explores DIFFERENT aspects/challenges
- Progressive complexity within each phase
- Distinct focus areas that don't overlap

**PREPARATION DIVERSITY (Topics 0-2):**
- Topic 0: Discovery/Research/Initial Planning
- Topic 1: Decision-Making/Resource Gathering/Skill Building
- Topic 2: Final Preparations/Confirmations/Pre-Launch

**CORE ACTION DIVERSITY (Topics 3-6):**
- Topic 3: Launch/Beginning/Initial Experiences
- Topic 4: Early Challenges/Adaptations/Progress
- Topic 5: Peak Performance/Deep Engagement/Mastery
- Topic 6: Final Push/Completion/Transition

**INTEGRATION DIVERSITY (Topics 7-9):**
- Topic 7: Immediate Reflection/Initial Processing
- Topic 8: Application/Transformation/Sharing
- Topic 9: Long-term Impact/Future Planning/Legacy

### Required Structure Per Subtopic
```json
{
  "id": [0-9],
  "category": "[Phase name]",
  "title": "[Unique descriptive title - NO REPETITION]",
  "theme": "[Distinct challenge/opportunity - MUST BE DIFFERENT]",
  "subtopics": ["10 DIVERSE sub-elements - NO OVERLAP with other topics"],
  "timeline": "[Date range]",
  "phase_type": "[preparation/core_action/integration]",
  "action_dates": {
    "main_action_type": "[type]",
    "main_action_starts": "[date]",
    "main_action_ends": "[date]",
    "main_action_duration": "[duration]",
    "current_phase_relation": "[before/during/after]"
  },
  "phase_boundaries": {
    "can_mention": ["Allowed activities"],
    "cannot_mention": ["Forbidden activities"],
    "tense_for_main_action": "[future/present/past]"
  },
  "key_milestones": ["3 unique milestones"],
  "future_references": ["Setup for continuity"],
  "continuity_hooks": ["Links to next topic"]
}
DIVERSITY ENFORCEMENT CHECKLIST
Before creating each subtopic:

 Is this theme/focus completely different from all others?
 Are the 10 sub-elements unique to this topic?
 Does it explore new aspects not covered elsewhere?
 Will it generate different types of conversations?
 Does it advance the narrative without repetition?

MAIN SUBTOPIC DISTRIBUTION
Spread the provided main_subtopics across topics you generate strategically:

Show evolution: basic → intermediate → advanced → mastery
Different angles in each phase (planning vs doing vs reflecting)

OUTPUT FORMAT
Generate ONLY this JSON structure:
json{
  "main_topic": "[Input]",
  "main_theme": "[Input]",
  "main_subtopics": ["Input array"],
  "total_timeline": "[Input]",
  "master_timeline": {
    "timeline_start": "[Date]",
    "timeline_end": "[Date]",
    "main_action_starts": "[Date]",
    "main_action_ends": "[Date]",
    "main_action_duration": "[Duration]",
    "preparation_phase": {
      "start": "[Date]",
      "end": "[Date]",
      "topics": [0, 1, 2]
    },
    "core_action_phase": {
      "start": "[Date]",
      "end": "[Date]",
      "duration": "[Duration]",
      "topics": [3, 4, 5, 6]
    },
    "integration_phase": {
      "start": "[Date]",
      "end": "[Date]",
      "topics": [7, 8, 9]
    }
  },
  "subtopics": [/* 10 UNIQUE subtopic objects */]
}
CRITICAL:

Each subtopic explores DIFFERENT aspects
NO thematic repetition across topics
Progressive narrative arc
Diverse conversation opportunities

Output ONLY the JSON. No explanations
"""
ten_m_generate_similar_topics_five_plan = """
You are creating a CHRONOLOGICAL SUBTOPIC FRAMEWORK that breaks down a main topic into 5 diverse, non-repetitive phases with strict timeline boundaries.

## INPUT DATA
- **MAIN TOPIC:** <main_topic>
- **MAIN THEME:** <main_theme>
- **MAIN SUBTOPICS:** <main_subtopics>
- **USER PROFILE:** <user_profile>
- **TOTAL TIMELINE:** <total_timeline>

## TIMELINE EXTRACTION (MANDATORY FIRST)

1. **Extract Core Action**: 
   - Duration from main topic (e.g., "x-day doing Y" = x days)
   - Action type (trip/project/course/challenge/etc.)
   - Total timeline span in months

2. **Calculate Key Dates**:
   - MAIN_ACTION_START: When core action begins
   - MAIN_ACTION_END: When core action ends
   - Allocate realistic prep/integration time around core action

## SUBTOPIC GENERATION RULES

### Phase Distribution (5 Topics)
- **Topic 0**: PREPARATION (before action starts)
- **Topics 1-3**: CORE ACTION (during main action period)  
- **Topic 4**: INTEGRATION (after action ends)

### MANDATORY DIVERSITY REQUIREMENTS

**EACH SUBTOPIC MUST BE UNIQUE:**
- No recycling of themes between subtopics
- Each explores DIFFERENT aspects/challenges
- Progressive complexity within each phase
- Distinct focus areas that don't overlap

**PREPARATION DIVERSITY (Topic 0):**
- Topic 0: Discovery/Research/Planning/Decision-Making/Resource Gathering

**CORE ACTION DIVERSITY (Topics 1-3):**
- Topic 1: Launch/Beginning/Initial Experiences/Early Challenges
- Topic 2: Peak Performance/Deep Engagement/Adaptations/Progress
- Topic 3: Final Push/Mastery/Completion/Transition

**INTEGRATION DIVERSITY (Topic 4):**
- Topic 4: Reflection/Processing/Application/Transformation/Future Planning

### Required Structure Per Subtopic
```json
{
  "id": [0-4],
  "category": "[Phase name]",
  "title": "[Unique descriptive title - NO REPETITION]",
  "theme": "[Distinct challenge/opportunity - MUST BE DIFFERENT]",
  "subtopics": ["10 DIVERSE sub-elements - NO OVERLAP with other topics"],
  "timeline": "[Date range]",
  "phase_type": "[preparation/core_action/integration]",
  "action_dates": {
    "main_action_type": "[type]",
    "main_action_starts": "[date]",
    "main_action_ends": "[date]",
    "main_action_duration": "[duration]",
    "current_phase_relation": "[before/during/after]"
  },
  "phase_boundaries": {
    "can_mention": ["Allowed activities"],
    "cannot_mention": ["Forbidden activities"],
    "tense_for_main_action": "[future/present/past]"
  },
  "key_milestones": ["3 unique milestones"],
  "future_references": ["Setup for continuity"],
  "continuity_hooks": ["Links to next topic"]
}
```

## DIVERSITY ENFORCEMENT CHECKLIST
Before creating each subtopic:

- [ ] Is this theme/focus completely different from all others?
- [ ] Are the 10 sub-elements unique to this topic?
- [ ] Does it explore new aspects not covered elsewhere?
- [ ] Will it generate different types of conversations?
- [ ] Does it advance the narrative without repetition?

## MAIN SUBTOPIC DISTRIBUTION
Spread the provided main_subtopics across topics you generate strategically:

- Show evolution: basic → intermediate → advanced → mastery
- Different angles in each phase (planning vs doing vs reflecting)

## OUTPUT FORMAT
Generate ONLY this JSON structure:
```json
{
  "main_topic": "[Input]",
  "main_theme": "[Input]",
  "main_subtopics": ["Input array"],
  "total_timeline": "[Input]",
  "master_timeline": {
    "timeline_start": "[Date]",
    "timeline_end": "[Date]",
    "main_action_starts": "[Date]",
    "main_action_ends": "[Date]",
    "main_action_duration": "[Duration]",
    "preparation_phase": {
      "start": "[Date]",
      "end": "[Date]",
      "topics": [0]
    },
    "core_action_phase": {
      "start": "[Date]",
      "end": "[Date]",
      "duration": "[Duration]",
      "topics": [1, 2, 3]
    },
    "integration_phase": {
      "start": "[Date]",
      "end": "[Date]",
      "topics": [4]
    }
  },
  "subtopics": [/* 5 UNIQUE subtopic objects */]
}
```

## CRITICAL:

- Each subtopic explores DIFFERENT aspects
- NO thematic repetition across topics
- Progressive narrative arc
- Diverse conversation opportunities

Output ONLY the JSON. No explanations.
"""
ten_m_generate_similar_topics_five_plan_coding = """
You are creating a CHRONOLOGICAL SUBTOPIC FRAMEWORK that breaks down a main coding topic into 5 diverse, non-repetitive phases with strict timeline boundaries.

## INPUT DATA
- **MAIN TOPIC:** <main_topic>
- **MAIN THEME:** <main_theme>
- **MAIN SUBTOPICS:** <main_subtopics>
- **USER PROFILE:** <user_profile>
- **TOTAL TIMELINE:** <total_timeline>

## TIMELINE EXTRACTION (MANDATORY FIRST)

1. **Extract Core Technical Action**: 
   - Duration from main topic (e.g., "x-week project building Y" = x weeks)
   - Action type (development project/learning course/migration/refactoring/deployment/etc.)
   - Total timeline span in months

2. **Calculate Key Technical Dates**:
   - MAIN_DEVELOPMENT_START: When core development/learning begins
   - MAIN_DEVELOPMENT_END: When core development/learning ends
   - Allocate realistic planning/deployment time around core development

## SUBTOPIC GENERATION RULES

### Phase Distribution (5 Topics)
- **Topic 0**: PLANNING/PREPARATION (before development starts)
- **Topics 1-3**: CORE DEVELOPMENT (during main development period)  
- **Topic 4**: DEPLOYMENT/INTEGRATION (after development ends)

### MANDATORY DIVERSITY REQUIREMENTS

**EACH SUBTOPIC MUST BE UNIQUE:**
- No recycling of technical themes between subtopics
- Each explores DIFFERENT coding aspects/challenges
- Progressive technical complexity within each phase
- Distinct technical focus areas that don't overlap

**PLANNING/PREPARATION DIVERSITY (Topic 0):**
- Topic 0: Technical Research/Architecture Planning/Technology Selection/Requirements Gathering/Environment Setup

**CORE DEVELOPMENT DIVERSITY (Topics 1-3):**
- Topic 1: Initial Implementation/Foundation Building/Core Features/Early Technical Challenges
- Topic 2: Advanced Features/Performance Optimization/Complex Logic/Integration Challenges
- Topic 3: Final Implementation/Testing/Bug Fixes/Code Review/Optimization

**DEPLOYMENT/INTEGRATION DIVERSITY (Topic 4):**
- Topic 4: Deployment/Production Issues/Performance Monitoring/Documentation/Knowledge Transfer/Maintenance Planning

### Required Structure Per Subtopic
```json
{
  "id": [0-4],
  "category": "[Technical Phase name]",
  "title": "[Unique descriptive technical title - NO REPETITION]",
  "theme": "[Distinct technical challenge/opportunity - MUST BE DIFFERENT]",
  "subtopics": ["10 DIVERSE technical sub-elements - NO OVERLAP with other topics"],
  "timeline": "[Date range]",
  "phase_type": "[planning/core_development/deployment]",
  "development_dates": {
    "main_development_type": "[type]",
    "main_development_starts": "[date]",
    "main_development_ends": "[date]",
    "main_development_duration": "[duration]",
    "current_phase_relation": "[before/during/after]"
  },
  "phase_boundaries": {
    "can_mention": ["Allowed technical activities"],
    "cannot_mention": ["Forbidden technical activities"],
    "tense_for_main_development": "[future/present/past]"
  },
  "key_technical_milestones": ["3 unique technical milestones"],
  "future_technical_references": ["Setup for technical continuity"],
  "technical_continuity_hooks": ["Links to next technical topic"]
}
```

## CODING DOMAIN FOCUS AREAS

Each subtopic should focus on different aspects of software development:

**PLANNING/PREPARATION ASPECTS:**
- Requirements analysis and technical specifications
- Architecture design and system planning
- Technology stack selection and evaluation
- Development environment setup
- Team coordination and project planning

**CORE DEVELOPMENT ASPECTS:**
- Feature implementation and coding
- Algorithm design and optimization
- Database design and integration
- API development and testing
- Code quality and refactoring
- Performance optimization
- Security implementation
- Third-party integrations

**DEPLOYMENT/INTEGRATION ASPECTS:**
- Deployment pipeline setup
- Production environment configuration
- Performance monitoring and analytics
- Bug fixes and hotfixes
- Documentation and knowledge transfer
- Maintenance and support planning

## DIVERSITY ENFORCEMENT CHECKLIST
Before creating each subtopic:

- [ ] Is this technical theme/focus completely different from all others?
- [ ] Are the 10 technical sub-elements unique to this topic?
- [ ] Does it explore new coding aspects not covered elsewhere?
- [ ] Will it generate different types of technical conversations?
- [ ] Does it advance the technical narrative without repetition?

## MAIN SUBTOPIC DISTRIBUTION
Spread the provided main_subtopics across topics you generate strategically:

- Show technical evolution: basic implementation → intermediate features → advanced optimization → production deployment
- Different technical angles in each phase (planning vs coding vs deploying)

## OUTPUT FORMAT
Generate ONLY this JSON structure:
```json
{
  "main_topic": "[Input]",
  "main_theme": "[Input]",
  "main_subtopics": ["Input array"],
  "total_timeline": "[Input]",
  "master_timeline": {
    "timeline_start": "[Date]",
    "timeline_end": "[Date]",
    "main_development_starts": "[Date]",
    "main_development_ends": "[Date]",
    "main_development_duration": "[Duration]",
    "planning_phase": {
      "start": "[Date]",
      "end": "[Date]",
      "topics": [0]
    },
    "core_development_phase": {
      "start": "[Date]",
      "end": "[Date]",
      "duration": "[Duration]",
      "topics": [1, 2, 3]
    },
    "deployment_phase": {
      "start": "[Date]",
      "end": "[Date]",
      "topics": [4]
    }
  },
  "subtopics": [/* 5 UNIQUE technical subtopic objects */]
}
```

## CRITICAL:

- Each subtopic explores DIFFERENT technical aspects
- NO thematic repetition across topics
- Progressive technical narrative arc
- Diverse coding conversation opportunities

Output ONLY the JSON. No explanations.
"""
ten_m_generate_similar_topics_ten_plan_coding = """
You are creating a CHRONOLOGICAL SUBTOPIC FRAMEWORK that breaks down a main coding topic into 10 diverse, non-repetitive phases with strict timeline boundaries.

## INPUT DATA
- **MAIN TOPIC:** <main_topic>
- **MAIN THEME:** <main_theme>
- **MAIN SUBTOPICS:** <main_subtopics>
- **USER PROFILE:** <user_profile>
- **TOTAL TIMELINE:** <total_timeline>

## TIMELINE EXTRACTION (MANDATORY FIRST)

1. **Extract Core Technical Action**: 
   - Duration from main topic (e.g., "x-week project building Y" = x weeks)
   - Action type (development project/learning course/migration/refactoring/deployment/etc.)
   - Total timeline span in months

2. **Calculate Key Technical Dates**:
   - MAIN_DEVELOPMENT_START: When core development/learning begins
   - MAIN_DEVELOPMENT_END: When core development/learning ends
   - Allocate realistic planning/deployment time around core development

## SUBTOPIC GENERATION RULES

### Phase Distribution (10 Topics)
- **Topics 0-1**: PLANNING/PREPARATION (before development starts)
- **Topics 2-7**: CORE DEVELOPMENT (during main development period)  
- **Topics 8-9**: DEPLOYMENT/INTEGRATION (after development ends)

### MANDATORY DIVERSITY REQUIREMENTS

**EACH SUBTOPIC MUST BE UNIQUE:**
- No recycling of technical themes between subtopics
- Each explores DIFFERENT coding aspects/challenges
- Progressive technical complexity within each phase
- Distinct technical focus areas that don't overlap

**PLANNING/PREPARATION DIVERSITY (Topics 0-1):**
- Topic 0: Technical Research/Requirements Analysis/Feasibility Study
- Topic 1: Architecture Planning/Technology Selection/Environment Setup/Team Formation

**CORE DEVELOPMENT DIVERSITY (Topics 2-7):**
- Topic 2: Foundation Building/Initial Setup/Basic Infrastructure/Core Architecture
- Topic 3: Early Feature Implementation/Basic Functionality/Initial Prototypes
- Topic 4: Core Feature Development/Primary Logic Implementation/Main Algorithms
- Topic 5: Advanced Features/Complex Integrations/Secondary Systems
- Topic 6: Performance Optimization/Scalability Improvements/Code Refactoring
- Topic 7: Testing Suite/Quality Assurance/Bug Fixes/Final Polish

**DEPLOYMENT/INTEGRATION DIVERSITY (Topics 8-9):**
- Topic 8: Deployment Preparation/CI/CD Setup/Production Configuration
- Topic 9: Production Monitoring/Documentation/Knowledge Transfer/Maintenance Planning

### Required Structure Per Subtopic
```json
{
  "id": [0-9],
  "category": "[Technical Phase name]",
  "title": "[Unique descriptive technical title - NO REPETITION]",
  "theme": "[Distinct technical challenge/opportunity - MUST BE DIFFERENT]",
  "subtopics": ["10 DIVERSE technical sub-elements - NO OVERLAP with other topics"],
  "timeline": "[Date range]",
  "phase_type": "[planning/core_development/deployment]",
  "development_dates": {
    "main_development_type": "[type]",
    "main_development_starts": "[date]",
    "main_development_ends": "[date]",
    "main_development_duration": "[duration]",
    "current_phase_relation": "[before/during/after]"
  },
  "phase_boundaries": {
    "can_mention": ["Allowed technical activities"],
    "cannot_mention": ["Forbidden technical activities"],
    "tense_for_main_development": "[future/present/past]"
  },
  "key_technical_milestones": ["3 unique technical milestones"],
  "future_technical_references": ["Setup for technical continuity"],
  "technical_continuity_hooks": ["Links to next technical topic"]
}
```

## CODING DOMAIN FOCUS AREAS

Each subtopic should focus on different aspects of software development:

**PLANNING/PREPARATION ASPECTS (Topics 0-1):**
- Requirements analysis and technical specifications
- Stakeholder interviews and use case definition
- Architecture design and system planning
- Technology stack selection and evaluation
- Development environment setup
- Team coordination and project planning
- Risk assessment and mitigation strategies
- Resource allocation and timeline planning

**CORE DEVELOPMENT ASPECTS (Topics 2-7):**
- Foundation and infrastructure setup
- Database schema design and implementation
- Core feature implementation and coding
- Algorithm design and optimization
- API development and versioning
- Frontend/backend integration
- Third-party service integrations
- Security implementation and hardening
- Performance profiling and optimization
- Code quality and refactoring cycles
- Automated testing implementation
- Cross-platform compatibility
- Accessibility features
- Internationalization and localization

**DEPLOYMENT/INTEGRATION ASPECTS (Topics 8-9):**
- Deployment pipeline setup and automation
- Production environment configuration
- Load balancing and scaling strategies
- Performance monitoring and analytics
- Security audits and penetration testing
- Bug fixes and hotfixes
- Documentation and API reference
- Knowledge transfer and training
- Maintenance procedures and runbooks
- Support system establishment

## DIVERSITY ENFORCEMENT CHECKLIST
Before creating each subtopic:

- [ ] Is this technical theme/focus completely different from all others?
- [ ] Are the 10 technical sub-elements unique to this topic?
- [ ] Does it explore new coding aspects not covered elsewhere?
- [ ] Will it generate different types of technical conversations?
- [ ] Does it advance the technical narrative without repetition?
- [ ] Does it add meaningful depth to the overall development journey?

## MAIN SUBTOPIC DISTRIBUTION
Spread the provided main_subtopics across topics you generate strategically:

- Show technical evolution: planning → foundation → basic features → advanced features → optimization → testing → deployment → monitoring
- Different technical angles in each phase (research vs design vs coding vs testing vs deploying)
- Ensure each topic has sufficient depth for 2000+ conversations

## OUTPUT FORMAT
Generate ONLY this JSON structure:
```json
{
  "main_topic": "[Input]",
  "main_theme": "[Input]",
  "main_subtopics": ["Input array"],
  "total_timeline": "[Input]",
  "master_timeline": {
    "timeline_start": "[Date]",
    "timeline_end": "[Date]",
    "main_development_starts": "[Date]",
    "main_development_ends": "[Date]",
    "main_development_duration": "[Duration]",
    "planning_phase": {
      "start": "[Date]",
      "end": "[Date]",
      "topics": [0, 1]
    },
    "core_development_phase": {
      "start": "[Date]",
      "end": "[Date]",
      "duration": "[Duration]",
      "topics": [2, 3, 4, 5, 6, 7]
    },
    "deployment_phase": {
      "start": "[Date]",
      "end": "[Date]",
      "topics": [8, 9]
    }
  },
  "subtopics": [/* 10 UNIQUE technical subtopic objects */]
}
```

## CRITICAL:

- Each subtopic explores DIFFERENT technical aspects
- NO thematic repetition across topics
- Progressive technical narrative arc
- Diverse coding conversation opportunities
- Granular breakdown allowing for deep technical discussions
- Natural progression through entire software development lifecycle

Output ONLY the JSON. No explanations.
"""
ten_m_generate_similar_topics_five_plan_math = """
You are creating a CHRONOLOGICAL SUBTOPIC FRAMEWORK that breaks down a main mathematical topic into 5 diverse, non-repetitive phases with strict timeline boundaries.

## INPUT DATA
- **MAIN TOPIC:** <main_topic>
- **MAIN THEME:** <main_theme>
- **MAIN SUBTOPICS:** <main_subtopics>
- **USER PROFILE:** <user_profile>
- **TOTAL TIMELINE:** <total_timeline>

## TIMELINE EXTRACTION (MANDATORY FIRST)

1. **Extract Core Mathematical Action**: 
   - Duration from main topic (e.g., "x-week studying Y" = x weeks)
   - Action type (course/research/competition/proof/project/etc.)
   - Total timeline span in months

2. **Calculate Key Mathematical Dates**:
   - MAIN_STUDY_START: When core mathematical learning begins
   - MAIN_STUDY_END: When core mathematical learning ends
   - Allocate realistic preparation/application time around core study

## SUBTOPIC GENERATION RULES

### Phase Distribution (5 Topics)
- **Topic 0**: PREPARATION/FOUNDATION (before main study starts)
- **Topics 1-3**: CORE LEARNING (during main study period)  
- **Topic 4**: APPLICATION/MASTERY (after main study ends)

### MANDATORY DIVERSITY REQUIREMENTS

**EACH SUBTOPIC MUST BE UNIQUE:**
- No recycling of mathematical themes between subtopics
- Each explores DIFFERENT mathematical aspects/challenges
- Progressive mathematical complexity within each phase
- Distinct mathematical focus areas that don't overlap

**PREPARATION/FOUNDATION DIVERSITY (Topic 0):**
- Topic 0: Prerequisites Review/Resource Selection/Study Planning/Foundational Concepts/Mathematical Background

**CORE LEARNING DIVERSITY (Topics 1-3):**
- Topic 1: Initial Concepts/Basic Theorems/Fundamental Techniques/Early Problem-Solving
- Topic 2: Advanced Applications/Complex Problems/Proof Techniques/Mathematical Connections
- Topic 3: Mastery/Integration/Advanced Topics/Synthesis/Evaluation

**APPLICATION/MASTERY DIVERSITY (Topic 4):**
- Topic 4: Real-World Applications/Research Extensions/Teaching Others/Advanced Projects/Future Mathematical Planning

### Required Structure Per Subtopic
```json
{
  "id": [0-4],
  "category": "[Mathematical Phase name]",
  "title": "[Unique descriptive mathematical title - NO REPETITION]",
  "theme": "[Distinct mathematical challenge/opportunity - MUST BE DIFFERENT]",
  "subtopics": ["10 DIVERSE mathematical sub-elements - NO OVERLAP with other topics"],
  "timeline": "[Date range]",
  "phase_type": "[preparation/core_learning/application]",
  "study_dates": {
    "main_study_type": "[type]",
    "main_study_starts": "[date]",
    "main_study_ends": "[date]",
    "main_study_duration": "[duration]",
    "current_phase_relation": "[before/during/after]"
  },
  "phase_boundaries": {
    "can_mention": ["Allowed mathematical activities"],
    "cannot_mention": ["Forbidden mathematical activities"],
    "tense_for_main_study": "[future/present/past]"
  },
  "key_mathematical_milestones": ["3 unique mathematical milestones"],
  "future_mathematical_references": ["Setup for mathematical continuity"],
  "mathematical_continuity_hooks": ["Links to next mathematical topic"]
}
```

## MATHEMATICAL DOMAIN FOCUS AREAS

Each subtopic should focus on different aspects of mathematical learning:

**PREPARATION/FOUNDATION ASPECTS:**
- Prerequisites review and knowledge gaps assessment
- Mathematical resource selection and study materials
- Foundational concept reinforcement
- Study strategy and time management planning
- Mathematical background research

**CORE LEARNING ASPECTS:**
- Theorem understanding and proof comprehension
- Problem-solving technique development
- Mathematical reasoning and logic building
- Concept application and practice
- Mathematical connections and patterns
- Advanced problem-solving strategies
- Mathematical communication and notation
- Integration of multiple mathematical concepts

**APPLICATION/MASTERY ASPECTS:**
- Real-world mathematical modeling
- Research project development
- Teaching and explaining mathematical concepts
- Advanced mathematical explorations
- Cross-disciplinary mathematical applications
- Mathematical software and computational tools

## DIVERSITY ENFORCEMENT CHECKLIST
Before creating each subtopic:

- [ ] Is this mathematical theme/focus completely different from all others?
- [ ] Are the 10 mathematical sub-elements unique to this topic?
- [ ] Does it explore new mathematical aspects not covered elsewhere?
- [ ] Will it generate different types of mathematical conversations?
- [ ] Does it advance the mathematical narrative without repetition?

## MAIN SUBTOPIC DISTRIBUTION
Spread the provided main_subtopics across topics you generate strategically:

- Show mathematical evolution: basic concepts → intermediate applications → advanced mastery → research extensions
- Different mathematical angles in each phase (learning vs applying vs teaching)

## OUTPUT FORMAT
Generate ONLY this JSON structure:
```json
{
  "main_topic": "[Input]",
  "main_theme": "[Input]",
  "main_subtopics": ["Input array"],
  "total_timeline": "[Input]",
  "master_timeline": {
    "timeline_start": "[Date]",
    "timeline_end": "[Date]",
    "main_study_starts": "[Date]",
    "main_study_ends": "[Date]",
    "main_study_duration": "[Duration]",
    "preparation_phase": {
      "start": "[Date]",
      "end": "[Date]",
      "topics": [0]
    },
    "core_learning_phase": {
      "start": "[Date]",
      "end": "[Date]",
      "duration": "[Duration]",
      "topics": [1, 2, 3]
    },
    "application_phase": {
      "start": "[Date]",
      "end": "[Date]",
      "topics": [4]
    }
  },
  "subtopics": [/* 5 UNIQUE mathematical subtopic objects */]
}
```

## CRITICAL:

- Each subtopic explores DIFFERENT mathematical aspects
- NO thematic repetition across topics
- Progressive mathematical narrative arc
- Diverse mathematical conversation opportunities

Output ONLY the JSON. No explanations.
"""
ten_m_generate_similar_topics_ten_plan_math = """
You are creating a CHRONOLOGICAL SUBTOPIC FRAMEWORK that breaks down a main mathematical topic into 10 diverse, non-repetitive phases with strict timeline boundaries.

## INPUT DATA
- **MAIN TOPIC:** <main_topic>
- **MAIN THEME:** <main_theme>
- **MAIN SUBTOPICS:** <main_subtopics>
- **USER PROFILE:** <user_profile>
- **TOTAL TIMELINE:** <total_timeline>

## TIMELINE EXTRACTION (MANDATORY FIRST)

1. **Extract Core Mathematical Action**: 
   - Duration from main topic (e.g., "x-week studying Y" = x weeks)
   - Action type (course/research/competition/proof/project/etc.)
   - Total timeline span in months

2. **Calculate Key Mathematical Dates**:
   - MAIN_STUDY_START: When core mathematical learning begins
   - MAIN_STUDY_END: When core mathematical learning ends
   - Allocate realistic preparation/application time around core study

## SUBTOPIC GENERATION RULES

### Phase Distribution (10 Topics)
- **Topics 0-1**: PREPARATION/FOUNDATION (before main study starts)
- **Topics 2-7**: CORE LEARNING (during main study period)  
- **Topics 8-9**: APPLICATION/MASTERY (after main study ends)

### MANDATORY DIVERSITY REQUIREMENTS

**EACH SUBTOPIC MUST BE UNIQUE:**
- No recycling of mathematical themes between subtopics
- Each explores DIFFERENT mathematical aspects/challenges
- Progressive mathematical complexity within each phase
- Distinct mathematical focus areas that don't overlap

**PREPARATION/FOUNDATION DIVERSITY (Topics 0-1):**
- Topic 0: Prerequisites Assessment/Knowledge Gap Analysis/Initial Mathematical Review
- Topic 1: Resource Selection/Study Planning/Foundation Building/Mathematical Toolkit Setup

**CORE LEARNING DIVERSITY (Topics 2-7):**
- Topic 2: Fundamental Concepts/Basic Definitions/Initial Theorems/Elementary Examples
- Topic 3: Core Theory Development/Essential Proofs/Primary Techniques
- Topic 4: Intermediate Applications/Problem-Solving Methods/Mathematical Connections
- Topic 5: Advanced Concepts/Complex Theorems/Sophisticated Techniques
- Topic 6: Deep Mathematical Analysis/Proof Construction/Abstract Extensions
- Topic 7: Synthesis and Integration/Comprehensive Understanding/Mastery Consolidation

**APPLICATION/MASTERY DIVERSITY (Topics 8-9):**
- Topic 8: Real-World Applications/Mathematical Modeling/Practical Implementation
- Topic 9: Research Extensions/Teaching Preparation/Future Mathematical Directions

### Required Structure Per Subtopic
```json
{
  "id": [0-9],
  "category": "[Mathematical Phase name]",
  "title": "[Unique descriptive mathematical title - NO REPETITION]",
  "theme": "[Distinct mathematical challenge/opportunity - MUST BE DIFFERENT]",
  "subtopics": ["10 DIVERSE mathematical sub-elements - NO OVERLAP with other topics"],
  "timeline": "[Date range]",
  "phase_type": "[preparation/core_learning/application]",
  "study_dates": {
    "main_study_type": "[type]",
    "main_study_starts": "[date]",
    "main_study_ends": "[date]",
    "main_study_duration": "[duration]",
    "current_phase_relation": "[before/during/after]"
  },
  "phase_boundaries": {
    "can_mention": ["Allowed mathematical activities"],
    "cannot_mention": ["Forbidden mathematical activities"],
    "tense_for_main_study": "[future/present/past]"
  },
  "key_mathematical_milestones": ["3 unique mathematical milestones"],
  "future_mathematical_references": ["Setup for mathematical continuity"],
  "mathematical_continuity_hooks": ["Links to next mathematical topic"]
}
```

## MATHEMATICAL DOMAIN FOCUS AREAS

Each subtopic should focus on different aspects of mathematical learning:

**PREPARATION/FOUNDATION ASPECTS (Topics 0-1):**
- Prerequisites review and knowledge gaps assessment
- Mathematical diagnostic testing and self-evaluation
- Resource selection and study materials curation
- Foundational concept reinforcement
- Study strategy and time management planning
- Mathematical background research
- Notation systems and mathematical language
- Problem-solving methodology introduction

**CORE LEARNING ASPECTS (Topics 2-7):**
- Definition comprehension and concept formation
- Axiom understanding and logical foundations
- Basic theorem understanding and proof comprehension
- Elementary problem-solving technique development
- Intermediate concept application and practice
- Mathematical reasoning and logic building
- Advanced proof techniques and strategies
- Complex problem analysis and solution methods
- Mathematical connections and pattern recognition
- Abstract thinking and generalization
- Rigorous proof construction
- Integration of multiple mathematical concepts
- Mathematical intuition development
- Computational methods and algorithms

**APPLICATION/MASTERY ASPECTS (Topics 8-9):**
- Real-world mathematical modeling
- Interdisciplinary applications
- Research project development
- Mathematical paper writing and presentation
- Teaching and explaining mathematical concepts
- Advanced mathematical explorations
- Cross-disciplinary mathematical applications
- Mathematical software and computational tools
- Professional mathematical communication
- Future research directions and open problems

## DIVERSITY ENFORCEMENT CHECKLIST
Before creating each subtopic:

- [ ] Is this mathematical theme/focus completely different from all others?
- [ ] Are the 10 mathematical sub-elements unique to this topic?
- [ ] Does it explore new mathematical aspects not covered elsewhere?
- [ ] Will it generate different types of mathematical conversations?
- [ ] Does it advance the mathematical narrative without repetition?
- [ ] Does it add meaningful depth to the overall learning journey?

## MAIN SUBTOPIC DISTRIBUTION
Spread the provided main_subtopics across topics you generate strategically:

- Show mathematical evolution: preparation → foundations → basic concepts → intermediate applications → advanced theory → synthesis → real-world applications → research extensions
- Different mathematical angles in each phase (learning vs applying vs teaching vs researching)
- Ensure each topic has sufficient depth for 2000+ conversations

## OUTPUT FORMAT
Generate ONLY this JSON structure:
```json
{
  "main_topic": "[Input]",
  "main_theme": "[Input]",
  "main_subtopics": ["Input array"],
  "total_timeline": "[Input]",
  "master_timeline": {
    "timeline_start": "[Date]",
    "timeline_end": "[Date]",
    "main_study_starts": "[Date]",
    "main_study_ends": "[Date]",
    "main_study_duration": "[Duration]",
    "preparation_phase": {
      "start": "[Date]",
      "end": "[Date]",
      "topics": [0, 1]
    },
    "core_learning_phase": {
      "start": "[Date]",
      "end": "[Date]",
      "duration": "[Duration]",
      "topics": [2, 3, 4, 5, 6, 7]
    },
    "application_phase": {
      "start": "[Date]",
      "end": "[Date]",
      "topics": [8, 9]
    }
  },
  "subtopics": [/* 10 UNIQUE mathematical subtopic objects */]
}
```

## CRITICAL:

- Each subtopic explores DIFFERENT mathematical aspects
- NO thematic repetition across topics
- Progressive mathematical narrative arc
- Diverse mathematical conversation opportunities
- Granular breakdown allowing for deep mathematical discussions
- Natural progression through entire mathematical learning lifecycle

Output ONLY the JSON. No explanations.
""" 

# ================================ plan generation ================================

ten_m_following_plan_generation_prompt = """
You are a long-form narrative planning specialist creating a COHERENT STORY PLANSET for natural conversational flow. Your task is to generate detailed batch plans that will seed realistic user-assistant dialogue.

## INPUT DATA
- **TOPIC:** <topic>
- **THEME:** <theme>
- **TIMELINE:** <timeline>
- **NUM_BATCHES:** <num_batches> batches
- **LABELS:** <provided_labels>
- **USER PROFILE:** <user_profile>
- **CORE RELATIONSHIPS:** <core_relationships>
- **NEW RELATIONSHIPS:** <new_relationships>
- **PREVIOUS PLAN:** <previous_plan>
- **INCLUDE_INTRODUCTION:** <YES/NO>

═══════════════ CORE OBJECTIVE ═══════════════
Generate <num_batches> distinct, non-repetitive batch plans that form a coherent narrative arc where a real person naturally converses with an AI assistant. Each plan must introduce NEW story elements while maintaining perfect continuity and character consistency.

═══════════════ NARRATIVE FRAMEWORK ═══════════════
This is NOT about generating random conversations - this is about creating a realistic, evolving story where:
- The user naturally seeks AI assistance across different life situations
- Each conversation builds upon previous interactions and established context
- The story progresses chronologically with authentic character development
- Relationships, situations, and circumstances evolve realistically over time
- The user's needs, challenges, and interests naturally expand and deepen

═══════════════ CRITICAL NARRATIVE PERSPECTIVE ═══════════════
**MANDATORY FIRST-PERSON PERSPECTIVE:**
- ALL content must be written from the USER's perspective (first-person)
- Use first-person perspective throughout but VARY sentence structures
- Natural narrative flow - avoid starting every bullet with "I"
- Mix active and passive voice while maintaining first-person perspective

═══════════════ CONTINUITY REQUIREMENTS ═══════════════
**CRITICAL**: If PREVIOUS PLAN is provided, you MUST:
- **Reference Previous Events**: Include specific callbacks to events, decisions, and outcomes from the previous plan
- **Maintain Core Character Consistency**: Keep USER PROFILE and CORE RELATIONSHIPS names and details exactly the same
- **Integrate New Relationships**: Naturally introduce NEW RELATIONSHIPS as appropriate to the current topic and timeline
- **Show Temporal Progression**: Demonstrate clear time advancement from the previous plan's timeline
- **Build Upon Previous Decisions**: Show consequences and follow-up actions from previous plan choices
- **Preserve Established Facts**: Keep all previously mentioned numbers, dates, locations, and core relationship details consistent
- **Continue Relationship Arcs**: Show evolution of existing relationships while adding new ones organically

═══════════════ STRICT TIMELINE ENFORCEMENT ═══════════════
**CRITICAL TIMELINE PARSING (MANDATORY FIRST STEP):**

Before generating ANY content, you MUST internally calculate timeline boundaries.

**STEP 1: Extract and Write Timeline Boundaries**
Parse TIMELINE to identify:
- **TIMELINE START**: [Extract exact date, e.g., "May 1, 2024"]
- **TIMELINE END**: [Extract exact date, e.g., "June 30, 2024"]
- **TOTAL DAYS**: [Calculate exact number of days]

**CALCULATE YOUR PARSED DATES:**
- Timeline Start Date: ________________
- Timeline End Date: ________________
- Total Days Available: ________________

**STEP 2: Create Batch Date Assignments**
Divide timeline into <num_batches> segments:
- Days per batch = TOTAL DAYS ÷ <num_batches>
- Batch 1 covers: Day 1 to Day [X]
- Batch 2 covers: Day [X+1] to Day [Y]
- Continue for all batches...

**CRITICAL**: Do these calculations INTERNALLY. Do NOT write them in your output.

**ABSOLUTE TIMELINE RULES:**
1. **EVERY date mentioned MUST be between START and END dates**
2. **NO future references beyond TIMELINE END** (no "next month" if timeline ends this month)
3. **NO past references before TIMELINE START**
4. **Temporal anchors MUST progress chronologically within boundaries**
5. **Final batch MUST conclude naturally before or on END DATE**

**TEMPORAL ANCHOR REQUIREMENTS:**
- First bullet of EACH batch MUST be temporal anchor
- Format: "• **Temporal Anchor:** [Month] [Day], [year], [event description]"
- Each temporal anchor date MUST be within that batch's assigned date range
- Dates must progress: Batch 2's date > Batch 1's date, etc.

**TIMELINE VIOLATION EXAMPLES (FORBIDDEN):**
Timeline is "May-June" but mentioning "July plans"
Timeline is "May-June" but saying "next month" in late June
Timeline starts May 1 but referencing "last month's meeting"
Any date outside the [START DATE] to [END DATE] range

**PRE-GENERATION CHECKLIST:**
Before writing each batch, verify:
- [ ] Have I identified my assigned date range for this batch?
- [ ] Is my temporal anchor within this range?
- [ ] Do all time references respect timeline boundaries?
- [ ] Have I avoided any dates outside [START, END]?
- [ ] Does the narrative flow naturally within constraints?

**ENFORCEMENT**: If your timeline is "May - June 2024", then:
- Batch 1 might use May 3
- Batch 5 might use May 28 
- Batch 10 might use June 25
- But NEVER July 1 or April 30

═══════════════ CRITICAL DETAIL REQUIREMENTS ═══════════════
**MANDATORY SPECIFIC DETAILS:**
Every batch MUST include numerous concrete, verifiable details that enable single-word or short factual answers:

**Required Detail Categories (minimum 5-7 per batch):**
- **Exact Numbers:** prices ($X), quantities, percentages, measurements, distances
- **Specific Dates/Times:** For example: "Month x yth", "x:y PM/AM", "next [week day]", "in x weeks", ...
- **Named Locations:** restaurants, stores, streets, buildings, parks, venues
- **Brand/Product Names:** specific items, services, companies, tools, software
- **Yes/No Situations:** decisions made, preferences stated, conflicts resolved
- **Event Outcomes:** what happened, who won/lost, what was chosen/rejected
- **Specific Preferences:** favorite foods, colors, activities, music, books
- **Quantifiable Results:** test scores, rankings, ratings, completion times

**Detail Distribution Rules:**
- Each bullet must contain AT LEAST one verifiable detail
- Avoid vague statements like "discussed options" - specify WHAT options
- Replace "had a meeting" with "had a x PM/AM meeting at [place name] on [street name]"
- Instead of "considering choices" use "choosing between X, Y, and Z"

═══════════════ STRUCTURE REQUIREMENTS ═══════════════
**1. OUTPUT FORMAT:**
- Generate exactly <num_batches> plans
- Format: `BATCH X PLAN` headers
- Each plan contains exactly 30 bullets
- Each bullet: "• **[LABEL CATEGORY]:[LABEL DESCRIPTION]:** [content]" (≤25 words)
- NOTE: Each label consists of category and description. Use both for each bullet point.
- Use only the provided LABELS - no custom categories
- **MANDATORY**: First bullet MUST be Temporal Anchor with the ONLY date reference in the batch

**2. STORY PROGRESSION ARCHITECTURE:**

**IF INCLUDE_INTRODUCTION = YES:**
**BATCH 1 (Story Foundation):**
- First bullet MUST be: "• **Personal Introduction:**"
- Establish initial context with SPECIFIC details (age, location, job title, salary range)
- Introduce all relationships with CONCRETE contexts (how long known, where met)
- Set up measurable goals, deadlines, and quantifiable challenges

**IF INCLUDE_INTRODUCTION = NO:**
**BATCH 1 (Continuation):**
- NO personal introduction bullets
- Begin directly with current topic-related content
- Reference established character details from PREVIOUS PLAN
- Show clear progression from previous plan's timeline and events

**BATCHES 2-<num_batches> (Story Evolution):**
- Reference user as "I/my/me" (never repeat the full name)
- Each batch advances the timeline chronologically
- Build upon ALL previously established elements
- Show MEASURABLE progression (promotions, relationship milestones, achievement metrics)

**3. RELATIONSHIP CONTINUITY SYSTEM:**

**Core vs. New Relationship Management:**
- **CORE RELATIONSHIPS** (partner, children, parents, siblings): Must remain consistent across all plans - same names, established details, ongoing dynamics
- **NEW RELATIONSHIPS** (friends, colleagues, acquaintances): Introduce naturally based on current topic and life phase
- **Relationship Integration**: New relationships should enhance the current topic while respecting established core relationship dynamics

**Relationship Evolution Mandate:**
Every relationship mention MUST include specific interaction details:

**Evolution Stages with Required Details:**
- **Introduction:** "Met [Name] at [specific place] on [date/time]"
- **Development:** "[Name] suggested [specific action] which resulted in [outcome]"
- **Deepening:** "[Name] revealed [specific information] during [specific event]"
- **Maturation:** "After [X months/years], [Name] and I [specific change]"

**Interaction Variety (rotate - never repeat within 3 batches):**
- Collaborative, Supportive, Conflictual, Social, Professional, Personal, Transactional, Serendipitous

**Character Consistency Rules:**
- **Core Characters**: Track specific preferences, established history, and ongoing relationship status
- **New Characters**: Introduce with clear context for how they fit into current topic/life phase
- Reference past specific events and their measurable consequences
- Include 2-3 relationship bullets per batch with concrete details (mix of core and new relationships)

═══════════════ CONFLICT & RESOLUTION TRACKING ═══════════════
**Mandatory Conflict Elements:**
Each batch must include at least 2-3 situations with:
- **Clear Stakes:** what's at risk (money amount, deadline, relationship status)
- **Binary Decisions:** chose A over B, accepted/rejected offer, yes/no to proposal
- **Measurable Outcomes:** gained/lost $X, saved X hours, improved by X%
- **Specific Disagreements:** who wanted what, what compromise was reached

**Conflict Types to Rotate:**
- Financial decisions with specific amounts
- Time management with exact deadlines
- Relationship boundaries with specific incidents
- Professional choices with concrete options
- Personal values with specific scenarios

═══════════════ ANTI-REPETITION VERIFICATION ═══════════════
**Before writing ANY bullet, verify:**
- Have I included at least one specific, verifiable detail?
- Can this generate a question with a one-word answer?
- Does this show MEASURABLE progression from previous mentions?
- Are the numbers, dates, names, and locations specific?
- Is this a NEW piece of information with NEW details?

**FORBIDDEN:**
- Vague time references ("recently", "soon") without specific dates
- General locations ("coffee shop", "restaurant") without names
- Unspecified amounts ("some money", "a few people")
- Abstract outcomes ("went well", "had issues") without details
- Repeated specific details (same restaurant, same activity, same problem)

═══════════════ CONTENT DISTRIBUTION STRATEGY ═══════════════
**Per Batch Requirements:**
- 2-3 bullets: Relationship developments with specific incidents (mix of core and new relationships)
- 2-4 bullets: Current situation with measurable metrics
- 1 bullet: Exact temporal anchor (specific date/time)
- 5-7 bullets: Events with verifiable outcomes
- 3-4 bullets: Decisions/preferences with specific choices
- Rest: Using remaining labels with concrete details

**Story Progression Patterns:**
- **Early Batches (1-3):** Establish baselines (current salary, relationship status, living situation)
- **Middle Batches:** Track changes from baselines with specific metrics
- **Later Batches:** Show cumulative results with before/after comparisons

═══════════════ NATURAL CONVERSATION FLOW ═══════════════
These plans generate conversations where users seek AI assistance for SPECIFIC situations:
- "Should I accept the $x job offer or stay at my $y position?"
- "The deadline is Month[] xth - can I finish all y modules by then?"
- "Sarah wants to meet at x at y PM but z suggested x1 at y1 PM"
- "My rent increased from $x to $y - should I move?"

═══════════════ QUALITY STANDARDS ═══════════════
**Specificity Checklist:**
- Every person has a full name and defined relationship
- Every event has a date, time, or specific temporal reference
- Every location has a name or address
- Every decision has concrete options with specific details
- Every outcome is measurable or verifiable

**Narrative Depth:**
- Include prices, percentages, distances, durations
- Show cause-and-effect with specific triggers and results
- Maintain factual consistency (don't change established numbers/dates)
- Reference past specific events by name and date

═══════════════ EXECUTION NOTES ═══════════════
- Prioritize concrete details over abstract descriptions
- Every bullet should enable at least 2-3 factual questions
- Include cultural, financial, and geographic specificity
- Ensure details are realistic and internally consistent
- If PREVIOUS PLAN provided, include 3-5 specific references to previous events per batch
- End immediately after `BATCH <num_batches> PLAN`

**FINAL TIMELINE REMINDER:**
- Parse TIMELINE boundaries FIRST
- EVERY date must fall within those boundaries
- NO exceptions to timeline limits
- Verify each batch respects the timeline

Output ONLY the batch plans. No explanations or additional text.

Begin generation now.
"""
ten_m_following_plan_generation_prompt_coding = """
You are a long-form technical narrative planning specialist creating a COHERENT CODING STORY PLANSET for natural developer-assistant conversational flow. Your task is to generate detailed batch plans that will seed realistic developer-AI dialogue about coding projects and technical challenges.

## INPUT DATA
- **TOPIC:** <topic>
- **THEME:** <theme>
- **TIMELINE:** <timeline>
- **NUM_BATCHES:** <num_batches> batches
- **LABELS:** <provided_labels>
- **USER PROFILE:** <user_profile>
- **CORE RELATIONSHIPS:** <core_relationships>
- **NEW RELATIONSHIPS:** <new_relationships>
- **PREVIOUS PLAN:** <previous_plan>
- **INCLUDE_INTRODUCTION:** <YES/NO>

═══════════════ CORE OBJECTIVE ═══════════════
Generate <num_batches> distinct, non-repetitive batch plans that form a coherent technical narrative arc where a real developer naturally converses with an AI assistant. Each plan must introduce NEW coding elements while maintaining perfect continuity and technical consistency.

═══════════════ TECHNICAL NARRATIVE FRAMEWORK ═══════════════
This is NOT about generating random coding conversations - this is about creating a realistic, evolving technical story where:
- The developer naturally seeks AI assistance across different coding situations
- Each conversation builds upon previous technical interactions and established codebase context
- The story progresses chronologically with authentic technical skill development
- Technical relationships, projects, and technologies evolve realistically over time
- The developer's technical needs, challenges, and expertise naturally expand and deepen

═══════════════ CRITICAL NARRATIVE PERSPECTIVE ═══════════════
**MANDATORY FIRST-PERSON DEVELOPER PERSPECTIVE:**
- ALL content must be written from the DEVELOPER's perspective (first-person)
- Use first-person perspective throughout but VARY sentence structures
- Natural technical narrative flow - avoid starting every bullet with "I"
- Mix active and passive voice while maintaining first-person developer perspective

═══════════════ CONTINUITY REQUIREMENTS ═══════════════
**CRITICAL**: If PREVIOUS PLAN is provided, you MUST:
- **Reference Previous Technical Events**: Include specific callbacks to deployments, bug fixes, feature implementations, and technical decisions from the previous plan
- **Maintain Core Technical Consistency**: Keep USER PROFILE and CORE RELATIONSHIPS names and technical details exactly the same
- **Integrate New Technical Relationships**: Naturally introduce NEW RELATIONSHIPS (new team members, clients, vendors) as appropriate to the current coding topic and timeline
- **Show Technical Progression**: Demonstrate clear advancement from the previous plan's technical timeline
- **Build Upon Previous Technical Decisions**: Show consequences and follow-up implementations from previous plan choices
- **Preserve Established Technical Facts**: Keep all previously mentioned version numbers, technologies, configurations, and core relationship details consistent
- **Continue Technical Relationship Arcs**: Show evolution of existing team dynamics while adding new technical collaborators organically

═══════════════ STRICT TIMELINE ENFORCEMENT ═══════════════
**CRITICAL TIMELINE PARSING (MANDATORY FIRST STEP):**

Before generating ANY content, you MUST internally calculate timeline boundaries.

**STEP 1: Extract and Write Timeline Boundaries**
Parse TIMELINE to identify:
- **TIMELINE START**: [Extract exact date, e.g., "May 1, 2024"]
- **TIMELINE END**: [Extract exact date, e.g., "June 30, 2024"]
- **TOTAL DAYS**: [Calculate exact number of days]

**CALCULATE YOUR PARSED DATES:**
- Timeline Start Date: ________________
- Timeline End Date: ________________
- Total Days Available: ________________

**STEP 2: Create Batch Date Assignments**
Divide timeline into <num_batches> segments:
- Days per batch = TOTAL DAYS ÷ <num_batches>
- Batch 1 covers: Day 1 to Day [X]
- Batch 2 covers: Day [X+1] to Day [Y]
- Continue for all batches...

**CRITICAL**: Do these calculations INTERNALLY. Do NOT write them in your output.

**ABSOLUTE TIMELINE RULES:**
1. **EVERY date mentioned MUST be between START and END dates**
2. **NO future references beyond TIMELINE END** (no "next sprint" if timeline ends this sprint)
3. **NO past references before TIMELINE START**
4. **Temporal anchors MUST progress chronologically within boundaries**
5. **Final batch MUST conclude naturally before or on END DATE**

**TEMPORAL ANCHOR REQUIREMENTS:**
- First bullet of EACH batch MUST be temporal anchor
- Format: "• **Temporal Anchor:** [Month] [Day], [year], [technical event description]"
- Each temporal anchor date MUST be within that batch's assigned date range
- Dates must progress: Batch 2's date > Batch 1's date, etc.

**TIMELINE VIOLATION EXAMPLES (FORBIDDEN):**
Timeline is "May-June" but mentioning "July deployment"
Timeline is "May-June" but saying "next quarter" in late June
Timeline starts May 1 but referencing "last month's code review"
Any date outside the [START DATE] to [END DATE] range

**PRE-GENERATION CHECKLIST:**
Before writing each batch, verify:
- [ ] Have I identified my assigned date range for this batch?
- [ ] Is my temporal anchor within this range?
- [ ] Do all time references respect timeline boundaries?
- [ ] Have I avoided any dates outside [START, END]?
- [ ] Does the technical narrative flow naturally within constraints?

**ENFORCEMENT**: If your timeline is "May - June 2024", then:
- Batch 1 might use May 3
- Batch 5 might use May 28 
- Batch 10 might use June 25
- But NEVER July 1 or April 30

═══════════════ CRITICAL TECHNICAL DETAIL REQUIREMENTS ═══════════════
**MANDATORY SPECIFIC TECHNICAL DETAILS:**
Every batch MUST include numerous concrete, verifiable technical details that enable single-word or short factual answers:

**Required Technical Detail Categories (minimum 5-7 per batch):**
- **Exact Numbers:** version numbers (v2.3.1), port numbers (3000), response times (250ms), file sizes (2.5MB), memory usage (512MB), CPU usage (45%), database records (50,000), concurrent users (1,200)
- **Specific Dates/Times:** deployment dates, sprint deadlines, meeting times, build timestamps, release schedules, maintenance windows
- **Named Technologies:** specific frameworks, libraries, tools, services (React 18.2, PostgreSQL 14, AWS Lambda, Docker 20.10, Node.js 18.16)
- **Error Messages:** exact error texts, status codes (404, 500), stack trace snippets, exception types, HTTP response codes
- **Yes/No Situations:** feature implemented, bug fixed, test passed, deployment successful, code review approved, merge completed
- **Performance Metrics:** load times (2.3s), query speeds (150ms), memory usage (1.2GB), API response times (200ms), uptime (99.9%), throughput (500 req/sec)
- **Configuration Details:** environment variables (NODE_ENV=production), API endpoints (/api/v1/users), database schemas, server configurations, network settings
- **Quantifiable Results:** test coverage (85%), uptime (99.9%), user count (1,000+), bug count (12 open), code quality score (8.5/10), build time (3m 45s)

**Technical Detail Distribution Rules:**
- Each bullet must contain AT LEAST one verifiable technical detail
- Avoid vague statements like "worked on feature" - specify WHAT feature and HOW
- Replace "had a bug" with "encountered 'undefined is not a function' error in UserAuth.js line 42"
- Instead of "improved performance" use "reduced API response time from 800ms to 200ms"
- Replace "deployed code" with "deployed v1.2.3 to production at 2:30 PM, serving 1,500 concurrent users"
- Instead of "fixed database issue" use "optimized PostgreSQL query reducing execution time from 2.1s to 300ms"

═══════════════ STRUCTURE REQUIREMENTS ═══════════════
**1. OUTPUT FORMAT:**
- Generate exactly <num_batches> plans
- Format: `BATCH X PLAN` headers
- Each plan contains exactly 30 bullets
- Each bullet: "• **[LABEL CATEGORY]:[LABEL DESCRIPTION]:** [content]" (≤25 words)
- NOTE: Each label consists of category and description. Use both for each bullet point.
- Use only the provided LABELS - no custom categories
- **MANDATORY**: First bullet MUST be Temporal Anchor with the ONLY date reference in the batch

**2. TECHNICAL STORY PROGRESSION ARCHITECTURE:**

**IF INCLUDE_INTRODUCTION = YES:**
**BATCH 1 (Technical Foundation):**
- First bullet MUST be: "• **Personal Introduction:**"
- Establish technical context with SPECIFIC details (years of experience, programming languages, current role, stack preferences)
- Introduce all technical relationships with CONCRETE contexts (team size, project duration, technologies used)
- Set up measurable technical goals, sprint deadlines, and quantifiable coding challenges

**IF INCLUDE_INTRODUCTION = NO:**
**BATCH 1 (Technical Continuation):**
- NO personal introduction bullets
- Begin directly with current coding topic-related content
- Reference established technical details from PREVIOUS PLAN
- Show clear technical progression from previous plan's timeline and implementations

**BATCHES 2-<num_batches> (Technical Evolution):**
- Reference developer as "I/my/me" (never repeat the full name)
- Each batch advances the technical timeline chronologically
- Build upon ALL previously established technical elements
- Show MEASURABLE technical progression (performance improvements, feature completions, skill advancements, system metrics)

**3. TECHNICAL RELATIONSHIP CONTINUITY SYSTEM:**

**Core vs. New Technical Relationship Management:**
- **CORE RELATIONSHIPS** (team lead, senior developers, product manager): Must remain consistent across all plans - same names, established technical dynamics, ongoing project contexts
- **NEW RELATIONSHIPS** (new team members, external developers, vendors, clients): Introduce naturally based on current technical topic and project phase
- **Technical Relationship Integration**: New relationships should enhance the current coding topic while respecting established core team dynamics

**Technical Relationship Evolution Mandate:**
Every technical relationship mention MUST include specific interaction details:

**Technical Evolution Stages with Required Details:**
- **Introduction:** "Met [Name] during [specific technical event] for [specific project/technology]"
- **Development:** "[Name] suggested [specific technical solution] which improved [specific metric] by [amount]"
- **Deepening:** "[Name] revealed [specific technical insight] during [specific code review/meeting]"
- **Maturation:** "After [X sprints/months], [Name] and I [specific technical collaboration change]"

**Technical Interaction Variety (rotate - never repeat within 3 batches):**
- Code Review, Pair Programming, Architecture Discussion, Bug Triage, Sprint Planning, Technical Mentoring, System Design, Deployment Coordination

**Technical Character Consistency Rules:**
- **Core Technical Characters**: Track specific technical preferences, established expertise areas, and ongoing project responsibilities
- **New Technical Characters**: Introduce with clear context for how they fit into current project/technical phase
- Reference past specific technical events and their measurable technical consequences
- Include 2-3 technical relationship bullets per batch with concrete technical details (mix of core and new relationships)

═══════════════ TECHNICAL CONFLICT & RESOLUTION TRACKING ═══════════════
**Mandatory Technical Conflict Elements:**
Each batch must include at least 2-3 technical situations with:
- **Clear Technical Stakes:** what's at risk (system downtime, performance degradation, deadline pressure, budget constraints)
- **Binary Technical Decisions:** chose framework A over B, accepted/rejected architecture proposal, implemented/rejected feature
- **Measurable Technical Outcomes:** reduced latency by Xms, improved test coverage by X%, fixed X critical bugs
- **Specific Technical Disagreements:** who preferred which solution, what technical compromise was reached

**Technical Conflict Types to Rotate:**
- Architecture decisions with specific technology choices
- Performance optimization with exact metrics
- Code quality standards with specific implementation details
- Deployment strategies with concrete configuration options
- Technical debt management with specific refactoring plans

═══════════════ ANTI-REPETITION VERIFICATION ═══════════════
**Before writing ANY bullet, verify:**
- Have I included at least one specific, verifiable technical detail?
- Can this generate a technical question with a one-word or short factual answer?
- Does this show MEASURABLE technical progression from previous mentions?
- Are the version numbers, configurations, metrics, and technologies specific?
- Is this a NEW piece of technical information with NEW technical details?

**FORBIDDEN:**
- Vague technical references ("recently deployed", "soon releasing") without specific dates
- General technologies ("database", "API") without specific names and versions
- Unspecified metrics ("improved performance", "faster queries") without exact numbers
- Abstract technical outcomes ("refactored code", "fixed issues") without specific details
- Repeated specific technical details (same bug, same optimization, same deployment)

═══════════════ TECHNICAL CONTENT DISTRIBUTION STRATEGY ═══════════════
**Per Batch Technical Requirements:**
- 2-3 bullets: Technical relationship developments with specific coding incidents (mix of core and new relationships)
- 2-4 bullets: Current technical situation with measurable coding metrics
- 1 bullet: Exact temporal anchor (specific date/time for technical event)
- 5-7 bullets: Technical events with verifiable coding outcomes
- 3-4 bullets: Technical decisions/preferences with specific technology choices
- Rest: Using remaining labels with concrete technical details

**Technical Story Progression Patterns:**
- **Early Batches (1-3):** Establish technical baselines (current tech stack, performance metrics, team structure)
- **Middle Batches:** Track technical changes from baselines with specific coding metrics
- **Later Batches:** Show cumulative technical results with before/after technical comparisons

═══════════════ NATURAL CODING CONVERSATION FLOW ═══════════════
These plans generate conversations where developers seek AI assistance for SPECIFIC technical situations:
- "Should I upgrade from React 17.0.2 to React 18.2.0 for this 50,000-user application?"
- "The deployment deadline is June 15th - can I complete all 8 API endpoints by then?"
- "Sarah suggests using PostgreSQL but Mike recommended MongoDB for this 1TB dataset"
- "My API response time increased from 200ms to 800ms after the latest update"

═══════════════ TECHNICAL QUALITY STANDARDS ═══════════════
**Technical Specificity Checklist:**
- Every technical person has a full name and defined technical role
- Every technical event has a date, time, or specific temporal reference
- Every technology has a name, version, and configuration details
- Every technical decision has concrete options with specific technical details
- Every technical outcome is measurable or verifiable with metrics

**Technical Narrative Depth:**
- Include version numbers, response times, memory usage, user counts
- Show technical cause-and-effect with specific triggers and measurable results
- Maintain technical factual consistency (don't change established versions/configurations)
- Reference past specific technical events by name, version, and date

═══════════════ EXECUTION NOTES ═══════════════
- Prioritize concrete technical details over abstract descriptions
- Every bullet should enable at least 2-3 factual technical questions
- Include technology-specific, performance-related, and configuration specificity
- Ensure technical details are realistic and internally consistent
- If PREVIOUS PLAN provided, include 3-5 specific references to previous technical events per batch
- End immediately after `BATCH <num_batches> PLAN`

**FINAL TIMELINE REMINDER:**
- Parse TIMELINE boundaries FIRST
- EVERY date must fall within those boundaries
- NO exceptions to timeline limits
- Verify each batch respects the timeline

Output ONLY the batch plans. No explanations or additional text.

Begin generation now.
"""
ten_m_following_plan_generation_prompt_math = """
You are a long-form mathematical narrative planning specialist creating a COHERENT MATH STORY PLANSET for natural student-assistant conversational flow. Your task is to generate detailed batch plans that will seed realistic student-AI dialogue about mathematical learning and problem-solving.

## INPUT DATA
- **TOPIC:** <topic>
- **THEME:** <theme>
- **TIMELINE:** <timeline>
- **NUM_BATCHES:** <num_batches> batches
- **LABELS:** <provided_labels>
- **USER_PROFILE:** <user_profile>
- **CORE_RELATIONSHIPS:** <core_relationships>
- **NEW_RELATIONSHIPS:** <new_relationships>
- **PREVIOUS_PLAN:** <previous_plan>
- **INCLUDE_INTRODUCTION:** <YES/NO>

═══════════════ CORE OBJECTIVE ═══════════════
Generate <num_batches> distinct, non-repetitive batch plans that form a coherent mathematical narrative arc where a real student naturally converses with an AI assistant. Each plan must introduce NEW mathematical elements while maintaining perfect continuity and mathematical consistency.

═══════════════ MATHEMATICAL NARRATIVE FRAMEWORK ═══════════════
This is NOT about generating random math conversations - this is about creating a realistic, evolving mathematical story where:
- The student naturally seeks AI assistance across different mathematical situations
- Each conversation builds upon previous mathematical interactions and established learning context
- The story progresses chronologically with authentic mathematical skill development
- Mathematical relationships, concepts, and understanding evolve realistically over time
- The student's mathematical needs, challenges, and expertise naturally expand and deepen

═══════════════ CRITICAL NARRATIVE PERSPECTIVE ═══════════════
**MANDATORY FIRST-PERSON STUDENT PERSPECTIVE:**
- ALL content must be written from the STUDENT's perspective (first-person)
- Use first-person perspective throughout but VARY sentence structures
- Natural mathematical narrative flow - avoid starting every bullet with "I"
- Mix active and passive voice while maintaining first-person student perspective

═══════════════ CONTINUITY REQUIREMENTS ═══════════════
**CRITICAL**: If PREVIOUS PLAN is provided, you MUST:
- **Reference Previous Mathematical Events**: Include specific callbacks to problem-solving sessions, concept mastery, and mathematical decisions from the previous plan
- **Maintain Core Mathematical Consistency**: Keep USER PROFILE and CORE RELATIONSHIPS names and mathematical details exactly the same
- **Integrate New Mathematical Relationships**: Naturally introduce NEW RELATIONSHIPS (new study partners, tutors, professors) as appropriate to the current mathematical topic and timeline
- **Show Mathematical Progression**: Demonstrate clear advancement from the previous plan's mathematical timeline
- **Build Upon Previous Mathematical Decisions**: Show consequences and follow-up learning from previous plan choices
- **Preserve Established Mathematical Facts**: Keep all previously mentioned scores, concepts, formulas, and core relationship details consistent
- **Continue Mathematical Relationship Arcs**: Show evolution of existing study dynamics while adding new mathematical collaborators organically

═══════════════ STRICT TIMELINE ENFORCEMENT ═══════════════
**CRITICAL TIMELINE PARSING (MANDATORY FIRST STEP):**

Before generating ANY content, you MUST internally calculate timeline boundaries.

**STEP 1: Extract and Write Timeline Boundaries**
Parse TIMELINE to identify:
- **TIMELINE START**: [Extract exact date, e.g., "May 1, 2024"]
- **TIMELINE END**: [Extract exact date, e.g., "June 30, 2024"]
- **TOTAL DAYS**: [Calculate exact number of days]

**CALCULATE YOUR PARSED DATES:**
- Timeline Start Date: ________________
- Timeline End Date: ________________
- Total Days Available: ________________

**STEP 2: Create Batch Date Assignments**
Divide timeline into <num_batches> segments:
- Days per batch = TOTAL DAYS ÷ <num_batches>
- Batch 1 covers: Day 1 to Day [X]
- Batch 2 covers: Day [X+1] to Day [Y]
- Continue for all batches...

**CRITICAL**: Do these calculations INTERNALLY. Do NOT write them in your output.

**ABSOLUTE TIMELINE RULES:**
1. **EVERY date mentioned MUST be between START and END dates**
2. **NO future references beyond TIMELINE END** (no "next semester" if timeline ends this semester)
3. **NO past references before TIMELINE START**
4. **Temporal anchors MUST progress chronologically within boundaries**
5. **Final batch MUST conclude naturally before or on END DATE**

**TEMPORAL ANCHOR REQUIREMENTS:**
- First bullet of EACH batch MUST be temporal anchor
- Format: "• **Temporal Anchor:** [Month] [Day], [year], [mathematical event description]"
- Each temporal anchor date MUST be within that batch's assigned date range
- Dates must progress: Batch 2's date > Batch 1's date, etc.

**TIMELINE VIOLATION EXAMPLES (FORBIDDEN):**
Timeline is "May-June" but mentioning "July exams"
Timeline is "May-June" but saying "next semester" in late June
Timeline starts May 1 but referencing "last month's quiz results"
Any date outside the [START DATE] to [END DATE] range

**PRE-GENERATION CHECKLIST:**
Before writing each batch, verify:
- [ ] Have I identified my assigned date range for this batch?
- [ ] Is my temporal anchor within this range?
- [ ] Do all time references respect timeline boundaries?
- [ ] Have I avoided any dates outside [START, END]?
- [ ] Does the mathematical narrative flow naturally within constraints?

**ENFORCEMENT**: If your timeline is "May - June 2024", then:
- Batch 1 might use May 3
- Batch 5 might use May 28 
- Batch 10 might use June 25
- But NEVER July 1 or April 30

═══════════════ CRITICAL MATHEMATICAL DETAIL REQUIREMENTS ═══════════════
**MANDATORY SPECIFIC MATHEMATICAL DETAILS:**
Every batch MUST include numerous concrete, verifiable mathematical details that enable single-word or short factual answers:

**Required Mathematical Detail Categories (minimum 8-10 per batch):**
- **Exact Numbers:** specific values (x = 3.14159), coefficients (2x² + 5x - 3), dimensions (5×7 matrix), constants (e ≈ 2.718), angles (45°, π/4 radians)
- **Specific Problems:** complete equations (x² - 4x + 3 = 0), definite integrals (∫(2x+1)dx from 0 to 5), derivatives (d/dx(sin x) = cos x), limits (lim[x→0] sin x/x = 1)
- **Named Concepts:** theorem names (Pythagorean Theorem, Fundamental Theorem of Calculus), method names (Gaussian elimination, L'Hôpital's rule), formulas (quadratic formula, distance formula)
- **Calculation Results:** exact answers (x = 4, y = -2), decimal results (π ≈ 3.14159), fractions (3/4, 7/12), percentages (85% correct)
- **Yes/No Situations:** problem solved correctly, method applicable, theorem satisfied, solution exists, function continuous, series convergent
- **Score/Grade Metrics:** test scores (85%), homework grades (18/20), quiz results (9/10 correct), assignment percentages (92%), participation scores (8/10)
- **Time/Duration:** study hours (3.5 hours), problem completion time (15 minutes), exam duration (2 hours), lecture time (50 minutes), office hours (30 minutes)
- **Mathematical Properties:** function characteristics (continuous, differentiable, injective), matrix properties (invertible, symmetric, orthogonal), set properties (closed, bounded, compact)
- **Course Information:** chapter numbers (Chapter 7), section references (7.3), page numbers (p. 142), problem numbers (#15, #23-27), textbook editions (9th edition)
- **Software/Tools:** calculator models (TI-84), software names (Mathematica, MATLAB, Desmos), programming languages (Python, R), specific functions (plot(), solve(), integrate())

**Mathematical Detail Distribution Rules:**
- Each bullet must contain AT LEAST one verifiable mathematical detail
- Avoid vague statements like "worked on problems" - specify WHICH problems and results
- Replace "studied math" with "completed 5 quadratic equation problems, solved 4 correctly in 45 minutes"
- Instead of "improved understanding" use "increased quiz score from 70% to 85% on derivatives"
- Replace "attended class" with "learned integration by parts in Calculus II, Section 8.2, solved problems #12-18"
- Instead of "struggled with concept" use "spent 2 hours on parametric equations, solved 3 of 8 practice problems correctly"

═══════════════ STRUCTURE REQUIREMENTS ═══════════════
**1. OUTPUT FORMAT:**
- Generate exactly <num_batches> plans
- Format: `BATCH X PLAN` headers
- Each plan contains exactly 30 bullets
- Each bullet: "• **[LABEL CATEGORY]:[LABEL DESCRIPTION]:** [content]" (≤25 words)
- NOTE: Each label consists of category and description. Use both for each bullet point.
- Use only the provided LABELS - no custom categories
- **MANDATORY**: First bullet MUST be Temporal Anchor with the ONLY date reference in the batch

**2. MATHEMATICAL STORY PROGRESSION ARCHITECTURE:**

**IF INCLUDE_INTRODUCTION = YES:**
**BATCH 1 (Mathematical Foundation):**
- First bullet MUST be: "• **Personal Introduction:**"
- Establish mathematical context with SPECIFIC details (years of study, current courses, GPA, mathematical strengths/weaknesses)
- Introduce all mathematical relationships with CONCRETE contexts (study group size, tutor sessions, professor office hours)
- Set up measurable mathematical goals, exam deadlines, and quantifiable learning challenges

**IF INCLUDE_INTRODUCTION = NO:**
**BATCH 1 (Mathematical Continuation):**
- NO personal introduction bullets
- Begin directly with current mathematical topic-related content
- Reference established mathematical details from PREVIOUS PLAN
- Show clear mathematical progression from previous plan's timeline and learning

**BATCHES 2-<num_batches> (Mathematical Evolution):**
- Reference student as "I/my/me" (never repeat the full name)
- Each batch advances the mathematical timeline chronologically
- Build upon ALL previously established mathematical elements
- Show MEASURABLE mathematical progression (grade improvements, concept mastery, skill advancements, problem-solving speed)

**3. MATHEMATICAL RELATIONSHIP CONTINUITY SYSTEM:**

**Core vs. New Mathematical Relationship Management:**
- **CORE RELATIONSHIPS** (professors, regular study partners, tutors): Must remain consistent across all plans - same names, established mathematical dynamics, ongoing learning contexts
- **NEW RELATIONSHIPS** (new classmates, guest lecturers, online tutors, study group members): Introduce naturally based on current mathematical topic and learning phase
- **Mathematical Relationship Integration**: New relationships should enhance the current mathematical topic while respecting established core learning dynamics

**Mathematical Relationship Evolution Mandate:**
Every mathematical relationship mention MUST include specific interaction details:

**Mathematical Evolution Stages with Required Details:**
- **Introduction:** "Met [Name] during [specific mathematical event] for [specific topic/course]"
- **Development:** "[Name] explained [specific mathematical concept] which improved my understanding of [specific problem type]"
- **Deepening:** "[Name] revealed [specific mathematical insight] during [specific study session/office hours]"
- **Maturation:** "After [X weeks/months], [Name] and I [specific mathematical collaboration change]"

**Mathematical Interaction Variety (rotate - never repeat within 3 batches):**
- Problem-Solving Session, Concept Explanation, Proof Review, Exam Preparation, Homework Collaboration, Mathematical Discussion, Tutoring Session, Study Group

**Mathematical Character Consistency Rules:**
- **Core Mathematical Characters**: Track specific mathematical preferences, established expertise areas, and ongoing learning responsibilities
- **New Mathematical Characters**: Introduce with clear context for how they fit into current mathematical topic/learning phase
- Reference past specific mathematical events and their measurable learning consequences
- Include 2-3 mathematical relationship bullets per batch with concrete mathematical details (mix of core and new relationships)

═══════════════ MATHEMATICAL CONFLICT & RESOLUTION TRACKING ═══════════════
**Mandatory Mathematical Conflict Elements:**
Each batch must include at least 2-3 mathematical situations with:
- **Clear Mathematical Stakes:** what's at risk (grade points, exam performance, course completion, prerequisite satisfaction)
- **Binary Mathematical Decisions:** chose method A over B, accepted/rejected mathematical approach, attempted/skipped difficult problem
- **Measurable Mathematical Outcomes:** improved score by X points, reduced errors by X%, completed X more problems correctly
- **Specific Mathematical Disagreements:** who preferred which solution method, what mathematical compromise was reached

**Mathematical Conflict Types to Rotate:**
- Solution method decisions with specific technique choices
- Time management with exact study schedules and exam deadlines
- Conceptual understanding with specific theorem applications
- Problem-solving strategies with concrete approach options
- Academic performance with specific grade targets and mathematical standards

═══════════════ ANTI-REPETITION VERIFICATION ═══════════════
**Before writing ANY bullet, verify:**
- Have I included at least one specific, verifiable mathematical detail?
- Can this generate a mathematical question with a one-word or short factual answer?
- Does this show MEASURABLE mathematical progression from previous mentions?
- Are the numbers, formulas, theorems, and scores specific?
- Is this a NEW piece of mathematical information with NEW mathematical details?

**FORBIDDEN:**
- Vague mathematical references ("recently studied", "soon taking exam") without specific dates
- General mathematical concepts ("algebra", "calculus") without specific topics and problems
- Unspecified mathematical results ("improved performance", "better understanding") without exact numbers
- Abstract mathematical outcomes ("grasped concept", "solved problems") without specific details
- Repeated specific mathematical details (same problem, same theorem, same score)

═══════════════ MATHEMATICAL CONTENT DISTRIBUTION STRATEGY ═══════════════
**Per Batch Mathematical Requirements:**
- 2-3 bullets: Mathematical relationship developments with specific learning incidents (mix of core and new relationships)
- 2-4 bullets: Current mathematical situation with measurable learning metrics
- 1 bullet: Exact temporal anchor (specific date/time for mathematical event)
- 5-7 bullets: Mathematical events with verifiable learning outcomes
- 3-4 bullets: Mathematical decisions/preferences with specific concept/method choices
- Rest: Using remaining labels with concrete mathematical details

**Mathematical Story Progression Patterns:**
- **Early Batches (1-3):** Establish mathematical baselines (current grades, concept understanding, problem-solving abilities)
- **Middle Batches:** Track mathematical changes from baselines with specific learning metrics
- **Later Batches:** Show cumulative mathematical results with before/after learning comparisons

═══════════════ NATURAL MATHEMATICAL CONVERSATION FLOW ═══════════════
These plans generate conversations where students seek AI assistance for SPECIFIC mathematical situations:
- "Should I use integration by parts or substitution for ∫xe^x dx?"
- "The calculus exam is May 15th - can I master all derivatives by then if I study 2 hours daily?"
- "Sarah suggests using matrices but Mike recommended systems of equations for this optimization problem"
- "My quiz average dropped from 85% to 78% after Chapter 7 - how can I improve?"

═══════════════ MATHEMATICAL QUALITY STANDARDS ═══════════════
**Mathematical Specificity Checklist:**
- Every mathematical person has a full name and defined mathematical role
- Every mathematical event has a date, time, or specific temporal reference
- Every mathematical concept has a name, formula, or specific notation
- Every mathematical decision has concrete options with specific mathematical details
- Every mathematical outcome is measurable or verifiable with scores/metrics

**Mathematical Narrative Depth:**
- Include specific grades, problem numbers, formula names, theorem references
- Show mathematical cause-and-effect with specific triggers and measurable results
- Maintain mathematical factual consistency (don't change established scores/concepts)
- Reference past specific mathematical events by name, score, and date

═══════════════ EXECUTION NOTES ═══════════════
- Prioritize concrete mathematical details over abstract descriptions
- Every bullet should enable at least 2-3 factual mathematical questions
- Include course-specific, grade-related, and concept-specific details
- Ensure mathematical details are realistic and internally consistent
- If PREVIOUS PLAN provided, include 3-5 specific references to previous mathematical events per batch
- End immediately after `BATCH <num_batches> PLAN`

**FINAL TIMELINE REMINDER:**
- Parse TIMELINE boundaries FIRST
- EVERY date must fall within those boundaries
- NO exceptions to timeline limits
- Verify each batch respects the timeline

Output ONLY the batch plans. No explanations or additional text.

Begin generation now.
"""

ten_m_similar_plan_generation_prompt = """
You are a precision narrative architect generating TEMPORALLY COHERENT BATCH PLANS that strictly adhere to subtopic boundaries and phase-specific timelines. Your task is to create detailed plans that maintain absolute timeline integrity and phase-appropriate content.

## CRITICAL INPUT DATA
- **MAIN_TOPIC:** <main_topic>
- **MAIN_THEME:** <main_theme>
- **TOPIC:** <topic>
- **THEME:** <theme>
- **TIMELINE:** <timeline>
- **NUM_BATCHES:** <num_batches> batches
- **LABELS:** <provided_labels>
- **USER_PROFILE:** <user_profile>
- **CORE_RELATIONSHIPS:** <core_relationships>
- **NEW_RELATIONSHIPS:** <new_relationships>
- **ALL_SUBTOPIC_PLANS:** <all_subtopic_plans>
- **PREVIOUS_PLANS_SUMMARY:** <previous_plans_summary>
- **PREVIOUS_PLAN:** <previous_plan>
- **CURRENT_SUBTOPIC_DATA:** <current_subtopic_data>
- **CURRENT_SUBTOPIC_ID:** <current_subtopic_id>
- **INCLUDE_INTRODUCTION:** <YES/NO>

═══════════════ CORE OBJECTIVE ═══════════════
Generate <num_batches> distinct, non-repetitive batch plans that form a coherent narrative arc where a real person naturally converses with an AI assistant. Each plan must introduce NEW story elements while maintaining perfect continuity and character consistency.

═══════════════ NARRATIVE FRAMEWORK ═══════════════
This is NOT about generating random conversations - this is about creating a realistic, evolving story where:
- The user naturally seeks AI assistance across different life situations
- Each conversation builds upon previous interactions and established context
- Relationships, situations, and circumstances evolve realistically over time
- The user's needs, challenges, and interests naturally expand and deepen

═══════════════ CRITICAL NARRATIVE PERSPECTIVE ═══════════════

**MANDATORY FIRST-PERSON PERSPECTIVE:**
- ALL content must be written from the USER's perspective (first-person)
- Use first-person perspective throughout but VARY sentence structures
- Natural narrative flow - avoid starting every bullet with "I"
- Mix active and passive voice while maintaining first-person perspective

═══════════════ CRITICAL DETAIL REQUIREMENTS ═══════════════

**MANDATORY SPECIFIC DETAILS:**
Every batch MUST include numerous concrete, verifiable details that enable single-word or short factual answers:

**Required Detail Categories (minimum 8-10 per batch):**
- **Exact Numbers:** prices ($X), quantities, percentages, measurements, distances
- **Specific Dates/Times:** For example: "Month x yth", "x:y PM/AM", "next [week day]", "in x weeks", ...
- **Named Locations:** restaurants, stores, streets, buildings, parks, venues
- **Brand/Product Names:** specific items, services, companies, tools, software
- **Yes/No Situations:** decisions made, preferences stated, conflicts resolved
- **Event Outcomes:** what happened, who won/lost, what was chosen/rejected
- **Specific Preferences:** favorite foods, colors, activities, music, books
- **Quantifiable Results:** test scores, rankings, ratings, completion times

**Detail Distribution Rules:**
- Each bullet must contain AT LEAST one verifiable detail
- Avoid vague statements like "discussed options" - specify WHAT options
- Replace "had a meeting" with "had a x PM/AM meeting at [place name] on [street name]"
- Instead of "considering choices" use "choosing between X, Y, and Z"

═══════════════ CRITICAL STRUCTURE REQUIREMENTS ═══════════════

**OUTPUT FORMAT:**
- Generate exactly <num_batches> plans
- Format: `BATCH X PLAN` headers (NO timeline headers)
- Each plan contains exactly 30 bullets
- Each bullet: "• **[LABEL CATEGORY]:[LABEL DESCRIPTION]:** [detailed content with specific facts]" (≤30 words)
- NOTE: Each label consists of category and description. Use both for each bullet point.
- Use only the provided LABELS in LABELS section - no custom categories
- **MANDATORY**: First bullet MUST be Temporal Anchor with the ONLY date reference in the batch

**TEMPORAL ANCHOR RULES:**
- **ONLY the first bullet** of each batch contains a date
- **NO OTHER BULLET** in the batch should include dates
- **Format**: "• **Temporal Anchor:** [Specific date], [rich contextual explanation of what's happening and why it's significant]"
- All other bullets refer to activities happening "around this time" without specific dates

═══════════════ CHARACTER AND RELATIONSHIP INTRODUCTION ═══════════════

**INTRODUCTION REQUIREMENTS:**

**IF INCLUDE_INTRODUCTION = YES:**
- Introduce CORE_RELATIONSHIPS with context about their roles and importance
- Establish the user's motivation and context for the main topic

**BATCH 1 (Story Foundation):**
- First bullet MUST be: "• **Personal Introduction:**"
- Establish initial context with SPECIFIC details (age, location, job title, salary range)
- Introduce all relationships with CONCRETE contexts (how long known, where met)
- Set up measurable goals, deadlines, and quantifiable challenges

**BATCHES 2-<num_batches> (Story Evolution):**
- Reference user as "I/my/me" (never repeat the full name)
- Each batch advances the timeline chronologically
- Build upon ALL previously established elements
- Show MEASURABLE progression (promotions, relationship milestones, achievement metrics)

**FOR ALL PLANS (regardless of INCLUDE_INTRODUCTION):**
- When ANY person from NEW_RELATIONSHIPS appears for the FIRST time:
  - Include their relationship to the user
  - Include their age
  - Provide brief context about who they are
  - Make their introduction feel natural within the narrative
- After first introduction, refer to them naturally without re-explaining

**RELATIONSHIP TRACKING:**
- Keep mental note of which relationships have been introduced
- First mention includes context; subsequent mentions assume familiarity
- Ensure consistency in how relationships are portrayed

**RELATIONSHIP CONTINUITY SYSTEM:**

**Relationship Evolution Mandate:**
Every relationship mention MUST include specific interaction details:

**Evolution Stages with Required Details:**
- **Introduction:** "Met [Name] at [specific place] on [date/time]"
- **Development:** "[Name] suggested [specific action] which resulted in [outcome]"
- **Deepening:** "[Name] revealed [specific information] during [specific event]"
- **Maturation:** "After [X months/years], [Name] and I [specific change]"

**Interaction Variety (rotate - never repeat within 3 batches):**
- Collaborative, Supportive, Conflictual, Social, Professional, Personal, Transactional, Serendipitous

**Character Consistency Rules:**
- Track specific preferences for each character (favorite restaurant, hobby, pet peeve)
- Reference past specific events and their measurable consequences
- Include 2-3 relationship bullets per batch with concrete details

═══════════════ CONTENT DISTRIBUTION STRATEGY ═══════════════

**Per Batch Requirements:**
- 2-3 bullets: Relationship developments with specific incidents
- 2-4 bullets: Current situation with measurable metrics
- 1 bullet: Exact temporal anchor (specific date/time)
- 5-7 bullets: Events with verifiable outcomes
- 3-4 bullets: Decisions/preferences with specific choices
- 1 bullet: **Preference Statement**: implicitly showing user preferences
- Rest: Using remaining labels in **LABELS** section with concrete details

**Story Progression Patterns:**
- **Early Batches (1-3):** Establish baselines
- **Middle Batches:** Track changes from baselines with specific metrics
- **Later Batches:** Show cumulative results with before/after comparisons

═══════════════ ANTI-REPETITION VERIFICATION ═══════════════

**Before writing ANY bullet, verify:**
- Have I included at least one specific, verifiable detail?
- Can this generate a question with a one-word answer?
- Does this show MEASURABLE progression from previous mentions?
- Are the numbers, dates, names, and locations specific?
- Is this a NEW piece of information with NEW details?

**FORBIDDEN:**
- Vague time references ("recently", "soon") without specific dates
- General locations ("coffee shop", "restaurant") without names
- Unspecified amounts ("some money", "a few people")
- Abstract outcomes ("went well", "had issues") without details
- Repeated specific details (same restaurant, same activity, same problem)

═══════════════ MANDATORY REPETITION PREVENTION ═══════════════

**CRITICAL REPETITION CHECK:**
Before writing ANY bullet point, verify against ALL previous batches:
- [ ] Have I mentioned this exact fact before?
- [ ] Is this a new development or just confirmation of previous content?
- [ ] Does this bullet advance the story or just repeat information?
- [ ] Can I add new details, numbers, or perspectives to make this unique?

**FORBIDDEN REPETITION PATTERNS:**
- Confirming/verifying previously established facts without new information
- Restating numerical values, dates, or decisions already mentioned
- Repeating relationship interactions without new developments
- Listing the same options, prices, or arrangements multiple times
- Re-explaining established processes or procedures
- Duplicating research findings or information sources
- Rehashing previous conversations or meetings without new outcomes

**REQUIRED PROGRESSION:**
Each bullet must either:
- Introduce completely new information
- Show progression/change from previous mentions  
- Add new details to previously mentioned elements
- Present new perspectives or complications
- Reveal new developments or discoveries
- Show evolution in understanding or approach
- Introduce new stakeholders or variables
- Present new challenges or opportunities

═══════════════ MANDATORY ACTION DATE EXTRACTION ═══════════════

**CRITICAL FIRST STEP - EXTRACT ACTION DATES:**

From CURRENT_SUBTOPIC_DATA, extract:
1. **action_dates.main_action_starts**: [EXACT DATE]
2. **action_dates.main_action_ends**: [EXACT DATE]
3. **action_dates.main_action_duration**: [DURATION]
4. **action_dates.current_phase_relation**: [before/during/after]
5. **phase_type**: [preparation/core_action/integration]

**WRITE THESE DATES HERE NOW:**
- Main Action Starts: ________________
- Main Action Ends: ________________
- Current Phase Type: ________________
- Current Phase Relation: ________________

═══════════════ ABSOLUTE TEMPORAL BOUNDARIES ═══════════════

**PHASE-SPECIFIC DATE BOUNDARIES:**

Based on the extracted action dates and current phase_type:

**IF phase_type = "preparation" (before main action):**
- **EARLIEST DATE**: First day of TIMELINE
- **LATEST DATE**: Day BEFORE main_action_starts
- **FORBIDDEN**: ANY date on or after main_action_starts
- **TENSE FOR MAIN ACTION**: FUTURE (planning/preparatory language)

**IF phase_type = "core_action" (during main action):**
- **EARLIEST DATE**: main_action_starts
- **LATEST DATE**: main_action_ends
- **FORBIDDEN**: ANY date before main_action_starts OR after main_action_ends
- **TENSE FOR MAIN ACTION**: PRESENT (active/ongoing language)

**IF phase_type = "integration" (after main action):**
- **EARLIEST DATE**: Day AFTER main_action_ends
- **LATEST DATE**: Last day of TIMELINE
- **FORBIDDEN**: ANY date before or during main action
- **TENSE FOR MAIN ACTION**: PAST (reflective/analytical language)

═══════════════ ABSOLUTE DATE BOUNDARIES ENFORCEMENT ═══════════════
**CRITICAL TIMELINE RULES:**


**EARLIEST ALLOWED DATE:** [START_DATE from TIMELINE]
**LATEST ALLOWED DATE:** [END_DATE from TIMELINE]


**ABSOLUTELY FORBIDDEN:**
- ANY date before START_DATE
- ANY date after END_DATE
- Creating dates outside the timeline range
- Extending the timeline beyond specified boundaries


**MANDATORY COMPLIANCE:**
- Every temporal anchor MUST use a date within [START_DATE, END_DATE]
- If timeline is 3 days, ALL content must fit within those 3 days
- No exceptions, no extensions, no violations

═══════════════ CONTENT BOUNDARY ENFORCEMENT ═══════════════

**PHASE-LOCKED CONTENT RULES:**

**PREPARATION PHASE - ALLOWED ONLY:**
- Research, planning, comparing, calculating, deciding
- Future-oriented language about the main action
- Preparation activities that happen BEFORE the main action starts
- Information gathering, skill building, resource acquisition

**PREPARATION PHASE - ABSOLUTELY FORBIDDEN:**
- Any present-tense description of actively doing the main action
- Completed executions or implementations
- Experiences that would only occur during the main action
- Post-action reflections or outcomes

**CORE ACTION PHASE - ALLOWED ONLY:**
- Real-time experiences, immediate decisions, active participation
- Present-tense descriptions of ongoing activities
- Activities happening DURING the main action period
- Direct execution of previously planned elements

**INTEGRATION PHASE - ALLOWED ONLY:**
- Reflection, analysis, lessons learned, future planning
- Past-tense descriptions of the completed main action
- Processing and applying experiences
- Knowledge transfer and outcome evaluation

═══════════════ CONTINUITY AND CONTEXT INTEGRATION ═══════════════

**PREVIOUS CONTEXT INTEGRATION:**

1. **Review Previous Plans Summary:**
   - Understand what has already been covered in earlier subtopics
   - Identify established facts, decisions, and relationships
   - Note any commitments or plans made for current timeframe

2. **Analyze Previous Plan (if exists):**
   - Continue narrative threads from immediately preceding plan
   - Reference decisions or discoveries made
   - Build upon established momentum
   - Avoid contradicting previous facts

3. **Introduction Handling:**
   - **IF INCLUDE_INTRODUCTION = YES**: First batch should introduce user's situation naturally
   - **IF INCLUDE_INTRODUCTION = NO**: Continue from previous narrative without re-introduction
   - Ensure smooth transition either way

**CONTINUITY REQUIREMENTS:**
- Reference previously established facts consistently
- Build upon prior decisions and learnings
- Maintain relationship continuity
- Honor previously mentioned dates/plans
- Show progression from previous subtopic's ending

═══════════════ TIMELINE DISTRIBUTION STRATEGY ═══════════════

**MANDATORY TIMELINE PARSING:**

1. **Parse Current Subtopic Timeline:**
   - START: [Extract from TIMELINE]
   - END: [Extract from TIMELINE]
   - DURATION: [Calculate in days/months]

2. **Calculate Timeline Distribution Method:**
   - Total Days = END - START + 1
   - IF Total Days >= <num_batches>:
     - Days per Batch = Total Days ÷ <num_batches>
     - Each batch gets unique date progression
   - IF Total Days < <num_batches>:
     - Use grouped date distribution to maintain coherence

3. **Create Batch Timeline Segments:**

   **FOR TIMELINES WITH SUFFICIENT DAYS (Total Days >= <num_batches>):**
   - Batch 1: Days 1-X of timeline
   - Batch 2: Days X+1-Y of timeline
   - Continue sequential progression for all batches

   **FOR SHORT TIMELINES (Total Days < <num_batches>):**
   - Calculate batches per day: <num_batches> ÷ Total Days
   - Group consecutive batches to same date
   - Distribute evenly across available dates
   - Example pattern for X available days:
     - First [batches_per_day] batches: Day 1
     - Next [batches_per_day] batches: Day 2
     - Continue until all batches assigned
   - Ensure each available day gets equal batch distribution
   - Maintain chronological order within same-day batches

4. **Batch Content Differentiation for Same-Day Batches:**
   - When multiple batches share same date, differentiate by:
     - Time of day progression (morning → afternoon → evening)
     - Activity focus areas within the day
     - Different stakeholder perspectives
     - Various aspects of same-day experiences
     - Progressive depth of engagement

5. **Verify Against Action Dates:**
   - EVERY date must respect phase boundaries
   - NO date can violate the action date rules above
   - Maintain logical progression even with repeated dates
   - Ensure content advancement despite date repetition

═══════════════ MANDATORY CONTENT BOUNDARY EXTRACTION ═══════════════

**CRITICAL STEP - EXTRACT CONTENT RESTRICTIONS:**

From CURRENT_SUBTOPIC_DATA, extract:
1. **phase_boundaries.can_mention**: [Allowed content types]
2. **phase_boundaries.cannot_mention**: [Forbidden content types] 
3. **phase_boundaries.tense_for_main_action**: [past/present/future]
4. **subtopics**: [Current subtopic's allowed activities]

**WRITE RESTRICTIONS HERE:**
- Can Mention: ________________
- Cannot Mention: ________________
- Required Tense: ________________
- Subtopic Activities: ________________

NOTE: WRITE INTERNALLY. DO NOT WRITE IT IN OUTPUT.

**ABSOLUTE CONTENT RULES:**
- ONLY generate content listed in can_mention
- NEVER generate content listed in cannot_mention  
- ONLY reference current subtopic activities
- Use ONLY the specified tense for main action

═══════════════ PRE-GENERATION VALIDATION GATES ═══════════════

**GATE 1: ACTION DATE VERIFICATION**
Before generating ANY content, confirm:
- [ ] I have extracted the exact main_action_starts date
- [ ] I have extracted the exact main_action_ends date
- [ ] I know whether I'm BEFORE, DURING, or AFTER these dates
- [ ] I understand what tense to use for the main action

**GATE 2: PHASE BOUNDARY CHECK**
For the current phase_type, verify:
- [ ] I know exactly which dates are allowed
- [ ] I know exactly which dates are forbidden
- [ ] I understand which activities are appropriate
- [ ] I know which phrases/words to avoid

**GATE 3: CONTENT BOUNDARY VERIFICATION**
From current subtopic data, confirm:
- [ ] I know what content is allowed vs forbidden
- [ ] I know the current subtopic's activity scope
- [ ] I understand the required tense for main action
- [ ] All content fits within current subtopic boundaries
- [ ] No content belongs to future subtopics

**CONTENT VERIFICATION FOR EACH BULLET:**
Before writing any bullet, verify:
- [ ] Is this activity in can_mention?
- [ ] Is this activity NOT in cannot_mention?  
- [ ] Does this belong to current subtopic activities?
- [ ] Am I using the correct tense?
- [ ] Does this belong to a future subtopic?

**GATE 4: TIMELINE BOUNDARY VERIFICATION**
Before generating ANY content, confirm:
- [ ] I have extracted START_DATE and END_DATE correctly
- [ ] I have calculated TOTAL_DAYS correctly
- [ ] I know my specific assigned date for this batch
- [ ] My assigned date is within the timeline boundaries


**GATE 5: DATE ASSIGNMENT VERIFICATION**
For my specific batch number, verify:
- [ ] I know whether to use sequential or grouped distribution
- [ ] I have calculated my exact assigned date
- [ ] My date does not exceed END_DATE
- [ ] My date follows the distribution formula


**Structure Compliance:**
- [ ] EXACTLY 30 bullets per batch
- [ ] Proper label format for every bullet
- [ ] Progressive complexity across batches

═══════════════ QUALITY STANDARDS ═══════════════

**Specificity Checklist:**
- Every person has a full name and defined relationship
- Every event has a date, time, or specific temporal reference
- Every location has a name or address
- Every decision has concrete options with specific details
- Every outcome is measurable or verifiable

**Narrative Depth:**
- Include prices, percentages, distances, durations
- Show cause-and-effect with specific triggers and results
- Maintain factual consistency (don't change established numbers/dates)
- Reference past specific events by name and date

═══════════════ FINAL EXECUTION PROTOCOL ═══════════════

1. **FIRST**: Extract and verify action dates
2. **SECOND**: Write all content in FIRST-PERSON
3. **THIRD**: Include date ONLY in temporal anchor
4. **FOURTH**: Pack MAXIMUM detail into every bullet
5. **FIFTH**: Ensure exactly 30 bullets with required composition
6. **SIXTH**: Validate all boundaries and progression

**REMEMBER:**
- Write as "I" not as third-person narrator
- Only ONE date per batch (in temporal anchor)
- MAXIMUM detail density in every bullet
- EXACTLY 30 bullets following composition requirements

Output ONLY the batch plans. No explanations or additional text.
End immediately after `BATCH <num_batches> PLAN`

Begin generation now.
"""

ten_m_similar_plan_generation_prompt_coding = """
You are a precision technical narrative architect generating TEMPORALLY COHERENT CODING BATCH PLANS that strictly adhere to subtopic boundaries and phase-specific timelines. Your task is to create detailed technical plans that maintain absolute timeline integrity and phase-appropriate coding content.

## CRITICAL INPUT DATA
- **MAIN_TOPIC:** <main_topic>
- **MAIN_THEME:** <main_theme>
- **TOPIC:** <topic>
- **THEME:** <theme>
- **TIMELINE:** <timeline>
- **NUM_BATCHES:** <num_batches> batches
- **LABELS:** <provided_labels>
- **USER_PROFILE:** <user_profile>
- **CORE_RELATIONSHIPS:** <core_relationships>
- **NEW_RELATIONSHIPS:** <new_relationships>
- **ALL_SUBTOPIC_PLANS:** <all_subtopic_plans>
- **PREVIOUS_PLANS_SUMMARY:** <previous_plans_summary>
- **PREVIOUS_PLAN:** <previous_plan>
- **CURRENT_SUBTOPIC_DATA:** <current_subtopic_data>
- **CURRENT_SUBTOPIC_ID:** <current_subtopic_id>
- **INCLUDE_INTRODUCTION:** <YES/NO>

═══════════════ CORE OBJECTIVE ═══════════════
Generate <num_batches> distinct, non-repetitive batch plans that form a coherent technical narrative arc where a real developer naturally converses with an AI assistant. Each plan must introduce NEW coding elements while maintaining perfect continuity and technical consistency.

═══════════════ TECHNICAL NARRATIVE FRAMEWORK ═══════════════
This is NOT about generating random coding conversations - this is about creating a realistic, evolving technical story where:
- The developer naturally seeks AI assistance across different coding situations
- Each conversation builds upon previous technical interactions and established codebase context
- Technical relationships, projects, and technologies evolve realistically over time
- The developer's technical needs, challenges, and expertise naturally expand and deepen

═══════════════ CRITICAL NARRATIVE PERSPECTIVE ═══════════════

**MANDATORY FIRST-PERSON DEVELOPER PERSPECTIVE:**
- ALL content must be written from the DEVELOPER's perspective (first-person)
- Use first-person perspective throughout but VARY sentence structures
- Natural technical narrative flow - avoid starting every bullet with "I"
- Mix active and passive voice while maintaining first-person developer perspective

═══════════════ CRITICAL TECHNICAL DETAIL REQUIREMENTS ═══════════════

**MANDATORY SPECIFIC TECHNICAL DETAILS:**
Every batch MUST include numerous concrete, verifiable technical details that enable single-word or short factual answers:

**Required Technical Detail Categories (minimum 8-10 per batch):**
- **Exact Numbers:** version numbers (v2.3.1), port numbers (3000), response times (250ms), file sizes (2.5MB), memory usage (512MB), CPU usage (45%), database records (50,000), concurrent users (1,200), build times (3m 15s)
- **Specific Dates/Times:** deployment dates, sprint deadlines, meeting times, build timestamps, release schedules, maintenance windows, code review deadlines
- **Named Technologies:** specific frameworks, libraries, tools, services (React 18.2, PostgreSQL 14, AWS Lambda, Docker 20.10, Node.js 18.16, Express 4.18.2)
- **Error Messages:** exact error texts, status codes (404, 500), stack trace snippets, exception types (TypeError, ReferenceError), HTTP response codes
- **Yes/No Situations:** feature implemented, bug fixed, test passed, deployment successful, code review approved, merge completed, CI/CD pipeline passed
- **Performance Metrics:** load times (2.3s), query speeds (150ms), memory usage (1.2GB), API response times (200ms), uptime (99.9%), throughput (500 req/sec), test execution time (45s)
- **Configuration Details:** environment variables (NODE_ENV=production), API endpoints (/api/v1/users), database schemas, server configurations (nginx.conf), network settings (port 8080)
- **Quantifiable Results:** test coverage (85%), uptime (99.9%), user count (1,000+), bug count (12 open), code quality score (8.5/10), build success rate (96%), security vulnerabilities (3 critical)

**Technical Detail Distribution Rules:**
- Each bullet must contain AT LEAST one verifiable technical detail
- Avoid vague statements like "worked on feature" - specify WHAT feature and HOW
- Replace "had a bug" with "encountered 'undefined is not a function' error in UserAuth.js line 42"
- Instead of "improved performance" use "reduced API response time from 800ms to 200ms"
- Replace "deployed code" with "deployed v1.2.3 to production at 2:30 PM, serving 1,500 concurrent users"
- Instead of "fixed database issue" use "optimized PostgreSQL query reducing execution time from 2.1s to 300ms"
- Replace "completed testing" with "achieved 92% test coverage with 147 unit tests passing in 2m 30s"

═══════════════ CRITICAL STRUCTURE REQUIREMENTS ═══════════════

**OUTPUT FORMAT:**
- Generate exactly <num_batches> plans
- Format: `BATCH X PLAN` headers (NO timeline headers)
- Each plan contains exactly 30 bullets
- Each bullet: "• **[LABEL CATEGORY]:[LABEL DESCRIPTION]:** [detailed technical content with specific facts]" (≤30 words)
- NOTE: Each label consists of category and description. Use both for each bullet point.
- Use only the provided LABELS - no custom categories
- **MANDATORY**: First bullet MUST be Temporal Anchor with the ONLY date reference in the batch

**TEMPORAL ANCHOR RULES:**
- **ONLY the first bullet** of each batch contains a date
- **NO OTHER BULLET** in the batch should include dates
- **Format**: "• **Temporal Anchor:** [Specific date], [rich technical contextual explanation of what's happening and why it's significant]"
- All other bullets refer to technical activities happening "around this time" without specific dates

═══════════════ TECHNICAL CHARACTER AND RELATIONSHIP INTRODUCTION ═══════════════

**TECHNICAL INTRODUCTION REQUIREMENTS:**

**IF INCLUDE_INTRODUCTION = YES:**
- Introduce CORE_RELATIONSHIPS with context about their technical roles and importance
- Establish the developer's motivation and context for the main coding topic

**BATCH 1 (Technical Foundation):**
- First bullet MUST be: "• **Personal Introduction:**"
- Establish technical context with SPECIFIC details (years of experience, programming languages, current role, tech stack, salary range)
- Introduce all technical relationships with CONCRETE contexts (team size, project duration, technologies used)
- Set up measurable technical goals, sprint deadlines, and quantifiable coding challenges

**BATCHES 2-<num_batches> (Technical Evolution):**
- Reference developer as "I/my/me" (never repeat the full name)
- Each batch advances the technical timeline chronologically
- Build upon ALL previously established technical elements
- Show MEASURABLE technical progression (performance improvements, feature completions, skill advancements)

**FOR ALL PLANS (regardless of INCLUDE_INTRODUCTION):**
- When ANY person from NEW_RELATIONSHIPS appears for the FIRST time:
  - Include their technical relationship to the user (senior dev, DevOps engineer, product manager)
  - Include their experience level and specialization
  - Provide brief context about their role in the project
  - Make their introduction feel natural within the technical narrative
- After first introduction, refer to them naturally without re-explaining

**TECHNICAL RELATIONSHIP TRACKING:**
- Keep mental note of which technical relationships have been introduced
- First mention includes technical context; subsequent mentions assume familiarity
- Ensure consistency in how technical relationships are portrayed

**TECHNICAL RELATIONSHIP CONTINUITY SYSTEM:**

**Technical Relationship Evolution Mandate:**
Every technical relationship mention MUST include specific interaction details:

**Technical Evolution Stages with Required Details:**
- **Introduction:** "Met [Name] during [specific technical event] for [specific project/technology]"
- **Development:** "[Name] suggested [specific technical solution] which improved [specific metric] by [amount]"
- **Deepening:** "[Name] revealed [specific technical insight] during [specific code review/meeting]"
- **Maturation:** "After [X sprints/months], [Name] and I [specific technical collaboration change]"

**Technical Interaction Variety (rotate - never repeat within 3 batches):**
- Code Review, Pair Programming, Architecture Discussion, Bug Triage, Sprint Planning, Technical Mentoring, System Design, Deployment Coordination

**Technical Character Consistency Rules:**
- Track specific technical preferences for each character (favorite IDE, programming language, deployment tool)
- Reference past specific technical events and their measurable consequences
- Include 2-3 technical relationship bullets per batch with concrete details

═══════════════ TECHNICAL CONTENT DISTRIBUTION STRATEGY ═══════════════

**Per Batch Technical Requirements:**
- 2-3 bullets: Technical relationship developments with specific coding incidents
- 3-4 bullets: Current technical situation with measurable coding metrics
- 1 bullet: Exact temporal anchor (specific date/time for technical event)
- 5-6 bullets: Technical events with verifiable coding outcomes
- 4-5 bullets: Technical decisions/preferences with specific technology choices
- Rest: Using remaining labels with concrete technical details

**Technical Story Progression Patterns:**
- **Early Batches (1-3):** Establish technical baselines (current tech stack, performance metrics, team structure)
- **Middle Batches:** Track technical changes from baselines with specific coding metrics
- **Later Batches:** Show cumulative technical results with before/after comparisons

═══════════════ ANTI-REPETITION VERIFICATION ═══════════════

**Before writing ANY bullet, verify:**
- Have I included at least one specific, verifiable technical detail?
- Can this generate a technical question with a one-word or short factual answer?
- Does this show MEASURABLE technical progression from previous mentions?
- Are the version numbers, configurations, metrics, and technologies specific?
- Is this a NEW piece of technical information with NEW details?

**FORBIDDEN:**
- Vague technical references ("recently deployed", "soon releasing") without specific dates
- General technologies ("database", "API") without specific names and versions
- Unspecified metrics ("improved performance", "faster queries") without exact numbers
- Abstract technical outcomes ("refactored code", "fixed issues") without specific details
- Repeated specific technical details (same bug, same optimization, same deployment)

═══════════════ MANDATORY REPETITION PREVENTION ═══════════════

**CRITICAL TECHNICAL REPETITION CHECK:**
Before writing ANY bullet point, verify against ALL previous batches:
- [ ] Have I mentioned this exact technical fact before?
- [ ] Is this a new technical development or just confirmation of previous content?
- [ ] Does this bullet advance the technical story or just repeat information?
- [ ] Can I add new technical details, metrics, or perspectives to make this unique?

**FORBIDDEN TECHNICAL REPETITION PATTERNS:**
- Confirming/verifying previously established technical facts without new information
- Restating version numbers, performance metrics, or technical decisions already mentioned
- Repeating technical relationship interactions without new developments
- Listing the same technologies, configurations, or architectures multiple times
- Re-explaining established development processes or procedures
- Duplicating technical research findings or performance benchmarks
- Rehashing previous code reviews or technical meetings without new outcomes

**REQUIRED TECHNICAL PROGRESSION:**
Each bullet must either:
- Introduce completely new technical information
- Show technical progression/change from previous mentions  
- Add new technical details to previously mentioned elements
- Present new technical perspectives or complications
- Reveal new technical developments or discoveries
- Show evolution in technical understanding or approach
- Introduce new technical stakeholders or variables
- Present new technical challenges or opportunities

═══════════════ MANDATORY ACTION DATE EXTRACTION ═══════════════

**CRITICAL FIRST STEP - EXTRACT TECHNICAL ACTION DATES:**

From CURRENT_SUBTOPIC_DATA, extract:
1. **development_dates.main_development_starts**: [EXACT DATE]
2. **development_dates.main_development_ends**: [EXACT DATE]
3. **development_dates.main_development_duration**: [DURATION]
4. **development_dates.current_phase_relation**: [before/during/after]
5. **phase_type**: [planning/core_development/deployment]

**WRITE THESE DATES HERE NOW:**
- Main Development Starts: ________________
- Main Development Ends: ________________
- Current Phase Type: ________________
- Current Phase Relation: ________________

═══════════════ ABSOLUTE TEMPORAL BOUNDARIES ═══════════════

**PHASE-SPECIFIC DATE BOUNDARIES:**

Based on the extracted development dates and current phase_type:

**IF phase_type = "planning" (before main development):**
- **EARLIEST DATE**: First day of TIMELINE
- **LATEST DATE**: Day BEFORE main_development_starts
- **FORBIDDEN**: ANY date on or after main_development_starts
- **TENSE FOR MAIN DEVELOPMENT**: FUTURE (planning/preparatory language)

**IF phase_type = "core_development" (during main development):**
- **EARLIEST DATE**: main_development_starts
- **LATEST DATE**: main_development_ends
- **FORBIDDEN**: ANY date before main_development_starts OR after main_development_ends
- **TENSE FOR MAIN DEVELOPMENT**: PRESENT (active/ongoing development language)

**IF phase_type = "deployment" (after main development):**
- **EARLIEST DATE**: Day AFTER main_development_ends
- **LATEST DATE**: Last day of TIMELINE
- **FORBIDDEN**: ANY date before or during main development
- **TENSE FOR MAIN DEVELOPMENT**: PAST (reflective/analytical language)

═══════════════ ABSOLUTE DATE BOUNDARIES ENFORCEMENT ═══════════════
**CRITICAL TIMELINE RULES:**

**EARLIEST ALLOWED DATE:** [START_DATE from TIMELINE]
**LATEST ALLOWED DATE:** [END_DATE from TIMELINE]

**ABSOLUTELY FORBIDDEN:**
- ANY date before START_DATE
- ANY date after END_DATE
- Creating dates outside the timeline range
- Extending the timeline beyond specified boundaries

**MANDATORY COMPLIANCE:**
- Every temporal anchor MUST use a date within [START_DATE, END_DATE]
- If timeline is 3 days, ALL content must fit within those 3 days
- No exceptions, no extensions, no violations

═══════════════ TECHNICAL CONTENT BOUNDARY ENFORCEMENT ═══════════════

**PHASE-LOCKED TECHNICAL CONTENT RULES:**

**PLANNING/PREPARATION PHASE - ALLOWED ONLY:**
- Technical research, architecture planning, technology selection, requirements analysis
- Future-oriented language about the main development work
- Planning activities that happen BEFORE the main development starts
- Technical information gathering, skill assessment, environment setup

**PLANNING/PREPARATION PHASE - ABSOLUTELY FORBIDDEN:**
- Any present-tense description of actively coding the main project
- Completed implementations or deployments
- Technical experiences that would only occur during the main development
- Post-development reflections or production outcomes

**CORE DEVELOPMENT PHASE - ALLOWED ONLY:**
- Real-time coding experiences, immediate technical decisions, active development
- Present-tense descriptions of ongoing development activities
- Technical activities happening DURING the main development period
- Direct implementation of previously planned features

**DEPLOYMENT/INTEGRATION PHASE - ALLOWED ONLY:**
- Deployment activities, production monitoring, post-development analysis
- Past-tense descriptions of the completed main development
- Technical processing and applying development experiences
- Performance evaluation and maintenance planning

═══════════════ CONTINUITY AND CONTEXT INTEGRATION ═══════════════

**PREVIOUS TECHNICAL CONTEXT INTEGRATION:**

1. **Review Previous Technical Plans Summary:**
   - Understand what technical work has already been covered in earlier subtopics
   - Identify established technical facts, architectural decisions, and team relationships
   - Note any technical commitments or development plans made for current timeframe

2. **Analyze Previous Technical Plan (if exists):**
   - Continue technical narrative threads from immediately preceding plan
   - Reference technical decisions or discoveries made
   - Build upon established technical momentum
   - Avoid contradicting previous technical facts

3. **Technical Introduction Handling:**
   - **IF INCLUDE_INTRODUCTION = YES**: First batch should introduce developer's technical situation naturally
   - **IF INCLUDE_INTRODUCTION = NO**: Continue from previous technical narrative without re-introduction
   - Ensure smooth technical transition either way

**TECHNICAL CONTINUITY REQUIREMENTS:**
- Reference previously established technical facts consistently
- Build upon prior technical decisions and learnings
- Maintain technical relationship continuity
- Honor previously mentioned deployment dates/technical plans
- Show technical progression from previous subtopic's ending

═══════════════ TIMELINE DISTRIBUTION STRATEGY ═══════════════

**MANDATORY TIMELINE PARSING:**

1. **Parse Current Subtopic Timeline:**
   - START: [Extract from TIMELINE]
   - END: [Extract from TIMELINE]
   - DURATION: [Calculate in days/months]

2. **Calculate Timeline Distribution Method:**
   - Total Days = END - START + 1
   - IF Total Days >= <num_batches>:
     - Days per Batch = Total Days ÷ <num_batches>
     - Each batch gets unique date progression
   - IF Total Days < <num_batches>:
     - Use grouped date distribution to maintain coherence

3. **Create Batch Timeline Segments:**

   **FOR TIMELINES WITH SUFFICIENT DAYS (Total Days >= <num_batches>):**
   - Batch 1: Days 1-X of timeline
   - Batch 2: Days X+1-Y of timeline
   - Continue sequential progression for all batches

   **FOR SHORT TIMELINES (Total Days < <num_batches>):**
   - Calculate batches per day: <num_batches> ÷ Total Days
   - Group consecutive batches to same date
   - Distribute evenly across available dates
   - Example pattern for X available days:
     - First [batches_per_day] batches: Day 1
     - Next [batches_per_day] batches: Day 2
     - Continue until all batches assigned
   - Ensure each available day gets equal batch distribution
   - Maintain chronological order within same-day batches

4. **Batch Technical Content Differentiation for Same-Day Batches:**
   - When multiple batches share same date, differentiate by:
     - Time of day progression (morning standup → afternoon coding → evening deployment)
     - Technical focus areas within the day
     - Different technical stakeholder perspectives
     - Various aspects of same-day development experiences
     - Progressive technical depth of engagement

5. **Verify Against Development Dates:**
   - EVERY date must respect technical phase boundaries
   - NO date can violate the development date rules above
   - Maintain logical technical progression even with repeated dates
   - Ensure technical content advancement despite date repetition

═══════════════ MANDATORY CONTENT BOUNDARY EXTRACTION ═══════════════

**CRITICAL STEP - EXTRACT TECHNICAL CONTENT RESTRICTIONS:**

From CURRENT_SUBTOPIC_DATA, extract:
1. **phase_boundaries.can_mention**: [Allowed technical content types]
2. **phase_boundaries.cannot_mention**: [Forbidden technical content types] 
3. **phase_boundaries.tense_for_main_development**: [past/present/future]
4. **subtopics**: [Current subtopic's allowed technical activities]

**WRITE TECHNICAL RESTRICTIONS HERE:**
- Can Mention: ________________
- Cannot Mention: ________________
- Required Tense: ________________
- Technical Subtopic Activities: ________________

NOTE: WRITE INTERNALLY. DO NOT WRITE IT IN OUTPUT.

**ABSOLUTE TECHNICAL CONTENT RULES:**
- ONLY generate technical content listed in can_mention
- NEVER generate technical content listed in cannot_mention  
- ONLY reference current subtopic technical activities
- Use ONLY the specified tense for main development action

═══════════════ PRE-GENERATION VALIDATION GATES ═══════════════

**GATE 1: TECHNICAL ACTION DATE VERIFICATION**
Before generating ANY content, confirm:
- [ ] I have extracted the exact main_development_starts date
- [ ] I have extracted the exact main_development_ends date
- [ ] I know whether I'm BEFORE, DURING, or AFTER these development dates
- [ ] I understand what tense to use for the main development work

**GATE 2: TECHNICAL PHASE BOUNDARY CHECK**
For the current phase_type, verify:
- [ ] I know exactly which dates are allowed for technical activities
- [ ] I know exactly which dates are forbidden for technical work
- [ ] I understand which technical activities are appropriate
- [ ] I know which technical phrases/words to avoid

**GATE 3: TECHNICAL CONTENT BOUNDARY VERIFICATION**
From current subtopic data, confirm:
- [ ] I know what technical content is allowed vs forbidden
- [ ] I know the current subtopic's technical activity scope
- [ ] I understand the required tense for main development action
- [ ] All technical content fits within current subtopic boundaries
- [ ] No technical content belongs to future subtopics

**TECHNICAL CONTENT VERIFICATION FOR EACH BULLET:**
Before writing any bullet, verify:
- [ ] Is this technical activity in can_mention?
- [ ] Is this technical activity NOT in cannot_mention?  
- [ ] Does this belong to current subtopic technical activities?
- [ ] Am I using the correct tense for development work?
- [ ] Does this technical content belong to a future subtopic?

**GATE 4: TIMELINE BOUNDARY VERIFICATION**
Before generating ANY content, confirm:
- [ ] I have extracted START_DATE and END_DATE correctly
- [ ] I have calculated TOTAL_DAYS correctly
- [ ] I know my specific assigned date for this batch
- [ ] My assigned date is within the timeline boundaries

**GATE 5: DATE ASSIGNMENT VERIFICATION**
For my specific batch number, verify:
- [ ] I know whether to use sequential or grouped distribution
- [ ] I have calculated my exact assigned date
- [ ] My date does not exceed END_DATE
- [ ] My date follows the distribution formula

**Structure Compliance:**
- [ ] EXACTLY 30 bullets per batch
- [ ] Proper label format for every bullet
- [ ] Progressive technical complexity across batches

═══════════════ TECHNICAL QUALITY STANDARDS ═══════════════

**Technical Specificity Checklist:**
- Every technical person has a full name and defined technical role
- Every technical event has a date, time, or specific temporal reference
- Every technology has a name, version, and configuration details
- Every technical decision has concrete options with specific technical details
- Every technical outcome is measurable or verifiable with metrics

**Technical Narrative Depth:**
- Include version numbers, response times, memory usage, user counts
- Show technical cause-and-effect with specific triggers and measurable results
- Maintain technical factual consistency (don't change established versions/configurations)
- Reference past specific technical events by name, version, and date

═══════════════ FINAL EXECUTION PROTOCOL ═══════════════

1. **FIRST**: Extract and verify technical development dates
2. **SECOND**: Write all content in FIRST-PERSON developer perspective
3. **THIRD**: Include date ONLY in temporal anchor
4. **FOURTH**: Pack MAXIMUM technical detail into every bullet
5. **FIFTH**: Ensure exactly 30 bullets with required technical composition
6. **SIXTH**: Validate all technical boundaries and progression

**REMEMBER:**
- Write as "I" not as third-person narrator
- Only ONE date per batch (in temporal anchor)
- MAXIMUM technical detail density in every bullet
- EXACTLY 30 bullets following technical composition requirements

Output ONLY the batch plans. No explanations or additional text.
End immediately after `BATCH <num_batches> PLAN`

Begin generation now.
"""
ten_m_similar_plan_generation_prompt_math = """
You are a precision mathematical narrative architect generating TEMPORALLY COHERENT MATH BATCH PLANS that strictly adhere to subtopic boundaries and phase-specific timelines. Your task is to create detailed mathematical plans that maintain absolute timeline integrity and phase-appropriate mathematical content.

## CRITICAL INPUT DATA
- **MAIN_TOPIC:** <main_topic>
- **MAIN_THEME:** <main_theme>
- **TOPIC:** <topic>
- **THEME:** <theme>
- **TIMELINE:** <timeline>
- **NUM_BATCHES:** <num_batches> batches
- **LABELS:** <provided_labels>
- **USER_PROFILE:** <user_profile>
- **CORE_RELATIONSHIPS:** <core_relationships>
- **NEW_RELATIONSHIPS:** <new_relationships>
- **ALL_SUBTOPIC_PLANS:** <all_subtopic_plans>
- **PREVIOUS_PLANS_SUMMARY:** <previous_plans_summary>
- **PREVIOUS_PLAN:** <previous_plan>
- **CURRENT_SUBTOPIC_DATA:** <current_subtopic_data>
- **CURRENT_SUBTOPIC_ID:** <current_subtopic_id>
- **INCLUDE_INTRODUCTION:** <YES/NO>

═══════════════ CORE OBJECTIVE ═══════════════
Generate <num_batches> distinct, non-repetitive batch plans that form a coherent mathematical narrative arc where a real student naturally converses with an AI assistant. Each plan must introduce NEW mathematical elements while maintaining perfect continuity and mathematical consistency.

═══════════════ MATHEMATICAL NARRATIVE FRAMEWORK ═══════════════
This is NOT about generating random mathematical conversations - this is about creating a realistic, evolving mathematical story where:
- The student naturally seeks AI assistance across different mathematical situations
- Each conversation builds upon previous mathematical interactions and established learning context
- Mathematical relationships, concepts, and understanding evolve realistically over time
- The student's mathematical needs, challenges, and expertise naturally expand and deepen

═══════════════ CRITICAL NARRATIVE PERSPECTIVE ═══════════════

**MANDATORY FIRST-PERSON STUDENT PERSPECTIVE:**
- ALL content must be written from the STUDENT's perspective (first-person)
- Use first-person perspective throughout but VARY sentence structures
- Natural mathematical narrative flow - avoid starting every bullet with "I"
- Mix active and passive voice while maintaining first-person student perspective

═══════════════ CRITICAL MATHEMATICAL DETAIL REQUIREMENTS ═══════════════

**MANDATORY SPECIFIC MATHEMATICAL DETAILS:**
Every batch MUST include numerous concrete, verifiable mathematical details that enable single-word or short factual answers:

**Required Mathematical Detail Categories (minimum 10-12 per batch):**
- **Exact Numbers:** specific values (x = 3.14159), coefficients (2x² + 5x - 3), dimensions (5×7 matrix), constants (e ≈ 2.718), angles (45°, π/4 radians), coordinates (3, -2)
- **Specific Problems:** complete equations (x² - 4x + 3 = 0), definite integrals (∫(2x+1)dx from 0 to 5), derivatives (d/dx(sin x) = cos x), limits (lim[x→0] sin x/x = 1), systems (2x + y = 5, x - y = 1)
- **Named Concepts:** theorem names (Pythagorean Theorem, Mean Value Theorem), method names (Gaussian elimination, L'Hôpital's rule), formulas (quadratic formula, distance formula), axioms (Axiom of Choice)
- **Calculation Results:** exact answers (x = 4, y = -2), decimal results (π ≈ 3.14159), fractions (3/4, 7/12), percentages (85% correct), approximations (√2 ≈ 1.414)
- **Yes/No Situations:** problem solved correctly, method applicable, theorem satisfied, solution exists, function continuous, series convergent, matrix invertible
- **Score/Grade Metrics:** test scores (85%), homework grades (18/20), quiz results (9/10 correct), assignment percentages (92%), participation scores (8/10), cumulative averages (87.5%)
- **Time/Duration:** study hours (3.5 hours), problem completion time (15 minutes), exam duration (2 hours), lecture time (50 minutes), office hours (30 minutes), homework time (45 minutes)
- **Mathematical Properties:** function characteristics (continuous, differentiable, injective, surjective), matrix properties (invertible, symmetric, orthogonal, positive definite), set properties (closed, bounded, compact, connected)
- **Course Information:** chapter numbers (Chapter 7), section references (7.3), page numbers (p. 142), problem numbers (#15, #23-27), textbook editions (9th edition), exercise sets (odd problems 1-25)
- **Software/Tools:** calculator models (TI-84 Plus), software names (Mathematica 13.2, MATLAB R2023a, Desmos Graphing Calculator), programming languages (Python 3.11, R 4.3.0), specific functions (plot(), solve(), integrate(), factor())
- **Academic Metrics:** GPA values (3.67), credit hours (15), prerequisite courses (Calculus I), grade distributions (A: 23%, B: 35%, C: 25%), class rankings (top 15%), semester standings
- **Error Types:** computational errors (sign error in line 3), conceptual mistakes (forgot chain rule), algebraic errors (factoring mistake), logical errors (invalid assumption)

**Mathematical Detail Distribution Rules:**
- Each bullet must contain AT LEAST one verifiable mathematical detail
- Avoid vague statements like "worked on problems" - specify WHICH problems and results
- Replace "studied math" with "completed 5 quadratic equation problems from Section 4.2, solved 4 correctly in 45 minutes"
- Instead of "improved understanding" use "increased quiz score from 70% to 85% on derivatives after 3 hours of practice"
- Replace "attended class" with "learned integration by parts in Calculus II, Section 8.2, solved problems #12-18 with 90% accuracy"
- Instead of "struggled with concept" use "spent 2 hours on parametric equations from Chapter 10, solved 3 of 8 practice problems correctly"
- Replace "used calculator" with "used TI-84 Plus to graph y = sin(2x) + cos(x) and find intersections at x = π/6, 5π/6"

═══════════════ CRITICAL STRUCTURE REQUIREMENTS ═══════════════

**OUTPUT FORMAT:**
- Generate exactly <num_batches> plans
- Format: `BATCH X PLAN` headers (NO timeline headers)
- Each plan contains exactly 30 bullets
- Each bullet: "• **[LABEL CATEGORY]:[LABEL DESCRIPTION]:** [detailed mathematical content with specific facts]" (≤30 words)
- NOTE: Each label consists of category and description. Use both for each bullet point.
- Use only the provided LABELS - no custom categories
- **MANDATORY**: First bullet MUST be Temporal Anchor with the ONLY date reference in the batch

**TEMPORAL ANCHOR RULES:**
- **ONLY the first bullet** of each batch contains a date
- **NO OTHER BULLET** in the batch should include dates
- **Format**: "• **Temporal Anchor:** [Specific date], [rich mathematical contextual explanation of what's happening and why it's significant]"
- All other bullets refer to mathematical activities happening "around this time" without specific dates

═══════════════ MATHEMATICAL CHARACTER AND RELATIONSHIP INTRODUCTION ═══════════════

**MATHEMATICAL INTRODUCTION REQUIREMENTS:**

**IF INCLUDE_INTRODUCTION = YES:**
- Introduce CORE_RELATIONSHIPS with context about their mathematical roles and importance
- Establish the student's motivation and context for the main mathematical topic

**BATCH 1 (Mathematical Foundation):**
- First bullet MUST be: "• **Personal Introduction:**"
- Establish mathematical context with SPECIFIC details (years of study, current courses, GPA, mathematical strengths/weaknesses, calculator model)
- Introduce all mathematical relationships with CONCRETE contexts (study group size, tutor sessions, professor office hours, lab partners)
- Set up measurable mathematical goals, exam deadlines, and quantifiable learning challenges

**BATCHES 2-<num_batches> (Mathematical Evolution):**
- Reference student as "I/my/me" (never repeat the full name)
- Each batch advances the mathematical timeline chronologically
- Build upon ALL previously established mathematical elements
- Show MEASURABLE mathematical progression (grade improvements, concept mastery, problem-solving speed, accuracy rates)

**FOR ALL PLANS (regardless of INCLUDE_INTRODUCTION):**
- When ANY person from NEW_RELATIONSHIPS appears for the FIRST time:
  - Include their mathematical relationship to the user (professor, teaching assistant, study partner, tutor)
  - Include their mathematical background and specialization
  - Provide brief context about their role in the mathematical learning
  - Make their introduction feel natural within the mathematical narrative
- After first introduction, refer to them naturally without re-explaining

**MATHEMATICAL RELATIONSHIP TRACKING:**
- Keep mental note of which mathematical relationships have been introduced
- First mention includes mathematical context; subsequent mentions assume familiarity
- Ensure consistency in how mathematical relationships are portrayed

**MATHEMATICAL RELATIONSHIP CONTINUITY SYSTEM:**

**Mathematical Relationship Evolution Mandate:**
Every mathematical relationship mention MUST include specific interaction details:

**Mathematical Evolution Stages with Required Details:**
- **Introduction:** "Met [Name] during [specific mathematical event] for [specific topic/course with number]"
- **Development:** "[Name] explained [specific mathematical concept] which improved my accuracy on [specific problem type] by [percentage]"
- **Deepening:** "[Name] revealed [specific mathematical insight] during [specific study session/office hours] about [specific theorem/method]"
- **Maturation:** "After [X weeks/months], [Name] and I [specific mathematical collaboration change] resulting in [measurable improvement]"

**Mathematical Interaction Variety (rotate - never repeat within 3 batches):**
- Problem-Solving Session, Concept Explanation, Proof Review, Exam Preparation, Homework Collaboration, Mathematical Discussion, Tutoring Session, Study Group, Office Hours

**Mathematical Character Consistency Rules:**
- Track specific mathematical preferences for each character (favorite proof technique, preferred calculator, teaching style, mathematical specialization)
- Reference past specific mathematical events and their measurable learning consequences
- Include 2-3 mathematical relationship bullets per batch with concrete mathematical details

═══════════════ MATHEMATICAL CONTENT DISTRIBUTION STRATEGY ═══════════════

**Per Batch Mathematical Requirements:**
- 2-3 bullets: Mathematical relationship developments with specific learning incidents
- 3-4 bullets: Current mathematical situation with measurable learning metrics
- 1 bullet: Exact temporal anchor (specific date/time for mathematical event)
- 5-6 bullets: Mathematical events with verifiable learning outcomes
- 4-5 bullets: Mathematical decisions/preferences with specific concept/method choices
- Rest: Using remaining labels with concrete mathematical details

**Mathematical Story Progression Patterns:**
- **Early Batches (1-3):** Establish mathematical baselines (current grades, concept understanding, problem-solving speed)
- **Middle Batches:** Track mathematical changes from baselines with specific learning metrics
- **Later Batches:** Show cumulative mathematical results with before/after learning comparisons

═══════════════ ANTI-REPETITION VERIFICATION ═══════════════

**Before writing ANY bullet, verify:**
- Have I included at least one specific, verifiable mathematical detail?
- Can this generate a mathematical question with a one-word or short factual answer?
- Does this show MEASURABLE mathematical progression from previous mentions?
- Are the numbers, formulas, theorems, and scores specific?
- Is this a NEW piece of mathematical information with NEW mathematical details?

**FORBIDDEN:**
- Vague mathematical references ("recently studied", "soon taking exam") without specific dates
- General mathematical concepts ("algebra", "calculus") without specific topics, problems, and results
- Unspecified mathematical results ("improved performance", "better understanding") without exact numbers
- Abstract mathematical outcomes ("grasped concept", "solved problems") without specific details
- Repeated specific mathematical details (same problem, same theorem, same score, same error)

═══════════════ MANDATORY REPETITION PREVENTION ═══════════════

**CRITICAL MATHEMATICAL REPETITION CHECK:**
Before writing ANY bullet point, verify against ALL previous batches:
- [ ] Have I mentioned this exact mathematical fact before?
- [ ] Is this a new mathematical development or just confirmation of previous content?
- [ ] Does this bullet advance the mathematical story or just repeat information?
- [ ] Can I add new mathematical details, metrics, or perspectives to make this unique?

**FORBIDDEN MATHEMATICAL REPETITION PATTERNS:**
- Confirming/verifying previously established mathematical facts without new information
- Restating numerical values, scores, or mathematical decisions already mentioned
- Repeating mathematical relationship interactions without new developments
- Listing the same problems, theorems, or methods multiple times
- Re-explaining established mathematical processes or procedures
- Duplicating mathematical research findings or concept explanations
- Rehashing previous study sessions or mathematical meetings without new outcomes

**REQUIRED MATHEMATICAL PROGRESSION:**
Each bullet must either:
- Introduce completely new mathematical information
- Show mathematical progression/change from previous mentions  
- Add new mathematical details to previously mentioned elements
- Present new mathematical perspectives or complications
- Reveal new mathematical developments or discoveries
- Show evolution in mathematical understanding or approach
- Introduce new mathematical stakeholders or variables
- Present new mathematical challenges or opportunities

═══════════════ MANDATORY ACTION DATE EXTRACTION ═══════════════

**CRITICAL FIRST STEP - EXTRACT MATHEMATICAL ACTION DATES:**

From CURRENT_SUBTOPIC_DATA, extract:
1. **study_dates.main_study_starts**: [EXACT DATE]
2. **study_dates.main_study_ends**: [EXACT DATE]
3. **study_dates.main_study_duration**: [DURATION]
4. **study_dates.current_phase_relation**: [before/during/after]
5. **phase_type**: [preparation/core_learning/application]

**WRITE THESE DATES HERE NOW:**
- Main Study Starts: ________________
- Main Study Ends: ________________
- Current Phase Type: ________________
- Current Phase Relation: ________________

═══════════════ ABSOLUTE TEMPORAL BOUNDARIES ═══════════════

**PHASE-SPECIFIC DATE BOUNDARIES:**

Based on the extracted study dates and current phase_type:

**IF phase_type = "preparation" (before main study):**
- **EARLIEST DATE**: First day of TIMELINE
- **LATEST DATE**: Day BEFORE main_study_starts
- **FORBIDDEN**: ANY date on or after main_study_starts
- **TENSE FOR MAIN STUDY**: FUTURE (planning/preparatory language)

**IF phase_type = "core_learning" (during main study):**
- **EARLIEST DATE**: main_study_starts
- **LATEST DATE**: main_study_ends
- **FORBIDDEN**: ANY date before main_study_starts OR after main_study_ends
- **TENSE FOR MAIN STUDY**: PRESENT (active/ongoing learning language)

**IF phase_type = "application" (after main study):**
- **EARLIEST DATE**: Day AFTER main_study_ends
- **LATEST DATE**: Last day of TIMELINE
- **FORBIDDEN**: ANY date before or during main study
- **TENSE FOR MAIN STUDY**: PAST (reflective/analytical language)

═══════════════ ABSOLUTE DATE BOUNDARIES ENFORCEMENT ═══════════════
**CRITICAL TIMELINE RULES:**

**EARLIEST ALLOWED DATE:** [START_DATE from TIMELINE]
**LATEST ALLOWED DATE:** [END_DATE from TIMELINE]

**ABSOLUTELY FORBIDDEN:**
- ANY date before START_DATE
- ANY date after END_DATE
- Creating dates outside the timeline range
- Extending the timeline beyond specified boundaries

**MANDATORY COMPLIANCE:**
- Every temporal anchor MUST use a date within [START_DATE, END_DATE]
- If timeline is 3 days, ALL content must fit within those 3 days
- No exceptions, no extensions, no violations

═══════════════ MATHEMATICAL CONTENT BOUNDARY ENFORCEMENT ═══════════════

**PHASE-LOCKED MATHEMATICAL CONTENT RULES:**

**PREPARATION/FOUNDATION PHASE - ALLOWED ONLY:**
- Mathematical research, prerequisite review, study planning, resource selection
- Future-oriented language about the main mathematical learning
- Preparation activities that happen BEFORE the main study starts
- Mathematical background gathering, skill assessment, concept review

**PREPARATION/FOUNDATION PHASE - ABSOLUTELY FORBIDDEN:**
- Any present-tense description of actively learning the main mathematical topic
- Completed mastery or advanced applications
- Mathematical experiences that would only occur during the main study
- Post-study reflections or advanced outcomes

**CORE LEARNING PHASE - ALLOWED ONLY:**
- Real-time mathematical learning experiences, immediate problem-solving, active study
- Present-tense descriptions of ongoing mathematical activities
- Mathematical activities happening DURING the main study period
- Direct learning of previously planned mathematical concepts

**APPLICATION/MASTERY PHASE - ALLOWED ONLY:**
- Mathematical application, advanced projects, teaching others, research extensions
- Past-tense descriptions of the completed main mathematical study
- Mathematical processing and applying learned concepts
- Advanced mathematical exploration and outcome evaluation

═══════════════ CONTINUITY AND CONTEXT INTEGRATION ═══════════════

**PREVIOUS MATHEMATICAL CONTEXT INTEGRATION:**

1. **Review Previous Mathematical Plans Summary:**
   - Understand what mathematical work has already been covered in earlier subtopics
   - Identify established mathematical facts, concept mastery, and study relationships
   - Note any mathematical commitments or learning plans made for current timeframe

2. **Analyze Previous Mathematical Plan (if exists):**
   - Continue mathematical narrative threads from immediately preceding plan
   - Reference mathematical decisions or discoveries made
   - Build upon established mathematical momentum
   - Avoid contradicting previous mathematical facts

3. **Mathematical Introduction Handling:**
   - **IF INCLUDE_INTRODUCTION = YES**: First batch should introduce student's mathematical situation naturally
   - **IF INCLUDE_INTRODUCTION = NO**: Continue from previous mathematical narrative without re-introduction
   - Ensure smooth mathematical transition either way

**MATHEMATICAL CONTINUITY REQUIREMENTS:**
- Reference previously established mathematical facts consistently
- Build upon prior mathematical decisions and learnings
- Maintain mathematical relationship continuity
- Honor previously mentioned exam dates/mathematical plans
- Show mathematical progression from previous subtopic's ending

═══════════════ TIMELINE DISTRIBUTION STRATEGY ═══════════════

**MANDATORY TIMELINE PARSING:**

1. **Parse Current Subtopic Timeline:**
   - START: [Extract from TIMELINE]
   - END: [Extract from TIMELINE]
   - DURATION: [Calculate in days/months]

2. **Calculate Timeline Distribution Method:**
   - Total Days = END - START + 1
   - IF Total Days >= <num_batches>:
     - Days per Batch = Total Days ÷ <num_batches>
     - Each batch gets unique date progression
   - IF Total Days < <num_batches>:
     - Use grouped date distribution to maintain coherence

3. **Create Batch Timeline Segments:**

   **FOR TIMELINES WITH SUFFICIENT DAYS (Total Days >= <num_batches>):**
   - Batch 1: Days 1-X of timeline
   - Batch 2: Days X+1-Y of timeline
   - Continue sequential progression for all batches

   **FOR SHORT TIMELINES (Total Days < <num_batches>):**
   - Calculate batches per day: <num_batches> ÷ Total Days
   - Group consecutive batches to same date
   - Distribute evenly across available dates
   - Example pattern for X available days:
     - First [batches_per_day] batches: Day 1
     - Next [batches_per_day] batches: Day 2
     - Continue until all batches assigned
   - Ensure each available day gets equal batch distribution
   - Maintain chronological order within same-day batches

4. **Batch Mathematical Content Differentiation for Same-Day Batches:**
   - When multiple batches share same date, differentiate by:
     - Time of day progression (morning study → afternoon practice → evening review)
     - Mathematical focus areas within the day
     - Different mathematical stakeholder perspectives
     - Various aspects of same-day mathematical experiences
     - Progressive mathematical depth of engagement

5. **Verify Against Study Dates:**
   - EVERY date must respect mathematical phase boundaries
   - NO date can violate the study date rules above
   - Maintain logical mathematical progression even with repeated dates
   - Ensure mathematical content advancement despite date repetition

═══════════════ MANDATORY CONTENT BOUNDARY EXTRACTION ═══════════════

**CRITICAL STEP - EXTRACT MATHEMATICAL CONTENT RESTRICTIONS:**

From CURRENT_SUBTOPIC_DATA, extract:
1. **phase_boundaries.can_mention**: [Allowed mathematical content types]
2. **phase_boundaries.cannot_mention**: [Forbidden mathematical content types] 
3. **phase_boundaries.tense_for_main_study**: [past/present/future]
4. **subtopics**: [Current subtopic's allowed mathematical activities]

**WRITE MATHEMATICAL RESTRICTIONS HERE:**
- Can Mention: ________________
- Cannot Mention: ________________
- Required Tense: ________________
- Mathematical Subtopic Activities: ________________

NOTE: WRITE INTERNALLY. DO NOT WRITE IT IN OUTPUT.

**ABSOLUTE MATHEMATICAL CONTENT RULES:**
- ONLY generate mathematical content listed in can_mention
- NEVER generate mathematical content listed in cannot_mention  
- ONLY reference current subtopic mathematical activities
- Use ONLY the specified tense for main study action

═══════════════ PRE-GENERATION VALIDATION GATES ═══════════════

**GATE 1: MATHEMATICAL ACTION DATE VERIFICATION**
Before generating ANY content, confirm:
- [ ] I have extracted the exact main_study_starts date
- [ ] I have extracted the exact main_study_ends date
- [ ] I know whether I'm BEFORE, DURING, or AFTER these mathematical study dates
- [ ] I understand what tense to use for the main mathematical study

**GATE 2: MATHEMATICAL PHASE BOUNDARY CHECK**
For the current phase_type, verify:
- [ ] I know exactly which dates are allowed for mathematical activities
- [ ] I know exactly which dates are forbidden for mathematical work
- [ ] I understand which mathematical activities are appropriate
- [ ] I know which mathematical phrases/words to avoid

**GATE 3: MATHEMATICAL CONTENT BOUNDARY VERIFICATION**
From current subtopic data, confirm:
- [ ] I know what mathematical content is allowed vs forbidden
- [ ] I know the current subtopic's mathematical activity scope
- [ ] I understand the required tense for main study action
- [ ] All mathematical content fits within current subtopic boundaries
- [ ] No mathematical content belongs to future subtopics

**MATHEMATICAL CONTENT VERIFICATION FOR EACH BULLET:**
Before writing any bullet, verify:
- [ ] Is this mathematical activity in can_mention?
- [ ] Is this mathematical activity NOT in cannot_mention?  
- [ ] Does this belong to current subtopic mathematical activities?
- [ ] Am I using the correct tense for mathematical study?
- [ ] Does this mathematical content belong to a future subtopic?

**GATE 4: TIMELINE BOUNDARY VERIFICATION**
Before generating ANY content, confirm:
- [ ] I have extracted START_DATE and END_DATE correctly
- [ ] I have calculated TOTAL_DAYS correctly
- [ ] I know my specific assigned date for this batch
- [ ] My assigned date is within the timeline boundaries

**GATE 5: DATE ASSIGNMENT VERIFICATION**
For my specific batch number, verify:
- [ ] I know whether to use sequential or grouped distribution
- [ ] I have calculated my exact assigned date
- [ ] My date does not exceed END_DATE
- [ ] My date follows the distribution formula

**Structure Compliance:**
- [ ] EXACTLY 30 bullets per batch
- [ ] Proper label format for every bullet
- [ ] Progressive mathematical complexity across batches

═══════════════ MATHEMATICAL QUALITY STANDARDS ═══════════════

**Mathematical Specificity Checklist:**
- Every mathematical person has a full name and defined mathematical role
- Every mathematical event has a date, time, or specific temporal reference
- Every mathematical concept has a name, formula, or specific notation
- Every mathematical decision has concrete options with specific mathematical details
- Every mathematical outcome is measurable or verifiable with scores/metrics

**Mathematical Narrative Depth:**
- Include specific grades, problem numbers, formula names, theorem references
- Show mathematical cause-and-effect with specific triggers and measurable results
- Maintain mathematical factual consistency (don't change established scores/concepts)
- Reference past specific mathematical events by name, score, and date

═══════════════ FINAL EXECUTION PROTOCOL ═══════════════

1. **FIRST**: Extract and verify mathematical study dates
2. **SECOND**: Write all content in FIRST-PERSON student perspective
3. **THIRD**: Include date ONLY in temporal anchor
4. **FOURTH**: Pack MAXIMUM mathematical detail into every bullet
5. **FIFTH**: Ensure exactly 30 bullets with required mathematical composition
6. **SIXTH**: Validate all mathematical boundaries and progression

**REMEMBER:**
- Write as "I" not as third-person narrator
- Only ONE date per batch (in temporal anchor)
- MAXIMUM mathematical detail density in every bullet
- EXACTLY 30 bullets following mathematical composition requirements

Output ONLY the batch plans. No explanations or additional text.
End immediately after `BATCH <num_batches> PLAN`

Begin generation now.
"""


# ################################################## Probing Questions Generation ##################################################


# ================================ candidate generation ================================

information_extraction_prompt = """
This is a plan that contains detailed bullet points about a topic. This plan is used to generate realistic chat conversations between a user and an AI assistant, which are then used to evaluate the long-term memory capabilities of LLMs. 

Your task is to analyze this plan and select bullet points that would be most effective for testing information extraction abilities when incorporated into chat conversations.

Analyze this plan and identify bullet points that contain specific factual information ideal for testing precise recall and information extraction capabilities.

## INPUT DATA
- **PLAN**: <plan>

## CRITICAL REQUIREMENT: EARLY BATCH PRIORITIZATION
**SELECTION PRIORITY ORDER:**
1. **Batch 1-3 (HIGHEST PRIORITY)**: Select 70-80% of your choices from these early batches
2. **Batch 4-6 (MEDIUM PRIORITY)**: Select 10-20% of your choices from these middle batches  
3. **Batch 7+ (LOW PRIORITY)**: Select only 5-10% of your choices from later batches

Focus on bullet points with:
- **Specific numbers, quantities, measurements, prices, percentages**
- **Proper names of people, organizations, brands, locations**
- **Exact dates, times, schedules, or deadlines**
- **Contact details such as addresses, phone numbers, email IDs**
- **Technical or detailed descriptions (model names, product codes, ratings, specifications)**
- **Distinctive events, awards, or milestones**
- **Direct quotes, messages, or instructions with exact wording**
- **Precise parameters, formulas, or datasets in technical and academic contexts**
- **Mathematical expressions, theorems, proofs**

Prioritize information that:
- Appears early in the timeline (high forgetting risk over long chats)
- Contains multiple distinct factual details in one bullet point
- Includes uncommon names, technical terms, or culturally specific references
- Has precise numerical values or measurements that could be easily confused
- Could be misremembered if details are swapped, rounded, or reworded
- Requires high accuracy to preserve meaning (e.g., formulas, addresses, step-by-step processes)

Return your analysis in this exact JSON format:
[
    {
        "capability": "information_extraction",
        "batch_numbers": 1,
        "bullet_numbers": 3,
        "bullet_points": "• **Personal Introduction:** I am Sherry Rodriguez, 34, licensed conveyancer in Hollyborough, Bahrain, earning approximately $68,000 annually."
    }
]

Important formatting notes:
- The "batch_numbers" and "bullet_numbers" correspond to each other positionally
- "1" and "3" means: Batch 1 Bullet 3

Select ONLY <bullet_number> bullet points total that would generate the highest quality information extraction questions.

NOTE: Only output the list without any explanation before or after the list.
"""

multi_session_reasoning_prompt = """
This is a plan that contains detailed bullet points about a topic. This plan is used to generate realistic chat conversations between a user and an AI assistant, which are then used to evaluate the long-term memory capabilities of LLMs. 

Your task is to analyze this plan and select GROUPS of related bullet points that would be most effective for testing multi-session reasoning abilities when incorporated into chat conversations.

Analyze this project plan and identify GROUPS of bullet points that enable testing of aggregation, comparison, and synthesis across multiple batches/sessions. Each group should contain 2-6 related bullet points that together enable complex multi-hop reasoning questions.

## INPUT DATA
- **PLAN**: <plan>

## CRITICAL REQUIREMENT: EARLY BATCH PRIORITIZATION
**SELECTION PRIORITY ORDER:**
1. **Groups starting in Batches 1-3 (HIGHEST PRIORITY)**: Select 70-80% of your groups with primary content from early batches
2. **Groups spanning early to middle batches (MEDIUM PRIORITY)**: Select 10-20% of groups that bridge early-to-middle timeline
3. **Groups from later batches only (LOW PRIORITY)**: Select only 5-10% from purely later batches

Focus on bullet point groups that involve:
- **Aggregation opportunities**: Multiple costs that need to be summed, events that need counting, measurements to be totaled
- **Comparison patterns**: Same categories appearing in different batches (budget changes, progress updates, relationship interactions)
- **Evolution tracking**: How preferences, decisions, or situations change over time across multiple bullet points
- **Cross-reference relationships**: Information that connects between different people, events, or decisions across batches

Prioritize bullet point groups that:
- Are part of recurring themes across multiple batches (budget tracking, progress monitoring, relationship dynamics)
- Enable mathematical aggregation across multiple entries (total costs, time durations, quantity counting)
- Allow before/after comparisons of the same entities across different batches
- Require synthesis of information from 3+ different batches
- Create opportunities for complex multi-hop reasoning questions

Return your analysis in this exact JSON format where each object contains multiple related bullet points:
[
    {
        "capability": "multi_session_reasoning",
        "batch_numbers": "1, 2, 3, 5",
        "bullet_numbers": "10, 4, 7, 7",
        "bullet_points": "Financial & Budget:Cost Estimation: Initial budget set at $12,500, including materials and labor for decoupled framing and MLV. | Financial & Budget:Expense Tracking: Paid $2,200 deposit to QuietFlow Bahrain for HVAC silencing on March 14 via bank transfer. | Financial & Budget:Expense Tracking: Total spent $9,300 by April 1 on materials, labor, and consultant fees. | Financial & Budget:Expense Tracking: Total project spending $12,000 as of May 1, within original $12,500 budget."
    }
]

Important formatting notes:
- The "batch_numbers" and "bullet_numbers" correspond to each other positionally
- "1, 2, 3, 5" and "10, 4, 7, 7" means: Batch 1 Bullet 10, Batch 2 Bullet 4, Batch 3 Bullet 7, Batch 5 Bullet 7
- Use comma-separated values for batch_number and bullet_number
- Separate multiple bullet_point entries with " | "
- Each group should contain 2-6 related bullet points
- Focus on groups that enable the most sophisticated multi-hop aggregation and comparison questions

Select 8-12 groups of bullet points that would enable the most sophisticated multi-session reasoning questions.

NOTE: Only output the list without any explanation before or after the list.
"""
multi_session_reasoning_prompt_detailed = """
This is a plan that contains detailed bullet points about a topic. This plan is used to generate realistic chat conversations between a user and an AI assistant, which are then used to evaluate the long-term memory capabilities of LLMs. 

Your task is to analyze this plan and select GROUPS of related bullet points that would be most effective for testing multi-session reasoning abilities when incorporated into chat conversations.

Analyze this project plan and identify GROUPS of bullet points that enable testing of aggregation, comparison, and synthesis across multiple batches/sessions. Each group should contain ALL related bullet points that together enable comprehensive multi-hop reasoning questions.

## INPUT DATA
- **PLAN**: <plan>

## CRITICAL REQUIREMENT: EARLY BATCH PRIORITIZATION
**SELECTION PRIORITY ORDER:**
1. **Groups starting in Batches 1-3 (HIGHEST PRIORITY)**: Select 70-80% of your groups with primary content from early batches
2. **Groups spanning early to middle batches (MEDIUM PRIORITY)**: Select 10-20% of groups that bridge early-to-middle timeline
3. **Groups from later batches only (LOW PRIORITY)**: Select only 5-10% from purely later batches

## CRITICAL REQUIREMENT: COMPREHENSIVE BULLET POINT COLLECTION
- You MUST include ALL bullet points related to the same theme/topic across ALL batches
- Scan the ENTIRE plan systematically to find all mentions of the same topic
- Missing related bullet points will result in incomplete probing questions
- Prioritize completeness over arbitrary size limits

Focus on bullet point groups that involve:
- **Aggregation opportunities**: Multiple related quantities that can be summed, combined, or tallied (e.g., total expenses, total hours spent, number of events attended, total resources used)
- **Comparison patterns**: Similar categories appearing in different batches that allow before/after comparisons or side-by-side evaluation (e.g., price changes, progress updates, preference shifts)
- **Evolution tracking**: How a situation, preference, or plan develops over time (e.g., itinerary changes, diet adjustments, relationship developments, business strategy pivots)
- **Cross-reference relationships**: Information that connects across different people, events, locations, or decisions (e.g., one person’s actions affecting another, linking an earlier decision to a later consequence)

Prioritize bullet point groups that:
- Are part of recurring themes across multiple batches (e.g., budget tracking, health progress, project milestones, travel updates)
- Require aggregation across multiple entries (e.g., adding up costs from different suppliers, combining durations from several activities, counting cumulative occurrences)
- Enable comparisons across time or entities (e.g., comparing earlier vs. later performance, or two different options discussed in separate batches)
- Require synthesis of information from 3+ batches to form a complete understanding
- Support complex multi-hop reasoning where the answer depends on linking and analyzing information from different points in the timeline

Return your analysis in this exact JSON format where each object contains multiple related bullet points:
[
    {
        "capability": "multi_session_reasoning",
        "batch_numbers": "1, 2, 3, 5",
        "bullet_numbers": "10, 4, 7, 7",
        "bullet_points": "Travel & Accommodation:Initial Planning: Set estimated trip budget at $12,500, including flights, lodging, and activities for a 30-day itinerary. | Travel & Accommodation:Payment Tracking: Paid $2,200 deposit to Sunrise Tours for guided excursions on March 14 via credit card. | Travel & Accommodation:Expense Tracking: Total spent $9,300 by April 1 on flights, lodging, and tour bookings. | Travel & Accommodation:Expense Tracking: Total trip spending $12,000 as of May 1, within original $12,500 budget."
    }
]

Important formatting notes:
- The "batch_numbers" and "bullet_numbers" correspond to each other positionally
- "1, 2, 3, 5" and "10, 4, 7, 7" means: Batch 1 Bullet 10, Batch 2 Bullet 4, Batch 3 Bullet 7, Batch 5 Bullet 7
- Use comma-separated values for batch_number and bullet_number
- Separate multiple bullet_point entries with " | "
- Each group should contain all the related bullet points
- Focus on groups that enable the most sophisticated multi-hop aggregation and comparison questions

Select 6-10 groups of bullet points with COMPLETE coverage that would enable the most sophisticated and comprehensive multi-session reasoning questions.

NOTE: Only output the list without any explanation before or after the list.
"""
ten_m_multi_session_reasoning_prompt_detailed = """
This is a set of plans that contain detailed bullet points about various topics. These plans are used to generate realistic chat conversations between a user and an AI assistant, which are then used to evaluate the long-term memory capabilities of LLMs.

Your task is to analyze these plans and select GROUPS of related bullet points that would be most effective for testing multi-session reasoning abilities when incorporated into chat conversations.

Analyze these project plans and identify GROUPS of bullet points that enable testing of aggregation, comparison, and synthesis across multiple batches/sessions and across multiple plans.

## INPUT DATA
- **PLANS**: <plans>

## CRITICAL REQUIREMENTS:
- Select exactly 2 groups of related bullet points
- Each group must contain Between 5 and 10 bullet point indexes total (spread across all plans) and MUST cover all the plans
- For each object, across all plans, MUST have between 5 and 10 indexes, not more not less
- You MUST include the complete bullet point text for every single index you specify
- Distribute indexes across different plans when possible for better cross-plan reasoning
- If you cannot fit all bullet point text due to length limits, reduce the number of indexes rather than omitting text

## MANDATORY CROSS-PLAN REQUIREMENT:
EVERY single group MUST include bullet points from ALL plans provided in the input. No group should contain bullet points from only one plan. If a topic doesn't appear across all plans, do not select it. This is a hard requirement - any group that doesn't span all plans is invalid.

Focus on bullet point groups that involve:
- **Aggregation opportunities**: Multiple related quantities that can be summed, combined, or tallied (e.g., total expenses, total hours spent, number of events attended, total resources used)
- **Comparison patterns**: Similar categories appearing in different batches that allow before/after comparisons or side-by-side evaluation (e.g., price changes, progress updates, preference shifts)
- **Evolution tracking**: How a situation, preference, or plan develops over time (e.g., itinerary changes, diet adjustments, relationship developments, business strategy pivots)
- **Cross-reference relationships**: Information that connects across different people, events, locations, or decisions (e.g., one person’s actions affecting another, linking an earlier decision to a later consequence)

Prioritize bullet point groups that:
- Are part of recurring themes across multiple batches (e.g., budget tracking, health progress, project milestones, travel updates)
- Require aggregation across multiple entries (e.g., adding up costs from different suppliers, combining durations from several activities, counting cumulative occurrences)
- Enable comparisons across time or entities (e.g., comparing earlier vs. later performance, or two different options discussed in separate batches)
- Require synthesis of information from 3+ batches to form a complete understanding
- Support complex multi-hop reasoning where the answer depends on linking and analyzing information from different points in the timeline

Return your analysis in this exact JSON format where each object contains multiple related bullet points:
[
    {
        "capability": "multi_session_reasoning",
        "index": {
            "plan 1": [[1, 10], [2, 4]],
            "plan 2": [[1, 5], [4, 12]],
            "plan 3": [[2, 8]]
        },
        "bullet_points": "Complete text of Plan 1 Batch 1 Bullet 10 | Complete text of Plan 1 Batch 2 Bullet 4 | Complete text of Plan 2 Batch 1 Bullet 5 | Complete text of Plan 2 Batch 4 Bullet 12 | Complete text of Plan 3 Batch 2 Bullet 8"
    }
]

Important formatting notes:
- The "index" field contains a nested structure where each plan number maps to a list of [batch_number, bullet_number] pairs
- Indexes must cover all the plans
- Use the EXACT plan numbers as they appear in the input data (e.g., "plan 1", "plan 2", "plan 3", etc.)
- "plan 1": [[1, 10], [2, 4]] means Plan 1 Batch 1 Bullet 10, Plan 1 Batch 2 Bullet 4
- Each group should contain AT MOST 10 total bullet point indexes across all plans
- Include all plans that contain related bullet points in the index
- Separate multiple bullet_point entries with " | "
- The bullet_points field must contain the complete text for every single index specified
- Focus on groups that enable the most sophisticated multi-hop aggregation and comparison questions

VALIDATION CHECK: Before outputting each group, verify that its "index" field contains entries for every single plan number from the input. If any plan is missing from a group, that group is invalid and must be discarded.

Return exactly 2 JSON objects, each with at most 10 indexes total, with COMPLETE bullet point text for every index specified.

NOTE: Only output the JSON list without any explanation before or after the list.
"""

knowledge_update_prompt = """
This is a plan that contains detailed bullet points about a topic. This plan is used to generate realistic chat conversations between a user and an AI assistant, which are then used to evaluate the long-term memory capabilities of LLMs. 

Your task is to analyze this plan and select PAIRS of related bullet points that would be most effective for testing knowledge update abilities when incorporated into chat conversations.

Analyze this project plan and identify PAIRS of bullet points that represent information updates, corrections, or changes to previously established facts. Each pair should contain an original fact/decision and its subsequent update/change, enabling questions about how information evolved over time.

## INPUT DATA
- **PLAN**: <plan>

Focus on bullet point pairs that show:
- **Direct updates**: Original information paired with new information that explicitly changes previous facts
- **Corrections**: Initial statements paired with information that contradicts or modifies earlier statements
- **Timeline changes**: Original schedules paired with schedule modifications, deadline adjustments, date shifts
- **Budget revisions**: Initial costs paired with cost changes, budget reallocations, price adjustments
- **Decision reversals**: Original preferences paired with changed preferences, altered plans, new choices
- **Status updates**: Previous progress paired with progress changes, completion percentages, milestone updates
- **Relationship changes**: Initial interactions paired with evolving interactions, changed boundaries, new agreements

Prioritize bullet point pairs that:
- Show clear before/after relationships between original and updated information
- Use words like "updated," "changed," "revised," "adjusted," "increased," "decreased"
- Reference earlier decisions or facts that are now different
- Show progression or evolution of the same topic across batches
- Include information updates marked in the plan
- Enable questions about what changed, when it changed, and why it changed

Return your analysis in this exact JSON format where each object contains exactly TWO related bullet points (original + update):
[
    {
        "capability": "knowledge_update",
        "batch_numbers": "1, 2",
        "bullet_numbers": "9, 17",
        "bullet_points": "• **Financial & Budget:Cost Estimation:** Initial budget set at $12,500, including materials and labor for decoupled framing and MLV. | • **Conflict & Resolution:Budget Adjustment:** Contractor quoted $14,000, exceeding budget by $1,500; negotiated to reduce labor hours saving $1,000."
    }
]

Important formatting notes:
- The "batch_numbers" and "bullet_numbers" correspond to each other positionally
- "1, 2" and "9, 17" means: Batch 1 Bullet 9, Batch 2 Bullet 17
- Each object must contain exactly 2 bullet points separated by " | "
- Use comma-separated values for batch_number and bullet_number
- First bullet point should represent the original information
- Second bullet point should represent the update/change
- Focus on pairs that enable questions like "How did X change from the initial plan?"

Select 8-12 pairs of bullet points that demonstrate the clearest examples of information updates and changes.

NOTE: Only output the list without any explanation before or after the list.
"""
knowledge_update_special_bullets_prompt = """
This is a plan that contains detailed bullet points about a topic. This plan is used to generate realistic chat conversations between a user and an AI assistant, which are then used to evaluate the long-term memory capabilities of LLMs.

Your task is to analyze this plan and select PAIRS of related bullet points that would be most effective for testing knowledge update abilities when incorporated into chat conversations.

Analyze this plan and identify bullet points labeled as "Information Update" and match them with their corresponding original facts from earlier in the plan.

## INPUT DATA
- **PLAN**: <plan>

## CRITICAL REQUIREMENT: SPECIAL UPDATE BULLETS WITH ORIGINAL FACTS
Focus on bullet points that:
- **Are labeled "Information Update"**: Look specifically for bullet points with this exact label
- **Have corresponding original facts**: Find the earlier bullet point that contains the original information being updated
- **Show clear before/after relationships**: Original information paired with its explicit update or correction

For each "Information Update" bullet point you find:
1. **Locate the original fact** in an earlier bullet point that this update refers to
2. **Create a pair** with the original bullet point first, then the "Information Update" bullet point second
3. **Ensure clear connection** between the original fact and its update

Look specifically for "Information Update" bullet points that contain:
- Clear update language ("updated," "changed," "revised," "rescheduled," "increased," "decreased")
- References to modifications of previously mentioned information
- Corrections or adjustments to earlier facts
- Timeline or specification changes

Then match each update with its original fact from earlier bullet points.

Return your analysis in this exact JSON format where each object contains exactly TWO related bullet points (original + Information Update):
[
    {
        "capability": "knowledge_update",
        "batch_numbers": "1, 3",
        "bullet_numbers": "9, 31",
        "bullet_points": "• **Financial & Budget:Cost Estimation:** Initial budget set at $12,500, including materials and labor for decoupled framing and MLV. | Information Update: The initial framing materials purchase included an additional 10% surplus to accommodate unexpected cuts and errors."
    }
]

Important formatting notes:
- The "batch_numbers" and "bullet_numbers" correspond to each other positionally
- "1, 3" and "9, 31" means: Batch 1 Bullet 9 (original), Batch 3 Bullet 31 (Information Update)
- Each object must contain exactly 2 bullet points separated by " | "
- Use comma-separated values for batch_number and bullet_number
- First bullet point should represent the original information
- Second bullet point should be the "Information Update" labeled bullet
- Focus on pairs that enable questions like "How did the original plan change when you got the update?"

Select all "Information Update" bullet points and pair them with their corresponding original facts (approximately 10 pairs total).

NOTE: Only output the list without any explanation before or after the list.
"""

temporal_reasoning_prompt = """
This is a plan that contains detailed bullet points about a topic. This plan is used to generate realistic chat conversations between a user and an AI assistant, which are then used to evaluate the long-term memory capabilities of LLMs. 

Your task is to analyze this plan and select PAIRS of related bullet points that would be most effective for testing temporal reasoning abilities when incorporated into chat conversations.

Analyze this project plan and identify PAIRS of bullet points that enable testing duration calculations and sequence understanding between two events. Each pair should enable questions about time duration, sequence, or temporal relationships between two events.

## INPUT DATA
- **PLAN**: <plan>

## CRITICAL REQUIREMENT: BALANCED BATCH DISTRIBUTION
**SELECTION PRIORITY ORDER:**
1. **Pairs starting in Batches 1-3 (MEDIUM-HIGH PRIORITY)**: Select 40-50% of your pairs with at least one bullet from early batches
2. **Far-distance pairs (HIGH PRIORITY)**: Select 30-40% of pairs that span large batch distances (e.g., Batch 1 & Batch 6, Batch 2 & Batch 8, Batch 1 & Batch 7, etc.) to test long-term temporal reasoning
3. **Pairs spanning early to middle batches (MEDIUM PRIORITY)**: Select 10-15% of pairs that bridge early-to-middle timeline
4. **Pairs from later batches only (LOW PRIORITY)**: Select only 5-10% from purely later batches

Focus on bullet point pairs that:
- Enable duration calculations between two time points
- Show sequence relationships between events
- Allow comparison of timing across different batches
- Demonstrate temporal progression or changes over time
- Include scheduling, deadlines, or milestone comparisons

## EXPLICIT TIME MENTION REQUIREMENTS
**ONLY absolute dates count as explicit time mentions:**
- "May 15, 2024", "March 3rd", "January 20, 2025"
- "December 8, 2023", "April 22nd, 2024"
- "June 1, 2025", "September 15th, 2024"

**THESE DO NOT COUNT as explicit time mentions:**
- Specific times: "2:30 PM", "9:00 AM", "11:45 PM"
- Calendar references: "next Tuesday", "this Friday", "Monday morning"
- Specific weekdays: "Wednesday's meeting", "Saturday's event"
- Relative durations: "2 weeks", "3 months", "5 days"
- Time periods: "over time", "recently", "soon"
- Vague references: "later", "earlier", "afterwards"
- Duration spans: "within a month", "by next year"

## IMPORTANT TIME ANCHOR RULES:
1. If BOTH bullet points contain explicit absolute dates, use them as-is
2. If ONE bullet point lacks explicit absolute dates, prepend that bullet point with its batch's Time Anchor
3. If BOTH bullet points lack explicit absolute dates, prepend both with their respective Time Anchors

FORMAT EXAMPLES:
Case 1 - Both have time mentions (no Time Anchor needed):
Case 1 - Both have explicit absolute dates (no Time Anchor needed):
{
 "capability": "temporal_reasoning",
 "batch_numbers": "1, 2",
 "bullet_numbers": "17, 9",
 "bullet_points": "Meeting scheduled for May 15, 2024... | Deadline confirmed for June 3, 2024..."
}

Case 2 - Second bullet point lacks explicit absolute dates (add Time Anchor to second):
{
 "capability": "temporal_reasoning",
 "batch_numbers": "1, 2",
 "bullet_numbers": "17, 6",
 "bullet_points": "Meeting scheduled for May 15, 2024... | June 10, 2024 Increased quiz score from 75% to 88% over 2 weeks..."
}

Case 3 - Both bullet points lack explicit absolute dates (add Time Anchors to both):
{
 "capability": "temporal_reasoning",
 "batch_numbers": "3, 5",
 "bullet_numbers": "12, 8",
 "bullet_points": "July 5, 2024 Increased quiz score from 75% to 88% over 2 weeks... | August 20, 2024 Completed project within budget constraints..."
}

Return your analysis in this exact JSON format where each object contains exactly TWO related bullet points:
[
    {
        "capability": "temporal_reasoning",
        "batch_numbers": "1, 2",
        "bullet_numbers": "17, 9",
        "bullet_points": "Bullet Description: ... | Bullet Description: ..."
    }
]

Important formatting notes:
- The "batch_numbers" and "bullet_numbers" correspond to each other positionally
- "1, 2" and "17, 9" means: Batch 1 Bullet 17, Batch 2 Bullet 9
- Each object must contain exactly 2 bullet points separated by " | "
- Use comma-separated values for batch_number and bullet_number
- Add Time Anchors before bullet points that lack explicit time mentions
- Focus on pairs that enable duration calculation questions like "How many days between X and Y?"

Select 8-10 pairs of bullet points that would enable the most sophisticated temporal reasoning and duration calculation questions.

NOTE: Only output the list without any explanation before or after the list.
"""
ten_m_temporal_reasoning_prompt = """
This is a set of plans that contain detailed bullet points about various topics. These plans are used to generate realistic chat conversations between a user and an AI assistant, which are then used to evaluate the long-term memory capabilities of LLMs.

Your task is to analyze these plans and select PAIRS of related bullet points that would be most effective for testing temporal reasoning abilities when incorporated into chat conversations.

Analyze these project plans and identify PAIRS of bullet points that enable testing duration calculations and sequence understanding between two events across multiple plans. Each pair should enable questions about time duration, sequence, or temporal relationships between two events.

## INPUT DATA
- **PLANS**: <plans>

## CRITICAL REQUIREMENTS:
- Select exactly 3 pairs of related bullet points
- Each pair must contain exactly 2 bullet point indexes (MUST be from different plans)
- You MUST include the complete bullet point text for every single index you specify
- Distribute pairs across different plans when possible for better cross-plan temporal reasoning

## MANDATORY CROSS-PLAN REQUIREMENT:
EVERY single group MUST include bullet points from ALL plans provided in the input. No group should contain bullet points from only one plan. If a topic doesn't appear across all plans, do not select it. This is a hard requirement - any group that doesn't span all plans is invalid.

Focus on bullet point pairs that:
- Enable duration calculations between two time points
- Show sequence relationships between events across plans
- Allow comparison of timing across different batches and plans
- Demonstrate temporal progression or changes over time across multiple plans
- Include scheduling, deadlines, or milestone comparisons between plans

## EXPLICIT TIME MENTION REQUIREMENTS
**ONLY absolute dates count as explicit time mentions:**
- "May 15, 2024", "March 3rd", "January 20, 2025"
- "December 8, 2023", "April 22nd, 2024"
- "June 1, 2025", "September 15th, 2024"

**THESE DO NOT COUNT as explicit time mentions:**
- Specific times: "2:30 PM", "9:00 AM", "11:45 PM"
- Calendar references: "next Tuesday", "this Friday", "Monday morning"
- Specific weekdays: "Wednesday's meeting", "Saturday's event"
- Relative durations: "2 weeks", "3 months", "5 days"
- Time periods: "over time", "recently", "soon"
- Vague references: "later", "earlier", "afterwards"
- Duration spans: "within a month", "by next year"

## IMPORTANT TIME ANCHOR RULES:
1. If BOTH bullet points contain explicit absolute dates, use them as-is
2. If ONE bullet point lacks explicit absolute dates, prepend that bullet point with its batch's Time Anchor
3. If BOTH bullet points lack explicit absolute dates, prepend both with their respective Time Anchors

Return your analysis in this exact JSON format where each object contains exactly TWO related bullet points:
[
   {
      "capability": "temporal_reasoning",
      "index": {
         "plan 1": [[1, 17]],
         "plan 2": [[2, 9]]
      },
      "bullet_points": "Complete text of Plan 1 Batch 1 Bullet 17 | Complete text of Plan 2 Batch 2 Bullet 9"
   }
]

Important formatting notes:
- The "index" field contains a nested structure where each plan number maps to a list of [batch_number, bullet_number] pairs
- Each pair MUST be from different plans
- Use the EXACT plan numbers as they appear in the PLANS (e.g., "plan 1", "plan 2", "plan 3", etc.)
- "plan 1": [[1, 17]] and "plan 2": [[2, 9]] means Plan 1 Batch 1 Bullet 17 paired with Plan 2 Batch 2 Bullet 9
- Each object must contain exactly 2 bullet points separated by " | "
- The bullet_points field must contain the complete text for every single index specified
- Add Time Anchors before bullet points that lack explicit absolute dates
- Focus on pairs that enable duration calculation questions like "How many days between X and Y?" across plans

VALIDATION CHECK: Before outputting each group, verify that its "index" field contains entries for every single plan number from the input. If any plan is missing from a group, that group is invalid and must be discarded.

Return exactly 3 JSON objects, each representing one temporal pair, with COMPLETE bullet point text for every index specified.

NOTE: Only output the JSON list without any explanation before or after the list.
"""

preference_following_prompt = """
This is a plan that contains detailed bullet points about a topic. This plan is used to generate realistic chat conversations between a user and an AI assistant, which are then used to evaluate the long-term memory capabilities of LLMs.

Your task is to analyze this plan and select bullet points that would be most effective for testing preference following abilities when incorporated into chat conversations.

Analyze this plan and identify bullet points labeled as "Preference Statement" and select all.

## INPUT DATA
- **PLAN**: <plan>

Focus on bullet points with:
- **Explicit preference statements**: "I prefer", "I like", "I choose", "I favor"
- **Decision choices**: Selections between options with stated reasoning
- **Personal preferences**: Style, approach, method, or format preferences
- **Avoidance statements**: "I don't like", "I avoid", "I prefer not to"
- **Priority preferences**: What user values most or considers important

Prioritize preferences that:
- Are clearly stated with specific reasoning
- Involve choices between multiple options
- Contain detailed preference explanations
- Include comparative preferences (X over Y)
- Express strong preferences or dislikes
- Relate to recurring decisions or situations

NOTE: ONLY CONSIDER ''PREFERENCE'' NOT INSTRUCTION.

Return your analysis in this exact JSON format:
[
    {
        "capability": "preference_following",
        "batch_numbers": 1,
        "bullet_numbers": 17,
        "bullet_points": "• **Preference Statement:** I prefer materials that balance cost and performance; chose 3.5 lb/ft² MLV despite 20% higher price."
    }
]

Important formatting notes:
- The "batch_numbers" and "bullet_numbers" correspond to each other positionally
- "1" and "17" means: Batch 1 Bullet 17

Select ONLY <bullet_number> bullet points total that would generate the highest quality preference following questions.

NOTE: Only output the list without any explanation before or after the list.
"""
ten_m_preference_following_prompt = """
This is a plan that contains detailed bullet points about a topic. This plan is used to generate realistic chat conversations between a user and an AI assistant, which are then used to evaluate the long-term memory capabilities of LLMs.

Your task is to analyze this plan and select bullet points that would be most effective for testing preference following abilities when incorporated into chat conversations.

Analyze this plan and identify bullet points that express user preferences.

## INPUT DATA
- **PLAN**: <plan>

Focus on bullet points with:
- **Explicit preference statements**: "I prefer", "I like", "I choose", "I favor"
- **Decision choices**: Selections between options with stated reasoning
- **Personal preferences**: Style, approach, method, or format preferences
- **Avoidance statements**: "I don't like", "I avoid", "I prefer not to"
- **Priority preferences**: What user values most or considers important

Prioritize preferences that:
- Are clearly stated with specific reasoning
- Involve choices between multiple options
- Contain detailed preference explanations
- Include comparative preferences (X over Y)
- Express strong preferences or dislikes
- Relate to recurring decisions or situations

NOTE: ONLY CONSIDER ''PREFERENCE'' NOT INSTRUCTION.

Return your analysis in this exact JSON format:
[
    {
        "capability": "preference_following",
        "batch_numbers": 1,
        "bullet_numbers": 17,
        "bullet_points": "• **Preference Statement:** I prefer materials that balance cost and performance; chose 3.5 lb/ft² MLV despite 20% higher price."
    }
]

Important formatting notes:
- The "batch_numbers" and "bullet_numbers" correspond to each other positionally
- "1" and "17" means: Batch 1 Bullet 17

Select ONLY <bullet_number> bullet points total that would generate the highest quality preference following questions.

NOTE: Only output the list without any explanation before or after the list.
"""

event_ordering_prompt = """
This is a plan that contains detailed bullet points about a topic. This plan is used to generate realistic chat conversations between a user and an AI assistant, which are then used to evaluate the long-term memory capabilities of LLMs. 

Your task is to analyze this plan and select GROUPS of related bullet points that would be most effective for testing event ordering abilities when incorporated into chat conversations.

Event ordering tests whether the LLM can recall the chronological order in which events or topics were MENTIONED in the conversation, regardless of when the actual events occurred in real life.

Analyze this plan and identify GROUPS of 8-12 or more related bullet points that represent the same topic/theme mentioned across different batches, enabling testing of mention-order recall and conversation sequence understanding.

## INPUT DATA
- **PLAN**: <plan>

## CRITICAL REQUIREMENT: EARLY BATCH PRIORITIZATION
**SELECTION PRIORITY ORDER:**
1. **Groups starting in Batches 1-3 (HIGHEST PRIORITY)**: Select 70-80% of your groups with first mention in early batches
2. **Groups spanning early to middle batches (MEDIUM PRIORITY)**: Select 10-20% of groups that bridge early-to-middle timeline
3. **Groups from later batches only (LOW PRIORITY)**: Select only 5-10% from purely later batches

Focus on bullet point groups that show:
- **Same person mentioned multiple times**: Different interactions or mentions of the same person across batches
- **Same component/process discussed repeatedly**: Multiple mentions of the same equipment, material, or process
- **Same location/venue referenced**: Multiple mentions of the same place or address
- **Same decision/topic revisited**: The same subject brought up in different conversation sessions
- **Same problem/solution mentioned**: Multiple references to the same issue across different times
- **Same financial item tracked**: Multiple mentions of the same cost, budget item, or expense

Prioritize bullet point groups that:
- Contain 8-12 mentions of the same topic across different batches
- Enable questions about "In what order events X,Y,Z,... happen?" Or ...
- Allow testing of conversation chronology rather than real-world event chronology  
- Test recall of mention sequence: "Which did I talk about first, second, third?"
- Focus on the order topics appeared in conversation, not when events actually happened
- Create opportunities to test conversational memory rather than factual timeline memory

Return your analysis in this exact JSON format where each object contains 3+ bullet points about the same topic across different batches:
[
    {
        "capability": "event_ordering",
        "batch_numbers": "1, 3, 5, 7",
        "bullet_numbers": "22, 18, 11, 27",
        "bullet_points": "• **Character & Relationship:Acoustic Consultant:** Met Rami Al-Hassan at Bahrain Acoustic Expo on Feb 20; he recommended HVAC silencing at $2,200. | • **Character & Relationship:Acoustic Consultant:** Rami conducted mid-project site visit April 3, advised on bass trap repositioning to improve 5 dB absorption. | • **Character & Relationship:Acoustic Consultant:** Rami praised progress in May 1 email; suggested minor EQ tweaks. | • **Character & Relationship:Acoustic Consultant:** Rami praised final results August 20; recommended ongoing maintenance and periodic EQ checks."
    }
]

Important formatting notes:
- The "batch_numbers" and "bullet_numbers" correspond to each other positionally
- "1, 2, 3, 5, 7" and "22, 18, 11, 27" means: Batch 1 Bullet 22, Batch 3 Bullet 18, Batch 5 Bullet 11, Batch 7 Bullet 27
- Each object must contain 8-12 related bullet points separated by " | "
- Use comma-separated values for batch_number and bullet_number  
- All bullet points must reference the same topic/person/component/theme
- Focus on groups that enable mention-order questions
- Test conversational chronology, not real-world event chronology

Select 8-10 groups of bullet points that would enable the most sophisticated mention-order and conversation sequence questions.

CRITICAL NOTE: DO NOT consider bulletpoint names for selecting the bullets. ONLY consider the bullets contents.
NOTE: Only output the list without any explanation before or after the list.
"""
event_ordering_prompt_detailed = """
This is a plan that contains detailed bullet points about a topic. 
This plan is used to generate realistic chat conversations between a user and an AI assistant, which are then used to evaluate the long-term memory capabilities of LLMs. 

Your task is to analyze this plan and select GROUPS of related bullet points that would be most effective for testing event ordering abilities when incorporated into chat conversations.

Event ordering tests whether the LLM can recall the chronological order in which events or topics were MENTIONED in the conversation, regardless of when the actual events occurred in real life.

Analyze this plan and identify GROUPS of ALL related bullet points that represent the same entity/content mentioned across different batches, enabling testing of mention-order recall and conversation sequence understanding.

## INPUT DATA
- **PLAN**: <plan>

## CRITICAL REQUIREMENT: EARLY BATCH PRIORITIZATION
**SELECTION PRIORITY ORDER:**
1. **Groups starting in Batches 1-3 (HIGHEST PRIORITY)**: Select 70-80% of your groups with first mention in early batches
2. **Groups spanning early to middle batches (MEDIUM PRIORITY)**: Select 10-20% of groups that bridge early-to-middle timeline
3. **Groups from later batches only (LOW PRIORITY)**: Select only 5-10% from purely later batches

## CRITICAL REQUIREMENT: COMPREHENSIVE MENTION COLLECTION
- You MUST include ALL bullet points that mention the same entity/content across ALL batches
- Scan the ENTIRE plan systematically to find ALL mentions of the same entity/content
- Missing related mentions will result in incomplete mention-order questions
- Prioritize completeness over arbitrary size limits

## CRITICAL REQUIREMENT: CONTENT-BASED ANALYSIS
**ANALYZE BULLET CONTENT, NOT CATEGORY NAMES:**
- Read the actual bullet point text to identify mentions of entitites (people, places, items, topics, amounts, ...)
- The same entity might appear in different category types - include ALL mentions across all categories

**SEARCH METHODOLOGY:**
1. **Identify key entities** in bullet content: names, places, amounts, equipment, topics
2. **Search ALL batches** for any mention of these entities in ANY category
3. **Group by content similarity**, not category similarity  
4. **Include ALL mentions** regardless of how they're categorized

## Focus on bullet point groups that show ALL mentions of:
- **Same person or character**: EVERY interaction or mention of the same individual across ALL batches (e.g., colleagues, clients, teammates, public figures, historical characters)
- **Same object, item, or component**: ALL mentions of the same product, tool, material, asset, or resource
- **Same place or setting**: ALL references to the same physical or virtual location (e.g., countries, cities, venues, websites, platforms)
- **Same decision, plan, or topic**: ALL times the same concept, goal, rule, policy, or subject was discussed
- **Same issue, challenge, or solution**: ALL mentions of the same metric, quantity, budget, score, date, or technical parameter
- **Same task, project, or process**: ALL mentions of the same workflow, activity, research task, experiment, or creative process

Prioritize bullet point groups that:
- Enable questions about "In what order events X,Y,Z,... happen?" Or ...
- Allow testing of conversation chronology rather than real-world event chronology  
- Test recall of FULL mention sequence from first to last appearance
- Focus on the order topics appeared in conversation, not when events actually happened
- Create opportunities to test conversational memory rather than factual timeline memory
- Create opportunities to test complete conversational memory of topic evolution
- ALL mentions of the same workflow, activity, research task, experiment, or creative process

Return your analysis in this exact JSON format where each object contains ALL related bullet points about the same entity/content across different batches:
[
    {
        "capability": "event_ordering",
        "batch_numbers": "1, 3, 5, 7",
        "bullet_numbers": "22, 18, 11, 27",
        "bullet_points": "• **Person & Interaction:Project Mentor:** Met Dr. Elena Vargas at the International Research Summit on March 5; she suggested adopting a new data analysis method costing $3,200. | • **Person & Interaction:Project Mentor:** Elena attended a mid-project review meeting on April 18, recommended reorganizing the methodology to improve accuracy by 7%. | • **Person & Interaction:Project Mentor:** Elena commended progress in a May 30 report; proposed minor adjustments to data visualization. | • **Person & Interaction:Project Mentor:** Elena praised final project results on September 12; advised scheduling quarterly reviews and updating the methodology annually."
    }
]

**CRITICAL: INCLUDE ALL MENTIONS, NOT JUST ONE PER BATCH**
- If an entity appears 3 times in Batch 1, include ALL 3 bullet points
- If an entity appears 2 times in Batch 2, include ALL 2 bullet points  
- If an entity appears 1 time in Batch 3, include that 1 bullet point
- The goal is COMPLETE mention coverage, not sampling

Important formatting notes:
- The "batch_numbers" and "bullet_numbers" correspond to each other positionally
- "1, 2, 3, 5, 7" and "22, 18, 11, 27" means: Batch 1 Bullet 22, Batch 3 Bullet 18, Batch 5 Bullet 11, Batch 7 Bullet 27
- Each object must contain all the related bullet points separated by " | "
- Use comma-separated values for batch_number and bullet_number  
- All bullet points must reference the same entity, subject, or recurring element — such as a specific person, location, object, process, decision, event, or concept — consistently across all mentions.
- Focus on groups that enable mention-order questions
- **NO LIMIT on number of bullet points** - include as many as needed for complete coverage

CRITICAL NOTES: 
- **ANALYZE BULLET CONTENT, NOT CATEGORY NAMES**: Search for mentions of entities in the actual text
- **IGNORE CATEGORY LABELS**: The same entity mentioned in different category types should all be grouped together
- **COMPREHENSIVE ENTITY SEARCH**: For each entity, scan ALL batches and ALL categories for any mention
- Include ALL mentions regardless of bullet point category if they reference the same entity in the content

Select ALL groups of bullet points with COMPLETE mention coverage that would enable the most sophisticated and comprehensive mention-order and conversation sequence questions.

NOTE: Only output the list without any explanation before or after the list.
"""
ten_m_event_ordering_prompt_detailed = """
This is a set of plans that contain detailed bullet points about various topics. These plans are used to generate realistic chat conversations between a user and an AI assistant, which are then used to evaluate the long-term memory capabilities of LLMs.

Your task is to analyze these plans and select GROUPS of related bullet points that would be most effective for testing event ordering abilities when incorporated into chat conversations.

Event ordering tests whether the LLM can recall the chronological order in which events or topics were MENTIONED in the conversation, regardless of when the actual events occurred in real life.

Analyze these project plans and identify GROUPS of 3 or more related bullet points that represent the same topic/theme mentioned across different batches and plans, enabling testing of mention-order recall and conversation sequence understanding.

## INPUT DATA
- **PLANS**: <plans>

## CRITICAL REQUIREMENTS:
- Select exactly 2 groups of related bullet points
- Each group must contain between 5 and 10 bullet point indexes total (spread across all plans) and MUST cover all the plans
- For each object, across all plans, MUST have between 5 and 10 indexes, not more not less
- You MUST include the complete bullet point text for every single index you specify
- Distribute indexes across different plans when possible for better cross-plan mention-order reasoning
- If you cannot fit all bullet point text due to length limits, reduce the number of groups rather than omitting text

## MANDATORY CROSS-PLAN REQUIREMENT:
EVERY single group MUST include bullet points from ALL plans provided in the input. No group should contain bullet points from only one plan. If a topic doesn't appear across all plans, do not select it. This is a hard requirement - any group that doesn't span all plans is invalid.

## CRITICAL REQUIREMENT: COMPREHENSIVE MENTION COLLECTION
- You MUST include ALL bullet points that mention the same topic/theme across ALL batches and ALL plans
- Scan ALL plans systematically to find ALL mentions of the same topic
- Missing related mentions will result in incomplete mention-order questions
- Prioritize completeness over arbitrary size limits

## CRITICAL REQUIREMENT: CONTENT-BASED ANALYSIS
**ANALYZE BULLET CONTENT, NOT CATEGORY NAMES:**
- Read the actual bullet point text to identify mentions of entitites (people, places, items, topics, amounts, ...)
- The same entity might appear in different category types - include ALL mentions across all categories

**SEARCH METHODOLOGY:**
1. **Identify key entities** in bullet content: names, places, amounts, equipment, topics
2. **Search ALL batches** for any mention of these entities in ANY category
3. **Group by content similarity**, not category similarity  
4. **Include ALL mentions** regardless of how they're categorized

## Focus on bullet point groups that show ALL mentions of:
- **Same person or character**: EVERY interaction or mention of the same individual across ALL batches (e.g., colleagues, clients, teammates, public figures, historical characters)
- **Same object, item, or component**: ALL mentions of the same product, tool, material, asset, or resource
- **Same place or setting**: ALL references to the same physical or virtual location (e.g., countries, cities, venues, websites, platforms)
- **Same decision, plan, or topic**: ALL times the same concept, goal, rule, policy, or subject was discussed
- **Same issue, challenge, or solution**: ALL mentions of the same metric, quantity, budget, score, date, or technical parameter
- **Same task, project, or process**: ALL mentions of the same workflow, activity, research task, experiment, or creative process

Prioritize bullet point groups that:
- Enable questions about "In what order events X,Y,Z,... happen?" Or ...
- Allow testing of conversation chronology rather than real-world event chronology  
- Test recall of FULL mention sequence from first to last appearance
- Focus on the order topics appeared in conversation, not when events actually happened
- Create opportunities to test conversational memory rather than factual timeline memory
- Create opportunities to test complete conversational memory of topic evolution
- ALL mentions of the same workflow, activity, research task, experiment, or creative process

Return your analysis in this exact JSON format where each object contains 3+ bullet points about the same topic across different batches and plans:
[
    {
        "capability": "event_ordering",
        "index": {
            "plan 1": [[1, 22], [5, 11]],
            "plan 2": [[3, 18]],
            "plan 3": [[7, 27]]
        },
        "bullet_points": "Complete text of Plan 1 Batch 1 Bullet 22 | Complete text of Plan 2 Batch 3 Bullet 18 | Complete text of Plan 1 Batch 5 Bullet 11 | Complete text of Plan 3 Batch 7 Bullet 27"
    }
]

Important formatting notes:
- The "index" field contains a nested structure where each plan number maps to a list of [batch_number, bullet_number] pairs
- Indexes must cover all the plans
- Use the EXACT plan numbers as they appear in the input data (e.g., "plan 1", "plan 2", "plan 3", etc.)
- Each group should contain between 5-10 total bullet point indexes across all plans
- All bullet points must reference the same entity, subject, or recurring element — such as a specific person, location, object, process, decision, event, or concept — consistently across all mentions.
- Include all plans that contain mentions of the same topic in the index
- Separate multiple bullet_point entries with " | "
- The bullet_points field must contain the complete text for every single index specified
- All bullet points must reference the same topic/person/component/theme across plans
- Focus on groups that enable mention-order questions across multiple plans

CRITICAL NOTES:
- DO NOT consider bullet point category names for selecting bullets. ONLY consider bullet point contents.
- Include ALL mentions regardless of bullet point category if they reference the same topic across plans
- Focus on tracking how the same topic evolves across different conversation sessions (plans)

VALIDATION CHECK: Before outputting each group, verify that its "index" field contains entries for every single plan number from the input. If any plan is missing from a group, that group is invalid and must be discarded.

Return exactly 2 JSON objects representing groups with COMPLETE mention coverage that would enable the most sophisticated and comprehensive mention-order and conversation sequence questions across multiple plans.

NOTE: Only output the JSON list without any explanation before or after the list.
"""

contradiction_resolution_prompt = """
This is a plan that contains detailed bullet points about a topic. This plan is used to generate realistic chat conversations between a user and an AI assistant, which are then used to evaluate the long-term memory capabilities of LLMs. 

Your task is to analyze this plan and select PAIRS of bullet points that would be most effective for testing contradiction resolution abilities when incorporated into chat conversations.

Contradiction resolution tests whether the LLM can detect and appropriately handle impossible contradictions - statements that logically cannot both be true simultaneously.

Analyze this project plan and identify PAIRS of bullet points where one completely contradicts the other with impossible contradictions. Each pair should contain statements that are logically incompatible and cannot both be true.

## INPUT DATA
- **PLAN**: <plan>

Focus on bullet point pairs that show:
- **Never-Statement Violations**: One bullet says "never" did something, another shows they did it
- **Always-Statement Violations**: One bullet claims "always" pattern, another breaks that pattern  
- **Only-Statement Conflicts**: One bullet claims exclusivity ("only"), another contradicts it
- **Impossible Reversals**: Age going backward, timeline impossibilities, logical reversals
- **Dead-Alive Contradictions**: References to deceased people being active
- **Mutually Exclusive States**: Being in two places simultaneously, having contradictory capabilities
- **Absolute Negations**: Claiming something is impossible then showing it happened

**Types of Impossible Contradictions to look for:**
1. **Never-Statement Violations**: "Never attended X" vs "Attended X event"
2. **Always-Statement Violations**: "Always lived in Y" vs "Moved from Z to Y"  
3. **Only-Statement Conflicts**: "Only child" vs "Has siblings"
4. **Timeline Impossibilities**: Events happening in wrong chronological order
5. **Capability Contradictions**: "Cannot do X" vs "Successfully did X"
6. **Location Impossibilities**: Being in two places at once
7. **Relationship Contradictions**: "Never met person" vs "Long friendship with person"

Prioritize bullet point pairs that:
- Contain completely impossible contradictions that cannot be resolved or explained
- Use absolute language ("never," "always," "only," "impossible," "cannot")
- Create clear logical impossibilities rather than simple inconsistencies
- Enable questions about detecting fundamental contradictions
- Test whether the AI can identify when statements are mutually exclusive
- Focus on contradictions that are objectively impossible, not subjective differences

Return your analysis in this exact JSON format where each object contains exactly TWO contradicting bullet points:
[
    {
        "capability": "contradiction_resolution",
        "batch_numbers": "1, 8",
        "bullet_numbers": "30, 29",
        "bullet_points": "• **Logical Contradiction:** Jeremiah has never attended any Bahrain Jazz Festival events. | • **Character & Relationship:Close Friend:** Jeremiah, 37, met at Bahrain Jazz Festival 2015, recommended an acoustic consultant."
    }
]

Important formatting notes:
- The "batch_numbers" and "bullet_numbers" correspond to each other positionally
- "1, 8" and "30, 29" means: Batch 1 Bullet 30, Batch 8 Bullet 29
- Each object must contain exactly 2 bullet points separated by " | "
- Use comma-separated values for batch_number and bullet_number
- First bullet point can be the contradiction marker or the contradicted statement
- Second bullet point should directly contradict the first with impossible logic
- Focus on pairs that test detection of fundamental logical impossibilities

Select <bullet_number> pairs of bullet points that demonstrate the clearest impossible contradictions for testing contradiction resolution abilities.

NOTE: Only output the list without any explanation before or after the list.
"""

summarization_prompt = """
This is a plan that contains detailed bullet points about a topic. This plan is used to generate realistic chat conversations between a user and an AI assistant, which are then used to evaluate the long-term memory capabilities of LLMs. 

Your task is to analyze this plan and select GROUPS of bullet points that would be most effective for testing summarization abilities when incorporated into chat conversations.

Summarization tests whether the LLM can synthesize and condense information from across multiple conversation sessions into coherent, comprehensive summaries.

Analyze this plan and identify GROUPS of 8-12 related bullet points that represent topics suitable for summarization testing. Groups can vary in size depending on the richness and complexity of the topic.

## INPUT DATA
- **PLAN**: <plan>

## CRITICAL REQUIREMENT: EARLY BATCH PRIORITIZATION
**SELECTION PRIORITY ORDER:**
1. **Groups starting in Batches 1-3 (HIGHEST PRIORITY)**: Select 60-70% of your groups with foundational content from early batches
2. **Groups spanning early to middle batches (MEDIUM PRIORITY)**: Select 20-30% of groups that bridge early-to-middle timeline
3. **Groups from later batches only (LOW PRIORITY)**: Select only 10-20% from purely later batches

## CRITICAL REQUIREMENT: CONTENT-BASED ANALYSIS
**ANALYZE BULLET CONTENT, NOT CATEGORY NAMES:**
- Read the actual bullet point text to identify mentions of entities (people, places, items, topics, amounts, processes)
- The same entity might appear in different category types - include mentions across all categories
- The same process might appear in different category types - include mentions across all categories
- The same project might appear in different category types - include mentions across all categories

**SEARCH METHODOLOGY:**
1. **Identify key entities** in bullet content: names, places, amounts, equipment, topics, processes
2. **Search ALL batches** for any mention of these entities in ANY category
3. **Group by content similarity**, not category similarity  
4. **Include 8-12 mentions** regardless of how they're categorized

Focus on complete topic clusters that enable summarization of:
- **Entity or Relationship Histories**: interactions, developments, or changes related to a specific person, organization, group, or other identifiable entity across the entire plan (complete relationship or entity arc)
- **End-to-End Processes**: steps, stages, or phases of a specific process, workflow, or methodology from initiation to conclusion across the entire plan (no missing steps)
- **Resource or Asset Lifecycles**: mentions of acquisition, allocation, usage, modification, and outcomes for a specific resource, asset, or material across the entire plan
- **Decision and Strategy Journeys**: details of decision-making, planning, and strategy development from problem identification through implementation across the entire plan
- **Problem/Challenge Resolution Narratives**: instances of identifying, analyzing, addressing, and resolving a particular issue or challenge across the entire plan
- **Timeline-Driven Developments**: events and updates showing chronological evolution of a specific project, initiative, or topic across the entire plan
- **Knowledge or Skill Development Sequences**: progress updates, milestones, and learning activities related to acquiring or improving a specific skill or knowledge area across the entire plan
- **Discussion and Agreement Processes**: discussions, debates, negotiations, and agreements related to a specific matter across the entire plan

Prioritize bullet point groups that:
- Contain rich, interconnected information suitable for synthesis
- Enable questions like "Can you summarize my interactions with X?" or "Summarize the [X] process"
- Include both factual/quantitative details and qualitative/narrative elements for well-rounded summaries
- Have varying complexity levels (simple single-topic vs. complex multi-faceted stories)
- Allow testing of information condensation across multiple conversation sessions
- Include both factual details and narrative elements for comprehensive summarization
- Create opportunities to test synthesis of scattered information into coherent narratives

Return your analysis in this exact JSON format where each object contains 8-12 related bullet points:
[
    {
        "capability": "summarization",
        "batch_numbers": "1, 1, 2, 3, 4, 5",
        "bullet_numbers": "5, 22, 18, 19, 23, 31",
        "bullet_points": "• **Character & Relationship:Close Friend:** Jeremiah, 37, met at festival, recommended consultant. | • **Conflict & Resolution:Relationship Boundaries:** Jeremiah requested exclusive studio access; agreed to 3 hours only. | • **Character & Relationship:Close Friend:** Jeremiah helped install MLV, bringing snacks from bakery. | • **Character & Relationship:Close Friend:** Jeremiah invited me to music club to test prototype. | • **Character & Relationship:Close Friend:** Jeremiah brought dinner during late work session. | • **Goals & Progress:Milestone Celebration:** Hosted listening party with Jeremiah, Jon, and Tonya."
    }
]

Important formatting notes:
- The "batch_numbers" and "bullet_numbers" correspond to each other positionally
- "1, 1, 2, 3, 4, 5" and "5, 22, 18, 19, 23, 31" means: Batch 1 Bullet 5, Batch 1 Bullet 22, Batch 2 Bullet 18, Batch 3 Bullet 19, Batch 4 Bullet 23, Batch 5 Bullet 31
- Each bullet point separated by " | "
- Use comma-separated values for batch_number and bullet_number
- Vary group sizes based on topic complexity and richness
- Focus on groups that enable comprehensive summarization questions
- Include both simple single-topic and complex multi-topic groups
- **NO LIMIT on number of bullet points** - include as many as needed for complete coverage

CRITICAL NOTES: 
- **ANALYZE BULLET CONTENT, NOT CATEGORY NAMES**: Search for mentions of entities in the actual text
- **IGNORE CATEGORY LABELS**: The same entity mentioned in different category types should all be grouped together
- **COMPREHENSIVE ENTITY SEARCH**: For each entity/topic/process, scan ALL batches and ALL categories for any mention
- Include 8-12 mentions regardless of bullet point category if they reference the same entity/topic in the content

Select 7-9 groups of bullet points with COMPLETE mention coverage that would enable the most sophisticated and comprehensive summarization questions across different complexity levels.

NOTE: Only output the list without any explanation before or after the list.
"""
ten_m_summarization_prompt = """
This is a set of plans that contain detailed bullet points about various topics. These plans are used to generate realistic chat conversations between a user and an AI assistant, which are then used to evaluate the long-term memory capabilities of LLMs.

Your task is to analyze these plans and select GROUPS of bullet points that would be most effective for testing summarization abilities when incorporated into chat conversations.

Summarization tests whether the LLM can synthesize and condense information from across multiple conversation sessions and plans into coherent, comprehensive summaries.

Analyze these project plans and identify GROUPS of ALL related bullet points that represent topics suitable for summarization testing across multiple plans. Groups can vary in size depending on the richness and complexity of the topic.

## INPUT DATA
- **PLANS**: <plans>

## CRITICAL REQUIREMENTS:
- Select exactly 2 groups of related bullet points
- Each group must contain between ALL the realted bullet point indexes total (spread across all plans) and MUST cover all the plans
- You MUST include the complete bullet point text for every single index you specify
- Distribute indexes across different plans when possible for better cross-plan summarization
- If you cannot fit all bullet point text due to length limits, reduce the number of groups rather than omitting text

## MANDATORY CROSS-PLAN REQUIREMENT:
EVERY single group MUST include bullet points from ALL plans provided in the input. No group should contain bullet points from only one plan. If a topic doesn't appear across all plans, do not select it. This is a hard requirement - any group that doesn't span all plans is invalid.

Focus on complete topic clusters that enable summarization of:
- **Entity or Relationship Histories**: ALL interactions, developments, or changes related to a specific person, organization, group, or other identifiable entity across the entire plan (complete relationship or entity arc)
- **End-to-End Processes**: ALL steps, stages, or phases of a specific process, workflow, or methodology from initiation to conclusion across the entire plan (no missing steps)
- **Resource or Asset Lifecycles**: ALL mentions of acquisition, allocation, usage, modification, and outcomes for a specific resource, asset, or material across the entire plan
- **Decision and Strategy Journeys**: ALL details of decision-making, planning, and strategy development from problem identification through implementation across the entire plan
- **Problem/Challenge Resolution Narratives**: ALL instances of identifying, analyzing, addressing, and resolving a particular issue or challenge across the entire plan
- **Timeline-Driven Developments**: ALL events and updates showing chronological evolution of a specific project, initiative, or topic across the entire plan
- **Knowledge or Skill Development Sequences**: ALL progress updates, milestones, and learning activities related to acquiring or improving a specific skill or knowledge area across the entire plan
- **Discussion and Agreement Processes**: ALL discussions, debates, negotiations, and agreements related to a specific matter across the entire plan

Prioritize bullet point groups that:
- Contain rich, interconnected information suitable for synthesis across multiple plans
- Enable questions like "Can you summarize my interactions with X across all our conversations?" or "Summarize the [X] process across all projects"
- Have varying complexity levels (simple single-topic vs. complex multi-faceted stories spanning plans)
- Include both factual/quantitative details and qualitative/narrative elements for well-rounded summaries
- Allow testing of information condensation across multiple conversation sessions and plans
- Include both factual details and narrative elements for comprehensive cross-plan summarization
- Create opportunities to test synthesis of scattered information into coherent narratives across plans

Return your analysis in this exact JSON format where each object contains 2-8 related bullet points:
[
    {
        "capability": "summarization",
        "index": {
            "plan 1": [[1, 22], [2, 18]],
            "plan 2": [[4, 19]],
            "plan 3": [[5, 23]]
        },
        "bullet_points": "Complete text of Plan 1 Batch 1 Bullet 22 | Complete text of Plan 1 Batch 2 Bullet 18 | Complete text of Plan 2 Batch 4 Bullet 19 | Complete text of Plan 3 Batch 5 Bullet 23"
    }
]

Important formatting notes:
- The "index" field contains a nested structure where each plan number maps to a list of [batch_number, bullet_number] pairs
- Use the EXACT plan numbers as they appear in the input data (e.g., "plan 1", "plan 2", "plan 3", etc.)
- Indexes must cover all the plans
- Each group should contain ALL the related bullet point indexes across all plans
- Include all plans that contain related information in the index
- Separate multiple bullet_point entries with " | "
- The bullet_points field must contain the complete text for every single index specified
- Vary group sizes based on topic complexity and richness across plans
- Focus on groups that enable comprehensive summarization questions across multiple plans
- Include both simple single-topic and complex multi-topic groups spanning plans

VALIDATION CHECK: Before outputting each group, verify that its "index" field contains entries for every single plan number from the input. If any plan is missing from a group, that group is invalid and must be discarded.

Return exactly 2 JSON objects representing groups with varying sizes that would enable the most sophisticated summarization questions across different complexity levels and multiple plans.

NOTE: Only output the JSON list without any explanation before or after the list.
"""

instruction_following_prompt = """
This is a plan that contains detailed bullet points about a topic. This plan is used to generate realistic chat conversations between a user and an AI assistant, which are then used to evaluate the long-term memory capabilities of LLMs.

Your task is to analyze this plan and select bullet points that would be most effective for testing instruction following abilities when incorporated into chat conversations.

Analyze this plan and identify bullet points that contain user instructions ideal for testing whether the LLM remembers and follows user-given instructions.

## INPUT DATA
- **PLAN**: <plan>

Focus on bullet points with:
- **User Instruction** category/label
- **Explicit instruction statements**: "Always", "Never", "When I ask about X, do Y"
- **Behavioral directives**: How the AI should respond or behave
- **Format instructions**: Specific response formats or structures requested
- **Content instructions**: What to include or exclude in responses
- **Process instructions**: How to handle specific types of requests

Look specifically for bullet points labeled as "User Instruction" that contain:
- Clear directive language ("Always provide", "Never include", "When I ask")
- Specific behavioral expectations for the AI assistant
- Conditional instructions ("When I ask about X, do Y")
- Response formatting requirements
- Content inclusion/exclusion rules

Return your analysis in this exact JSON format:
[
    {
        "capability": "instruction_following",
        "batch_numbers": 1,
        "bullet_numbers": 32,
        "bullet_points": "User Instruction: Always provide detailed cost breakdowns when I ask about budget estimates."
    }
]

Important formatting notes:
- The "batch_numbers" and "bullet_numbers" correspond to each other positionally
- "1" and "32" means: Batch 1 Bullet 32
- Include the full bullet point text as it appears in the plan
- Focus specifically on "User Instruction" labeled bullet points

Select all bullet points labeled as "User Instruction" from each batch (approximately 10 total).

NOTE: Only output the list without any explanation before or after the list.
"""

# ================================ qa generation various levels ================================

information_extraction_probing_question_easy_prompt = """
You are tasked with generating a probing question to test information extraction capabilities of LLMs. You will be given a bullet point and the corresponding multi-turn dialog between a user and assistant that incorporates this bullet point information.

Your task is to create ONE question that tests whether an LLM can precisely extract and recall specific factual details from the conversation.

## INPUT DATA
- **BULLET POINT**: <bullet_point>
- **CONVERSATION TURNS**: <conversation_turns>

## CRITICAL REQUIREMENT: EASY INFORMATION EXTRACTION
- The question should test information that was mentioned once or embedded in context
- Focus on details that were stated within broader discussions but clearly present
- Test straightforward recall of facts that appeared in context but weren't necessarily emphasized
- Ask for information that requires basic attention to extract from surrounding context
- Remove ALL specific details from the question that would give away the answer

## FORBIDDEN QUESTION ELEMENTS
- Do NOT repeat specific names, numbers, or details being tested
- Do NOT mention key characteristics or attributes being extracted
- Do NOT include descriptive words that hint at the answer
- Do NOT reference specific categories or types being tested
- Do NOT use qualifying details that narrow down the answer

## QUESTION GENERATION GUIDELINES
Focus on extracting contextually embedded:
- **Numbers & Units: specific amounts, prices, durations, counts, scores, measurements, percentages.
- **Named Entities: people, teams, organizations, brands, models, products, venues, platforms.
- **Temporal Details: exact dates, days, times, deadlines, appointment slots, event schedules.
- **Locations & Contacts: cities, addresses, venues, URLs, emails, phone numbers, handles.
- **Specifications & Attributes: model names, versions, ratings, sizes, ingredients, requirements, thresholds.
- **Quoted/Exact Wording: brief statements, instructions, or constraints the user phrased specifically.
- **Procedures & Steps: a particular step, method, setting, technique, or criterion within a larger process.
- **Statuses & Outcomes: current state, results, conditions, eligibility, availability.
- **Relationships & Roles: affiliations, responsibilities, dependencies, who does what for whom.

## DIRECT QUESTIONING STRATEGIES
1. **Contextual Fact Questions**: "What [specific detail] did I mention about [topic]?"
2. **Embedded Number Recall**: "How much did I say [item/service] cost?" / "What quantity did I mention for [item]?"
3. **Context Date/Time Questions**: "When did I mention [event] happened?" / "What time did I say [meeting] was scheduled?"
4. **Embedded Location Questions**: "Where did I say I met [person]?" / "What location did I mention for [event]?"
5. **Context Detail Questions**: "What [specification] did I mention for [item]?" / "Which [brand/model] did I say I was using?"
6. **Process Detail Questions**: "What step did I mention for [process]?" / "How did I say to [accomplish task]?"
7. **Status Information Questions**: "What condition did I mention about [item]?" / "What outcome did I describe for [situation]?"
8. **Relationship Questions**: "Who did I say [person] worked for?" / "What connection did I mention between [X] and [Y]?"

## QUESTION LANGUAGE REQUIREMENTS
- Write questions as if the USER is asking them naturally
- **If testing information from USER messages**: Use first person ("I", "my", "me") in question → Answer uses ("you", "your")
  - Example: "How did I decide on the location?" → "You decided on the location because..."
- **If testing information from ASSISTANT messages**: Use second person ("you", "your") in question → Answer uses ("I", "my") 
  - Example: "What steps did you suggest for handling this?" → "I suggested doing..."
- Avoid phrases like "according to the conversation", "based on what was discussed", "from our chat history"
- Make questions sound conversational and natural
- Questions should flow naturally as if continuing the conversation
- Ask directly for information that was mentioned once or embedded in context

## CHAT ID TRACKING REQUIREMENT
- You MUST identify which specific chat_id(s) contain the information being tested
- List ALL chat_ids where the answer appears
- NOTE: If the answer is spread out between multiple chat_ids, group them in one list
- NOTE: DO NOT INCLUDE chat_ids in the answer
- If answer spans multiple chats, include all relevant chat_ids
- Use the exact chat_id numbers from the conversation turns

## DIFFICULTY LEVEL: EASY
- **Easy**: Information mentioned once or embedded in context
- Focus on facts that were clearly stated but within broader discussions
- Test information that requires basic extraction from surrounding context
- Include details that were mentioned but not necessarily emphasized

## OUTPUT FORMAT
Return your analysis in this exact JSON format:
{
    "question": "str",
    "answer": "str",
    "difficulty": "easy",
    "question_type": "numerical_precision",
    "conversation_reference": "Turn 2: ...",
    "key_facts_tested": ["...", ...],
    "source_chat_ids": [X, Y, ...]
}

## IMPORTANT REQUIREMENTS
1. **Direct questioning**: Ask specifically for information that was mentioned once
2. **Question source**: The question and answer to it MUST BE based on information from USER messages in CONVERSATION TURNS. You MUST NOT generate questions about assistant responses or suggestions.
3. **User information only**: Only create questions that test details the user provided, not assistant advice or recommendations.
4. **Context extraction**: Test ability to extract details from broader discussions
5. **Natural conversation flow**: Question should sound like normal information request
6. **Single mention focus**: Focus on information stated once or embedded in context
7. **Clear answer expectation**: Answer should contain the contextually mentioned facts

Generate ONE high-quality information extraction question that tests recall of details mentioned once or embedded within broader conversation context.

NOTE: Only output the JSON object without any explanation before or after.
"""
information_extraction_probing_question_medium_prompt = """
You are tasked with generating a probing question to test information extraction capabilities of LLMs. You will be given a bullet point and the corresponding multi-turn dialog between a user and assistant that incorporates this bullet point information.

Your task is to create ONE question that tests whether an LLM can precisely extract and recall specific factual details from the conversation.

## INPUT DATA
- **BULLET POINT**: <bullet_point>
- **CONVERSATION TURNS**: <conversation_turns>

## CRITICAL REQUIREMENT: MEDIUM INFORMATION EXTRACTION
- The question should test specific details from early in conversation that require memory retention
- Focus on information that was mixed with similar information requiring discrimination
- Test recall of facts that were mentioned early and might be forgotten
- Ask for specific details that could be confused with other similar information
- Remove ALL specific details from the question that would give away the answer

## FORBIDDEN QUESTION ELEMENTS
- Do NOT repeat specific names, numbers, or details being tested
- Do NOT mention key characteristics or attributes being extracted
- Do NOT include descriptive words that hint at the answer
- Do NOT reference specific categories or types being tested
- Do NOT use qualifying details that narrow down the answer

## QUESTION GENERATION GUIDELINES
Focus on extracting challenging details:
- **Numbers & Units**: amounts, costs, durations, counts, percentages mentioned early or alongside similar figures.
- **Named Entities**: people, organizations, brands, places, events, titles mentioned early or among similar names.
- **Temporal Details**: dates, times, deadlines, schedules, time references mentioned early or alongside similar ones.
- **Locations & Contacts**: addresses, venues, coordinates, URLs, emails, phone numbers mentioned early or in similar contexts.
- **Specifications & Attributes**: versions, models, ratings, sizes, requirements mentioned early or among similar specs.
- **Exact Wording**: quotes, phrased instructions, key statements mentioned early or among other directives.
- **Procedures & Steps**: specific steps, methods, or sequences mentioned early or among alternative approaches.
- **Statuses & Results**: conditions, outcomes, or progress updates stated early or among similar situations.
- **Relationships & Roles**: connections, affiliations, responsibilities mentioned early or among similar associations.
- **Categories & Types**: groupings, classifications, or labels mentioned early or among similar categories.
- **Preferences & Decisions**: choices, selections, or stated priorities mentioned early or among similar options.

## MODERATE QUESTIONING STRATEGIES
1. **Early Conversation Recall**: "What [specific detail] did I mention at the beginning of our conversation?" / "What was the first [item/fact] I brought up about [topic]?"
2. **Discriminative Questions**: "Which [specific option] did I say had [characteristic]?" / "Among the [items] I mentioned, which one was [specific attribute]?"
3. **Early Detail Questions**: "What was the first [detail] I mentioned about [topic]?" / "What initial [information] did I provide regarding [subject]?"
4. **Similarity Discrimination**: "Among the [similar items] I mentioned, which one was [specific characteristic]?" / "Which of the [similar options] did I say was [particular feature]?"
5. **Memory Retention Questions**: "What [early detail] did I mention before we discussed [later topic]?" / "What [information] did I share earlier about [subject]?"
6. **Sequential Detail Questions**: "What was the [order/sequence] I mentioned for [process/items]?" / "Which [step/item] did I say came first in [sequence]?"
7. **Comparative Discrimination**: "Between [option A] and [option B] I mentioned, which one had [specific feature]?" / "Which [item] did I say was [comparative attribute] than the other?"
8. **Temporal Discrimination**: "What [detail] did I mention happened [time reference] compared to [other event]?" / "Which [event] did I say occurred [temporal relationship]?"
9. **Category Discrimination**: "Among the [category] items I discussed, which one was [specific attribute]?" / "Which [type] did I say belonged to [specific group]?"
10. **Context Discrimination**: "What [detail] did I mention in the context of [situation A] versus [situation B]?" / "Which [information] was related to [specific context]?"

## QUESTION LANGUAGE REQUIREMENTS
- Write questions as if the USER is asking them naturally
- **If testing information from USER messages**: Use first person ("I", "my", "me") in question → Answer uses ("you", "your")
  - Example: "How did I decide on the location?" → "You decided on the location because..."
- **If testing information from ASSISTANT messages**: Use second person ("you", "your") in question → Answer uses ("I", "my") 
  - Example: "What steps did you suggest for handling this?" → "I suggested doing..."
- Avoid phrases like "according to the conversation", "based on what was discussed", "from our chat history"
- Make questions sound conversational and natural
- Questions should flow naturally as if continuing the conversation
- Ask for specific information that requires memory retention or discrimination

## CHAT ID TRACKING REQUIREMENT
- You MUST identify which specific chat_id(s) contain the information being tested
- List ALL chat_ids where the answer appears
- NOTE: If the answer is spread out between multiple chat_ids, group them in one list
- NOTE: DO NOT INCLUDE chat_ids in the answer
- If answer spans multiple chats, include all relevant chat_ids
- Use the exact chat_id numbers from the conversation turns

## DIFFICULTY LEVEL: MEDIUM
- **Medium**: Specific details from early in conversation or mixed with similar information
- Focus on facts that require memory retention over time
- Test information that could be confused with other similar details
- Include details that were mentioned early and require recall effort

## OUTPUT FORMAT
Return your analysis in this exact JSON format:
{
    "question": "What was the date I mentioned for meeting the consultant at the expo?",
    "answer": "You said you met Rami Al-Hassan at the Bahrain Acoustic Expo on Feb 20.",
    "difficulty": "medium",
    "question_type": "date_recall",
    "conversation_reference": "Turn 2: Date mentioned early in meeting description",
    "key_facts_tested": ["date: Feb 20", "event: meeting at expo", "person: Rami Al-Hassan"],
    "source_chat_ids": [X, Y, ...]
}

## IMPORTANT REQUIREMENTS
1. **Memory challenge**: Ask for information from early in conversation
2. **Question source**: The question and answer to it MUST BE based on information from USER messages in CONVERSATION TURNS. You MUST NOT generate questions about assistant responses or suggestions.
3. **User information only**: Only create questions that test details the user provided, not assistant advice or recommendations.
4. **Discrimination required**: Test details that could be confused with similar information
5. **Retention focus**: Focus on information that requires memory over conversation time
6. **Specific detail precision**: Ask for exact facts that require careful recall
7. **Natural phrasing**: Question should sound like normal follow-up inquiry

Generate ONE high-quality information extraction question that tests recall of specific details from early conversation or mixed with similar information.

NOTE: Only output the JSON object without any explanation before or after.
"""
information_extraction_probing_question_hard_prompt = """
You are tasked with generating a probing question to test information extraction capabilities of LLMs. You will be given a bullet point and the corresponding multi-turn dialog between a user and assistant that incorporates this bullet point information.

Your task is to create ONE question that tests whether an LLM can precisely extract and recall specific factual details from the conversation through indirect questioning that requires synthesizing multiple details from different parts of the conversation.

## INPUT DATA
- **BULLET POINT**: <bullet_point>
- **CONVERSATION TURNS**: <conversation_turns>

## CRITICAL REQUIREMENT: HARD INFORMATION EXTRACTION
- The question MUST NOT directly ask for the information being tested
- Ask about related topics/contexts that require the LLM to synthesize multiple details from different conversation parts
- Force the LLM to extract and combine information scattered across different conversation turns
- Make the LLM demonstrate knowledge of facts without being directly asked for them
- Require connecting and integrating information from multiple different conversation elements
- Remove ALL specific details from the question that would give away the answer

## FORBIDDEN QUESTION ELEMENTS
- Do NOT repeat specific names, numbers, or details being tested
- Do NOT mention key characteristics or attributes being extracted
- Do NOT include descriptive words that hint at the answer
- Do NOT reference specific categories or types being tested
- Do NOT use qualifying details that narrow down the answer

## QUESTION LANGUAGE REQUIREMENTS
- Write questions as if the USER is asking them naturally
- Questions MUST ONLY BE from USER language not ASSISTANT
- **If testing information from USER messages**: Use first person ("I", "my", "me") in question → Answer uses ("you", "your")
  - Example: "How did I decide on the location?" → "You decided on the location because..."
- **If testing information from ASSISTANT messages**: Use second person ("you", "your") in question → Answer uses ("I", "my") 
  - Example: "What steps did you suggest for handling this?" → "I suggested doing..."
- Avoid phrases like "according to the conversation", "based on what was discussed", "from our chat history"
- Make questions sound conversational and natural
- Questions should flow naturally as if continuing the conversation
- Ask about context, or relationships rather than direct facts

## INDIRECT QUESTIONING STRATEGIES
### 1. **Context-Based Recall**
Ask about the surrounding circumstances instead of the exact fact:
- “How did I come across this [solution/approach/option]?”
- “Which [options/alternatives] fit within my [limits/criteria/range]?”
- “How would I reach that [place/venue/resource]?”
- “What events led up to [decision/event/action]?”
- “How did I determine the appropriate [requirements/criteria] for my needs?”

### 2. **Comparison Questions**
Encourage differentiation between similar elements:
- “How does [person/source A’s] [suggestion/approach] compare with [person/source B’s] [method/proposal]?”
- “Which [option/alternative] provided the most [detailed/practical/conservative] guidance?”
- “What’s the difference between the [choices/options/approaches] I evaluated?”
- “How do the [features/benefits/limitations] of [option A] compare to [option B]?”
- “Which [choice/solution] seemed most suitable for my [goals/needs/context]?”

### 3. **Timeline Integration**
Link facts to their sequence in time:
- “What happened after I [took an action/spoke to someone]?”
- “How did my initial [interaction/research] influence later decisions?”
- “What changed between my first and later [attempts/interactions/discussions]?”
- “How did [earlier event] impact my [later choice/result]?”
- “What developments followed my [initial/exploratory] steps?”

### 4. **Problem-Solution Context**
Frame questions around issues and how they were addressed:
- “Who helped me resolve the [challenge/issue] in [specific area]?”
- “Which [source/approach] provided the most effective solution to [problem]?”
- “How did I address the [limitations/obstacles] related to [topic]?”
- “What [method/strategy] did I use to solve [specific challenge]?”
- “Who assisted in overcoming the [barrier/complication] in [area]?”

### 5. **Discovery and Learning Process**
Focus on the origin of knowledge or awareness:
- “How did I first learn about [option/approach/tool]?”
- “What led me to consider [alternative/method]?”
- “How did I become aware of [opportunity/resource]?”
- “What prompted me to explore [topic/solution]?”
- “How did I find out about [service/tool/information]?”

### 6. **Relationship and Connection Context**
Test understanding of associations:
- “How are [entity A] and [entity B] connected in this context?”
- “What role does [individual/group] play in my [plan/project]?”
- “How did [person/entity] become involved in [situation/decision]?”
- “What’s the relationship between [element A] and [element B]?”
- “How do [components/participants] work together in this [process/project]?”


## FORBIDDEN DIRECT QUESTIONS
- Do NOT ask "Who did I meet?" or "What's their name?"
- Do NOT ask "How much did it cost?" or "What was the price?"
- Do NOT ask "When did this happen?" or "What date was it?"
- Do NOT ask "Where did I meet?" or "What location?"

## CHAT ID TRACKING REQUIREMENT
- You MUST identify which specific chat_id(s) contain the information being tested
- List ALL chat_ids where the answer appears
- NOTE: If the answer is spread out between multiple chat_ids, group them in one list
- NOTE: DO NOT INCLUDE chat_ids in the answer
- If answer spans multiple chats, include all relevant chat_ids
- Use the exact chat_id numbers from the conversation turns

## DIFFICULTY LEVEL: HARD
- **Hard**: Requires synthesizing multiple details from different parts of conversation
- Force integration of information scattered across multiple conversation turns
- Test ability to connect related facts from different conversation contexts
- Require deep understanding and synthesis rather than simple recall

## OUTPUT FORMAT
Return your analysis in this exact JSON format:
{
    "question": "How did I find out about HVAC silencing as a solution for my studio?",
    "answer": "You found out about HVAC silencing when you met Rami Al-Hassan at the Bahrain Acoustic Expo on Feb 20, and he recommended it at $2,200.",
    "difficulty": "hard",
    "question_type": "context_based_recall", # one of: [Context-Based Recall | Comparison Questions | Timeline Integration | Problem-Solution Context | Discovery and Learning Process | Relationship and Connection Context]
    "conversation_reference": "Multiple turns: Meeting details, recommendation context, cost information",
    "key_facts_tested": ["name: Rami Al-Hassan", "location: Bahrain Acoustic Expo", "date: Feb 20", "recommendation: HVAC silencing", "cost: $2,200"],
    "extraction_challenge": "LLM must synthesize meeting context, recommendation details, and cost information from different conversation parts to explain discovery process",
    "source_chat_ids": [X, Y, ...]
}

## IMPORTANT REQUIREMENTS
1. **Indirect questioning**: Ask about context rather than direct facts
2. **Question source flexibility**: Questions can be based on information from EITHER user messages OR assistant messages
3. **Perspective matching**: Question perspective must match the source of information:
   - **User info** → "I/my/me" question → "you/your" answer
   - **Assistant info** → "you/your" question → "I/my" answer
4. **Assistant information questions**: When testing assistant advice/suggestions, use "What did you suggest/recommend/advise..." format
5. **Multi-detail synthesis**: Question should require combining information from different conversation parts
6. **Cross-turn integration**: Force LLM to connect scattered information across multiple turns
7. **Complex reasoning**: Require understanding of relationships and synthesis of multiple elements
8. **Challenging extraction**: Force LLM to demonstrate knowledge through indirect demonstration

Generate ONE high-quality indirect information extraction question that tests recall of specific factual details through contextual questioning requiring synthesis of multiple details from different parts of the conversation.

NOTE: Only output the JSON object without any explanation before or after.
"""
information_extraction_probing_question_assistant_prompt = """
You are tasked with generating a probing question to test information extraction capabilities of LLMs. You will be given a multi-turn dialog between a user and assistant.

Your task is to create ONE question that tests whether an LLM can precisely extract and recall specific factual details from the conversation.

## INPUT DATA
- **CONVERSATION TURNS**: <conversation_turns>

## CRITICAL REQUIREMENT: ASSISTANT RESPONSE FOCUS ONLY
- The question MUST test information that appears ONLY in assistant responses
- Do NOT test information mentioned by the user
- Focus exclusively on facts, details, and information provided by the assistant
- The answer should contain information that the assistant provided, not what the user said
- Remove ALL specific details from the question that would give away the answer

## FORBIDDEN QUESTION ELEMENTS
- Do NOT repeat specific names, numbers, or details being tested
- Do NOT mention key characteristics or attributes being extracted
- Do NOT include descriptive words that hint at the answer
- Do NOT reference specific categories or types being tested
- Do NOT use qualifying details that narrow down the answer

## QUESTION GENERATION GUIDELINES
Focus on extracting:
- **Specific numbers, measurements, quantities, percentages, rates, scores**
- **Proper names of people, places, organizations, brands, products, services**
- **Exact dates, times, locations, addresses, contact information, references**
- **Technical details, specifications, models, versions, ratings, classifications**
- **Precise statements, quotes, instructions, recommendations, guidelines**
- **Process steps, procedures, methods, techniques, approaches**
- **Status updates, conditions, outcomes, results, findings**
- **Categories, types, classifications, levels, stages**
- **Relationships, connections, associations, dependencies**
- **Criteria, requirements, standards, benchmarks, thresholds**

## QUESTION TYPES TO GENERATE
1. **Direct Fact Extraction**: Ask for specific details mentioned in the conversation
2. **Numerical Precision**: Test recall of exact numbers, quantities, measurements, percentages
3. **Name Recognition**: Test recall of proper names (people, places, organizations, brands)
4. **Technical Detail Recall**: Ask for specifications, models, versions, ratings, classifications
5. **Quote/Statement Recall**: Test memory of exact phrases, instructions, recommendations
6. **Process Detail Recall**: Test memory of specific steps, procedures, methods
7. **Status Information Recall**: Test recall of conditions, outcomes, results, findings
8. **Category/Classification Recall**: Test memory of types, levels, stages, categories
9. **Relationship Recall**: Test understanding of connections, associations, dependencies
10. **Criteria/Standard Recall**: Test memory of requirements, benchmarks, thresholds

## QUESTION LANGUAGE REQUIREMENTS
- Write questions as if the USER is asking them naturally
- Use first person ("I", "my", "me") when referring to the user
- Use second person ("you") when addressing the assistant
- Avoid phrases like "according to the conversation", "based on what was discussed", "from our chat history"
- Make questions sound conversational and natural
- Questions should flow naturally as if continuing the conversation

## CHAT ID TRACKING REQUIREMENT
- You MUST identify which specific chat_id(s) contain the information being tested
- List ALL chat_ids where the answer appears
- NOTE: If the answer is spread out between multiple chat_ids, group them in one list
- NOTE: DO NOT INCLUDE chat_ids in the answer
- If answer spans multiple chats, include all relevant chat_ids
- Use the exact chat_id numbers from the conversation turns

## OUTPUT FORMAT
Return your analysis in this exact JSON format:
{
    "question": "Who did I meet at the Bahrain Acoustic Expo and what did they recommend?",
    "answer": "You met Rami Al-Hassan at the Bahrain Acoustic Expo on Feb 20, and he recommended HVAC silencing at $2,200.",
    "difficulty": "medium",
    "question_type": "name_recognition",
    "conversation_reference": "Turn 2: User mentioned meeting consultant",
    "key_facts_tested": ["name: Rami Al-Hassan", "location: Bahrain Acoustic Expo", "date: Feb 20", "recommendation: HVAC silencing", "cost: $2,200"],
    "source_chat_ids": [X, Y, ...]
}

## IMPORTANT REQUIREMENTS
1. **Precise Answer**: Provide exact, unambiguous answer with specific details
2. **Conversation Reference**: Note which turn(s) contain the tested information
3. **Key Facts**: List the specific factual elements being tested
4. **Realistic Question**: Create a question that sounds natural in a memory evaluation context
5. **Best Coverage**: Select the most important/challenging fact from the bullet point to test

Generate ONE high-quality information extraction question that tests recall of the most important specific factual detail from the given bullet point and conversation.

NOTE: Only output the JSON object without any explanation before or after.
"""

multi_session_reasoning_probing_question_easy_prompt = """
You are tasked with generating a probing question to test multi-session reasoning capabilities of LLMs. You will be given multiple related bullet points and the corresponding multi-turn dialogs between a user and assistant that incorporate this information across different conversation sessions.

Your task is to create ONE question that tests whether an LLM can perform basic aggregation or comparison across 2-3 conversation sessions.

## INPUT DATA
- **BULLET POINTS**: <bullet_points>
- **CONVERSATION TURNS**: <conversation_turns>

## CRITICAL REQUIREMENT: EASY MULTI-SESSION REASONING
- The question MUST NOT include any explicit number, dates, times, duration, or temporal references
- Focus on simple aggregation or basic comparison across 2-3 sessions
- Test straightforward multi-session recall with minimal synthesis required
- Ask for basic calculations or simple comparisons that span multiple sessions

## QUESTION GENERATION GUIDELINES
Focus on creating questions that require:
- **Simple Aggregation**: Basic summing or counting across 2-3 sessions
- **Basic Comparison**: Simple before/after or this vs. that comparisons
- **Straightforward Synthesis**: Combining obvious information from multiple sessions
- **Direct Multi-session Recall**: Connecting clear information across sessions

## QUESTION TYPES TO GENERATE (EASY LEVEL)
1. **Basic Mathematical Aggregation**
2. **Simple Comparison**
3. **Straightforward Counting**
4. **Simple Cross-session Facts**
5. **Basic Category Aggregation**
6. **Simple Status Tracking**

## REASONING COMPLEXITY LEVEL: EASY
- **Easy**: Requires basic aggregation or comparison across 2-3 sessions
- Focus on simple calculations or obvious comparisons
- Test straightforward information combination
- Avoid complex synthesis or multi-hop reasoning

## QUESTION LANGUAGE REQUIREMENTS
- Write questions as if the USER is asking them naturally
- **If testing information from USER messages**: Use first person ("I", "my", "me") in question → Answer uses ("you", "your")
  - Example: "How did I decide on the location?" → "You decided on the location because..."
- **If testing information from ASSISTANT messages**: Use second person ("you", "your") in question → Answer uses ("I", "my") 
  - Example: "What steps did you suggest for handling this?" → "I suggested doing..."
- Avoid phrases like "according to the conversation", "based on what was discussed", "from our chat history"
- Make questions sound conversational and natural
- Questions should flow naturally as if continuing the conversation

## CHAT ID TRACKING REQUIREMENT
- You MUST identify which specific chat_id(s) contain the information needed for reasoning
- List ALL chat_ids where relevant information appears across the reasoning chain
- NOTE: If the answer is spread out between multiple chat_ids, group them in one list
- NOTE: DO NOT INCLUDE chat_ids in the answer
- If reasoning spans multiple chats, include all relevant chat_ids
- Use the exact chat_id numbers from the conversation turns

## OUTPUT FORMAT
You will output exactly ONE JSON object matching this schema:
{
  "question": string,                       # ≤30 words, first‑person "I" for the user
  "answer": string,                         # exact, objective fact or calculation
  "difficulty": "easy",                     # always "easy" for this prompt
  "reasoning_type":                         # one of:
    "basic_aggregation"|
    "simple_comparison"|
    "straightforward_counting"|
    "simple_cross_session_facts"|
    "basic_category_aggregation"|
    "simple_status_tracking",
  "sessions_required": integer,             # 2-3 sessions
  "conversation_references": [string,...],   # titles or session IDs, length ≥ sessions_required
  "reasoning_steps": [string,...],           # a numbered chain of 2-3 simple steps
  "source_chat_ids": [integer,...]          # ALL chat_ids containing information used in reasoning
}

## IMPORTANT REQUIREMENTS
1. **Simple multi-session dependency**: Question must require basic information from 2-3 conversation sessions
2. **Question source**: The question and answer to it MUST BE based on information from USER messages in CONVERSATION TURNS. You MUST NOT generate questions about assistant responses or suggestions.
3. **User information only**: Only create questions that test details the user provided, not assistant advice or recommendations.
4. **Clear reasoning path**: Provide simple step-by-step reasoning required to answer
5. **Precise answer**: Give exact answer that can be objectively verified
6. **Session references**: Note which sessions contain relevant information
7. **Basic complexity**: Ensure question requires simple multi-session reasoning

Generate ONE high-quality easy multi-session reasoning question.

NOTE: Only output the JSON object without any explanation before or after.
"""
multi_session_reasoning_probing_question_medium_prompt = """
You are tasked with generating a probing question to test multi-session reasoning capabilities of LLMs. You will be given multiple related bullet points and the corresponding multi-turn dialogs between a user and assistant that incorporate this information across different conversation sessions.

Your task is to create ONE question that tests whether an LLM can perform moderate aggregation, comparison, and synthesis across 3-4 conversation sessions.

## INPUT DATA
- **BULLET POINTS**: <bullet_points>
- **CONVERSATION TURNS**: <conversation_turns>

## CRITICAL REQUIREMENT: MEDIUM MULTI-SESSION REASONING
- The question MUST NOT include any explicit number, dates, times, duration, or temporal references
- Focus on moderate complexity requiring synthesis across 3-4 sessions
- Test aggregation or comparison that requires some analytical thinking
- Ask for calculations or comparisons that need moderate reasoning steps

## QUESTION GENERATION GUIDELINES
Focus on creating questions that require:
- **Moderate Aggregation**: Summing or counting with some complexity across 3-4 sessions
- **Analytical Comparison**: Comparing trends, changes, or patterns between sessions
- **Moderate Synthesis**: Combining information that requires some reasoning
- **Pattern Analysis**: Identifying trends or progressions across sessions
- **Categorized Calculations**: Grouping and calculating across different categories

## QUESTION TYPES TO GENERATE (MEDIUM LEVEL)
1. **Categorized Aggregation**
2. **Pattern Analysis**
3. **Evolution Tracking**
4. **Performance Comparison**
5. **Resource Distribution**
6. **Progress Assessment**
7. **Cross-session Correlation**

## REASONING COMPLEXITY LEVEL: MEDIUM
- **Medium**: Requires moderate aggregation, comparison, or synthesis across 3-4 sessions
- Focus on calculations or analysis requiring multiple reasoning steps
- Test ability to identify patterns or trends across sessions
- Include some analytical thinking beyond simple recall

## QUESTION LANGUAGE REQUIREMENTS
- Write questions as if the USER is asking them naturally
- **If testing information from USER messages**: Use first person ("I", "my", "me") in question → Answer uses ("you", "your")
  - Example: "How did I decide on the location?" → "You decided on the location because..."
- **If testing information from ASSISTANT messages**: Use second person ("you", "your") in question → Answer uses ("I", "my") 
  - Example: "What steps did you suggest for handling this?" → "I suggested doing..."
- Avoid phrases like "according to the conversation", "based on what was discussed", "from our chat history"
- Make questions sound conversational and natural
- Questions should flow naturally as if continuing the conversation

## CHAT ID TRACKING REQUIREMENT
- You MUST identify which specific chat_id(s) contain the information needed for reasoning
- List ALL chat_ids where relevant information appears across the reasoning chain
- NOTE: If the answer is spread out between multiple chat_ids, group them in one list
- NOTE: DO NOT INCLUDE chat_ids in the answer
- If reasoning spans multiple chats, include all relevant chat_ids
- Use the exact chat_id numbers from the conversation turns

## OUTPUT FORMAT
You will output exactly ONE JSON objects matching this schema:
{
  "question": string,                       # ≤30 words, first‑person "I" for the user
  "answer": string,                         # exact, objective fact or calculation
  "difficulty": "medium",                   # always "medium" for this prompt
  "reasoning_type":                         # one of:
    "categorized_aggregation"|
    "pattern_analysis"|
    "evolution_tracking"|
    "performance_comparison"|
    "resource_distribution"|
    "progress_assessment"|
    "cross-session_correlation",
  "sessions_required": integer,             # 3-4 sessions
  "conversation_references": [string,...],   # titles or session IDs, length ≥ sessions_required
  "reasoning_steps": [string,...],          # a numbered chain of 3-4 reasoning steps
  "source_chat_ids": [integer,...]          # ALL chat_ids containing information used in reasoning
}

## IMPORTANT REQUIREMENTS
1. **Moderate multi-session dependency**: Question must require information from 3-4 conversation sessions
2. **Question source**: The question and answer to it MUST BE based on information from USER messages in CONVERSATION TURNS. You MUST NOT generate questions about assistant responses or suggestions.
3. **User information only**: Only create questions that test details the user provided, not assistant advice or recommendations.
4. **Analytical reasoning path**: Provide reasoning steps that require some analysis
5. **Precise answer**: Give exact answer that can be objectively verified
6. **Session references**: Note which sessions contain relevant information
7. **Medium complexity**: Ensure question requires moderate multi-session reasoning and analysis

Generate ONE high-quality medium multi-session reasoning question.

NOTE: Only output the JSON object without any explanation before or after.
"""
multi_session_reasoning_probing_question_hard_prompt = """
You are tasked with generating a probing question to test multi-session reasoning capabilities of LLMs. You will be given multiple related bullet points and the corresponding multi-turn dialogs between a user and assistant that incorporate this information across different conversation sessions.

Your task is to create ONE question that tests whether an LLM can perform complex multi-hop reasoning, synthesis, and analysis across 4+ conversation sessions.

## INPUT DATA
- **BULLET POINTS**: <bullet_points>
- **CONVERSATION TURNS**: <conversation_turns>

## CRITICAL REQUIREMENT: HARD MULTI-SESSION REASONING
- The question MUST NOT include any explicit number, dates, times, duration, or temporal references
- Focus on complex synthesis requiring multi-hop reasoning across 4+ sessions
- Test sophisticated analysis that requires connecting multiple data points
- Ask for complex calculations, patterns, or insights that need advanced reasoning

## QUESTION GENERATION GUIDELINES
Focus on creating questions that require:
- **Complex Aggregation**: Multi-step calculations across multiple sessions and categories
- **Advanced Synthesis**: Combining information that requires sophisticated reasoning
- **Multi-hop Reasoning**: Connecting information across 4+ different conversation sessions
- **Pattern Recognition**: Identifying complex trends, correlations, or relationships
- **Performance Evaluation**: Assessing outcomes, effectiveness, or success rates
- **Comparative Analysis**: Complex comparisons involving multiple variables
- **Predictive Reasoning**: Drawing conclusions based on patterns across sessions

## QUESTION TYPES TO GENERATE (HARD LEVEL)
1. **Complex Multi-hop Calculation**
2. **Performance Evaluation**
3. **Multi-variable Comparison**
4. **Complex Evolution Analysis**

## REASONING COMPLEXITY LEVEL: HARD
- **Hard**: Requires complex multi-hop reasoning, synthesis, and analysis across 4+ sessions
- Focus on sophisticated calculations or insights requiring advanced reasoning
- Test ability to identify complex patterns, correlations, or relationships
- Include deep analytical thinking and synthesis of multiple data points

## QUESTION LANGUAGE REQUIREMENTS
- Write questions as if the USER is asking them naturally
- **If testing information from USER messages**: Use first person ("I", "my", "me") in question → Answer uses ("you", "your")
  - Example: "How did I decide on the location?" → "You decided on the location because..."
- **If testing information from ASSISTANT messages**: Use second person ("you", "your") in question → Answer uses ("I", "my") 
  - Example: "What steps did you suggest for handling this?" → "I suggested doing..."
- Avoid phrases like "according to the conversation", "based on what was discussed", "from our chat history"
- Make questions sound conversational and natural
- Questions should flow naturally as if continuing the conversation

## CHAT ID TRACKING REQUIREMENT
- You MUST identify which specific chat_id(s) contain the information needed for reasoning
- List ALL chat_ids where relevant information appears across the reasoning chain
- NOTE: If the answer is spread out between multiple chat_ids, group them in one list
- NOTE: DO NOT INCLUDE chat_ids in the answer
- If reasoning spans multiple chats, include all relevant chat_ids
- Use the exact chat_id numbers from the conversation turns

## OUTPUT FORMAT
You will output exactly ONE JSON object matching this schema:
{
  "question": string,                       # ≤30 words, first‑person "I" for the user
  "answer": string,                         # exact, objective fact or calculation
  "difficulty": "hard",                     # always "hard" for this prompt
  "reasoning_type":                         # one of:
    "complex_multi_hop_calculation"|
    "performance_evaluation"|
    "multi_variable_comparison"|
    "predictive_synthesis"|
    "complex_evolution_analysis"|
    "advanced_optimization"|
    "strategic_synthesis"|
    "complex_trend_analysis",
  "sessions_required": integer,             # ≥4 sessions
  "conversation_references": [string,...],   # titles or session IDs, length ≥ sessions_required
  "reasoning_steps": [string,...],           # a numbered chain of ≥4 complex reasoning steps
  "source_chat_ids": [integer,...]          # ALL chat_ids containing information used in reasoning
}

## IMPORTANT REQUIREMENTS
1. **Complex multi-session dependency**: Question must require sophisticated information synthesis from 4+ conversation sessions
2. **Question source**: The question and answer to it MUST BE based on information from USER messages in CONVERSATION TURNS. You MUST NOT generate questions about assistant responses or suggestions.
3. **User information only**: Only create questions that test details the user provided, not assistant advice or recommendations.
5. **Advanced reasoning path**: Provide complex reasoning steps that require multi-hop thinking
6. **Precise answer**: Give exact answer that demonstrates complex analysis
7. **Session references**: Note which sessions contain relevant information
8. **High complexity**: Ensure question requires advanced multi-session reasoning and sophisticated synthesis

Generate ONE high-quality hard multi-session reasoning question.

NOTE: Only output the JSON object without any explanation before or after.
"""
multi_session_reasoning_probing_question_assistant_prompt = """
You are tasked with generating a probing question to test multi-session reasoning capabilities of LLMs. You will be given multiple related bullet points and the corresponding multi-turn dialogs between a user and assistant that incorporate this information across different conversation sessions.

Your task is to create ONE question that tests whether an LLM can aggregate, compare, and synthesize information across multiple conversation sessions to perform complex multi-hop reasoning.

## INPUT DATA
- **CONVERSATION TURNS**: <conversation_turns>

## CRITICAL REQUIREMENT: ASSISTANT RESPONSE FOCUS ONLY
- The question MUST NOT include any explicit number, dates, times, duration, or temporal references
- The question MUST be from information that appears ONLY in assistant responses
- Do NOT use information mentioned by the user
- Focus exclusively on facts, calculations, recommendations, and analysis provided by the assistant
- Ignore all user messages when selecting information
- The answer should contain information that the assistant provided across multiple sessions

## QUESTION GENERATION GUIDELINES
Focus on creating questions that require:
- **Aggregation**: Summing costs, counting events, totaling measurements across sessions
- **Comparison**: Analyzing changes, differences, or similarities between sessions
- **Synthesis**: Combining information from multiple sessions to form conclusions
- **Multi-hop reasoning**: Connecting information across 3+ different conversation sessions
- **Pattern recognition**: Identifying trends, progressions, or recurring themes
- **Prioritization**: Ranking or ordering items based on criteria across sessions
- **Performance evaluation**: Assessing success/failure of recommendations over time

## QUESTION TYPES TO GENERATE (ASSISTANT-FOCUSED)
1. **Mathematical Aggregation**: "What was the total [cost/amount/score/quantity/value] you calculated across all your [estimates/assessments/evaluations/analyses]?"
2. **Recommendation Comparison**: "How did your [recommendations/suggestions/advice/proposals] change from our first discussion to our last?"
3. **Analysis Evolution**: "What pattern emerged in your [assessments/evaluations/analyses/interpretations] over our conversations?"
4. **Cross-session Synthesis**: "Based on all your [explanations/analyses/assessments/evaluations], what were the main [factors/elements/components/variables] you identified?"
5. **Multi-hop Calculation**: "Calculate the difference between your [initial estimate/first assessment/original calculation] and [final calculation/last evaluation/updated analysis]."
6. **Prioritization Analysis**: "How did you rank/prioritize the [options/approaches/solutions/strategies] differently across our discussions?"
7. **Performance Evaluation**: "Which of your [recommendations/suggestions/strategies/approaches] proved most/least [effective/successful/useful/appropriate] over time?"
8. **Methodology Comparison**: "How did your [approach/methodology/strategy/technique] for [analyzing/solving/addressing] [issues/problems/challenges] evolve across sessions?"
9. **Insight Progression**: "What new [insights/understanding/perspectives/conclusions] did you develop as our conversations progressed?"
10. **Consistency Analysis**: "How [consistent/variable/different] were your [assessments/recommendations/conclusions/evaluations] across different [contexts/sessions/scenarios]?"
11. **Accuracy Assessment**: "How did the [accuracy/precision/reliability] of your [predictions/estimates/assessments] change over our multiple discussions?"
12. **Adaptive Response**: "How did you [adapt/modify/adjust] your [responses/recommendations/strategies] based on [new information/changing circumstances/updated requirements] across sessions?"

## QUESTION LANGUAGE REQUIREMENTS
- Write questions as if the USER is asking them naturally
- Use first person ("I", "my", "me") when referring to the user
- Use second person ("you") when addressing the assistant
- Avoid phrases like "according to the conversation", "based on what was discussed", "from our chat history"
- Make questions sound conversational and natural
- Questions should flow naturally as if continuing the conversation

## CHAT ID TRACKING REQUIREMENT
- You MUST identify which specific chat_id(s) contain the information needed for reasoning
- List ALL chat_ids where relevant information appears across the reasoning chain
- NOTE: If the answer is spread out between multiple chat_ids, group them in one list
- NOTE: DO NOT INCLUDE chat_ids in the answer
- If reasoning spans multiple chats, include all relevant chat_ids
- Use the exact chat_id numbers from the conversation turns

## OUTPUT FORMAT
You will output exactly ONE JSON object matching this schema:
{
  "question": string,                       # ≤30 words, first‑person “I” for the user
  "answer": string,                         # exact, objective fact or calculation
  "difficulty": "easy"|"medium"|"hard",   # pick one
  "reasoning_type":                         # one of:
    "mathematical_aggregation"|
    "temporal_comparison"|
    "evolution_analysis"|
    "cross-session_synthesis"|
    "multi-hop_calculation",
  "sessions_required": integer,             # ≥3
  "conversation_references": [string,...],   # titles or session IDs, length ≥ sessions_required
  "reasoning_steps": [string,...],           # a numbered chain of ≥3 steps
  "source_chat_ids": [integer,...]          # ALL chat_ids containing information used in reasoning
}

### GUIDELINES
- Must reference at least **3 distinct sessions** by name.
- Question must require **multi‑hop calculation** (or your chosen reasoning_type).
- Do **not** include any extra fields or commentary.
- Question text must **directly ask** for a comparison, sum, difference, or pattern across sessions.
- All numeric values in the answer must be bare numbers (no “$” or “%” signs).
- Plan internally in 2 sentences, then emit only the JSON.

## IMPORTANT REQUIREMENTS
1. **Multi-session dependency**: Question must require information from multiple conversation sessions
2. **Question source**: The question and answer to it MUST BE based on information from USER messages in CONVERSATION TURNS. You MUST NOT generate questions about assistant responses or suggestions.
3. **User information only**: Only create questions that test extraction of facts the user provided, not assistant advice or recommendations.
4. **Clear reasoning path**: Provide step-by-step reasoning required to answer
5. **Precise answer**: Give exact answer that can be objectively verified
6. **Session references**: Note which sessions contain relevant information
7. **Complexity justification**: Ensure question truly requires multi-hop reasoning, not simple recall

Generate ONE high-quality multi-session reasoning question that requires aggregation, comparison, or synthesis across the provided bullet points and conversation sessions.

NOTE: Only output the JSON object without any explanation before or after.
"""

knowledge_update_probing_question_final_prompt = """
You are tasked with generating a probing question to test knowledge update capabilities of LLMs. You will be given two related bullet points (original information and updated information) and the corresponding multi-turn dialogs between a user and assistant that incorporate both pieces of information across different conversation sessions.

Your task is to create ONE question that asks about the current/updated state of information, testing whether the LLM correctly recalls the most recent version rather than outdated information.

## INPUT DATA
- **BULLET POINTS**: <bullet_points>
- **CONVERSATION TURNS**: <conversation_turns>

## CRITICAL REQUIREMENT: NO SPECIFIC CONTEXT HINTS
- MUST NOT GIVE ANY INFORMATION RELATED TO OLD AND UPDATED INFORMATION/FACTS OR ANY HINTS THAT THERE IS UPDATE AT ALL
_ DO NOT use words like: currently, now, ... that shows update of information
- The question MUST NOT include specific dates, times, locations, or detailed circumstances
- Do NOT reference specific events, phases, or instances that would hint at which version to recall
- Ask about the general current state, not specific occurrences

## FACTUAL UPDATE IDENTIFICATION
Before creating the question:
1. Identify the EXACT fact that was updated in the "Information Update" bullet
2. Determine what the original fact was vs. the updated fact
3. Create a question that tests recall of the updated fact specifically
4. Ensure question asks for the factual detail, not procedures or implications

## QUESTION GENERATION GUIDELINES
Focus on creating questions that:
- **Ask about current state**: Question the most recent/updated version of information
- **Test update retention**: Whether LLM remembers the latest information, not the original
- **Avoid mentioning changes**: Don't explicitly ask "how did X change" - just ask about current state
- **Target updated facts**: Focus on information that was specifically updated/changed

## QUESTION TYPES TO GENERATE
1. **Current State Query**: "What is [value] of [x]?"
2. **Latest Status**: "What is the current timeline for []?"
3. **Updated Decision**: "What did [y] choose for []?"
4. **Final Information**: "What is the current [x] of []?"
5. **Recent Details**: "What are the current specifications for []?"

## QUESTION LANGUAGE REQUIREMENTS
- Write questions as if the USER is asking them naturally
- **If testing information from USER messages**: Use first person ("I", "my", "me") in question → Answer uses ("you", "your")
  - Example: "How did I decide on the location?" → "You decided on the location because..."
- **If testing information from ASSISTANT messages**: Use second person ("you", "your") in question → Answer uses ("I", "my") 
  - Example: "What steps did you suggest for handling this?" → "I suggested doing..."
- Avoid phrases like "according to the conversation", "based on what was discussed", "from our chat history"
- Make questions sound conversational and natural
- Questions should flow naturally as if continuing the conversation

## CHAT ID TRACKING REQUIREMENT
- You MUST identify which specific chat_id(s) contain the original and updated information
- List the chat_id with the original information and the chat_id with the updated information
- NOTE: If the answer is spread out between multiple chat_ids, group them in one list
- NOTE: DO NOT INCLUDE chat_ids in the answer
- Use the exact chat_id numbers from the conversation turns

## OUTPUT FORMAT
Return your analysis in this exact JSON format:
{
    "question": "What is Sherry's current budget for the studio project?",
    "answer": "$13,000 (after contractor quoted $14,000 but she negotiated to reduce labor hours saving $1,000)",
    "difficulty": "moderate",
    "update_type": "budget_revision",
    "tests_retention_of": "updated budget amount after negotiation",
    "conversation_references": ["Complete text of Bullet 1 (old information)", "Complete text of Bullet 2 (updated information)"],
    "potential_confusion": "LLM might incorrectly recall original $12,500 budget instead of updated amount",
    "source_chat_ids": {
        "original_info": [6, 8],
        "updated_info": [23, 29]
    }
}

## IMPORTANT REQUIREMENTS
1. Do not mention how or when the value changed.Question text must not contain words like “after,” “negotiated,” “updated,” “revised,” or any mention of a change process.
2. **Current state focus**: Question must ask about the updated/current information only
3. **No change language**: Avoid words like "changed," "updated," "revised" in the question
4. **Updated answer**: Answer must reflect the most recent version of the information
5. **Confusion potential**: Note what outdated information the LLM might incorrectly recall
6. **Natural phrasing**: Question should sound like asking for current facts, not testing memory updates
7. “Include at least **two** entries in `conversation_references`: one for the original fact session and one for the updated fact session.”

Generate ONE knowledge update question that tests whether the LLM correctly recalls the updated information rather than the original outdated version.

CRITICAL NOTE: Do not mention how or when the value changed.Question text must not contain words like “after,” “negotiated,” “updated,” “revised,” or any mention of a change process.

NOTE: Only output the JSON object without any explanation before or after.
"""

temporal_reasoning_probing_question_easy_prompt = """
You are tasked with generating a probing question to test temporal reasoning capabilities of LLMs. You will be given two related bullet points with temporal information and the corresponding multi-turn dialogs between a user and assistant that incorporate both time points across different conversation sessions.

Your task is to create ONE question that tests whether an LLM can perform basic duration calculations or sequence understanding between two events where one has explicit timing and one has relative timing.

## INPUT DATA
- **BULLET POINTS**: <bullet_points>
- **CONVERSATION TURNS**: <conversation_turns>

## CRITICAL REQUIREMENT: EASY TEMPORAL REASONING
- Focus on scenarios with one explicit date and one with relative timing or context clues
- Test basic temporal reasoning that requires minimal inference
- Ask for straightforward duration calculations or simple sequence questions
- Use events where timing information is relatively clear and accessible

## QUESTION GENERATION GUIDELINES
Focus on creating questions that test:
- **Basic duration calculations**: Simple time differences between clear events
- **Simple sequence understanding**: Which event happened first when one has explicit timing
- **Straightforward temporal relationships**: Clear before/after relationships
- **Basic timeline analysis**: Simple time gaps with minimal complexity
- **Direct scheduling comparisons**: Obvious temporal differences

## QUESTION TYPES TO GENERATE (EASY LEVEL)
1. **Simple Duration Calculation**: "How many days elapsed between [explicit event] and [relative event]?"
2. **Basic Sequence Query**: "Which happened first: [explicit event] or [relative event]?"
3. **Straightforward Time Gap**: "How long after [explicit event] did [relative event] occur?"
4. **Basic Timeline Comparison**: "What was the time difference between these two events?"
5. **Simple Temporal Ordering**: "In what order did these events happen?"
6. **Between-Time Information Extraction**: "What/Who/Where/How much/When [specific query] between [first event] and [second event]?"

## TEMPORAL COMPLEXITY LEVEL: EASY
- **Easy**: One explicit date, one with relative timing or context clues
- Focus on basic temporal reasoning with clear time references
- Test simple calculations or obvious sequence relationships
- Avoid complex inference or multi-step reasoning

## QUESTION LANGUAGE REQUIREMENTS
- Write questions as if the USER is asking them naturally
- Use first person ("I", "my", "me") when referring to the user
- Refer to all events using first‑person pronouns ("I", "my", "we"); do not use "you" or "your" when describing those events
- Avoid phrases like "according to the conversation", "based on what was discussed", "from our chat history"
- Make questions sound conversational and natural
- Questions should flow naturally as if continuing the conversation

## CHAT ID TRACKING REQUIREMENT
- You MUST identify which specific chat_id(s) contain the temporal information for both events
- List the chat_id for the first temporal event and the chat_id for the second temporal event
- NOTE: If the answer is spread out between multiple chat_ids, group them in one list
- NOTE: DO NOT INCLUDE chat_ids in the answer
- Use the exact chat_id numbers from the conversation turns

## OUTPUT FORMAT
Return your analysis in this exact JSON format:
{
    "question": "How many days elapsed between when I scheduled the inspection and when the installation was completed?",
    "answer": "5 days elapsed between the electrician inspection scheduled for March 15 and when the installation was completed the following week on March 20.",
    "difficulty": "easy",
    "temporal_type": "duration_calculation",
    "time_points": ["March 15: inspection scheduled", "March 20: installation completed"],
    "conversation_references": ["Session 1: Inspection scheduling", "Session 2: Installation completion"],
    "calculation_required": "March 20 - March 15 = 5 days",
    "source_chat_ids": {
        "first_event": [12, 15],
        "second_event": [28, 31]
    }
}

## IMPORTANT REQUIREMENTS
1. **Do not** include any explicit dates (e.g. "March 12") in the **question**. Refer only to the event descriptions; the model must recall the dates itself.
2. **Mixed time reference complexity**: One event should have explicit timing, one with relative timing
3. **Basic temporal reasoning**: Question should require simple temporal analysis
4. **Objective calculation**: Answer must be mathematically verifiable
5. **Clear time points**: Both events must have identifiable temporal references
6. **Natural phrasing**: Question should sound realistic for basic temporal memory testing

Generate ONE high-quality easy temporal reasoning question that tests basic duration calculation or sequence understanding with mixed explicit and relative timing.

NOTE: Only output the JSON object without any explanation before or after.
"""
temporal_reasoning_probing_question_medium_prompt = """
You are tasked with generating a probing question to test temporal reasoning capabilities of LLMs. You will be given two related bullet points with temporal information and the corresponding multi-turn dialogs between a user and assistant that incorporate both time points across different conversation sessions.

Your task is to create ONE question that tests whether an LLM can perform moderate duration calculations or sequence understanding that requires inference from multiple temporal references or batch anchors.

## INPUT DATA
- **BULLET POINTS**: <bullet_points>
- **CONVERSATION TURNS**: <conversation_turns>

## CRITICAL REQUIREMENT: MEDIUM TEMPORAL REASONING
- Focus on scenarios requiring inference from multiple temporal references or batch anchors
- Test moderate temporal reasoning that requires some deductive thinking
- Ask for calculations that need connecting multiple time clues
- Use events where timing must be inferred from context or relative references

## QUESTION GENERATION GUIDELINES
Focus on creating questions that test:
- **Inferential duration calculations**: Time differences requiring context interpretation
- **Context-based sequence understanding**: Order determination through contextual clues
- **Multi-reference temporal relationships**: Connecting multiple time indicators
- **Batch anchor analysis**: Using session timing to determine event timing
- **Moderate timeline reconstruction**: Piecing together timing from multiple sources

## QUESTION TYPES TO GENERATE (MEDIUM LEVEL)
1. **Inferential Duration Calculation**: "How many days elapsed between [contextual event] and [anchor-referenced event]?"
2. **Context Sequence Query**: "Which happened first: [event with batch anchor] or [event with relative timing]?"
3. **Multi-reference Time Gap**: "How long after [inferred event] did [context-referenced event] occur?"
4. **Timeline Reconstruction**: "What was the time difference between these events based on the session timing?"
5. **Anchor-based Ordering**: "In what chronological order did these events happen?"
6. **Between-Time Information Extraction**: "What/Who/Where/How much/When [specific query] between [contextual event] and [anchor-referenced event]?"

## TEMPORAL COMPLEXITY LEVEL: MEDIUM
- **Medium**: Requires inference from multiple temporal references or batch anchors
- Focus on moderate temporal reasoning requiring deductive thinking
- Test ability to connect multiple time clues or contextual references
- Include scenarios where timing must be derived rather than directly stated

## QUESTION LANGUAGE REQUIREMENTS
- Write questions as if the USER is asking them naturally
- Use first person ("I", "my", "me") when referring to the user
- Refer to all events using first‑person pronouns ("I", "my", "we"); do not use "you" or "your" when describing those events
- Avoid phrases like "according to the conversation", "based on what was discussed", "from our chat history"
- Make questions sound conversational and natural
- Questions should flow naturally as if continuing the conversation

## CHAT ID TRACKING REQUIREMENT
- You MUST identify which specific chat_id(s) contain the temporal information for both events
- List the chat_id for the first temporal event and the chat_id for the second temporal event
- NOTE: If the answer is spread out between multiple chat_ids, group them in one list
- NOTE: DO NOT INCLUDE chat_ids in the answer
- Use the exact chat_id numbers from the conversation turns

## OUTPUT FORMAT
Return your analysis in this exact JSON format:
{
    "question": "How many days elapsed between when I first mentioned the electrical concerns and when the safety check was completed?",
    "answer": "15 days elapsed between when you first mentioned electrical concerns (inferred from March 1 batch anchor) and when the safety check was completed on March 16.",
    "difficulty": "medium",
    "temporal_type": "inferential_duration_calculation",
    "time_points": ["March 1: electrical concerns first mentioned (batch anchor)", "March 16: safety check completed"],
    "conversation_references": ["Session 1: Initial electrical discussion", "Session 3: Safety verification"],
    "calculation_required": "March 16 - March 1 = 15 days (requires batch anchor inference)",
    "source_chat_ids": {
        "first_event": [12, 15],
        "second_event": [28, 31]
    }
}

## IMPORTANT REQUIREMENTS
1. **Do not** include any explicit dates (e.g. "March 12") in the **question**. Refer only to the event descriptions; the model must recall the dates itself.
2. **Inferential complexity**: Events should require inference from multiple temporal references
3. **Moderate temporal reasoning**: Question should require connecting multiple time clues
4. **Objective calculation**: Answer must be mathematically verifiable with inference explanation
5. **Contextual time points**: Events must have timing derivable from context or batch anchors
6. **Natural phrasing**: Question should sound realistic for moderate temporal memory testing

Generate ONE high-quality medium temporal reasoning question that tests duration calculation or sequence understanding requiring inference from multiple temporal references or batch anchors.

NOTE: Only output the JSON object without any explanation before or after.
"""
temporal_reasoning_probing_question_hard_prompt = """
You are tasked with generating a probing question to test temporal reasoning capabilities of LLMs. You will be given two related bullet points with temporal information and the corresponding multi-turn dialogs between a user and assistant that incorporate both time points across different conversation sessions.

Your task is to create ONE question that tests whether an LLM can perform complex multi-step temporal reasoning, advanced calculations, pattern analysis, or synthesis of multiple temporal relationships.

## INPUT DATA
- **BULLET POINTS**: <bullet_points>
- **CONVERSATION TURNS**: <conversation_turns>

## CRITICAL REQUIREMENTS: CHALLENGING TEMPORAL REASONING
- The question MUST NOT include any explicit dates, times, or temporal references
- Use only event descriptions that require the LLM to recall temporal information
- Create questions that require complex temporal reasoning, not simple lookups
- Test sophisticated temporal understanding across multiple conversation sessions

## ADVANCED QUESTION GENERATION GUIDELINES
Focus on creating questions that test:
- **Complex duration calculations**: Multi-step calculations involving multiple time periods
- **Relative temporal positioning**: Understanding temporal relationships without explicit dates
- **Cross-session temporal synthesis**: Connecting temporal information across different sessions
- **Temporal pattern recognition**: Identifying timing patterns or trends
- **Conditional temporal logic**: "If X happened before Y, how long until Z?"
- **Temporal inference**: Deriving timing from context clues rather than explicit dates

## SOPHISTICATED QUESTION TYPES

### **Duration & Calculation Questions**
1. **Multi-hop Duration**: "How much total time passed from when I first [started/began/initiated/mentioned] [activity/process/project/concern] until I [completed/finished/resolved/achieved] [outcome/goal/solution/milestone]?"
2. **Overlapping Periods**: "How long was there overlap between [process/activity/phase/treatment] and [process/activity/phase/treatment]?"
3. **Gap Analysis**: "What was the longest gap between any two [meetings/sessions/appointments/events/attempts/treatments/consultations]?"
4. **Cumulative Time**: "How much total time did I spend on [learning/practicing/working on/researching/developing] [skills/projects/subjects/treatments/solutions]?"
5. **Segmented Duration**: "How much time elapsed during the [initial/middle/final] [phase/stage/period/semester/quarter] of my [project/treatment/studies/training/development]?"

### **Sequence & Ordering Questions**
6. **Complex Sequencing**: "What was the order of the three most significant [breakthroughs/setbacks/decisions/discoveries/changes/milestones/achievements]?"
7. **Conditional Ordering**: "Which [event/session/meeting/treatment/attempt/decision] happened closest to when I [achieved/experienced/decided/realized/completed] [milestone/goal/breakthrough/change]?"
8. **Pattern Sequencing**: "In what sequence did I address the different [challenges/subjects/areas/concerns/goals/priorities/components]?"
9. **Progression Ordering**: "What was the chronological order of my [attempts/approaches/strategies/methods/treatments/studies]?"

### **Comparative & Analytical Questions**
10. **Timeline Comparison**: "Which took longer: the time between [event A/phase A/attempt A] and [event B/phase B/attempt B], or between [event B/phase B/attempt B] and [event C/phase C/attempt C]?"
11. **Frequency Analysis**: "How often did [successes/setbacks/breakthroughs/challenges/symptoms/improvements] occur compared to [failures/progress/difficulties/treatments/interventions/attempts]?"
12. **Temporal Density**: "During which period did I have the most [intense activity/concentrated effort/frequent sessions/rapid progress/significant changes/active treatment]?"
13. **Interval Comparison**: "Which period had [shorter/longer] intervals between [sessions/attempts/treatments/meetings/practice/study]?"
14. **Acceleration Analysis**: "During which timeframe did my [progress/improvement/learning/development/recovery/growth] accelerate most rapidly?"

### **Inferential & Complex Questions**
15. **Causal Temporal**: "How long after I [identified/discovered/experienced/implemented/changed/started] [problem/solution/symptom/treatment/approach/method] did [improvement/result/outcome/effect/change/resolution] happen?"
16. **Milestone Spacing**: "What was the average time between major [breakthroughs/achievements/milestones/improvements/setbacks/decisions/discoveries]?"
17. **Temporal Optimization**: "Which [events/sessions/treatments/attempts/approaches/interventions] happened with the shortest time gaps between them?"
18. **Phase Duration**: "How long did the [learning/recovery/development/research/preparation/implementation/training] [phase/period/stage/semester/cycle] last from start to finish?"
19. **Transition Timing**: "How much time passed between when I [stopped/ended/completed] [old approach/previous method/initial treatment] and [started/began/initiated] [new approach/different method/alternative treatment]?"
20. **Response Latency**: "How quickly after [implementing/starting/changing/trying] [strategy/treatment/approach/method] did I [notice/experience/achieve/observe] [results/improvement/changes/effects]?"

### **Between-Time Information Extraction**: 
21. "What/Who/Where/How much/When [specific query] between [starting point] and [ending point]?"

## FORBIDDEN QUESTION ELEMENTS
- Do NOT mention specific dates, times, or numbers in the question
- Do NOT use phrases like "on [specific date]" or "after [X] days/weeks/months"
- Do NOT reference explicit temporal markers like "January," "Monday," "3:00 PM"
- Do NOT make calculations obvious or simple
- Do NOT use calendar references or clock times
- Do NOT include duration units in the question itself

## GOOD VS BAD EXAMPLES

BAD (Too Easy): "How many days between March 15 and March 27?"
BAD (Date Reference): "How long after the March inspection did installation happen?"
BAD (Simple): "Which happened first, X or Y?"

GOOD (Complex): "How much total time elapsed from when I first discussed the electrical work until the final safety inspection was completed?"
GOOD (Multi-hop): "What was the longest gap between any consultant visits?"
GOOD (Inferential): "How long after I identified the noise problem did I implement the first solution?"

## TEMPORAL COMPLEXITY LEVEL: HARD
- **Hard**: Requires multi-step temporal reasoning across 3+ conversation sessions, complex calculations, pattern analysis, temporal inference, or synthesis of multiple temporal relationships

## QUESTION LANGUAGE REQUIREMENTS
- Write questions as if the USER is asking them naturally
- **If testing information from USER messages**: Use first person ("I", "my", "me") in question → Answer uses ("you", "your")
  - Example: "How did I decide on the location?" → "You decided on the location because..."
- **If testing information from ASSISTANT messages**: Use second person ("you", "your") in question → Answer uses ("I", "my") 
  - Example: "What steps did you suggest for handling this?" → "I suggested doing..."
- Avoid phrases like "according to the conversation", "based on what was discussed"
- Make questions sound conversational and natural
- Questions should require deep temporal reasoning to answer

## CHAT ID TRACKING REQUIREMENT
- You MUST identify which specific chat_id(s) contain the temporal information for both events
- List the chat_id for the first temporal event and the chat_id for the second temporal event
- NOTE: If the answer is spread out between multiple chat_ids, group them in one list
- NOTE: DO NOT INCLUDE chat_ids in the answer
- Use the exact chat_id numbers from the conversation turns

## OUTPUT FORMAT
Return your analysis in this exact JSON format:
{
    "question": "How much total time elapsed from when I first mentioned the electrical concerns until the final wiring safety check was completed?",
    "answer": "47 days elapsed from when you first mentioned electrical concerns on March 1 until the final wiring safety check was completed on April 17.",
    "difficulty": "hard",
    "temporal_type": "multi_hop_duration",
    "time_points": ["March 1: Initial electrical concerns", "April 17: Final safety check"],
    "conversation_references": ["Session 1: Initial electrical planning", "Session 4: Final safety verification"],
    "calculation_required": "Multi-step: March 1 to April 17 = 47 days total",
    "complexity_factors": ["requires identifying first and last electrical events", "spans multiple sessions", "involves process completion tracking"],
    "source_chat_ids": {
        "first_event": [12, 15],
        "second_event": [28, 31]
    }
}

## IMPORTANT REQUIREMENTS
1. **No temporal hints**: Question must NOT include dates, times, or temporal references
2. **Complex reasoning**: Require multi-step temporal analysis, not simple lookup
3. **Cross-session dependency**: Events should span multiple conversation sessions
4. **Advanced difficulty**: Always use "hard" difficulty level
5. **Sophisticated types**: Use advanced question types that test complex temporal reasoning
6. **Pattern recognition**: Include questions that test temporal patterns and relationships

Generate ONE high-quality, challenging temporal reasoning question that requires sophisticated temporal analysis between the provided bullet points.

NOTE: Only output the JSON object without any explanation before or after.
"""

abstention_probing_question_final_prompt = """
You are tasked with generating multiple probing questions to test abstention capabilities of LLMs. You will be given a plan containing bullet points that will be used to generate conversations between a user and AI assistant.

Your task is to create questions that test whether an LLM can appropriately respond with "I don't know" or "Based on the provided chat, there is no information related to [topic]" when asked about information that is missing or unavailable from the plan.

## INPUT DATA
- **PLAN**: <plan>

## CRITICAL REQUIREMENT: EARLY BATCH PRIORITIZATION
**SELECTION PRIORITY ORDER:**
1. **Batch 1-3 (HIGHEST PRIORITY)**: Select 70-80% of your questions from these early batches
2. **Batch 4-6 (MEDIUM PRIORITY)**: Select 10-20% of your questions from these middle batches  
3. **Batch 7+ (LOW PRIORITY)**: Select only 5-10% of your questions from later batches

## CRITICAL REQUIREMENT: CONTEXT-BASED HARD QUESTIONS
- Questions MUST be related to the plan's context and domain
- Ask about plausible information that SEEMS like it should be available but isn't
- Use names, places, events, and topics mentioned in the plan
- Ask for specific details about mentioned entities that aren't actually provided
- Create questions that would be natural follow-ups but can't be answered

## QUESTION GENERATION GUIDELINES
Focus on creating questions that test appropriate abstention for:
### 1. Missing Details About Mentioned People/Entities
- Ask about personal details, backgrounds, qualifications, or characteristics of mentioned [individuals/professionals/contacts/team members/experts/participants/characters/figures]
- Ask about relationships, connections, or histories between mentioned [people/entities/organizations/groups]
- Ask about [credentials/experience/opinions/preferences/motivations/backgrounds] that aren't provided
- Ask about [contact information/locations/affiliations/roles/responsibilities] not specified

### 2. Unavailable Specifics About Mentioned Events/Activities
- Ask for details about mentioned [meetings/sessions/appointments/consultations/treatments/classes/workshops/performances/competitions/ceremonies]
- Ask about [agendas/outcomes/discussions/decisions/results/feedback/reactions/atmosphere/participants] that weren't described
- Ask for [specific timing/duration/location/format/structure/content] of mentioned [events/activities/sessions/gatherings]
- Ask about [preparation/follow-up/consequences/impacts] of referenced [occasions/incidents/experiences]

### 3. Missing Information About Referenced Sources/Materials
- Ask about content of mentioned [documents/reports/studies/articles/books/websites/videos/presentations/recordings/files]
- Ask for details from referenced [research/data/statistics/findings/recommendations/guidelines/instructions/manuals]
- Ask about [authors/creators/publishers/sources/methodologies/conclusions] of mentioned [materials/resources/references]
- Ask for [specific quotes/sections/chapters/data points/examples] from referenced [sources/publications/media]

### 4. Unavailable Details About Mentioned Processes/Procedures
- Ask for specifics about mentioned [procedures/methods/techniques/approaches/strategies/protocols/systems/workflows]
- Ask about [steps/stages/requirements/prerequisites/tools/resources] for referenced [processes/treatments/training/development/implementation]
- Ask for [detailed instructions/guidelines/best practices/troubleshooting/variations] of mentioned [methods/approaches/systems]
- Ask about [timelines/costs/effectiveness/risks/alternatives] for described [procedures/strategies/solutions]

### 5. Missing Context About Mentioned Decisions/Choices
- Ask about reasoning behind [decisions/choices/selections/preferences/changes/recommendations/conclusions] that wasn't provided
- Ask for [criteria/factors/considerations/influences/constraints] that led to mentioned [decisions/outcomes/choices]
- Ask about [alternatives considered/rejected options/trade-offs/compromises] in referenced [decision-making/selection processes]
- Ask for [justifications/explanations/rationale/logic/evidence] behind stated [positions/recommendations/conclusions/actions]

### 6. Unavailable Quantitative/Measurement Details
- Ask for specific [numbers/amounts/quantities/measurements/percentages/rates/scores/rankings] not provided
- Ask about [costs/prices/budgets/expenses/investments/savings] for mentioned [items/services/activities/solutions]
- Ask for [timeframes/deadlines/schedules/durations/frequencies] of referenced [activities/processes/events/treatments]
- Ask about [performance metrics/success rates/effectiveness measures/comparison data] not specified

### 7. Missing Emotional/Subjective Information
- Ask about [feelings/emotions/reactions/satisfaction levels/comfort/stress/enjoyment] not described
- Ask for [opinions/preferences/impressions/evaluations/assessments] of mentioned [experiences/people/options/outcomes]
- Ask about [motivation/goals/hopes/concerns/fears/expectations] behind referenced [actions/decisions/choices]
- Ask for [subjective experiences/personal reactions/emotional responses] to described [situations/events/changes]

### 8. Unavailable Technical/Specialized Details
- Ask for [technical specifications/detailed features/advanced capabilities/limitations] of mentioned [tools/equipment/software/systems/products]
- Ask about [implementation details/configuration/setup/maintenance/troubleshooting] for referenced [technologies/solutions/systems]
- Ask for [scientific/medical/legal/financial/academic] details about mentioned [conditions/treatments/regulations/investments/studies]
- Ask about [industry standards/best practices/compliance requirements/certifications] related to discussed [areas/fields/domains]

### 9. Unavailable Future/Predictive Information
- Ask for [predictions/forecasts/projections/expectations] about mentioned [outcomes/trends/developments/changes]
- Ask about [future plans/next steps/upcoming events/anticipated results] not specified
- Ask for [long-term implications/consequences/effects/impacts] of described [actions/decisions/changes/treatments]
- Ask about [potential risks/opportunities/challenges/benefits] not discussed

## ABSTENTION QUESTION TYPES
Only generate these two types:
1. **Unavailable Information Questions**: Ask about topics, people, events, or details that are completely absent from the plan
2. **Missing Detail Questions**: Ask for specific details about topics that may be mentioned generally but lack the requested specifics

## DIFFICULTY LEVELS
Generate questions of varying abstention difficulty:
- **Easy**: Ask for details about mentioned entities that seem like they should be available
- **Medium**: Ask for specific information about mentioned processes/events that weren't detailed
- **Hard**: Ask for nuanced details that are plausible but not provided

## QUESTION LANGUAGE REQUIREMENTS
- Write questions as if the USER is asking them naturally
- **If testing information from USER messages**: Use first person ("I", "my", "me") in question → Answer uses ("you", "your")
  - Example: "How did I decide on the location?" → "You decided on the location because..."
- **If testing information from ASSISTANT messages**: Use second person ("you", "your") in question → Answer uses ("I", "my") 
  - Example: "What steps did you suggest for handling this?" → "I suggested doing..."
- Avoid phrases like "according to the conversation", "based on what was discussed", "from our chat history"
- Make questions sound conversational and natural
- Questions should flow naturally as if continuing the conversation

## OUTPUT FORMAT
Return your analysis in this exact JSON format:
[
    {
        "question": "What was the weather like during [specific event/day]?",
        "ideal_response": "Based on the provided chat, there is no information related to weather conditions.",
        "difficulty": "easy",
        "abstention_type": "unavailable_information",
        "why_unanswerable": "Weather information is not mentioned anywhere in the plan",
        "plan_reference": "No weather-related information provided in plan"
    },
    {
        "question": "What specific details were discussed in [mentioned meeting/conversation]?", 
        "ideal_response": "Based on the provided chat, there is no information related to the specific details of [meeting/conversation].",
        "difficulty": "medium",
        "abstention_type": "missing_detail",
        "why_unanswerable": "Meeting/conversation mentioned but specific content not provided",
        "plan_reference": "Plan mentions [meeting/conversation] but not detailed content"
    }
]

## IMPORTANT REQUIREMENTS
1. **Context-based questions**: Questions must relate to plan content and use mentioned entities
2. **Plausible but unavailable**: Ask for information that seems reasonable but isn't provided
3. **Natural follow-ups**: Questions should sound like logical next questions about mentioned topics
4. **Challenging abstention**: Make it harder for LLM to recognize information is missing
5. **Domain consistency**: Questions should fit naturally within the plan's subject matter

Generate 8-15 abstention questions that test the LLM's ability to appropriately say "Based on the provided chat, there is no information related to [topic]" when information is missing or unavailable in the plan.

NOTE: Only output the JSON array without any explanation before or after the list.
"""

preference_following_probing_question_final_prompt = """
You are tasked with generating a probing question to test preference following capabilities of LLMs. You will be given a bullet point containing a user preference and corresponding conversation turns where this preference was mentioned.

Your task is to create ONE question that tests whether an LLM remembers and respects the user's stated preference when making recommendations or providing advice.

## INPUT DATA
- **BULLET POINT**: <bullet_point>
- **CONVERSATION TURNS**: <conversation_turns>

## CRITICAL REQUIREMENT: COMPLETELY NEUTRAL QUESTION
- The question MUST BE COMPLETELY NEUTRAL with NO hints about any preference
- The question MUST NOT contain ANY words that suggest evaluation criteria
- The question should be so neutral it could test ANY type of preference in that domain
- The LLM should only know about the preference from previous conversation history

## MANDATORY PREFERENCE ANALYSIS STEP
BEFORE writing the question, you MUST:
1. **Extract ALL preference-related words** from the bullet point
2. **List ALL forbidden terms** including synonyms and related concepts
3. **Verify your question contains NONE of these terms**

## FORBIDDEN QUESTION ELEMENTS
- Do NOT mention any preference keywords
- Do NOT reference previous decisions or choices that reveal the preference
- Do NOT use phrases like "given my preference for X" or "considering I prefer Y"
- Do NOT hint at decision criteria or evaluation factors

## QUESTION LANGUAGE REQUIREMENTS
- Write questions as if the USER is asking them naturally
- Use first person ("I", "my", "me") when referring to the user
- Use second person ("you") when addressing the assistant
- Avoid phrases like "according to the conversation", "based on what was discussed", "from our chat history"
- Make questions sound conversational and natural
- Questions should flow naturally as if continuing the conversation
- NEVER mention the preference, decision criteria, or reasoning from the bullet point

## CHAT ID TRACKING REQUIREMENT
- You MUST identify which specific chat_id(s) contain the preference information
- List ALL chat_ids where the preference was mentioned or demonstrated
- NOTE: If the answer is spread out between multiple chat_ids, group them in one list
- NOTE: DO NOT INCLUDE chat_ids in the answer
- Use the exact chat_id numbers from the conversation turns

## OUTPUT FORMAT
Return your analysis in this exact JSON format:
{
    "question": "I'm considering different material options for my next project phase. What would you recommend?",
    "preference_being_tested": "I prefer materials that balance cost and performance; chose 3.5 lb/ft² MLV despite 20% higher price",
    "expected_compliance": "Response should recommend materials that balance cost and performance rather than just cheapest or most expensive options, acknowledging the user's preference for value optimization",
    "compliance_indicators": ["mentions cost-performance balance", "considers value over pure cost", "references previous material choice reasoning", "suggests options that optimize both factors"],
    "non_compliance_signs": ["only recommends cheapest option", "only recommends most expensive option", "ignores cost-performance balance preference", "doesn't consider user's stated values"],
    "difficulty": "medium",
    "preference_type": "decision_criteria",
     "source_chat_ids": [15, 22, 28]
}

## IMPORTANT REQUIREMENTS
1. **Preference-triggering question**: Question must create a situation where the stated preference should guide the response
2. **Clear compliance expectations**: Define what respecting the preference looks like
3. **Measurable indicators**: Provide specific signs of following vs. ignoring the preference
4. **Natural question phrasing**: Question should sound realistic and conversational
5. **Preference relevance**: Question must relate to the same domain/context as the stated preference

Generate ONE preference following question that tests whether the LLM remembers and applies the user's stated preference when providing recommendations or advice.

NOTE: Only output the JSON object without any explanation before or after.
"""

event_ordering_probing_question_easy_prompt = """
You are tasked with generating a probing question to test event ordering capabilities of LLMs. You will be given multiple related bullet points about the same topic/theme and the corresponding multi-turn dialogs between a user and assistant that incorporate these mentions across different conversation sessions.

Your task is to create ONE question that tests whether an LLM can recall the chronological order in which topics were MENTIONED in the conversation, regardless of when the actual events occurred in real life.

## INPUT DATA
- **BULLET POINTS**: <bullet_points>
- **CONVERSATION TURNS**: <conversation_turns>

## CRITICAL REQUIREMENT: NO EVENT SPOILERS
- The question MUST NOT list, mention, or hint at the specific events/mentions being tested
- The question should only specify the general topic/theme, not the individual events
- The LLM must recall and order the mentions entirely from memory
- This tests whether the LLM truly remembers the sequence without being given hints

## QUESTION GENERATION GUIDELINES
Focus on creating questions that test:
- **Mention sequence**: Order in which topics were brought up in conversation
- **Conversation chronology**: When topics appeared in chat sessions, not real-world timing
- **Discussion ordering**: Which topic was mentioned first, second, third in conversations
- **Reference sequence**: Order of mentions across different conversation sessions
- **Conversational timeline**: How topics were sequenced in the chat flow

## FORBIDDEN QUESTION ELEMENTS
- Do NOT list specific events like "including X, Y, and Z"
- Do NOT mention specific details
- Do NOT provide hints about what mentions to look for
- Do NOT reference specific people, dates, or activities unless asking about that person/topic generally

## QUESTION TYPES TO GENERATE (EASY LEVEL)
1. **Basic Mention Order**: "In what order did I mention [topic X] throughout our conversations?"
2. **Simple Discussion Sequence**: "Which did I talk about first: [option A], [option B], or [option C]?"
3. **Straightforward Timeline**: "Can you list the order in which I brought up different aspects of [topic]?"
4. **Basic Reference Ordering**: "When I discussed [topic], what was the sequence of mentions across our sessions?"
5. **Simple Chronology**: "In our conversation history, which [topic] did I mention earliest?"

## ORDERING COMPLEXITY LEVEL: EASY
- **Easy**: 4-5 mentions across multiple sessions with some temporal overlap
- Focus on moderate complexity requiring basic sequence reconstruction
- Test ability to track mentions across several sessions
- Include scenarios with some conversational overlap between sessions

## QUESTION LANGUAGE REQUIREMENTS
- Write questions as if the USER is asking them naturally
- Use first person ("I", "my", "me") when referring to the user
- Use second person ("you") when addressing the assistant
- Avoid phrases like "according to the conversation", "based on what was discussed", "from our chat history"
- Make questions sound conversational and natural
- Questions should flow naturally as if continuing the conversation

## MANDATORY QUESTION ENDING REQUIREMENT
- ALL questions MUST end with the phrase "in order" if previously didn't mention the order
- The order should mention ONLY ONCE
- This signals to the LLM that a sequential, ordered response is expected

## CHAT ID TRACKING REQUIREMENT [ONLY for source_chat_ids filed in JSON object]
- You MUST identify which specific chat_id(s) contain each mention in the ordering sequence
- List ALL chat_ids for each mention in chronological order in source_chat_ids field
- NOTE: If the answer is spread out between multiple chat_ids, group them in one list
- NOTE: DO NOT INCLUDE chat_ids in the answer
- Use the exact chat_id numbers from the conversation turns
- Map each mention to its source chat_id

## OUTPUT FORMAT
Return your analysis in this exact JSON format:
{
    "question": "In what order did I mention different interactions with Rami throughout our conversations?",
    "answer": "You mentioned Rami in this order: 1) First, meeting him at the Bahrain Acoustic Expo in February, 2) Then his site visit in April for sound testing, 3) Next, his progress praise via email in May, 4) Then his consultation recommendations, 5) Finally, his final results praise and maintenance recommendations in August.",
    "difficulty": "easy",
    "ordering_type": "mention_sequence",
    "total_mentions": 5,
    "conversation_references": ["Session 1: Initial meeting mention", "Session 2: Site visit mention", "Session 3: Email praise mention", "Session 4: Consultation", "Session 5: Final results mention"],
    "ordering_tested": ["1st: Expo meeting", "2nd: Site visit", "3rd: Email praise", "4th: Consultation", "5th: Final praise"],
    "source_chat_ids": [8, 15, 23, 31, 42]
}

## IMPORTANT REQUIREMENTS
1. **Conversational focus**: Question must test mention order in conversation, not real-world event order
2. **Clear sequence**: Answer must provide exact order of mentions across sessions
3. **Session awareness**: Reference which conversation sessions contained the mentions
4. **Mention specificity**: Identify specific aspects or details of each mention
5. **Moderate complexity**: Test sequence tracking across 4-5 mentions with some temporal overlap

Generate ONE high-quality event ordering question that tests the LLM's ability to recall the chronological order of 4-5 topic mentions across multiple conversation sessions.

NOTE: Only output the JSON object without any explanation before or after.
"""
event_ordering_probing_question_medium_prompt = """
You are tasked with generating a probing question to test event ordering capabilities of LLMs. You will be given multiple related bullet points about the same topic/theme and the corresponding multi-turn dialogs between a user and assistant that incorporate these mentions across different conversation sessions.

Your task is to create ONE question that tests whether an LLM can recall the chronological order in which topics were MENTIONED in the conversation, regardless of when the actual events occurred in real life.

## INPUT DATA
- **BULLET POINTS**: <bullet_points>
- **CONVERSATION TURNS**: <conversation_turns>

## CRITICAL REQUIREMENT: NO EVENT SPOILERS
- The question MUST NOT list, mention, or hint at the specific events/mentions being tested
- The question should only specify the general topic/theme, not the individual events
- The LLM must recall and order the mentions entirely from memory
- This tests whether the LLM truly remembers the sequence without being given hints

## QUESTION GENERATION GUIDELINES
Focus on creating questions that test:
- **Complex mention sequence**: Order in which topics were brought up with nuanced conversational flow
- **Sophisticated conversation chronology**: When topics appeared across sessions with contextual complexity
- **Advanced discussion ordering**: Which topics were mentioned in complex conversational patterns
- **Nuanced reference sequence**: Order of mentions across sessions with contextual subtleties
- **Complex conversational timeline**: How topics were sequenced with conversational nuance

## FORBIDDEN QUESTION ELEMENTS
- Do NOT list specific events like "including X, Y, and Z"
- Do NOT mention specific details
- Do NOT provide hints about what mentions to look for
- Do NOT reference specific people, dates, or activities unless asking about that person/topic generally

## QUESTION TYPES TO GENERATE (MEDIUM LEVEL)
1. **Nuanced Mention Order**: "In what order did I mention [topic X] throughout our conversations?"
2. **Complex Discussion Sequence**: "Which aspects of [topic] did I discuss first, and which came later?"
3. **Contextual Timeline**: "Can you list the order in which I brought up different elements of [topic]?"
4. **Advanced Reference Ordering**: "When I discussed [topic], what was the sequence of mentions across our sessions?"
5. **Sophisticated Chronology**: "How did my mentions of [topic] progress through our conversations?"

## ORDERING COMPLEXITY LEVEL: MEDIUM
- **Medium**: 5+ mentions with nuanced conversational flow and context
- Focus on complex sequence reconstruction with conversational subtleties
- Test ability to track mentions with sophisticated conversational patterns
- Include scenarios with nuanced context and complex mention patterns

## QUESTION LANGUAGE REQUIREMENTS
- Write questions as if the USER is asking them naturally
- Use first person ("I", "my", "me") when referring to the user
- Use second person ("you") when addressing the assistant
- Avoid phrases like "according to the conversation", "based on what was discussed", "from our chat history"
- Make questions sound conversational and natural
- Questions should flow naturally as if continuing the conversation

## MANDATORY QUESTION ENDING REQUIREMENT
- ALL questions MUST end with the phrase "in order" if previously didn't mention the order
- The order should mention ONLY ONCE
- This signals to the LLM that a sequential, ordered response is expected

## CHAT ID TRACKING REQUIREMENT [ONLY for source_chat_ids filed in JSON object]
- You MUST identify which specific chat_id(s) contain each mention in the ordering sequence
- List ALL chat_ids for each mention in chronological order in source_chat_ids field
- NOTE: If the answer is spread out between multiple chat_ids, group them in one list
- NOTE: DO NOT INCLUDE chat_ids in the answer
- Use the exact chat_id numbers from the conversation turns
- Map each mention to its source chat_id

## OUTPUT FORMAT
Return your analysis in this exact JSON format:
{
    "question": "In what order did I mention different budget concerns throughout our conversations?",
    "answer": "You mentioned budget concerns in this order: 1) Initial budget planning and estimates, 2) First contractor quote concerns, 3) Expense tracking and monitoring, 4) Budget adjustments and reallocations, 5) Cost overrun discussions, 6) Final budget reconciliation and analysis.",
    "difficulty": "medium",
    "ordering_type": "mention_sequence",
    "total_mentions": 6,
    "conversation_references": ["Session 1: Budget planning", "Session 2: Quote concerns", "Session 3: Expense tracking", "Session 4: Adjustments", "Session 5: Overrun issues", "Session 6: Final analysis"],
    "ordering_tested": ["1st: Planning", "2nd: Quote concerns", "3rd: Tracking", "4th: Adjustments", "5th: Overruns", "6th: Final analysis"],
    "source_chat_ids": [8, 15, 23, 31, 42]
}

## IMPORTANT REQUIREMENTS
1. **Conversational focus**: Question must test mention order in conversation, not real-world event order
2. **Clear sequence**: Answer must provide exact order of mentions across sessions
3. **Session awareness**: Reference which conversation sessions contained the mentions
4. **Mention specificity**: Identify specific aspects or details of each mention
5. **Complex patterns**: Test sequence tracking across 5+ mentions with nuanced conversational flow

Generate ONE high-quality event ordering question that tests the LLM's ability to recall the chronological order of 5+ topic mentions with nuanced conversational flow and context.

NOTE: Only output the JSON object without any explanation before or after.
"""
event_ordering_probing_question_hard_prompt = """
You are tasked with generating a probing question to test event ordering capabilities of LLMs. You will be given multiple related bullet points about the same topic/theme and the corresponding multi-turn dialogs between a user and assistant that incorporate these mentions across different conversation sessions.

Your task is to create ONE question that tests whether an LLM can recall the chronological order in which topics were MENTIONED in the conversation, regardless of when the actual events occurred in real life.

## INPUT DATA
- **BULLET POINTS**: <bullet_points>
- **CONVERSATION TURNS**: <conversation_turns>

## CRITICAL REQUIREMENTS: NO SPOILERS OR TIME HINTS
- The question MUST NOT list, mention, or hint at the specific events/mentions being tested
- The question should only specify the general topic/theme, not the individual events
- Do NOT include any time references, dates, or temporal hints in the question
- The LLM must recall and order the mentions entirely from memory without any hints

## ADVANCED QUESTION TYPES FOR EVENT ORDERING

### **Sequential Ordering Questions**
1. **General Mention Order**: "In what order did I mention [general topic]?"
2. **Discussion Progression**: "How did my discussions about [topic] evolve throughout our conversations?"
3. **Topic Development**: "What was the sequence of different aspects of [topic] I brought up?"

### **Comparative Ordering Questions**
4. **Priority Sequencing**: "Which aspects of [topic] did I discuss first, and which came later?"
5. **Category Comparison**: "In what order did I address the different types of [topic category]?"
6. **Frequency Ordering**: "Which [topic elements] did I mention most frequently, and in what order did they first appear?"

### **Pattern Recognition Questions**
7. **Mention Pattern**: "What pattern do you see in how I brought up [topic] across our conversations?"
8. **Discussion Flow**: "How did the flow of [topic] mentions progress through our sessions?"
9. **Topic Clustering**: "Which [topic aspects] did I tend to discuss together, and in what sequence?"

### **Analytical Ordering Questions**
10. **Chronological Reconstruction**: "Can you reconstruct the timeline of when I first mentioned each aspect of [topic]?"
11. **Session Distribution**: "How were my mentions of [topic] distributed across our different conversations?"
12. **Development Tracking**: "What was the progression of my thoughts about [topic] based on mention order?"

### **Complex Sequencing Questions**
13. **Multi-faceted Ordering**: "What was the order in which I explored different dimensions of [topic]?"
14. **Conversation Evolution**: "How did my focus on [topic] shift throughout our discussions?"
15. **Mention Density**: "Which periods of our conversations had the most mentions of [topic], and in what order?"

## FORBIDDEN QUESTION ELEMENTS
- Do NOT list specific events like "including X, Y, and Z"
- Do NOT mention specific details, dates, times, or temporal references
- Do NOT provide hints about what mentions to look for
- Do NOT reference specific timeframes (e.g., "in February", "during spring", "early in project")
- Do NOT use temporal words like "first", "then", "after", "before" in the question

## GOOD VS BAD EXAMPLES
BAD (Time Hints): "In what order did I mention Rami from February to August?"
BAD (Event Spoilers): "What was the sequence of meeting, site visit, and final consultation?"
BAD (Temporal References): "Which Rami interactions did I discuss first, then second?"

GOOD (General): "In what order did I mention different interactions with Rami?"
GOOD (Pattern): "What pattern do you see in how I brought up budget concerns?"
GOOD (Development): "How did my discussions about contractor issues evolve?"

## ORDERING COMPLEXITY LEVEL: HARD
- **Hard**: Either 8-10 mentions requiring chronological reconstruction or 8-10 mentions with complex conversational patterns or 8+ mentions requiring sophisticated sequence analysis
- Focus on advanced sequence reconstruction with sophisticated analysis
- Test ability to track complex mention patterns across multiple sessions
- Include scenarios requiring expert-level sequence analysis and pattern recognition

## QUESTION LANGUAGE REQUIREMENTS
- Write questions as if the USER is asking them naturally
- Use first person ("I", "my", "me") when referring to the user
- Use second person ("you") when addressing the assistant
- Avoid phrases like "according to the conversation", "based on what was discussed", "from our chat history"
- Make questions sound conversational and natural
- Questions should flow naturally as if continuing the conversation
- NEVER include temporal references or time-related words

## MANDATORY QUESTION ENDING REQUIREMENT
- ALL questions MUST end with the phrase "in order" if previously didn't mention the order
- The order should mention ONLY ONCE
- This signals to the LLM that a sequential, ordered response is expected

## CHAT ID TRACKING REQUIREMENT [ONLY for source_chat_ids filed in JSON object]
- You MUST identify which specific chat_id(s) contain each mention in the ordering sequence
- List ALL chat_ids for each mention in chronological order in source_chat_ids field
- NOTE: If the answer is spread out between multiple chat_ids, group them in one list
- NOTE: DO NOT INCLUDE chat_ids in the answer
- Use the exact chat_id numbers from the conversation turns
- Map each mention to its source chat_id

## OUTPUT FORMAT
Return your analysis in this exact JSON format:
{
    "question": "What pattern do you see in how I brought up different budget concerns throughout our conversations?",
    "answer": "You brought up budget concerns in this pattern: 1) Initial budget setting at the project start, 2) First contractor quote exceeding budget, 3) Multiple expense tracking updates, 4) Budget reallocations for different components, 5) Cost overrun discussions, 6) Savings identification opportunities, 7) Final budget reconciliation and project completion costs.",
    "difficulty": "hard",
    "ordering_type": "pattern_recognition",
    "total_mentions": 7,
    "conversation_references": ["Session 1: Initial budget discussion", "Session 2: Contractor quote concern", "Session 3: Expense tracking", "Session 4: Budget reallocation", "Session 5: Overrun discussions", "Session 6: Savings opportunities", "Session 7: Final costs"],
    "ordering_tested": ["1st: Initial budget", "2nd: Quote concern", "3rd: Expense tracking", "4th: Reallocations", "5th: Overruns", "6th: Savings", "7th: Final costs"],
    "complexity_factors": ["requires pattern recognition", "spans multiple sessions", "involves budget evolution tracking", "requires sophisticated sequence analysis"],
    "source_chat_ids": [8, 15, 23, 31, 42]
}

## IMPORTANT REQUIREMENTS
1. **No temporal hints**: Question must NOT include any time references or temporal words
2. **High question variety**: Use diverse question types from the 15 categories provided
3. **Complex reasoning**: Require sophisticated mention-order analysis
4. **Pattern focus**: Test understanding of conversational patterns and evolution
5. **Advanced difficulty**: Always use "hard" difficulty level
6. **General topic focus**: Ask about broad themes, not specific events
7. **Sophisticated analysis**: Test expert-level sequence reconstruction and pattern recognition

Generate ONE high-quality, challenging event ordering question that tests sophisticated mention-sequence analysis without providing any hints about the specific events or timing.

NOTE: Only output the JSON object without any explanation before or after.
"""

contradiction_resolution_probing_question_final_prompt = """
You are tasked with generating a probing question to test contradiction resolution capabilities of LLMs. You will be given two contradictory bullet points and the corresponding multi-turn dialogs between a user and assistant that incorporate both contradictory statements across different conversation sessions.

Your task is to create ONE question that asks about the contradicted topic as if seeking factual information, testing whether the LLM will detect the contradiction and ask for clarification rather than giving a definitive answer.

## INPUT DATA
- **BULLET POINTS**: <bullet_points>
- **CONVERSATION TURNS**: <conversation_turns>

## QUESTION GENERATION GUIDELINES
Focus on creating questions that:
- **Ask about the contradicted fact**: Question the topic that has contradictory information
- **Sound like normal fact-seeking**: Don't hint that there's a contradiction
- **Test contradiction detection**: Whether LLM notices conflicting information
- **Expect clarification request**: LLM should ask which contradictory statement is correct
- **Avoid revealing the contradiction**: Question should seem like routine information request

## CRITICAL REQUIREMENT:
- The question MUST be general and broad about the contradicted topic
- Do NOT include specific dates, times, locations, or detailed circumstances
- Do NOT reference specific events or instances that would narrow down the contradiction
- Ask about the general pattern/behavior, not specific occurrences
- This tests whether the LLM can detect contradictions across all related mentions

## QUESTION LANGUAGE REQUIREMENTS
- Write questions as if the USER is asking them naturally
- Use first person ("I", "my", "me") when referring to the user
- Use second person ("you") when addressing the assistant
- Avoid phrases like "according to the conversation", "based on what was discussed", "from our chat history"
- Make questions sound conversational and natural
- Questions should flow naturally as if continuing the conversation

## QUESTION FORMAT
Generate questions that ask about the contradicted topic directly:
- "Has Jeremiah ever attended Bahrain Jazz Festival events?"
- "How many siblings do you have?"
- "Where have you always lived?"
- "Is [person] still alive?"

## EXPECTED LLM BEHAVIOR
The ideal LLM response should:
1. Recognize the contradiction in previous statements
2. Not give a definitive answer
3. Ask for clarification: "You mentioned contradictory information about this. Which is correct?"
4. Reference both contradictory statements

## CHAT ID TRACKING REQUIREMENT
- You MUST identify which specific chat_id(s) contain each contradictory statement
- List the chat_id for the first contradictory statement and the chat_id for the second contradictory statement
- NOTE: If the answer is spread out between multiple chat_ids, group them in one list
- NOTE: DO NOT INCLUDE chat_ids in the answer
- Use the exact chat_id numbers from the conversation turns

## OUTPUT FORMAT
Return your analysis in this exact JSON format:
{
    "question": "Has Jeremiah ever attended Bahrain Jazz Festival events?",
    "ideal_answer": "I notice you've mentioned contradictory information about this. You said Jeremiah has never attended any Bahrain Jazz Festival events, but you also mentioned meeting him at the Bahrain Jazz Festival in 2015. Which statement is correct?",
    "difficulty": "clear",
    "contradiction_type": "never_statement_violation",
    "topic_questioned": "Jeremiah's festival attendance",
    "conversation_references": ["Session 1: Meeting at festival", "Session 8: Never attended statement"],
    "tests_for": "LLM should detect contradiction and request clarification instead of giving definitive answer",
    "source_chat_ids": {
        "first_statement": [12, 15],
        "second_statement": [34, 38]
    }
}

## IMPORTANT REQUIREMENTS
1. **Natural question phrasing**: Question should sound like normal fact-seeking, not contradiction testing
2. **Topic focus**: Ask directly about the contradicted subject
3. **Contradiction detection expectation**: LLM should notice and ask for clarification
4. **No hint giving**: Don't reveal that there's a contradiction in the question
5. **Clarification seeking**: Ideal response should ask which statement is correct

Generate ONE contradiction resolution question that tests whether the LLM will detect the contradiction and appropriately request clarification when asked about the contradicted topic.

CRITICAL NOTE: Do NOT include specific dates, times, locations, or detailed circumstances in the question that make the question easy.
NOTE: Only output the JSON object without any explanation before or after.
"""

summarization_probing_question_easy_prompt = """
You are tasked with generating a probing question to test basic summarization capabilities of LLMs. You will be given 2-3 related bullet points about the same topic/theme and the corresponding multi-turn dialogs between a user and assistant that incorporate this information across different conversation sessions.

Your task is to create ONE question that tests whether an LLM can synthesize and condense basic information from across 2-3 conversation sessions into simple, coherent summaries.

## INPUT DATA
- **BULLET POINTS**: <bullet_points>
- **CONVERSATION TURNS**: <conversation_turns>

## CRITICAL REQUIREMENT: EASY SUMMARIZATION
- Focus on basic information synthesis from 2-3 bullet points
- Test straightforward condensation of simple topics
- Require basic narrative coherence with minimal complexity
- Ask for simple overviews that combine clear, direct information

## CRITICAL REQUIREMENT: NEUTRAL SUMMARIZATION TESTING
- The question MUST NOT reveal what should be included in the summary
- The question MUST mention *only* the overarching topic—no specific bullet‑point details, subtopics, phases, or technical terms may appear.
- The question MUST NOT hint at the structure or content of the expected answer
- The question should be maximally generic, forcing the LLM to identify and synthesize all relevant information independently

## QUESTION GENERATION GUIDELINES
Focus on creating questions that test:
- **Basic information combination**: Merging simple details into brief narratives
- **Simple cross-session condensation**: Summarizing from 2-3 conversation sessions
- **Straightforward overview**: Capturing key aspects of simple topics
- **Basic narrative structure**: Creating simple, logical summaries
- **Essential detail inclusion**: Including important facts in concise format

## QUESTION TYPES TO GENERATE (EASY LEVEL)
1. **Simple Relationship Summary**: "Can you summarize my interactions with [Person X]?"
2. **Basic Process Overview**: "Summarize what happened with [simple process/task]."
3. **Direct Resource Summary**: "Give me a summary of [simple resource/item] information."
4. **Basic Decision Summary**: "Summarize my decision about [straightforward choice]."
5. **Simple Problem Summary**: "Can you summarize the [basic problem] and what happened?"
6. **Basic Development Summary**: "Summarize what happened with [topic] over time."
7. **Simple Learning Summary**: "Summarize what I learned about [basic subject]."
8. **Direct Experience Summary**: "Summarize my experience with [person/service/item]."

## SUMMARIZATION COMPLEXITY LEVEL: EASY
- **Easy**: 2-3 bullet points requiring basic topic overview with key facts
- Focus on simple information combination with minimal synthesis
- Test ability to condense straightforward information into brief summaries
- Include basic narrative flow without complex relationships

## QUESTION LANGUAGE REQUIREMENTS
- Write questions as if the USER is asking them naturally
- Use first person ("I", "my", "me") when referring to the user
- Use second person ("you") when addressing the assistant
- Avoid phrases like "according to the conversation", "based on what was discussed", "from our chat history"
- Make questions sound conversational and natural
- Questions should flow naturally as if continuing the conversation

## CHAT ID TRACKING REQUIREMENT
- You MUST identify which specific chat_id(s) contain the information needed for the summary
- List ALL chat_ids where relevant summary information appears
- NOTE: If the answer is spread out between multiple chat_ids, group them in one list
- NOTE: DO NOT INCLUDE chat_ids in the answer
- Use the exact chat_id numbers from the conversation turns

## OUTPUT FORMAT
Return your analysis in this exact JSON format:
{
    "question": "Can you summarize my interactions with the acoustic consultant?",
    "ideal_summary": "You met with Rami Al-Hassan, an acoustic consultant, at the Bahrain Acoustic Expo where he recommended HVAC silencing for $2,200. He then visited your site to conduct initial sound testing and measured 48 dB noise reduction. Your interactions focused on getting expert advice for your studio's acoustic needs.",
    "difficulty": "easy",
    "summarization_type": "simple_interaction_summary",
    "bullet_points_covered": 2,
    "conversation_sessions": 2,
    "key_elements_tested": ["basic interaction sequence", "simple factual combination", "straightforward narrative"],
    "synthesis_required": "Combining basic information into simple coherent summary",
    "source_chat_ids": [8, 15, 22, 29]
}

## IMPORTANT REQUIREMENTS
1. **Basic coverage**: Summary should include key information from 2-3 bullet points
2. **Simple coherence**: Create basic logical flow in the summary
3. **Minimal synthesis**: Combine straightforward information with basic structure
4. **Concise format**: Keep summaries brief and to the point
5. **Natural question phrasing**: Question should sound realistic for requesting simple summaries

Generate ONE basic summarization question that tests the LLM's ability to combine 2-3 bullet points into a simple, coherent summary.

NOTE: Only output the JSON object without any explanation before or after.
"""
summarization_probing_question_medium_prompt = """
You are tasked with generating a probing question to test intermediate summarization capabilities of LLMs. You will be given 4-5 related bullet points about the same topic/theme and the corresponding multi-turn dialogs between a user and assistant that incorporate this information across different conversation sessions.

Your task is to create ONE question that tests whether an LLM can synthesize and condense moderately complex information from across 3-4 conversation sessions into well-structured, comprehensive summaries.

## INPUT DATA
- **BULLET POINTS**: <bullet_points>
- **CONVERSATION TURNS**: <conversation_turns>

## CRITICAL REQUIREMENT: MEDIUM SUMMARIZATION
- Focus on moderate information synthesis from 4-5 bullet points
- Test multi-faceted condensation requiring narrative flow
- Require moderate synthesis with clear cause-and-effect relationships
- Ask for summaries that demonstrate progression and development

## CRITICAL REQUIREMENT: NEUTRAL SUMMARIZATION TESTING
- The question MUST NOT reveal what should be included in the summary
- The question MUST mention *only* the overarching topic—no specific bullet‑point details, subtopics, phases, or technical terms may appear.
- The question MUST NOT hint at the structure or content of the expected answer
- The question should be maximally generic, forcing the LLM to identify and synthesize all relevant information independently

## QUESTION GENERATION GUIDELINES
Focus on creating questions that test:
- **Moderate information synthesis**: Combining interconnected details into coherent narratives
- **Multi-session condensation**: Summarizing information from 3-4 conversation sessions
- **Progressive overview**: Capturing development and evolution of topics
- **Narrative flow**: Creating logical, well-structured summaries with clear progression
- **Balanced detail inclusion**: Including important information while maintaining narrative coherence

## QUESTION TYPES TO GENERATE (MEDIUM LEVEL)
1. **Developing Relationship Summary**: "Can you summarize my entire relationship and interactions with [Person X] throughout the project?"
2. **Multi-phase Process Overview**: "Summarize the complete [process/workflow] from start to current progress."
3. **Resource Evolution Summary**: "Give me a summary of how [resource/budget/timeline] evolved throughout our discussions."
4. **Complex Decision Journey**: "Summarize the decision-making process and considerations for [topic/choice]."
5. **Problem-Solution Narrative**: "Can you summarize how I identified and addressed [problem/challenge] over time?"
6. **Chronological Development**: "Summarize the development and progression of [topic] through our conversations."
7. **Learning Journey Summary**: "Summarize my learning experience and progress with [subject/skill]."
8. **Multi-stage Negotiation**: "Summarize the negotiation process and how it evolved for [topic]."

## SUMMARIZATION COMPLEXITY LEVEL: MEDIUM
- **Medium**: 4-5 bullet points requiring multi-faceted summary with narrative flow
- Focus on moderate synthesis requiring understanding of relationships and progression
- Test ability to identify patterns and development across sessions
- Include narrative elements with clear connections and causation

## QUESTION LANGUAGE REQUIREMENTS
- Write questions as if the USER is asking them naturally
- Use first person ("I", "my", "me") when referring to the user
- Use second person ("you") when addressing the assistant
- Avoid phrases like "according to the conversation", "based on what was discussed", "from our chat history"
- Make questions sound conversational and natural
- Questions should flow naturally as if continuing the conversation

## CHAT ID TRACKING REQUIREMENT
- You MUST identify which specific chat_id(s) contain the information needed for the summary
- List ALL chat_ids where relevant summary information appears
- NOTE: If the answer is spread out between multiple chat_ids, group them in one list
- NOTE: DO NOT INCLUDE chat_ids in the answer
- Use the exact chat_id numbers from the conversation turns

## OUTPUT FORMAT
Return your analysis in this exact JSON format:
{
    "question": "Can you summarize my entire relationship and all interactions with Rami throughout our project?",
    "ideal_summary": "Your relationship with Rami Al-Hassan, the acoustic consultant, evolved through several key interactions: You first met him at the Bahrain Acoustic Expo in February 2024, where he recommended HVAC silencing for $2,200. He then conducted an initial site visit in March, measuring 48 dB noise reduction. During a mid-project visit in April, he advised repositioning bass traps to improve absorption by 5 dB. Finally, he scheduled a consultation in April to verify your STC-65 achievement goal. Throughout this relationship, Rami provided expert guidance on acoustic optimization and helped ensure your studio met professional soundproofing standards.",
    "difficulty": "medium",
    "summarization_type": "progressive_relationship",
    "bullet_points_covered": 4,
    "conversation_sessions": 4,
    "key_elements_tested": ["relationship progression", "chronological development", "professional interactions", "technical recommendations", "project milestones"],
    "synthesis_required": "Combining scattered interactions into coherent relationship narrative with clear progression",
    "source_chat_ids": [8, 15, 22, 29]
}

## IMPORTANT REQUIREMENTS
1. **Progressive coverage**: Summary should show development and evolution across 4-5 bullet points
2. **Narrative coherence**: Create logical flow with clear cause-and-effect relationships
3. **Multi-session synthesis**: Combine information from 3-4 conversation sessions
4. **Balanced condensation**: Include important details while maintaining narrative flow
5. **Natural question phrasing**: Question should sound realistic for requesting comprehensive summaries

Generate ONE intermediate summarization question that tests the LLM's ability to synthesize 4-5 bullet points into a coherent, progressive summary.

NOTE: Only output the JSON object without any explanation before or after.
"""
summarization_probing_question_hard_prompt = """
You are tasked with generating a probing question to test advanced summarization capabilities of LLMs. You will be given 6-8 related bullet points about the same topic/theme and the corresponding multi-turn dialogs between a user and assistant that incorporate this information across different conversation sessions.

Your task is to create ONE question that tests whether an LLM can synthesize and condense complex, multi-faceted information from across 4+ conversation sessions into sophisticated, comprehensive summaries.

## INPUT DATA
- **BULLET POINTS**: <bullet_points>
- **CONVERSATION TURNS**: <conversation_turns>

## CRITICAL REQUIREMENT: HARD SUMMARIZATION
- Focus on complex information synthesis from 8-10 bullet points
- Test comprehensive synthesis requiring sophisticated analysis
- Require advanced narrative construction with multiple threads
- Ask for summaries that demonstrate deep understanding and integration

## CRITICAL REQUIREMENT: NEUTRAL SUMMARIZATION TESTING
- The question MUST NOT reveal what should be included in the summary
- The question MUST mention *only* the overarching topic—no specific bullet‑point details, subtopics, phases, or technical terms may appear.
- The question MUST NOT hint at the structure or content of the expected answer
- The question should be maximally generic, forcing the LLM to identify and synthesize all relevant information independently

## QUESTION GENERATION GUIDELINES
Focus on creating questions that test:
- **Complex information synthesis**: Combining multiple interconnected details into sophisticated narratives
- **Advanced cross-session condensation**: Summarizing information from 4+ conversation sessions
- **Comprehensive overview**: Capturing all key aspects with detailed progression and relationships
- **Sophisticated narrative coherence**: Creating complex, well-structured summaries with multiple threads
- **Strategic detail prioritization**: Including extensive information while maintaining logical structure

## QUESTION TYPES TO GENERATE (HARD LEVEL)
1. **Complex Relationship & Interaction Summary**: "Can you provide a comprehensive summary of all key relationships and interactions discussed?"
2. **Complete Sequence & Event Analysis**: "Summarize the entire sequence of events from the starting point through the conclusion, covering all stages and developments."
3. **Resource, Effort, & Timeline Evolution**: "Give me a detailed summary of how resources, efforts, and timelines were allocated and adjusted throughout the whole situation."
4. **Multi-factor Decision Process Review**: "Summarize the full decision-making process, including all factors, participants, and considerations that shaped the final outcome."
5. **Problem-to-Resolution Journey**: "Can you summarize the complete journey from identifying the issue to reaching a resolution, including all challenges and solutions?"
6. **Chronological Development Overview**: "Summarize the entire progression and evolution of the topic from the beginning to the end, highlighting all major turning points."
7. **Knowledge & Insight Integration Summary**: "Summarize the full process of gathering, developing, and applying knowledge or insights on this topic, including all relevant sources."
8. **Complex Negotiation or Agreement Path**: "Provide a comprehensive summary of the discussions and negotiations that took place, including positions, compromises, and final agreements."

## SUMMARIZATION COMPLEXITY LEVEL: HARD
- **Hard**: 8-10 bullet points requiring comprehensive synthesis with detailed progression
- Focus on sophisticated analysis requiring understanding of complex relationships and patterns
- Test ability to synthesize multiple narrative threads and extensive information
- Include advanced narrative elements with multi-layered connections and sophisticated causation

## QUESTION LANGUAGE REQUIREMENTS
- Write questions as if the USER is asking them naturally
- Use first person ("I", "my", "me") when referring to the user
- Use second person ("you") when addressing the assistant
- Avoid phrases like "according to the conversation", "based on what was discussed", "from our chat history"
- Make questions sound conversational and natural
- Questions should flow naturally as if continuing the conversation

## CHAT ID TRACKING REQUIREMENT
- You MUST identify which specific chat_id(s) contain the information needed for the summary
- List ALL chat_ids where relevant summary information appears
- NOTE: If the answer is spread out between multiple chat_ids, group them in one list
- NOTE: DO NOT INCLUDE chat_ids in the answer
- Use the exact chat_id numbers from the conversation turns

## OUTPUT FORMAT
Return your analysis in this exact JSON format:
{
    "question": "string",
    "ideal_summary": "string",
    "difficulty": "hard",
    "summarization_type": "comprehensive_project_analysis",
    "bullet_points_covered": 7,
    "conversation_sessions": 6,
    "key_elements_tested": ["multi-stakeholder coordination", "complex project progression", "technical and financial integration", "strategic decision-making", "comprehensive outcome analysis", "sophisticated narrative synthesis"],
    "synthesis_required": "Combining extensive scattered information into sophisticated, multi-threaded comprehensive narrative",
    "source_chat_ids": [8, 15, 22, 29]
}

## IMPORTANT REQUIREMENTS
1. **Comprehensive coverage**: Summary should integrate all key information from 8-10 bullet points
2. **Sophisticated coherence**: Create complex narrative with multiple threads and advanced logical structure
3. **Advanced multi-session synthesis**: Combine information from 4+ conversation sessions
4. **Strategic condensation**: Include extensive important details while maintaining sophisticated narrative structure
5. **Complex question phrasing**: Question should request comprehensive, sophisticated summaries

Generate ONE advanced summarization question that tests the LLM's ability to synthesize 8-10 bullet points into a sophisticated, comprehensive summary.

NOTE: Only output the JSON object without any explanation before or after.
"""

instruction_following_probing_question_final_prompt = """
You are tasked with generating a probing question to test instruction following capabilities of LLMs. You will be given a bullet point containing a user instruction and corresponding conversation turns where this instruction was mentioned.

Your task is to create ONE question that tests whether an LLM can follow the specific instruction by asking about the topic that triggers the instruction without including any hints or any part of the BULLET POINT in the question.

## INPUT DATA
- **BULLET POINT**: <bullet_point>
- **CONVERSATION TURNS**: <conversation_turns>

## CRITICAL REQUIREMENT: HIDDEN INSTRUCTION TESTING
- The question MUST be completely neutral and contain NO hints about the required response style
- The question MUST NOT reveal, mention, or hint at the instruction in any way
- The question should appear to be a normal request about the trigger topic
- Remove ALL words that could hint at the instruction requirement
- The question MUST exclude **every** word or phrase that appears in the `instruction_being_tested` field—no hard‑coded lists.  \
- Before generating, parse the instruction text and ban all its tokens from the question.

## QUESTION LANGUAGE REQUIREMENTS
- Write questions as if the USER is asking them naturally
- Use first person ("I", "my", "me") when referring to the user
- Use second person ("you") when addressing the assistant
- Avoid phrases like "according to the conversation", "based on what was discussed", "from our chat history"
- Make questions sound conversational and natural
- Questions should flow naturally as if continuing the conversation

## FORBIDDEN WORDS AND PHRASES
- Do NOT include ANY part of the BULLET POINT that gives any hints about instruction being tested in the generated QUESTION
- Do NOT use any words that appear in the instruction itself
- Do NOT use synonyms or related terms that could suggest the required response format
- The question must only mention the core topic WITHOUT any descriptive words about how to handle it
- (No need to list specific terms—your dynamic ban covers them all.)

## CORE PRINCIPLE
The LLM should have to RECALL and APPLY the instruction from memory, not receive any hints from the question itself. The question should be so basic that it could be answered in multiple ways, but the instruction should guide the LLM to respond in the specific required manner.

## CHAT ID TRACKING REQUIREMENT
- You MUST identify which specific chat_id(s) contain the instruction information
- List ALL chat_ids where the instruction was mentioned or demonstrated
- NOTE: If the answer is spread out between multiple chat_ids, group them in one list
- NOTE: DO NOT INCLUDE chat_ids in the answer
- Use the exact chat_id numbers from the conversation turns

## OUTPUT FORMAT
Return your analysis in this exact JSON format:
{
    "question": "Can you give me a budget estimate for the remaining work on my project?",
    "instruction_being_tested": "Always provide detailed cost breakdowns when I ask about budget estimates",
    "expected_compliance": "Response should include itemized costs, specific amounts for different categories, and detailed breakdown rather than just a total estimate",
    "compliance_indicators": ["itemized list of costs", "specific dollar amounts", "category-by-category breakdown", "detailed cost analysis"],
    "non_compliance_signs": ["only total estimate given", "vague cost ranges", "no itemization", "general budget discussion without specifics"],
    "difficulty": "medium",
    "instruction_type": "format_instruction",
    "source_chat_ids": [12, 25, 31]
}

## IMPORTANT REQUIREMENTS
1. **Completely neutral question**: Ask about core topic with NO style/format hints
2. **Instruction-triggering question**: Question must ask about the topic that triggers the specific instruction
3. **Natural question phrasing**: Question should sound realistic and conversational
4. **Zero instruction leakage**: Remove all words that could hint at the required behavior
5. **Pure topic focus**: Ask only about the subject matter, not how to present it

Generate ONE instruction following question that asks about the topic mentioned in the instruction to test whether the LLM properly follows the user's specified behavior.

NOTE: Only output the JSON object without any explanation before or after.
"""

# ################################################## LLM Judge prompts ##################################################

unified_llm_judge_base_prompt = """
You are an expert evaluator tasked with judging whether the LLM's response demonstrates compliance with the specified RUBRIC CRITERION.

## EVALUATION INPUTS
- QUESTION (what the user asked): <question>
- RUBRIC CRITERION (what to check): <rubric_item>
- RESPONSE TO EVALUATE: <llm_response>

## EVALUATION RUBRIC:
The rubric defines a specific requirement, constraint, or expected behavior that the LLM response should demonstrate. 

**IMPORTANT**: Pay careful attention to whether the rubric specifies:
- **Positive requirements** (things the response SHOULD include/do)
- **Negative constraints** (things the response SHOULD NOT include/do, often indicated by "no", "not", "avoid", "absent")

## RESPONSIVENESS REQUIREMENT (anchored to the QUESTION)
A compliant response must be **on-topic with respect to the QUESTION** and attempt to answer it.
- If the response does not address the QUESTION, score **0.0** and stop.
- For negative constraints, both must hold: (a) the response is responsive to the QUESTION, and (b) the prohibited element is absent.

## SEMANTIC TOLERANCE RULES:
Judge by meaning, not exact wording.
- Accept **paraphrases** and **synonyms** that preserve intent.
- **Case/punctuation/whitespace** differences must be ignored.
- **Numbers/currencies/dates** may appear in equivalent forms (e.g., “$68,000”, “68k”, “68,000 USD”, or “sixty-eight thousand dollars”). Treat them as equal when numerically equivalent.
- If the rubric expects a number or duration, prefer **normalized comparison** (extract and compare values) over string matching.

## STYLE NEUTRALITY (prevents style contamination):
Ignore tone, politeness, length, and flourish unless the rubric explicitly requires a format/structure (e.g., “itemized list”, “no citations”, “one sentence”).
- Do **not** penalize hedging, voice, or verbosity if content satisfies the rubric.
- Only evaluate format when the rubric **explicitly** mandates it.

## SCORING SCALE:
- **1.0 (Complete Compliance)**: Fully complies with the rubric criterion.
  - Positive: required element present, accurate, properly executed (allowing semantic equivalents).
  - Negative: prohibited element **absent** AND response is **responsive**.
  
- **0.5 (Partial Compliance)**: Partially complies.
  - Positive: element present but minor inaccuracies/incomplete execution.
  - Negative: generally responsive and mostly avoids the prohibited element but with minor/edge violations.
  
- **0.0 (No Compliance)**: Fails to comply.
  - Positive: required element missing or incorrect.
  - Negative: prohibited element present **or** response is non-responsive/evasive even if the element is absent.

## EVALUATION INSTRUCTIONS:
1. **Understand the Requirement**: Determine if the rubric is asking for something to be present (positive) or absent (negative/constraint).

2. **Parse Compound Statements**: If the rubric contains multiple elements connected by "and" or commas, evaluate whether:
   - **All elements** must be present for full compliance (1.0)
   - **Some elements** present indicates partial compliance (0.5)
   - **No elements** present indicates no compliance (0.0)
   
3. **Check Compliance**: 
   - For positive requirements: Look for the presence and quality of the required element
   - For negative constraints: Look for the absence of the prohibited element

4. **Assign Score**: Based on compliance with the specific rubric criterion according to the scoring scale above.

5. **Provide Reasoning**: Explain whether the rubric criterion was satisfied and justify the score.

## OUTPUT FORMAT:
Return your evaluation in JSON format with two fields:

{
   "score": [your score: 1.0, 0.5, or 0.0],
   "reason": "[detailed explanation of whether the rubric criterion was satisfied and why this justified the assigned score]"
}

NOTE: ONLY output the json object, without any explanation before or after that
"""

# **************** Metric-based prompts ****************

break_paragraph_to_facts_detailed_prompt = """
You are tasked with breaking down a paragraph or sentence into individual semantic fact units. Each fact unit should represent one distinct, atomic piece of information that can be independently verified or evaluated.

DEFINITION OF SEMANTIC FACT UNIT:
- A single, complete piece of information
- Cannot be broken down further without losing meaning
- Contains one main claim or statement
- Is independently verifiable
- Has clear subject-predicate relationship

EXTRACTION RULES:
1. Split compound sentences at conjunctions (and, but, or, so, etc.)
2. Separate temporal information into distinct facts
3. Break down lists into individual items
4. Isolate causal relationships (because, since, therefore)
5. Separate descriptive attributes from main statements
6. Extract numerical data as separate facts when relevant
7. Maintain context necessary for understanding each fact

QUESTION-BASED EXTRACTION NECESSITY:
- Identify what the question is asking for (who, what, when, where, why, how, how much, etc.)
- Extract semantic units that directly answer the question first
- Include supporting details and context as separate fact units
- Ensure extracted facts are meaningful in relation to the question asked

EXAMPLES:

INPUT: "John visited the store on Monday and bought three apples for $5, but he forgot to get milk because the dairy section was closed."

OUTPUT:
1. "John visited the store on Monday"
2. "John bought three apples"
3. "The apples cost $5"
4. "John forgot to get milk"
5. "The dairy section was closed"
6. "John forgot milk because the dairy section was closed"

INSTRUCTIONS:
- Extract ALL semantic fact units from the given text
- Number each fact unit sequentially
- Maintain factual accuracy - do not add or infer information
- Preserve important context within each fact unit
- Ensure each fact can stand alone as a meaningful statement
- DO NOT add any explanation before or after the text

QUESTION:
<question>

ANSWER TO EXTRACT FACTS FROM:
<input_text>

OUTPUT FORMAT:
1. [First semantic fact unit]
2. [Second semantic fact unit]
3. [Third semantic fact unit]
...

Begin extraction:
"""

# ################################################## Baseline prompts ##################################################

answer_generation_for_rag = """
You are an assistant that MUST answer questions using ONLY the information provided in the context below. 

STRICT INSTRUCTIONS:
1. Answer ONLY based on the provided context
2. Do NOT use your internal knowledge

CONTEXT:
<context>

QUESTION:
<question>

ANSWER REQUIREMENTS:
- Be direct and concise
- Only output the answer to the question without any explanation 

RESPONSE:
"""

# ################################################## Our method ##################################################

kv_creation_prompt = """ 
I provide you with a text. Your task it to identify all the details stated in the text,
and output that in key: value format.
E.g.:
Key 1: Value 1,
Key 2: Value 2,
Key 3: Value 3,
....

Also at the end, I want to provide a brieft summary of what this text was about in this format: Summary: 'summarized text'

Note: only ouput key-values and the summary. DO NOT provide any explanation before or after that.
Note: Do not ouput Key 1, Key 2, ...

text: <input_text>
"""

scratchpad_generation_prompt = """
You are a highly analytical AI assistant. Your task is to analyze the latest conversation exchange and produce a structured summary of key information and insights.

**Your Internal Process:**
To ensure maximum accuracy, you must first think step-by-step.
1.  **Analyze:** Break down the user's latest message.
2.  **Identify:** Pinpoint all facts, instructions, and updates.
3.  **Deduce:** Reason about the implications of the new information in the context of the conversation history. What is the user's underlying goal or state?
4.  **Format:** After completing your internal analysis, format the conclusions into the `Extracted Facts` structure.

**Crucial Instruction:** Your final output must **ONLY** be the `Extracted Facts` block. **DO NOT** include your step-by-step reasoning or any other text in your response. Strictly follow the format shown in the example's output.

---
**EXAMPLE**

**Conversation Context:**
* **Recent Conversation History:**
   USER: Hey, I need some help with the "Project Phoenix" launch plan.
   ASSISTANT: Of course. What do you need?
   USER: The launch date is set for September 15th, 2025. I'm responsible for the marketing materials.
* **Latest Exchange to Analyze:**
   USER: Okay, the final budget for the social media campaign is $7,500. The client, Innovate Corp, just approved it. Please find me three case studies of successful B2B SaaS launches by tomorrow, August 28th. And don't include any of our direct competitors in the examples.
   ASSISTANT: Understood. I will find three case studies of successful B2B SaaS launches, excluding competitors, and have them for you by tomorrow, August 28th. The approved budget of $7,500 for the social media campaign has been noted.

**Example of Correct Final Output:**
   * The client's name is "Innovate Corp".
   * The project is related to a "B2B SaaS launch".
   * The final budget for the social media campaign is $7,500.
   * A deadline is set for "tomorrow, August 28th".
   * User intends to review three case studies for the project.
   * Instruction: Find three case studies.
   * Constraint: Do not include direct competitors in the examples.
   * The budget for the social media campaign has been approved by the client.
   * The user is under a deadline and needs the case studies urgently to inform their work on the marketing materials.

---
**ACTUAL TASK**

**Recent Conversation History:**
<history>

**Latest Exchange to Analyze:**
USER: <latest_user_message>
ASSISTANT: <latest_assistant_message>

**Extracted Facts:**
"""

scratchpad_summarizer_all_at_once_prompt = """
You are tasked with processing multiple scratch pad entries from a conversation to create a unified, coherent summary.

**Input Scratch Pads (chronologically ordered):**
<content>

**Target Length:** <tokens_limit> words

**Your Task:**
Transform these individual scratch pad entries into a single, well-organized summary by clustering related information and removing redundancy.

**Process:**
1. **Identify Clusters**: Group related information across all scratch pads by topic, entity, theme, or subject matter
2. **Merge & Deduplicate**: Combine similar points, eliminate redundancy, and synthesize overlapping information
3. **Prioritize**: Keep the most important, actionable, and contextually relevant information
4. **Organize**: Structure the final summary logically with clear topic groupings

**Clustering Priorities:**
- **Entities** (people, organizations, products, locations mentioned multiple times)
- **Processes** (workflows, procedures, methodologies discussed)
- **Decisions** (choices made, preferences stated, requirements established)
- **Timeline Events** (chronological developments, milestones, deadlines)
- **Problems & Solutions** (issues raised and their resolutions)
- **Resources** (tools, documents, assets, budgets mentioned)

**Output Format:**
Return ONLY the clustered and summarized content organized as:

**KEY ENTITIES & RELATIONSHIPS:**
- [Consolidated information about important people, organizations, systems]

**CORE DECISIONS & PREFERENCES:**
- [Merged decision points, requirements, constraints, preferences]

**PROCESSES & WORKFLOWS:**
- [Combined procedural information, methodologies, steps]

**CRITICAL CONTEXT:**
- [Essential background information and situational details]

**ACTIONABLE ITEMS:**
- [Next steps, pending actions, follow-ups, deadlines]

**IMPORTANT DEVELOPMENTS:**
- [Significant events, changes, updates, milestones]

**Quality Requirements:**
- Each bullet point should be comprehensive yet concise
- Eliminate redundant information across scratch pads
- Prioritize information that provides ongoing context value
- Maintain chronological awareness where relevant
- Stay within the <tokens_limit> word limit while maximizing information density

**CRITICAL LENGTH REQUIREMENT:**
- Your response MUST be approximately <tokens_limit> words
- Your response MUST not be lower than <tokens_limit> words
- If your draft is significantly shorter than <tokens_limit> words, ADD MORE DETAIL
"""

scratchpad_summarizer_iterative_prompt = """
You are tasked with summarizing and compressing scratch pad content to fit within a specific token limit.
**Input Content:**
<content>

**Target Length:** <tokens_limit> tokens

**Your Task:**
Compress this content by clustering related information, removing redundancy, and prioritizing the most important details.

**Process:**
1. **Cluster**: Group related information by topic, entity, or theme
2. **Deduplicate**: Remove redundant or repetitive information
3. **Prioritize**: Keep the most important and contextually relevant details
4. **Compress**: Condense while maintaining essential meaning and context

**Output Format:**
Return ONLY the compressed content organized as:

**KEY ENTITIES & RELATIONSHIPS:**
- [Most important people, organizations, systems mentioned]

**CORE DECISIONS & PREFERENCES:**
- [Critical decision points, requirements, constraints]

**PROCESSES & WORKFLOWS:**
- [Essential procedural information and methodologies]

**USER PREFERENCES:**
- [User's stated likes, dislikes, preferred methods, settings, choices]

**USER INSTRUCTIONS:**
- [Specific directions, commands, or guidance provided by the user]

**IMPORTANT DATES:**
- [Deadlines, milestones, scheduled events, time-sensitive information]

**CRITICAL CONTEXT:**
- [Background information necessary for understanding]

**ACTIONABLE ITEMS:**
- [Next steps, pending actions, deadlines]

**IMPORTANT DEVELOPMENTS:**
- [Significant events, changes, milestones]

**Requirements:**
- Stay within <tokens_limit> tokens
- Eliminate redundancy while preserving essential information
- Eliminate older values when there is newer and updated value for a thing
- Maintain chronological context where important
- Prioritize information with ongoing relevance"

**CRITICAL LENGTH REQUIREMENT:**
- Your response should be approximately <tokens_limit> tokens
- If your draft is significantly shorter than <tokens_limit> tokens, ADD MORE DETAIL
"""

filter_chunk_context_prompt = """
I provide you with a user query and a text chunk.
You need to decide if the text chunk is nesseccery for answering user question.
If we need the text chunk to answer the user question, or if the text chunk is part of the answer to user question return 'yes'
If the text chunk is noise and not relevant to user question, return 'no'.
Output format: Return only 'yes' or 'no', without any explantion before or after that.

User query: <query> \n\n
Text chunk: <doc_text>
"""

filter_all_context_prompt = """
You are a precise information extractor.

Your task:
Given a USER QUESTION and a LONG TEXT, identify *only the passages that are necessary to answer the question*.  
Do not rewrite, summarize, or paraphrase. Copy the relevant spans exactly as they appear in the text.  
If multiple passages are relevant, extract them all.  
If nothing is relevant, return an empty string.

User query: <query> \n\n
Text chunk: <scratch_pad>
"""
