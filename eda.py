#Making imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Extracting the dataset
df = pd.read_csv("studentsessions.csv")

#Basic Information
df.info()
df.describe()

##Comparision of Difficulty Distributions Between the First and the Last Difficulty
#Create a 1x2 subplot
fig, axes = plt.subplots(1,2, figsize=(16, 6))

#Set Plot 1 as the first difficulty
sns.countplot(x='perceived_difficulty', data=df, ax=axes[0])
axes[0].set_title('Frequency Plot of Initial Difficulty')
axes[0].set_xlabel('Difficulty')
axes[0].set_ylabel('Count')

#Set Plot 2 as the final difficulty
sns.countplot(x='period_6_perceived_difficulty', data=df, ax=axes[1])
axes[1].set_title('Frequency Plot of Final Difficulty')
axes[1].set_xlabel('Difficulty')
axes[1].set_ylabel('Count')

#Prevent overlapping
plt.tight_layout()

#Show the plots
plt.show()

##Difficulty Over Time of all Assignments in a Class
#Subsets the dataset
df_class1 = df[df['class_id'] == 1]
df_class1 = df_class1[['assignment_id','perceived_difficulty','period_1_perceived_difficulty','period_2_perceived_difficulty', 'period_3_perceived_difficulty', 'period_4_perceived_difficulty','period_5_perceived_difficulty','period_6_perceived_difficulty']]

#Change the intial perceived difficulty to period 0
df_class1['period_0_perceived_difficulty'] = df_class1['perceived_difficulty']

# Melt the DataFrame
df_class1_melted = df_class1.melt(id_vars='assignment_id', 
                                  value_vars=['period_0_perceived_difficulty', 
                                              'period_1_perceived_difficulty', 
                                              'period_2_perceived_difficulty',
                                              'period_3_perceived_difficulty',
                                              'period_4_perceived_difficulty',
                                              'period_5_perceived_difficulty',
                                              'period_6_perceived_difficulty'], 
                                  var_name='Period', 
                                  value_name='Perceived_Difficulty')

# Extract the period number from the column names, for plotting
df_class1_melted['Period'] = df_class1_melted['Period'].str.extract(r'(\d+)').astype(int)

# Set up the plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_class1_melted, x='Period', y='Perceived_Difficulty', hue='assignment_id', alpha=0.7, marker = 'o') #Alpha makes the lines more transparent
plt.title('Perceived Difficulty Across Periods for Each Assignment for Class 1')
plt.xlabel('Period')
plt.ylabel('Perceived Difficulty')
plt.legend(title='Assignment ID', loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0.)

# Display the plot
plt.tight_layout()  # This makes sure the plot layout adjusts to fit everything, including the legend
plt.show()

#An example of one of line
assignment_id = df_class1_melted['assignment_id'].iloc[7]
df_class1_first_id = df_class1_melted[df_class1_melted['assignment_id'] == assignment_id]

#Create the plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_class1_first_id, x='Period', y='Perceived_Difficulty', marker='o', alpha=0.7, color = "grey")
plt.title('Perceived Difficulty Across Periods for Assignment H')
plt.xlabel('Period')
plt.ylabel('Perceived Difficulty')

# Display the plot
plt.tight_layout()  # Adjust the layout
plt.show()

## Understanding the Connection between Efficiency Score, Difficulty, and Perceived Time
#Removing a large outlier in the data
df_filtered = df[df['perceived_length'] <= 19]

#Group by class and calculate the averages
grouped_df = df_filtered.groupby('class_id')[['perceived_length','period_6_perceived_difficulty', 'efficiency_score']].mean()

#Create bar plot
grouped_df.plot(kind='bar' , figsize=(12,6))
plt.title('Average Efficiency Score and Hours by ID')
plt.xlabel('ID')
plt.ylabel('Average Value')
plt.xticks(rotation=45)
plt.tight_layout()

# Display the plot
plt.show()
