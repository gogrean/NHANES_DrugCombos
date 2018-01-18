import pandas as pd

def drug_translator(names):
    data_root = "/Users/gogrean/Documents/Insight_Fellowship/Research/Mental_Health/NHANES_Survey/data/"
    df_meds = pd.read_csv(data_root + "brand_to_generic_drug_names.csv", header=0)

    translated_names = []
    for name in names:
        if name.lower() in df_meds['Generic Name'].str.lower().values:
            translated_names.append(name.title())
        elif name.lower() in df_meds['Brand Name'].str.lower().values:
            translated_names.append(df_meds[df_meds['Brand Name'].str.lower() == name.lower()]['Generic Name'].values[0].title())    
        else:
            translated_names.append('N/A')
    return translated_names
