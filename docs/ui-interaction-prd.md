# UI & Interaction.PRD

Design the modern astectic , clean UI interface which is very user friendly to navigate the different menu items.
Create a website in dark theame

I would like to have option to navigate throught career map.  
UI should have the below dashboard
- Dashboard
  - Various matrix based on the student profile.
    - Total anlaysis
    - Total anlaysis based on the stream
    - Total anlaysis based on the State
    - Total anlaysis based on the board

- Student anlaysis
  - Student Profile
  - Student Psycology test
  - Geneate the report , view , downloadable pdf.
- RoadMap
- Reports
  - list all the analysis done.
- Top down approach
  - where student can have goal in mind and the application should be able to provide the guidance how to reach that goal.
    For e.g.
      I want to become the Nasa Scientist.
      I want to become the Doctor.

 StudentName
    - 10th
    - 12th
        - List all the options for each of the subject stream after 12th
        - list out top 10 college in india for each stream
        - list out top 5 colleges state wise in each steam.
    - Preparaton from Coaching institute for different stream ,for e.g Engineering coaching institiute , CA etc
    - Bachelors Degree option student have
      - list out top 10 college in india for each stream
      - list out all the top 5 colleges state wise in each steam.
    - Masther Degree option student have
      - list out top 10 college in india for each stream
      - list out all the top 5 colleges state wise in each steam.
    - Options of Higher studies , research , PHd etc 
   - Jobs option
     - Top 10 Indian company
  
## CareerGuide Analysis Agent

**Stability:** Medium--Low\
**Purpose:** Ensure the UI supports trust, clarity, and action --- not
just visualization.

------------------------------------------------------------------------

## 1. Purpose

The UI must:

- Present **analysis outcomes clearly and conservatively**
- Make every conclusion **explainable and traceable**
- Separate **analysis output from human decision-making**

------------------------------------------------------------------------

## 2. User Personas & Intent

### 2.1 Parents

**Primary Intent** - Parents should be able to navigate properly different streams & career for the student.
    - 10th -> Subject select (for e.g , Maths, Biology, Commerce, Economics , Arts) -> 12th -> (Engineering, Doctors, CA , Banking , UPSE, NDA, CDS etc )

**Key Questions** -
    - Suggest the potential of the specific branch based on the current india Growth Story.
    - Which stream can give a good growth based on the student profile.

------------------------------------------------------------------------

## 3. Core User Flows

### 3.1 Flow 1 -- User Inputs to Analyze the Data and Suggest the Career Path

  Student Name
  Standard : 10th , 12th
  Board: State board, CBSE , ICSE , list out other top boards in india
  State: In which studies are going on
  Year: Year of studies
  Percentage 10th
  Percentage 12th.
  Subject Interest: Radio button (single selection) — student picks ONE stream of interest.

### 3.2 Flow 2 -- User Should Be Able to See the Stream Tree Structure

    10th →  (Maths, Biology, Commerce, Economics, Arts, etc.)
    12th →  (Engineering, Medicine, CA, Banking, UPSC, NDA, CDS, etc.)
    Once parents select each of the Careers, all options available to the student upon completing education are shown.

    **UI Requirements** - Clearly display navigation tree for each of the items
    No forced conclusions

    **Outcome** - Generate the report for the student.

    Student Name
    Standard
    Board: State board, CBSE , ICSE etc
    State: in which studies are going on
    Year
    Percentage 10th
    Percentage 12th.
    Summary:
        Branch to select after 10th standard
        Career Options: Suggest the career options
        College: Suggest the top colleges with previous ranking on which they can seek admission.
        Industries: Once the stream is selected, list the industries that have opportunities.
        Pros:
        Cons:
        Growth aspects: Suggest for India as well as abroad
------------------------------------------------------------------------

## Closing Principle

The UI must make the agent:

- Transparent
- Conservative
- Explainable
- Predictable
