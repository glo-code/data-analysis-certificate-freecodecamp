import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import calendar
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',parse_dates=True,index_col='date')

print(df.head())

# Clean data
#df1=df.copy()
quantile1=df['value'].quantile(0.025)
quantile2=df['value'].quantile(0.975)


#df1['value']=df['value']/df['value'].sum()*100
df=df[(df['value']>=quantile1)&(df['value']<=quantile2)]


print(np.where(df['value']>=quantile1)[0])
print(np.where(df['value']<=quantile2)[0])

print(df.describe())




def draw_line_plot():
    # Draw line plot
    fig,ax=plt.subplots()
    plt.plot(df.index,df['value'])
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    #plt.show()
   


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

#print(draw_line_plot())

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['data']=pd.to_datetime(df.index)
    df_bar['month']=df_bar['data'].dt.month_name()
    df_bar['year']=df_bar['data'].dt.year
    df_unito=df_bar.groupby(['year','month'])['value'].mean().unstack()
    months=['January',
           'February',
           'March',
           'April', 
           'May',
           'June',
           'July', 
           'August', 
            'September', 
            'October',
           'November', 
           'December']
    print(df_unito)
    
    

    # Draw bar plot

    fig,ax=plt.subplots()
    df_unito.plot(kind='bar',ax=ax,figsize=(14,5))
    #sns.catplot(kind='bar',data=df_unito,x='year',y='value',hue='month',palette='husl')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(months,title='Months')
    #plt.show()



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

#print(draw_bar_plot())

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    print(df_box['value'])
    print(df_box['year'])

    # Draw box plots (using Seaborn)

    df_box['value']=df_box['value'].astype(int)
    #df_box['value']=df_box['value'].round(3)
    print(df_box['value'])
    lista_months=['Jan',
           'Feb',
           'Mar',
           'Apr', 
           'May',
           'Jun',
           'Jul', 
           'Aug', 
            'Sep', 
            'Oct',
           'Nov', 
           'Dec']

    
    fig,ax=plt.subplots(1,2,figsize=(15,20))    
    sns.boxplot(data=df_box,x='month',y='value',ax=ax[1],order=lista_months)
    ax[1].set_ylabel('Page Views')
    ax[1].set_xlabel('Month')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_ylim(0,200000,auto=False)
    ax[1].set_yticks(range(0,200001,20000))
    sns.boxplot(data=df_box,x='year',y='value',ax=ax[0])
    ax[0].set_ylabel('Page Views')
    ax[0].set_xlabel('Year')
    ax[0].set_title('Year-wise Box Plot (Trend)')
    #ax[0]=plt.gca()
    #plt.show()
    #ax=plt.axis()
    #plt.axis((ax[1],ax[0],20000,200000))

    
    ax[0].set_ylim(0,200001,auto=False)
    ax[0].set_yticks(range(0,200001,20000))


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

#print(draw_box_plot())
