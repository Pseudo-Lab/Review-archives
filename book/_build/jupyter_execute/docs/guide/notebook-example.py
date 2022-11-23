#!/usr/bin/env python
# coding: utf-8

# # Jupyter-notebook(.ipynb) Tips

# Jupyter Book에선 .ipynb파일 또한 지원합니다. 아래와 같이 코드를 입력하고, 그에 대응하는 출력물을 함께 웹페이지로 구성 가능합니다. 

# In[4]:


import matplotlib.pyplot as plt

plt.plot([3,1,2,1,3])


# [공식 홈페이지](https://jupyterbook.org/interactive/interactive.html#plotly)를 참고하여 interactive한 시각화도 가능합니다. 

# ## 1. Removing code cell content
# 
# - Reference: [https://jupyterbook.org/en/stable/interactive/hiding.html#hide-code-cell-content](https://jupyterbook.org/en/stable/interactive/hiding.html#hide-code-cell-content)
#   
# - Code cell을 숨기기고 싶은 경우 cell tag에 hide-cell을 추가한다. (input, output 모두 가려짐)
# - Visual Studio Code로 작업하는 경우 Cell 상단 ... 선택 후 "Add Cell Tag"로 추가 가능
#   

# In[1]:


# hide-cell tag 추가
import matplotlib.pyplot as plt

plt.plot([3,1,2,1,3])


# - Cell의 input 숨기기를 적용하는 경우 cell tag에 hide-input을 추가한다. (input 가려짐)

# In[3]:


# hide-input tag 추가
import matplotlib.pyplot as plt

plt.plot([3,1,2,1,3])


# - Cell의 input을 표시하지 않는 경우 cell tag에 remove-input을 추가한다. 

# In[4]:


# hide-input tag 추가
import matplotlib.pyplot as plt

plt.plot([3,1,2,1,3])

