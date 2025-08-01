

# 🧠 Customer Segmentation with Clustering | Gradio Dashboard

![Gradio UI Screenshot](./assets/dashboard_preview.png)

This project demonstrates an interactive **Customer Segmentation Tool** built with unsupervised learning using clustering algorithms. A clean, Gradio-powered interface allows users to upload customer data, visualize clustering outcomes, and understand segmentation insights.

---

## 📌 Project Highlights

* 🧩 Unsupervised learning with KMeans clustering
* 📊 Dynamic visualization of customer clusters
* 🧠 PCA-based dimensionality reduction
* 🌐 Interactive dashboard using **Gradio**
* 🔍 Segment-wise analysis: average features, proportions, and key differentiators
* 📁 Upload your own dataset for real-time analysis

---

## 📂 Project Structure

```bash
Clustering-CustoSeg/
├── seg.ipynb               # Main notebook with logic and Gradio interface
├── cluster_analysis.py     # Core clustering logic and data transformation
├── assets/                 # Images and assets used for UI/README
├── requirements.txt        # Dependencies
├── sample_data.csv         # Example customer dataset
├── README.md               # This file
```

---

## 🧪 Sample Inputs

You can start exploring the dashboard using the provided `sample_data.csv`.

**Columns:**

* `Age`: Age of the customer
* `Annual Income`: Income in USD
* `Spending Score`: Score assigned by marketing team
* `Gender`: Categorical column
* `Profession`: Job type/category
* `Family Size`: No. of dependents in household

---

## 🧠 How Clustering Works

1. **Data Preprocessing**
   → Handles missing values, categorical encoding, scaling

2. **PCA Visualization**
   → Reduces dimensionality for plotting clusters in 2D

3. **KMeans Clustering**
   → Segments users based on similarity

4. **Segment Interpretation**
   → Mean values and population of each cluster

---

## 🖥️ Gradio Dashboard Overview

| Section                     | Description                                                           |
| --------------------------- | --------------------------------------------------------------------- |
| **Upload CSV**              | Upload a custom dataset (`.csv` only) with relevant customer features |
| **Visualize Clusters**      | 2D scatterplot of clusters using PCA                                  |
| **Segment Table**           | Detailed breakdown of each cluster's stats                            |
| **Feature Distributions**   | Boxplots comparing clusters for each feature                          |
| **Download Segmented Data** | Export the labeled dataset with assigned cluster IDs                  |

---

## 🧪 Example Segment Analysis Output

| Cluster | Age (avg) | Income (avg) | Spending Score | Users (%) | Traits                   |
| ------- | --------- | ------------ | -------------- | --------- | ------------------------ |
| 0       | 23.4      | \$48,000     | 87.2           | 30%       | Young High-Spenders      |
| 1       | 45.2      | \$65,000     | 45.1           | 40%       | Mid-age Budget-Conscious |
| 2       | 34.9      | \$38,000     | 62.7           | 30%       | Young Moderate Spenders  |

---

## 📈 Exploratory Data Analysis (EDA)

✅ Null value analysis
✅ Feature distributions
✅ Correlation matrix
✅ Categorical feature breakdown
✅ Dimensionality reduction for visualization (PCA)

You can explore all this interactively using the notebook or integrate it into the Gradio app.

---

## 📦 Installation

```bash
git clone https://github.com/ttanishh/clustering-customerSegmentation.git
cd clustering-customerSegmentation
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 🚀 Run the App Locally

```bash
python seg.ipynb
# OR
# If exported as .py:
python seg.py
```

---

## 🧩 Requirements

```
pandas
numpy
scikit-learn
matplotlib
seaborn
gradio
```

> Install with: `pip install -r requirements.txt`

---

## 📦 Deployment Options

You can deploy it to:

* **Render** (recommended for simplicity)
* **HuggingFace Spaces**
* **Streamlit Sharing**
* **Dockerized on AWS / GCP / Azure**

---

## 💡 Future Enhancements

* 📬 User authentication for multi-tenant analysis
* 💾 Persistent segment storage
* 📊 Real-time dashboard with customer behavioral metrics
* 📈 Integration with marketing campaign data

---

## 👨‍💻 Author

**Tanish Panchal**
🔗 [GitHub](https://github.com/ttanishh)

