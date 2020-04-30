import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

ads = pd.read_csv("Social_Network_Ads.csv")

ads.head(5)

plt.scatter(ads['Age'],ads['EstimatedSalary'])
plt.xlabel('Age')
plt.ylabel('EstimatedSalary')
plt.title('Scatter plot between Age vs Estimated Salary')

sns.set_style('whitegrid')
sns.FacetGrid(ads,hue='Purchased',height=7).map(plt.scatter,'Age','EstimatedSalary').add_legend()
plt.show()

ads.drop(columns=['User ID'],inplace=True)

sns.set_style('whitegrid')
sns.pairplot(ads,hue='Purchased',height=5)
plt.show()

sns.boxplot(x='Purchased',y='EstimatedSalary',data=ads)

sns.clustermap(ads.corr(),figsize=(7,7),annot=True)
plt.show()

sns.heatmap(ads.corr(),annot =True,cbar_kws={'orientation':'horizontal'})
plt.show()

ads.isnull().sum()

ads.info()

ads.describe()