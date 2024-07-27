import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df=pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count=pd.Series(df['race'].value_counts(),name='race')

    # What is the average age of men?
    average_age_men=df.groupby('sex')['age'].mean()['Male'].round(1)
  
    # What is the percentage of people who have a Bachelor's degree?
    bachelors=df['education'].value_counts()/len(df['education'])*100
    percentage_bachelors=bachelors.iloc[2].round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education=pd.crosstab(df['education'],df['salary'],normalize='index')*100
    lower_education=pd.crosstab(df['education'],df['salary'],normalize='index')*100 

    # percentage with salary >50K
    higher_education_rich_1=df['education'].loc[(df['education']=='Bachelors')|(df['education']=='Masters')|(df['education']=='Doctorate')]
    salary=df['salary'].loc[df['salary']=='>50K']
    higher_education_rich_2=higher_education_rich_1.loc[higher_education_rich_1.index.isin(salary.index)==True].value_counts().sum()/len(higher_education_rich_1)*100
    higher_education_rich=higher_education_rich_2.round(1)
    lower_education_rich_1=df['education'].loc[~(df['education']=='Bachelors')|(df['education']=='Masters')|(df['education']=='Doctorate')]
    lower_education_rich_2=lower_education_rich_1.loc[lower_education_rich_1.index.isin(salary.index)==True].value_counts().sum()/len(df)*101
    lower_education_rich=lower_education_rich_2.round(1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours=df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers=pd.crosstab(df['hours-per-week'],df['salary'],normalize='index')*100
    rich_percentage=num_min_workers.loc[num_min_workers.index.get_level_values('hours-per-week')==df['hours-per-week'].min()].sum().iloc[1]

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country=pd.crosstab(df['native-country'],df['salary'],normalize='index').idxmax().iloc[1]
    highest_earning_country_percentage_1=pd.crosstab(df['native-country'],df['salary'],normalize='index').max().iloc[1]*100
    highest_earning_country_percentage=highest_earning_country_percentage_1.round(1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation=df['occupation'].value_counts().idxmax()
    #pd.crosstab(df['occupation'],df['salary'])#.idxmax().iloc[1]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
