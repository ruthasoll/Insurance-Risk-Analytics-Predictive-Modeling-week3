# Insurance-Risk-Analytics-Predictive-Modeling-week3


# AlphaCare Insurance Solutions (ACIS)  
## Car Insurance Risk & Predictive Analytics – South Africa  

Marketing Analytics Engineer: Ruth S.  
Period: February 2014 – August 2015 dataset (1,000,098 policies)  
Current Date: December 07, 2025  

 Project Goal
Identify low-risk customer segments to offer targeted premium discounts — growing volume profitably and gaining market share in the South African motor insurance market.

 Current Status (Tasks 1 & 2 – COMPLETED)

| Task | Status | Branch    | Key Deliverables |
|------|--------|-----------|------------------|
| Task 1 | Completed & merged | `task-1` → `main` | Full EDA + 3 flagship visualizations + GitHub Actions CI/CD |
| Task 2 | Completed & merged | `task-2` → `main` | DVC pipeline with local remote storage + reproducible data versioning |

 Key Achievements So Far
- Overall portfolio loss ratio = **19.8%** (very healthy)
- Discovered multiple low-risk segments ideal for discounts:
  - Female drivers → **18.9%** loss ratio
  - Gauteng & Western Cape → **<19%**
  - Toyota / VW / Ford owners → **14–17%**
  - Tracking device fitted → **13.2%**
  - Top postal codes (e.g. Sandton 2196) → **<12%**
- Built a fully reproducible pipeline using **Git + DVC** (large raw data no longer in Git-bloated)

 Project Structure

 ├── data/
│   └── MachineLearningRating_v3.txt.dvc    # tracked by DVC (~350 MB)
├── notebooks/
│   └── 01_eda_and_visualizations.ipynb
├── reports/
│   └── Task_1_and_2_Report.md (or .docx)
├── .dvc/                                   # DVC metadata
├── .github/workflows/                      # CI/CD
├── new_venv/                               # virtual environment
└── README.md                               # ← you are here


 Quick Start (for reviewers, teammates or future you)

bash
 Clone the repo
  git clone https://github.com/ruths/Insurance-Risk-Analytics-Predictive-Modeling-week3.git
  cd Insurance-Risk-Analytics-Predictive-Modeling-week3

  Checkout latest
  git checkout main

 Activate virtual environment (Windows)
  new_venv\Scripts\activate
  (or .venv\Scripts\activate if named differently)

  Install dependencies
  pip install -r requirements.txt
   (create one with: pip freeze > requirements.txt)

   Pull exact versioned data
  dvc pull

   ← downloads the original 350 MB dataset instantly

   Open the EDA notebook
  jupyter lab notebooks/01_eda_and_visualizations.ipynb
