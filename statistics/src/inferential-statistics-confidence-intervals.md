---
title: Confidence Intervals
---

[Back to index](index.html)

---
# Inferential Statistics
## Confidence Intervals

### Confidence Intervals (Inferential Statistics)

A **confidence interval** (CI) is a range of values, derived from sample statistics, that is likely to contain the true population parameter. It provides an estimated range that is likely to include the parameter of interest, such as a population mean or proportion, with a certain level of confidence. The confidence level is often expressed as a percentage, typically 95% or 99%.

#### Key Components of Confidence Intervals:

1. **Point Estimate:**
   - The sample statistic (e.g., sample mean or sample proportion) used as the best estimate of the population parameter.

2. **Margin of Error:**
   - The amount added to and subtracted from the point estimate to create the interval. The margin of error accounts for the variability or uncertainty in the sample estimate.

3. **Confidence Level:**
   - The probability that the confidence interval contains the true population parameter. For example, a 95% confidence level means that if you repeated the sampling process 100 times, approximately 95 out of those 100 confidence intervals would be expected to contain the actual population parameter.

4. **Confidence Interval Formula:**
   - For a population mean with a known standard deviation: 
     \(\text{CI} = \bar{x} \pm Z \frac{\sigma}{\sqrt{n}}\)
     where \(\bar{x}\) is the sample mean, \(Z\) is the Z-value from the standard normal distribution corresponding to the confidence level (e.g., 1.96 for 95%), \(\sigma\) is the population standard deviation, and \(n\) is the sample size.
   
   - For a population mean with an unknown standard deviation:
     \(\text{CI} = \bar{x} \pm t \frac{s}{\sqrt{n}}\)
     where \(t\) is the t-value from the t-distribution corresponding to the confidence level and degrees of freedom \( (n-1) \), and \(s\) is the sample standard deviation.

   - For a population proportion:
     \(\text{CI} = \hat{p} \pm Z \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}\)
     where \(\hat{p}\) is the sample proportion, and \(Z\) is the Z-value corresponding to the confidence level.

#### Examples:

1. **Mean Example:**
   - Suppose you collect a sample of 30 students’ test scores with a sample mean of 80 and a standard deviation of 10. To calculate a 95% confidence interval for the population mean:
     \[
     \text{CI} = 80 \pm 1.96 \frac{10}{\sqrt{30}} = 80 \pm 3.57
     \]
     So, the 95% confidence interval is \( (76.43, 83.57) \).

2. **Proportion Example:**
   - Suppose you survey 200 people and find that 60 are left-handed. The sample proportion \(\hat{p} = \frac{60}{200} = 0.3\). To calculate a 95% confidence interval for the population proportion:
     \[
     \text{CI} = 0.3 \pm 1.96 \sqrt{\frac{0.3 \times (1-0.3)}{200}} = 0.3 \pm 0.065
     \]
     So, the 95% confidence interval is \( (0.235, 0.365) \).

#### Interpretation:

- If you have a 95% confidence interval of \((76.43, 83.57)\) for the mean test scores, you can say, "We are 95% confident that the true population mean falls between 76.43 and 83.57."
- It does not mean that there is a 95% probability that the population mean is within this range for any given interval. Instead, it means that 95% of such constructed intervals from repeated sampling would contain the true mean.

Confidence intervals are a fundamental concept in inferential statistics because they provide a range of plausible values for population parameters, reflecting the uncertainty inherent in sample data.

---
[Back to index](index.html)
