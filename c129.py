import pandas as pd


dwarf_csv = pd.read_csv('dwarf_stars.csv')

scraped_csv = pd.read_csv('scarped_data.csv')


columns_to_clean = ['Distance','Mass','Radius']
dwarf_csv[columns_to_clean] = dwarf_csv[columns_to_clean].fillna('_')
dwarf_csv.head()

column_to_multiply = 'Radius'


multiplier = 0.102763 


dwarf_csv[column_to_multiply] = dwarf_csv[column_to_multiply] * multiplier
scraped_csv[column_to_multiply] = scraped_csv_csv[column_to_multiply] * multiplier


column_to_multiply2 ='Mass'

multiplier2 = 0.000954588

dwarf_csv[column_to_multiply2] = dwarf_csv[column_to_multiply2] * multiplier2
scraped_csv[column_to_multiply2] = scraped_csv_csv[column_to_multiply2] * multiplier2


merge_star_csv=pd.merge(dwarf_csv, scraped_csv, on = "id")
merge_star_csv.shape

merge_star_csv.to_csv('total_stars.csv')
