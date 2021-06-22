#################################################################
# AB Testing Project
#################################################################

# Dataset Story:
# In this dataset, which includes the website information of bombabomba.com, there is information such as the number of advertisements that users see and click and earnings information from here.
# There are two separate data sets, Control and Test group. These datasets are in separate sheets of the ab_testing.xlsx excel.

# Variables:
# Impression – Ad views count
# Click – Indicates the number of clicks/clicks on the displayed ad.
# Purchase – Indicates the number of products purchased after the purchase / clicked ads.
# Earning – Earnings / Earnings after purchased items

import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest
from helpers.Advanced_Functional_EDA import check_df

########################### TASK 1 ############################

# Define the hypothesis of the A/B test.

# H0: M1 = M2 / There is no statistically significant difference between the Test and Control groups.
# H1: M1!= M2 / There is a statistically significant difference between the Test and Control groups.


########################### TASK 2 ############################

# Perform the hypothesis test—comment on whether the results are statistically significant.

# Maximum bidding campaign: Control Group (available)
# Average bidding campaign: Test Group (new product)

control_group = pd.read_excel("hafta 5/datasets/ab_testing.xlsx", sheet_name ="Control Group")
test_group = pd.read_excel("hafta 5/datasets/ab_testing.xlsx", sheet_name ="Test Group")

check_df(control_group)
check_df(test_group)

control_group["Purchase"].mean()
# 550.8940587702316
test_group["Purchase"].mean()
# 582.1060966484675

# When we look at the purchase average of the two groups, we can observe that the test group, the average bidding campaign, is better. But this observation is not a statistically significant results.


####### Can we conclude statistically significant results? ##########

##### Indepented Two Sample T-Test #####
# The Independent Samples t Test compares the means of two independent groups in order to determine whether there is statistical evidence that the associated population means are significantly different.

#####  Requirements #####
# Normal distribution: Non-normal population distributions, especially those that are thick-tailed or heavily skewed, considerably reduce the power of the test
# Homogeneity of variances : When this assumption is violated and the sample sizes for each group differ, the p value is not trustworthy.

##### Hypotheses #####
# The null hypothesis (H0) and alternative hypothesis (H1) of the Independent Samples t Test can be expressed in two different but equivalent ways:

# H0: µ1 = µ2 (the two population means are equal)
# H1: µ1 ≠ µ2 (the two population means are not equal)

##### The Shapiro-Wilks Test for Normality #####
# H0: There is no statistically significant difference between sample distribution and theoretical normal distribution
# H1: There is statistically significant difference between sample distribution and theoretical normal distribution
# The test rejects the hypothesis of normality when the p-value is less than or equal to 0.05. Failing the normality test allows you to state with 95% confidence the data does not fit the normal distribution.
# p-value < 0.05 (H0 rejected)
# p-value > 0.05 (H0 not rejected)


# Shapiro-Wilks Test for Control Group
test_stat, pvalue = shapiro(control_group["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p-value:0.5891
# p-value greater then 0.05 so H0 is not rejected

# Shapiro-Wilks Test for Test Group
test_stat, pvalue = shapiro(test_group["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p-value: 0.1541
# p-value greater then 0.05 so H0 is not rejected

# There is no statistically significant difference between sample distribution and theoretical normal distribution in groups Control and Test Group.

##### Levene’s Test for Homogeneity of variances #####
# Levene’s test is an equal variance test. It can be used to check if our data sets fulfill the homogeneity of variance assumption before we perform the t-test or Analysis of Variance
# H0: the compared groups have equal variance.
# H1: the compared groups do not have equal variance.

test_stat, pvalue = levene(control_group["Purchase"], test_group["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p-value: 0.1083
# p-value greater then 0.05 so H0 is not rejected.

# The compared groups have equal variance.
# The assumptions of normality distribution and variance homogeneity were tested.Two assumptions are provided, we can now test for our main hypothesis.

# H0 : There is no statistically significant difference between the Control group that was served “maximum bidding” campaign and Test group that was served “average bidding” campaign.
# H1 : There is statistically significant difference between the Control group that was served “maximum bidding” campaign and Test group that was served “average bidding” campaign.


test_stat, pvalue = ttest_ind(control_group["Purchase"],
                              test_group["Purchase"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# p-value: 0.3493
# P-value greater then 0.05 so H0 is not rejected.So, There is no statistically significant difference between the Control group that was served “maximum bidding” campaign and Test group that was served “average bidding” campaign.


###### Which statistical test did we use, and why? ######
# We used independent t-test because we want to determine if there is a significant difference between the means of two indepented groups, which may be related in certain features.

###### What would be our recommendation to client? ######
# There is no statistically significant difference between the Control group that was served “maximum bidding” campaign and Test group that was served “average bidding” campaign. For this reason, we can recommend continuing with the maximum bidding campaign currently used.

###### Conclusion ######
# Hypothesis established and interpreted
# The data was analyzed, outliers were observed
# It was checked whether the assumptions were met for the statistical test to be applied
# The assumptions were observed and tested
# Commented based on -p-value
# Suggestion offered to customer









