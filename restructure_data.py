import pandas as pd

# Load the dataset
print("Loading dataset")
df = pd.read_csv("data/lightcast_job_postings.csv", low_memory=False)
print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# Table 1: Job_Postings
print("Creating Job_Postings table")
job_postings_df = df[[
    'ID', 'TITLE_RAW', 'TITLE_CLEAN', 'POSTED', 'EXPIRED',
    'SALARY_FROM', 'SALARY_TO', 'MIN_YEARS_EXPERIENCE', 'MAX_YEARS_EXPERIENCE',
    'SKILLS', 'SPECIALIZED_SKILLS', 'SOFTWARE_SKILLS', 'EMPLOYMENT_TYPE', 'COMPANY'
]].copy()
job_postings_df.rename(columns={'COMPANY': 'COMPANY_ID'}, inplace=True)
job_postings_df.to_csv("_output/job_postings.csv", index=False)
print(f"Job_Postings: {job_postings_df.shape[0]} rows")

# Table 2: Company
print("Creating Company table")
company_df = df[[
    'COMPANY', 'COMPANY_NAME', 'COMPANY_RAW', 'COMPANY_IS_STAFFING'
]].drop_duplicates().copy()
company_df.rename(columns={'COMPANY': 'COMPANY_ID'}, inplace=True)
company_df.to_csv("_output/company.csv", index=False)
print(f"Company: {company_df.shape[0]} rows")

# Table 3: Job_Location
print("Creating Job_Location table")
job_location_df = df[[
    'ID', 'CITY', 'STATE', 'COUNTY', 'LOCATION'
]].copy()
job_location_df.to_csv("_output/job_location.csv", index=False)
print(f"Job_Location: {job_location_df.shape[0]} rows")

# Table 4: SOC_Details
print("Creating SOC_Details table")
soc_df = df[[
    'ID', 'SOC_2', 'SOC_2_NAME', 'SOC_3', 'SOC_3_NAME',
    'SOC_4', 'SOC_4_NAME', 'SOC_5', 'SOC_5_NAME'
]].copy()
soc_df.to_csv("_output/soc_details.csv", index=False)
print(f"SOC_Details: {soc_df.shape[0]} rows")

# Table 5: LOT_Details
print("Creating LOT_Details table")
lot_df = df[[
    'ID', 'LOT_CAREER_AREA', 'LOT_CAREER_AREA_NAME',
    'LOT_OCCUPATION', 'LOT_OCCUPATION_NAME',
    'LOT_SPECIALIZED_OCCUPATION', 'LOT_SPECIALIZED_OCCUPATION_NAME'
]].copy()
lot_df.to_csv("_output/lot_details.csv", index=False)
print(f"LOT_Details: {lot_df.shape[0]} rows")

# Table 6: NAICS_Details
print("Creating NAICS_Details table")
naics_df = df[[
    'ID', 'NAICS2', 'NAICS2_NAME', 'NAICS3', 'NAICS3_NAME',
    'NAICS4', 'NAICS4_NAME', 'NAICS5', 'NAICS5_NAME',
    'NAICS6', 'NAICS6_NAME'
]].copy()
naics_df.to_csv("_output/naics_details.csv", index=False)
print(f"NAICS_Details: {naics_df.shape[0]} rows")

print("All tables saved to _output folder!")

