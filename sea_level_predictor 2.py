import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.common import index_labels_to_array
from scipy.stats import linregress
from scipy import stats
import numpy as np

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv',float_precision='legacy',encoding='utf-8')
    print(df.head(10))
    print(df['CSIRO Adjusted Sea Level'])

    # Create scatter plot
    plt.scatter(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])
    #plt.show()

    # Create first line of best fit
    linear=stats.linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    print(linear)
    lista=[1850.0,1875.0,1900.0,1925.0,1950.0,1975.0,2000.0,2025.0,2050.0,2075.0]
    #ind=np.where(df['Year'].isin(lista))[0]
    #livel2=df['CSIRO Adjusted Sea Level'].iloc[ind]
    #year1=df['Year'][df['Year'].isin(lista)]
    #plt.plot(df['Year'],df['CSIRO Adjusted Sea Level'])
    plt.plot(np.arange(1880,2051),
        linear.intercept+linear.slope*np.arange(1880,2051))
    #plt.show()


    # Create second line of best fit
    year=df['Year'][df['Year']>=2000]
    index=year.index
    livel=df['CSIRO Adjusted Sea Level'].iloc[index]
    print(year)
    linear1=stats.linregress(year,livel)
    print(linear1)
    #plt.plot(year,livel)
    plt.plot(np.arange(2000,2051),linear1.intercept+linear1.slope*np.arange(2000,2051),'r')


    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.xticks(lista)
    plt.ylabel('Sea Level (inches)')
    #plt.show()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


