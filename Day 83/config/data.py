# ==============================================================================
# 📝 PORTFOLIO CONFIGURATION
# ==============================================================================
# This file contains all data for your portfolio.
# Change the values to your own!
# ==============================================================================


# ==============================================================================
# 👤 PERSONAL INFORMATION
# ==============================================================================

PERSONAL_INFO = {
    # TODO: Replace with your name
    "name": "Nikita Lutik",

    # TODO: Replace with your role
    "role": "Data Scientist",

    # TODO: Short description for hero section (1-2 sentences)
    "tagline": "Transforming raw data into business solutions",

    # TODO: Replace with your email
    "email": "lutik.nikita228@gmail.com",

    # TODO: Replace with your Telegram (with @)
    "telegram": "@regraced",

    # TODO: Replace with your GitHub
    "github": "https://github.com/luvurgrace",

    # TODO: Replace with your LinkedIn
    "linkedin": "https://linkedin.com/in/nlutik",

    # TODO: City/Country
    "location": "Minsk, Belarus",

    # TODO: Write about yourself (for About section on main page)
    "bio": """
        Aspiring Data Scientist with experience working on machine learning 
        and data analysis projects. Completed "100 Days of Code" course 
        and constantly improving my skills. Looking for opportunities 
        to apply my knowledge in real-world projects.
    """,

    # TODO: Status (displayed on the site)
    # Options: "Open to opportunities", "Looking for work", "Busy"
    "status": "Open to opportunities",
}

# ==============================================================================
# 📊 STATISTICS (displayed on main page)
# ==============================================================================

STATS = {
    # TODO: Replace with your numbers
    "projects": "5+",  # Number of projects
    "models": "10+",  # Trained models
    "accuracy": "89%",  # Best model accuracy
    "experience": "1+",  # Years of experience (or months)
}

# ==============================================================================
# 🛠️ SKILLS (displayed on main page)
# ==============================================================================

# TODO: Keep only the technologies you know
SKILLS = {
    "languages": [
        {"name": "Python", "icon": "fab fa-python"},
        {"name": "SQL", "icon": "fas fa-database"},
        # {"name": "R", "icon": "fab fa-r-project"},  # Uncomment if you know R
    ],

    "data_science": [
        {"name": "Pandas", "icon": ""},
        {"name": "NumPy", "icon": ""},
        {"name": "Scikit-learn", "icon": ""},
        {"name": "Matplotlib", "icon": ""},
        {"name": "Seaborn", "icon": ""},
        # {"name": "TensorFlow", "icon": ""},  # Uncomment if you know
        # {"name": "PyTorch", "icon": ""},
        # {"name": "XGBoost", "icon": ""},
    ],

    "tools": [
        {"name": "Jupyter", "icon": ""},
        {"name": "Git", "icon": "fab fa-git-alt"},
        {"name": "VS Code", "icon": ""},
        # {"name": "Docker", "icon": "fab fa-docker"},
        # {"name": "Tableau", "icon": ""},
    ],
}

# ==============================================================================
# 💼 PROJECTS
# ==============================================================================

