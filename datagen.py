import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Sample towns, inspired by real place names
towns = ["Alderwood", "Brookfield", "Cedarville", "Dunford", "Elmdale", 
         "Fairview", "Glenwood", "Hillside", "Inglewood", "Jasper", 
         "Kingsland", "Lansdowne", "Maplewood", "Northdale", "Oakridge",
         "Pinecrest", "Quarryville", "Rosewood", "Springfield", "Tamarack"]

# Generate 1000 rows
num_rows = 1000
generated_towns = np.random.choice(towns, num_rows)

# Area between 800 and 3500 sq ft (typical house sizes)
generated_area = np.random.randint(800, 3501, num_rows)

# Price roughly $150-$250 per sq ft, add some noise +/- 20%
base_price_per_sqft = np.random.uniform(150, 250, num_rows)
noise_factor = np.random.uniform(0.8, 1.2, num_rows)
generated_price = (generated_area * base_price_per_sqft * noise_factor).astype(int)

# Create DataFrame
large_df = pd.DataFrame({
    "Town": generated_towns,
    "Area (sq ft)": generated_area,
    "Price ($)": generated_price
})

# Save to CSV
large_file_path = "ml_dummy_data_large.csv"
large_df.to_csv(large_file_path, index=False)

large_file_path
