#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[56]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
Heroes_of_pd = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
Heroes_of_pd = pd.read_csv("Resources/purchase_data.csv")
Heroes_of_pd.head()


# ## Player Count

# * Display the total number of players
# 

# ## Purchasing Analysis (Total)

# In[57]:


Total_Player_Count_df = Heroes_of_pd.groupby("SN")["SN"].unique()
Total_Players = ([{"Total_Players":Total_Player_Count_df.count()}])
Total_Players 

item_count = len(Heroes_of_pd["Item ID"].unique())
item_count


Average_Price = Heroes_of_pd["Price"].mean()
Average_Price

Average_Age = Heroes_of_pd["Age"].mean()
Average_Age

Total_Purchases = Heroes_of_pd["Purchase ID"].count()
Total_Purchases

Total_Revenue = Heroes_of_pd["Price"].sum()
Total_Revenue


# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[58]:


Purchase_Analysis_df = pd.DataFrame({"Number of Unique Items": [item_count],
                                          "Total Player Count": [Total_Players],
                                          "Average Price": [round(Average_Price, 2)],
                                          "Average Age": [Average_Age],
                                          "Total Purchases": [Total_Purchases],
                                          "Total Revenue": [Total_Revenue]})

Purchase_Analysis_df ["Number of Unique Items"] = Purchase_Analysis_df["Number of Unique Items"]
Purchase_Analysis_df ["Average Price"] = Purchase_Analysis_df["Average Price"].map("${:,.2f}".format)
Purchase_Analysis_df ["Total Purchases"] = Purchase_Analysis_df["Total Purchases"].map("{:,}".format)
Purchase_Analysis_df ["Total Revenue"] = Purchase_Analysis_df ["Total Revenue"].map("${:,.2f}".format)
Purchase_Analysis_df = Purchase_Analysis_df.loc[:,["Number of Unique Items", "Average Price", "Total Purchases", "Total Revenue"]]
Purchase_Analysis_df


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[223]:


male_df = Heroes_of_pd.loc[Heroes_of_pd["Gender"] == "Male",:]
male_count = len(male_df["SN"].unique())
percent_male = round((len(male_df)/len(Heroes_of_pd)) * 100, 2)

female_df = Heroes_of_pd.loc[Heroes_of_pd["Gender"] == "Female",:]
female_count = len(female_df["SN"].unique())
percent_female = round((len(female_df)/len(Heroes_of_pd)) * 100, 2)

others_data_df = Heroes_of_pd.loc[Heroes_of_pd["Gender"] == "Other / Non-Disclosed",:]
others_count = len(others_data_df["SN"].unique())
percent_others = round((len(others_data_df)/len(Heroes_of_pd)) * 100, 2)

gender_demo_df = {"Percentage Of Players" : [percent_male, percent_female, percent_others],
                    "Gender" : ["Male","Female","Other/Non-Disclosed"],
                    "Total Count" : [male_count, female_count, others_count]}

gender_demo_df = pd.DataFrame(gender_demo_df)

gender_demo_df.style.format({"Percentage of Players":"{:,.2f}%"})


# 
# ## Purchasing Analysis (Gender)

# In[208]:


Male_Purchase_Count = len(male_df)
Female_Purchase_Count = len(female_df)
Other_Purchase_Count = len(others_data_df)

Male_Average_Price = round((male_df['Price'].sum())/len(male_df['Price']),2)
Female_Average_Price = round((female_df['Price'].sum())/len(female_df['Price']),2)
Other_Average_Price = round((others_data_df['Price'].sum())/len(others_data_df['Price']),2)

Male_Total_Price = round((male_df['Price'].sum()),2)
Female_Total_Price = round((female_df['Price'].sum()),2)
Other_Total_Price = round((others_data_df['Price'].sum()),2)


Average_Price_Per_Person_Male = round((Male_Total_Price/male_count),2)
Average_Price_Per_Person_Female = round((Female_Total_Price/female_count),2)
Average_Price_Per_Person_Other = round((Other_Total_Price/others_count),2)


