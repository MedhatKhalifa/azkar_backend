import pandas as pd
from googletrans import Translator

# Load your dataset
file_path = 'azkar_backend/azkar/azkar_all.xlsx'
azkar_data = pd.ExcelFile(file_path)
morning_azkar = azkar_data.parse('morning')

# Fields to translate
fields_to_translate = ['sub_category','before','content', 'count', 'reward', 'after']

# Extract relevant fields and ensure they are strings
data_for_translation = morning_azkar[fields_to_translate].fillna("").astype(str)

# Initialize the translator
translator = Translator()

# Function to translate each row
def translate_row(row):
    translated_row = {}
    for field in fields_to_translate:
        try:
            # Ensure translation input is a valid string
            text = row[field].strip()
            translated_row[field] = translator.translate(text, src='ar', dest='en').text if text else ""
        except Exception as e:
            print(f"Error translating field {field} with value {row[field]}: {e}")
            translated_row[field] = row[field]  # Fallback to original value
    return translated_row

# Apply translation
translated_data = data_for_translation.apply(translate_row, axis=1)

# Convert to DataFrame
translated_df = pd.DataFrame(list(translated_data))

# Save translated data to a new file
translated_df.to_excel('translated_azkar.xlsx', index=False)
print("Translation complete. Saved to 'translated_azkar.xlsx'.")