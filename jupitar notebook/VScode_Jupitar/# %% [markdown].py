# %% [markdown]
# # Jupitar notebook in VS code

# %%
pip install TeX

# %%
print("Python ka chilla with Nosheen")

# %%
pip install nbconvert

# %%
%pip install --upgrade pip


# %%
pip install seaborn

# %%
pip install matplotlib

# %%
pip install numpy

# %%
pip install jupyter

# %%
pip install pandas

# %%


# %%
print("print python ka chilla with Nosheen")

# %%
Nosheen = "My name is Nosh"
Nosheen

# %%
import numpy as np
x = np.array([1, 2, 3, 4, 5])
x

# %%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

phool = pd.read_csv("iris.csv")
  

# %%
import pandas as pd
import matplotlib.pyplot as plt
phool = pd.read_csv("iris.csv")

plt.plot(iris.5.1, phool["Iris-setosa"], "r--") 
plt.show()

# %%
import seaborn as sns
sns.set_theme(style="ticks", palette="pastel")

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Draw a nested boxplot to show bills by day and time
sns.boxplot(x="day", y="total_bill",
            hue="smoker", palette=["m", "g"],
            data=tips)
sns.despine(offset=10, trim=True)

# %%
pip install "nbconvert[webpdf]"
jupyter nbconvert --to webpdf your_notebook.ipynb --allow-chromium-download

# %%
pip install nbconvert