Final_Purchase_Analysis = {'Purchase Count': [Male_Purchase_Count, Female_Purchase_Count, Other_Purchase_Count],
                           'Gender': ['Male', 'Female', 'Other'],
                           'Average Price': [Male_Average_Price, Female_Average_Price, Other_Average_Price],
                           'Average Price per Person': [Average_Price_Per_Person_Male, Average_Price_Per_Person_Female, Average_Price_Per_Person_Other],
                           'Total Price': [Male_Total_Price, Female_Total_Price, Other_Total_Price],
                            }

Final_Purchase_Analysis_df = pd.DataFrame(Final_Purchase_Analysis)
Final_Purchase_Analysis_df = Final_Purchase_Analysis_df.set_index('Gender')


Final_Purchase_Analysis_df['Purchase Count'] = Final_Purchase_Analysis_df['Purchase Count']
Final_Purchase_Analysis_df['Average Price'] = Final_Purchase_Analysis_df['Average Price'].map('${:,.2f}'.format)
Final_Purchase_Analysis_df['Average Price per Person'] = Final_Purchase_Analysis_df['Average Price per Person'].map('${:,.2f}'.format)
Final_Purchase_Analysis_df['Total Price'] = Final_Purchase_Analysis_df['Total Price'].map('${:,.2f}'.format)

Final_Purchase_Analysis_df


# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# ## Age Demographics

# In[221]:



age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

total_players = len(Heroes_of_pd["SN"].unique())

Heroes_of_pd["Age Group"] = pd.cut(Heroes_of_pd["Age"],age_bins, labels=group_names)
Heroes_of_pd

age_grouped = Heroes_of_pd.groupby("Age Group")

total_count_age = age_grouped["SN"].nunique()

percentage_by_age = (total_count_age/total_players) * 100

age_demographics = pd.DataFrame({"Percentage of Players": percentage_by_age, "Total Count": total_count_age})

age_demographics.index.name = None

 
age_demographics.style.format({"Percentage of Players":"{:,.2f}%"})


# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[273]:


purchase_count_age = age_grouped["Purchase ID"].count()

avg_purchase_price_age = age_grouped["Price"].mean()

total_purchase_value = age_grouped["Price"].sum()
 
avg_purchase_per_person_age = total_purchase_value/total_count_age

age_demographics = pd.DataFrame({"Purchase Count": purchase_count_age,
                                 "Average Purchase Price": avg_purchase_price_age,
                                 "Total Purchase Value":total_purchase_value,
                                 "Average Purchase Total per Person": avg_purchase_per_person_age})
age_demographics.index.name = None

age_demographics.style.format({"Average Purchase Price":"${:,.2f}",
                               "Total Purchase Value":"${:,.2f}",
                               "Average Purchase Total per Person":"${:,.2f}"})


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[276]:


spender_stats = Heroes_of_pd.groupby("SN")

purchase_count_spender = spender_stats["Purchase ID"].count()
 
avg_purchase_price_spender = spender_stats["Price"].mean()

purchase_total_spender = spender_stats["Price"].sum()

top_spenders = pd.DataFrame({"Purchase Count": purchase_count_spender,
                             "Average Purchase Price": avg_purchase_price_spender,
                             "Total Purchase Value":purchase_total_spender})

format_spenders = top_spenders.sort_values(["Total Purchase Value"], ascending=False).head()

# Format with currency style
format_spenders.style.format({"Average Purchase Total":"${:,.2f}",
                              "Average Purchase Price":"${:,.2f}", 
                              "Total Purchase Value":"${:,.2f}"
                             })


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[278]:


items = Heroes_of_pd[["Item ID", "Item Name", "Price"]]

item_stats = items.groupby(["Item ID","Item Name"])

purchase_count_item = item_stats["Price"].count()

purchase_value = (item_stats["Price"].sum()) 

item_price = purchase_value/purchase_count_item

most_popular_items = pd.DataFrame({"Purchase Count": purchase_count_item, 
                                   "Item Price": item_price,
                                   "Total Purchase Value":purchase_value})

popular_formatted = most_popular_items.sort_values(["Purchase Count"], ascending=False).head()

popular_formatted.style.format({"Item Price":"${:,.2f}",
                                "Total Purchase Value":"${:,.2f}"})


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[279]:


popular_formatted = most_popular_items.sort_values(["Total Purchase Value"],
                                                   ascending=False).head()
popular_formatted.style.format({"Item Price":"${:,.2f}",
                                "Total Purchase Value":"${:,.2f}"})


# In[ ]:




