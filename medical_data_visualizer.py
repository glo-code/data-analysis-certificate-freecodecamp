import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df=pd.read_csv('medical_examination.csv')


# Add 'overweight' column

#np.sqrt(df['height'])

df['height']=df['height'].apply(lambda c:c/100)
print(df['height'])
radice=df['height']**2
df['overweight']=df['weight']/radice
df.loc[df['overweight'] <= 25, 'overweight'] = 0
df.loc[df['overweight'] > 25, 'overweight'] = 1
df['overweight']=df['overweight'].astype(int)
print(df['overweight'])


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

#df.loc[df['gluc']>1,'gluc']=1
#df.loc[df['gluc']==1,'gluc']=0
#df.loc[df['cholesterol']>1,'cholesterol']=1
#df.loc[df['cholesterol']==1,'cholesterol']=0
df[['gluc','cholesterol']]=df[['gluc','cholesterol']].map(lambda x:1 if x>1 else 0)
#df[['gluc','cholesterol']]=df[['gluc','cholesterol']].map(lambda x:0 if x==1 else (1 if x>1 else x))
print(df['cholesterol'],df['gluc'])

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat=pd.melt(df,id_vars=['cardio'],value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
  
    df_cat_2=pd.DataFrame(df_cat.value_counts().reset_index())
    df_cat_2.rename(columns={"count": "total"}, inplace=True)
    #df_cat_2.drop(index=[24,25],inplace=True)
    df_cat_2.sort_values(by='variable', inplace=True)
    df_cat_2.sort_values(by='cardio', inplace=True)
    df_cat_2.sort_values('variable',ascending=True,inplace=True)
    print(df_cat_2.reset_index(drop=True))
    
  

    # Draw the catplot with 'sns.catplot()'
    #plt.figure(figsize=(10,5))
     
    fig,ax=plt.subplots()
    ax=sns.catplot(data=df_cat_2,kind='bar',x='variable',y='total',hue='value',col='cardio')
    #plt.show()
    #plt.set_legend(title='value')


    # Get the figure for the output
    fig=ax.fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig



# Draw Heat Map
def draw_heat_map():
    # Clean the data

    try:
      df_heat=df.copy()
  
      df_heat=df_heat[df['ap_lo']<=df['ap_hi']]
      df_heat=df_heat.dropna()
      df_heat['ap_lo']=df_heat['ap_lo'].astype(int)
      print(df_heat['ap_lo'])
    #funziona

      quantile_1=df['height'].quantile(0.025)
      quantile_2=df['height'].quantile(0.975)
      print(quantile_1,quantile_2)
      df_heat=df_heat[df['height']>=quantile_1]
    #funziona

      df_heat=df_heat[df['height']<=quantile_2]
      df_heat=df_heat.dropna()
      df_heat['height']=df_heat['height'].apply(lambda c:c*100)
      df_heat['height']=df_heat['height'].astype(int)
      df_heat['height']=df_heat['height'].apply(lambda h:h/100)
    #funziona
    #print(df_heat[df['height']<quantile_1])
    #print(df_heat[df['height']>quantile_2])
    
      print(df_heat['height'])
    
      quantile_weight=df['weight'].quantile(0.025)
      quantile_weight_1=df['weight'].quantile(0.975)
                           
      df_heat=df_heat[df['weight']>=quantile_weight]
      df_heat=df_heat[df['weight']<=quantile_weight_1]
      print(df_heat['height'].describe())
      print(df_heat['weight'].describe())
      print(quantile_weight,quantile_weight_1)
    #print(df_heat[df_heat['weight']<quantile_weight])
    #print(df_heat[df_heat['weight']>quantile_weight_1])
      df_heat=df_heat.dropna()
      print(df_heat['weight'])

    except ValueError:
        pass
    
    #df_heat['weight']=df_heat['weight'][(df_heat['weight']>df_heat['weight'].quantile(0.025))|(df_heat['weight']<df_heat['weight'].quantile(q=0.975))]
   
    df_heat.to_csv('df.csv')

    # Calculate the correlation matrix
    corr =df_heat.corr()
    print(corr)

    # Generate a mask for the upper triangle
    mask=np.triu(np.ones_like(corr))




    # Set up the matplotlib figure

    fig,ax=plt.subplots()
    

    # Draw the heatmap with 'sns.heatmap()'

    sns.heatmap(data=corr,annot=True,mask=mask,fmt='.1f',cbar=False,ax=ax)
    #plt.show()
    #plt.legend()

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

