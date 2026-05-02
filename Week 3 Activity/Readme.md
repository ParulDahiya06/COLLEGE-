# 📊 Data Cleaning and Visualization with Correlation Heatmap

## 📌 Project Overview

This project focuses on cleaning a messy dataset and performing data visualization to extract meaningful insights. A Pearson correlation heatmap is used to analyze linear relationships between numerical features.

---

## 🎯 Objectives

* Clean and preprocess the dataset (*messy_dataset.csv*)
* Handle missing and inconsistent data
* Detect and manage outliers
* Visualize relationships between variables
* Generate a Pearson correlation heatmap

---

## 🛠️ Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## 🧹 Data Cleaning Steps

* Removed duplicate records
* Handled missing values:

  * Numerical columns → filled with median
  * Categorical columns → filled with mode
* Converted incorrect data types
* Standardized column names
* Fixed inconsistent values

---

## 📦 Outlier Detection

Outliers were identified using the **Interquartile Range (IQR)** method.

* Calculated Q1 (25th percentile) and Q3 (75th percentile)
* Computed IQR = Q3 − Q1
* Values outside the range *(Q1 − 1.5×IQR, Q3 + 1.5×IQR)* were considered outliers
* Outliers were either removed or capped

---

## 📈 Data Visualization

A **correlation heatmap** was created using the Pearson correlation coefficient to identify linear relationships between features.

### Key Points:

* **+1** → Strong positive correlation
* **-1** → Strong negative correlation
* **0** → No linear correlation

---

## 🔍 Key Insights

* Strong correlations observed between some numerical features
* Weak or no correlation between unrelated variables
* Outliers detected in specific columns (refer to output)
* Cleaned dataset is more reliable for analysis and modeling

---

## 📁 Project Structure

```
Data-Cleaning-Visualization/
│── messy_dataset.csv
│── data_cleaning_visualization.ipynb
│── README.md
│── output_screenshots.png
```

---

## ▶️ How to Run

1. Clone the repository
2. Install required libraries:

   ```
   pip install pandas numpy matplotlib seaborn
   ```
3. Run the notebook or Python script

---

## 🔗 GitHub Link

(Add your repository link here)

---

## 🎥 Presentation

A 3-minute video presentation explains:

* Data cleaning process
* Outlier detection
* Correlation heatmap insights

---

## ✅ Conclusion

Data cleaning improved dataset quality, and visualization helped uncover meaningful patterns. The Pearson correlation heatmap provided clear insights into relationships between variables, supporting better decision-making for further analysis.

---
