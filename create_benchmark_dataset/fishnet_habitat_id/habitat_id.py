import pandas as pd

# Load your author CSV
author_df = pd.read_csv('author.csv')

# Combine the climate zone + water type columns into a text habitat_name
author_df['habitat_name'] = (
    author_df[['Tropical', 'Temperate', 'Subtropical', 'Boreal', 'Polar',
               'freshwater', 'saltwater', 'brackish']]
    .astype(str)
    .agg('_'.join, axis=1)
)

# Now create numeric habitat_id from habitat_name
author_df['habitat_id'] = author_df['habitat_name'].factorize()[0]

# Save for later use
author_df.to_csv('train_full_meta_with_habitat.csv', index=False)
print("Saved with habitat_name and habitat_id columns")
