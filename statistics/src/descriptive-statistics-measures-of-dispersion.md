---
title: Measures of Dispersion
---

[Back to index](index.html)

---
# Descriptive Statistics
## Measures of Dispersion

Measures of dispersion are statistical tools that describe the spread, variability, or distribution of a dataset. These measures give insights into how much the data points differ from the central tendency (mean, median, or mode) of the dataset. Understanding the dispersion can help in interpreting the reliability and consistency of the data. Here are some common measures of dispersion:

### 1. **Range**
- **Definition**: The difference between the highest and lowest values in a dataset.
- **Calculation**: \( \text{Range} = \text{Maximum Value} - \text{Minimum Value} \)
- **Advantages**: Simple to calculate and understand.
- **Disadvantages**: Does not provide information about the distribution of values between the extremes and can be affected by outliers.

### 2. **Variance**
- **Definition**: A measure of how much each data point differs from the mean of the dataset.
- **Calculation**: 
  \[
  \text{Variance} (\sigma^2) = \frac{\sum (x_i - \mu)^2}{N}
  \]
  where \( x_i \) is each data point, \( \mu \) is the mean, and \( N \) is the number of data points.
- **Advantages**: Takes all data points into account.
- **Disadvantages**: Measures in squared units, which can make interpretation difficult with respect to the original data units.

### 3. **Standard Deviation**
- **Definition**: The square root of the variance, providing a measure of dispersion in the same units as the data.
- **Calculation**:
  \[
  \text{Standard Deviation} (\sigma) = \sqrt{\frac{\sum (x_i - \mu)^2}{N}}
  \]
- **Advantages**: Easier to interpret compared to variance since it's in the same units as the data.
- **Disadvantages**: Can still be influenced by outliers.

### 4. **Interquartile Range (IQR)**
- **Definition**: The range between the first quartile (25th percentile) and the third quartile (75th percentile) of the dataset.
- **Calculation**: 
  \[
  \text{IQR} = Q3 - Q1
  \]
- **Advantages**: Not influenced by outliers or extreme values since it focuses on the middle 50% of the data.
- **Disadvantages**: Ignores data outside the interquartile range.

### 5. **Mean Absolute Deviation (MAD)**
- **Definition**: Average of the absolute differences between each data point and the mean of the dataset.
- **Calculation**:
  \[
  \text{MAD} = \frac{\sum |x_i - \mu|}{N}
  \]
- **Advantages**: Easier to understand than variance since it measures dispersion in the same units as the data without squaring the differences.
- **Disadvantages**: Less mathematically tractable compared to variance and standard deviation.

### Conclusion
Measures of dispersion are crucial for understanding the variability within a dataset. Each measure has its own strengths and weaknesses, and the choice of which to use often depends on the specific characteristics of the data and the objectives of the analysis.

---
[Back to index](index.html)
