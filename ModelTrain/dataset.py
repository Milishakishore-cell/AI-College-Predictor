import pandas as pd
import numpy as np

# Create a synthetic dataset
np.random.seed(42)
num_samples = 1000

data = {
    "class_10_gpa": np.random.uniform(5.0, 10.0, num_samples),  # Class 10 GPA (0 to 10)
    "class_12_gpa": np.random.uniform(5.0, 10.0, num_samples),  # Class 12 GPA (0 to 10)
    "jee_mains_rank": np.random.randint(1, 100000, num_samples),  # JEE Mains Rank
    "jee_advanced_rank": np.random.randint(1, 50000, num_samples),  # JEE Advanced Rank
    "neet_rank": np.random.randint(1, 200000, num_samples),  # NEET Rank
    "sat_score": np.random.randint(800, 1600, num_samples),  # SAT Score
    "extracurriculars": np.random.randint(0, 10, num_samples),  # Extracurricular activities
    "category": np.random.choice(["General", "OBC", "SC", "ST"], num_samples),  # Category
    "state_of_domicile": np.random.choice(["Maharashtra", "Delhi", "Karnataka", "Tamil Nadu"], num_samples),  # State
    "preferred_branch": np.random.choice(["Computer Science", "Mechanical", "Medicine", "Electrical"], num_samples),  # Preferred branch
    "college_admitted": np.random.choice(["IIT Bombay", "AIIMS Delhi", "Stanford University", "MIT"], num_samples)  # Target variable
}

df = pd.DataFrame(data)

# Save the dataset to a CSV file
df.to_csv("college_admission_dataset.csv", index=False)