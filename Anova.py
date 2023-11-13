import scipy.stats as stats
import pandas as pd

# 创建一个数据框，包含四个模型的性能数据
data = {
    '3 folds': [57.75, 77.57, 88.87, 64.36],
    '5 folds': [57.77, 78.62, 89.26, 64.44],
    '10 folds': [57.77, 79.41, 89.57, 64.48]
}

df = pd.DataFrame(data)

# 执行ANOVA以比较四个模型在不同折叠数下的性能
f_statistic, p_value = stats.f_oneway(df['3 folds'], df['5 folds'], df['10 folds'])

# 输出ANOVA结果
print("ANOVA F-statistic:", f_statistic)
print("ANOVA p-value:", p_value)

# 执行t-检验来比较每个模型的性能
t_statistic, t_p_values = stats.ttest_ind(df['3 folds'], df['5 folds'])
print("t-test for 3 folds vs. 5 folds:")
print("t-statistic:", t_statistic)
print("p-value:", t_p_values)

t_statistic, t_p_values = stats.ttest_ind(df['3 folds'], df['10 folds'])
print("t-test for 3 folds vs. 10 folds:")
print("t-statistic:", t_statistic)
print("p-value:", t_p_values)

t_statistic, t_p_values = stats.ttest_ind(df['5 folds'], df['10 folds'])
print("t-test for 5 folds vs. 10 folds:")
print("t-statistic:", t_statistic)
print("p-value:", t_p_values)