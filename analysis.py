import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Configuration générale
# -----------------------------
sns.set(style="whitegrid")

# -----------------------------
# Charger le dataset
# -----------------------------
df = pd.read_csv("data/Sleep_health_and_lifestyle_dataset.csv")

# -----------------------------
# Exploration initiale
# -----------------------------
print("Aperçu des 5 premières lignes :")
print(df.head())

print("\nDimensions du dataset :")
print(df.shape)

print("\nNoms des colonnes :")
print(df.columns)

print("\nStatistiques générales :")
print(df.describe())

print("\nValeurs manquantes :")
print(df.isnull().sum())

print("\nDistribution des troubles du sommeil :")
print(df["Sleep Disorder"].value_counts(dropna=False))

# -----------------------------
# Graphique 1 : durée du sommeil
# -----------------------------
plt.figure(figsize=(8, 5))
sns.histplot(df["Sleep Duration"], bins=20)

plt.title("Distribution of Sleep Duration Among Participants")
plt.xlabel("Sleep Duration (hours per night)")
plt.ylabel("Number of Participants")

plt.tight_layout()
plt.savefig("figures/sleep_duration_distribution.png")
plt.close()

# -----------------------------
# Graphique 2 : stress vs qualité du sommeil
# -----------------------------
plt.figure(figsize=(8, 5))
sns.scatterplot(
    x=df["Stress Level"],
    y=df["Quality of Sleep"],
    alpha=0.6
)

plt.title("Relationship Between Stress Level and Sleep Quality")
plt.xlabel("Stress Level")
plt.ylabel("Quality of Sleep Score")

plt.tight_layout()
plt.savefig("figures/stress_vs_sleep_quality.png")
plt.close()

# -----------------------------
# Graphique 3 : distribution des troubles du sommeil
# -----------------------------
plt.figure(figsize=(8, 5))
sns.countplot(x=df["Sleep Disorder"].fillna("None"))

plt.title("Distribution of Sleep Disorders in the Dataset")
plt.xlabel("Type of Sleep Disorder")
plt.ylabel("Number of Participants")

plt.tight_layout()
plt.savefig("figures/sleep_disorder_distribution.png")
plt.close()

# -----------------------------
# Graphique 4 : qualité du sommeil selon le niveau de stress
# -----------------------------
plt.figure(figsize=(8, 5))
sns.boxplot(x="Stress Level", y="Quality of Sleep", data=df)

plt.title("Quality of Sleep by Stress Level")
plt.xlabel("Stress Level")
plt.ylabel("Quality of Sleep Score")

plt.tight_layout()
plt.savefig("figures/quality_sleep_by_stress.png")
plt.close()

# -----------------------------
# Graphique 5 : qualité du sommeil selon le trouble du sommeil
# -----------------------------
plt.figure(figsize=(8, 5))
sns.boxplot(
    x=df["Sleep Disorder"].fillna("None"),
    y=df["Quality of Sleep"]
)

plt.title("Quality of Sleep by Sleep Disorder Type")
plt.xlabel("Sleep Disorder")
plt.ylabel("Quality of Sleep Score")

plt.tight_layout()
plt.savefig("figures/quality_sleep_by_disorder.png")
plt.close()

# -----------------------------
# Graphique 6 : heatmap des corrélations
# -----------------------------
plt.figure(figsize=(10, 8))

numeric_df = df.select_dtypes(include="number")
correlation_matrix = numeric_df.corr()

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Matrix of Sleep and Lifestyle Variables")

plt.tight_layout()
plt.savefig("figures/correlation_matrix.png")
plt.close()

print("\nToutes les figures ont été enregistrées dans le dossier 'figures'.")

# -----------------------------
# Simple sleep risk score
# -----------------------------
risk_df = df.copy()
risk_df["Sleep Disorder"] = risk_df["Sleep Disorder"].fillna("None")

risk_df["High Stress"] = (risk_df["Stress Level"] >= 7).astype(int)
risk_df["Low Sleep Quality"] = (risk_df["Quality of Sleep"] <= 5).astype(int)
risk_df["Short Sleep"] = (risk_df["Sleep Duration"] < 7).astype(int)

risk_df["Sleep Risk Score"] = (
    risk_df["High Stress"] +
    risk_df["Low Sleep Quality"] +
    risk_df["Short Sleep"]
)

print("\nAverage Sleep Risk Score by Sleep Disorder:")
print(risk_df.groupby("Sleep Disorder")["Sleep Risk Score"].mean())

plt.figure(figsize=(8, 5))
sns.boxplot(x="Sleep Disorder", y="Sleep Risk Score", data=risk_df)

plt.title("Sleep Risk Score by Sleep Disorder")
plt.xlabel("Sleep Disorder")
plt.ylabel("Risk Score")

plt.tight_layout()
plt.savefig("figures/sleep_risk_score_by_disorder.png")
plt.close()