# TODO: Replace with your projects
PROJECTS = [
    {
        # Unique ID (used in URL)
        "id": "customer-churn",

        # Project title
        "title": "Customer Churn Prediction",

        # Short description (for card)
        "short_description": "Predicting customer churn for a telecom company using machine learning",

        # Categories (for filtering)
        # Options: "ML", "EDA", "NLP", "CV", "Time Series", "Deep Learning"
        "categories": ["ML", "EDA"],

        # Project image (place in static/images/projects/)
        # TODO: Add project screenshot
        "image": "project1.jpg",

        # Icon (if no image)
        "icon": "fas fa-users",

        # Key metrics (displayed on card)
        "metrics": {
            "F1 Score": "0.85",
            "AUC-ROC": "0.91",
            "Data": "100K",
        },

        # Technologies
        "technologies": ["Python", "Pandas", "Scikit-learn", "XGBoost", "Matplotlib"],

        # Links
        # TODO: Replace with your links
        "github": "https://github.com/yourusername/customer-churn",
        "notebook": "https://github.com/yourusername/customer-churn/blob/main/analysis.ipynb",
        "demo": None,  # Demo link (if available)

        # Featured project (shown on main page)
        "featured": True,

        # ===== DETAILED INFORMATION (for project page) =====

        # Full project description
        "full_description": """
            This project is dedicated to analyzing customer churn for a telecommunications company. 
            The main goal is to build a machine learning model that can predict whether 
            a customer will leave based on their characteristics and behavior.
        """,

        # Business problem
        "business_problem": """
            The telecom company was losing up to 20% of customers monthly. Customer churn 
            led to significant financial losses, as acquiring a new customer costs 
            5-7 times more than retaining an existing one.

            It was necessary to create a tool for early identification of customers 
            prone to leaving, in order to take preventive measures.
        """,

        # Data description
        "data_description": """
            **Source:** Kaggle Telco Customer Churn Dataset

            **Size:** 7,043 records, 21 features

            **Features include:**
            - Demographic data (gender, age, marital status)
            - Account information (tenure, contract type)
            - Connected services (internet, TV, security)
            - Financial data (monthly charges, total amount)

            **Target variable:** Churn (left/stayed)

            **Peculiarities:** Imbalanced classes (26% churned)
        """,

        # Methodology
        "methodology": [
            {
                "step": "1. Exploratory Data Analysis (EDA)",
                "description": "Studying distributions, correlations, identifying patterns in data"
            },
            {
                "step": "2. Data Preprocessing",
                "description": "Handling missing values, encoding categorical variables, scaling"
            },
            {
                "step": "3. Feature Engineering",
                "description": "Creating new features: tenure categories, payment ratios"
            },
            {
                "step": "4. Model Training",
                "description": "Testing Logistic Regression, Random Forest, XGBoost, hyperparameter tuning"
            },
            {
                "step": "5. Evaluation and Interpretation",
                "description": "Metrics analysis, SHAP values for interpretation, conclusions"
            },
        ],

        # Model results
        "model_results": [
            {"model": "Logistic Regression", "accuracy": "0.79", "precision": "0.72", "recall": "0.69", "f1": "0.70"},
            {"model": "Random Forest", "accuracy": "0.84", "precision": "0.79", "recall": "0.76", "f1": "0.77"},
            {"model": "XGBoost", "accuracy": "0.87", "precision": "0.84", "recall": "0.82", "f1": "0.85", "best": True},
        ],

        # Key insights
        "insights": [
            "Customers with month-to-month contracts churn 3 times more often",
            "First 12 months are a critical retention period",
            "Lack of online security correlates with churn",
            "High monthly charges are a risk factor",
        ],

        # Business recommendations
        "recommendations": """
            1. **Focus on the first year:** Develop a loyalty program for new customers
            2. **Promote long-term contracts:** Offer discounts for annual contracts
            3. **Upsell security:** Customers with additional services are less likely to leave
            4. **Monitoring:** Implement the model into CRM for automatic scoring
        """,

        # Visualizations (file names in static/images/projects/)
        # TODO: Add graph screenshots
        "visualizations": [
            {"image": "project1_viz1.jpg", "caption": "Churn distribution by contract type"},
            {"image": "project1_viz2.jpg", "caption": "Feature Importance"},
            {"image": "project1_viz3.jpg", "caption": "ROC Curve"},
        ],
    },

    # -------------------------------------------------------------------------
    # PROJECT 2 - TODO: Replace with your project
    # -------------------------------------------------------------------------
    {
        "id": "eda-sales",

        "title": "Sales Data Analysis",

        "short_description": "Exploratory data analysis of sales data: identifying trends, seasonality, and insights",

        "categories": ["EDA"],

        "image": "project2.jpg",
        "icon": "fas fa-chart-line",

        "metrics": {
            "Records": "50K",
            "Features": "15",
            "Insights": "10+",
        },

        "technologies": ["Python", "Pandas", "Matplotlib", "Seaborn", "Plotly"],

        "github": "https://github.com/yourusername/sales-analysis",
        "notebook": "https://github.com/yourusername/sales-analysis/blob/main/EDA.ipynb",
        "demo": None,

        "featured": True,

        "full_description": """
            Comprehensive exploratory data analysis of retail chain sales data. 
            The project demonstrates skills in data manipulation, visualization, 
            and extracting business insights.
        """,

        "business_problem": """
            A retail chain wanted to understand sales patterns to optimize 
            procurement and marketing campaigns. It was necessary to answer questions:

            - Which products sell best?
            - Is there seasonality in sales?
            - What factors affect revenue?
        """,

        "data_description": """
            **Source:** Kaggle Retail Sales Dataset

            **Period:** 2020-2023

            **Size:** 50,000 transactions

            **Features:** Date, product category, quantity, price, store, region
        """,

        "methodology": [
            {"step": "1. Data Cleaning", "description": "Handling missing values, duplicates, outliers"},
            {"step": "2. Distribution Analysis", "description": "Studying numerical and categorical variables"},
            {"step": "3. Time Analysis", "description": "Trends, seasonality, anomalies"},
            {"step": "4. Segmentation", "description": "Analysis by categories, regions, customers"},
            {"step": "5. Visualization", "description": "Creating informative dashboards"},
        ],

        "model_results": None,  # No models in EDA project

        "insights": [
            "Sales peak occurs in December (+40% to average)",
            "Electronics category generates 35% of revenue",
            "Weekends show 25% more sales",
            "Central region leads in average check",
        ],

        "recommendations": """
            1. Increase inventory before the holiday season
            2. Expand electronics assortment
            3. Launch weekend promotions in underperforming regions
        """,

        "visualizations": [
            {"image": "project2_viz1.jpg", "caption": "Monthly sales dynamics"},
            {"image": "project2_viz2.jpg", "caption": "Top categories by revenue"},
        ],
    },

    # -------------------------------------------------------------------------
    # TODO: Add more projects following the same pattern
    # -------------------------------------------------------------------------
]

# ==============================================================================
# 📚 PROJECT CATEGORIES (for filtering)
# ==============================================================================

PROJECT_CATEGORIES = [
    {"id": "all", "name": "All Projects", "icon": "fas fa-th"},
    {"id": "ML", "name": "Machine Learning", "icon": "fas fa-robot"},
    {"id": "EDA", "name": "EDA", "icon": "fas fa-search"},
    {"id": "NLP", "name": "NLP", "icon": "fas fa-comment-dots"},
    {"id": "CV", "name": "Computer Vision", "icon": "fas fa-eye"},
    {"id": "Time Series", "name": "Time Series", "icon": "fas fa-chart-line"},
]