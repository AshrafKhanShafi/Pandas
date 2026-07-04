import pandas as pd
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
# excel = pd.ExcelFile("Students_mark_sheet.xlsx")
# print(excel.sheet_names)

excel = pd.read_excel("Students_mark_sheet.xlsx", sheet_name="6AM Sat")
# print(excel.head())
# column3 = excel["Unnamed: 1"]
# marks = excel["Marks"]
# print(excel.isnull().sum()) #Finding the missing values 
delete_null_values = excel.dropna() #row te null value thakle sei puro row remove kore dey
# print(delete_null_values)

replacing_null_values = excel.fillna(0) #Replacing Null values with Zero (0)
# print(replacing_null_values)

#=======sorting values========
sorting_by_columns = excel[["Student's Name", "Marks(3)"]].sort_values(by="Marks(3)", ascending=False)
print(sorting_by_columns)
# print(excel.columns)




# data = {
#     "Name": ["Shafi", "Rahim", "Karim","Rasel","Kamal","Borhan","Fahad","Rafi"],
#     "Age": [20, 21, 22,25,27,40,54,43],
#     "City": ["Rajshahi", "Dhaka", "Khulna","Sylhet","Rangpur","Mymenshing","Pabna","Barishal"]
# }

# df = pd.DataFrame(data)

# print(df)
# #==========adding or removing columns============

# df["Salary"] = df["Age"]*1000
# print("\nAdded Salary Column\n",df)
# print("\nMaximum Salary\n",df.loc[df["Salary"].idxmax()])

# print(excel.columns.to_list())
# print(column3)


# print(excel.head(10).to_string)
# print(excel.shape)













