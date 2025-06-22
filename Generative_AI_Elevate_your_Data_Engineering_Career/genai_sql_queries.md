
We have a Heart Disease prediction dataset with a single table which has the following attributes.

1. age - age in years
2. gender- gender (1 = male; 0 = female)
3. cp - chest pain type
- Value 1: typical angina
- Value 2: atypical angina
- Value 3: non-anginal pain
- Value 4: asymptomatic

4. trestbps - resting blood pressure (in mm Hg on admission to the hospital)
5. chol - serum cholestoral in mg/dl
6. fbs - (fasting blood sugar > 120 mg/dl)  (1 = true; 0 = false)
7. restecg - resting electrocardiographic results
 - Value 0: normal
 - Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
 - Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria
8. thalach - maximum heart rate achieved
9. exang - exercise induced angina (1 = yes; 0 = no)
10. oldpeak - ST depression induced by exercise relative to rest
11. slope - the slope of the peak exercise ST segment
- Value 1: upsloping
- Value 2: flat
- Value 3: downsloping
12. ca - number of major vessels (0-3) colored by flourosopy
13. thal - 3 = normal; 6 = fixed defect; 7 = reversable defect
14. num (the predicted attribute) - diagnosis of heart disease (angiographic disease status)
- Value 0: < 50% diameter narrowing
- Value 1: > 50% diameter narrowing

### Write an SQL query to find the minimum, maximum, and average age of patients in the dataset.

```sql
SELECT 
    MIN(age) AS min_age,
    MAX(age) AS max_age,
    AVG(age) AS avg_age
FROM 
    heart_disease_prediction_dataset;
```
### Write and SQL query to count the number of male and female patients in the dataset.
```sql
SELECT 
    CASE 
        WHEN gender = 1 THEN 'Male'
        WHEN gender = 0 THEN 'Female'
    END AS gender, 
    COUNT(*) AS patient_count
FROM 
    heart_disease_dataset
GROUP BY 
    gender;
```
### Write an SQL query to determine the frequency of each type of chest pain (typical angina, atypical angina, non-anginal pain, asymptomatic) among patients.

SELECT 
    cp, 
    COUNT(*) AS frequency
FROM 
    heart_disease_dataset
GROUP BY 
    cp
ORDER BY 
    frequency DESC;

Write an SQL query to investigate the distribution of the target variable (presence or absence of heart disease) within different age groups (e.g., 20-30, 30-40, etc.).

SELECT 
    CASE
        WHEN age BETWEEN 20 AND 30 THEN '20-30'
        WHEN age BETWEEN 31 AND 40 THEN '31-40'
        WHEN age BETWEEN 41 AND 50 THEN '41-50'
        WHEN age BETWEEN 51 AND 60 THEN '51-60'
        WHEN age BETWEEN 61 AND 70 THEN '61-70'
        ELSE 'Above 70'
    END AS age_group,
    SUM(CASE WHEN num = 1 THEN 1 ELSE 0 END) AS heart_disease_count,
    SUM(CASE WHEN num = 0 THEN 1 ELSE 0 END) AS no_heart_disease_count
FROM 
    heart_disease_prediction_dataset
GROUP BY 
    age_group
ORDER BY 
    age_group;

Find the range of cholesterol levels among patients (minimum, maximum).
SELECT 
    MIN(chol) AS min_cholesterol, 
    MAX(chol) AS max_cholesterol
FROM 
    heart_disease_dataset;

Determine the age range (youngest and oldest) for male and female patients separately.
SELECT 
    gender,
    MIN(age) AS youngest_age, 
    MAX(age) AS oldest_age
FROM 
    heart_disease_dataset
GROUP BY 
    gender;

Investigate the distribution of the target variable (presence or absence of heart disease) within different age groups (e.g., 20-30, 30-40, etc.).
WITH AgeBands AS (
    SELECT
        age,
        CASE 
            WHEN age BETWEEN 20 AND 30 THEN '20-30'
            WHEN age BETWEEN 31 AND 40 THEN '31-40'
            WHEN age BETWEEN 41 AND 50 THEN '41-50'
            WHEN age BETWEEN 51 AND 60 THEN '51-60'
            ELSE '60+'
        END AS age_band
    FROM 
        heart_disease_dataset
)
SELECT 
  age_band,
  COUNT(CASE WHEN num = 1 THEN 1 END) AS disease_positive,
  COUNT(CASE WHEN num = 0 THEN 1 END) AS disease_negative,
  COUNT(*) AS total
FROM 
  AgeBands
GROUP BY 
  age_band
ORDER BY 
  age_band;


  Find the maximum heart rate achieved during exercise for different age groups (e.g., 30-40, 40-50, etc.).
  WITH AgeBands AS (
    SELECT
        age,
        CASE 
            WHEN age BETWEEN 20 AND 30 THEN '20-30'
            WHEN age BETWEEN 31 AND 40 THEN '31-40'
            WHEN age BETWEEN 41 AND 50 THEN '41-50'
            WHEN age BETWEEN 51 AND 60 THEN '51-60'
            ELSE '60+'
        END AS age_band
    FROM 
        heart_disease_dataset
)
SELECT 
    age_band, 
    MAX(thalach) AS max_heart_rate
FROM 
    AgeBands 
GROUP BY 
    age_band
ORDER BY 
    age_band;

Calculate the percentage of patients with fasting blood sugar greater than 120 mg/dl.
SELECT 
    (COUNT(*) FILTER (WHERE fbs = 1) * 100.0 / COUNT(*)) AS pct_fbs_above_120
FROM 
    heart_disease_dataset;

Find the ratio of patients with abnormal resting electrocardiographic results to those with normal results.
SELECT 
    COUNT(CASE WHEN restecg = 0 THEN 1 END) AS normal_count,
    COUNT(CASE WHEN restecg IN (1, 2) THEN 1 END) AS abnormal_count,
    (COUNT(CASE WHEN restecg IN (1, 2) THEN 1 END)::float / COUNT(CASE WHEN restecg = 0 THEN 1 END)) AS ratio
FROM 
    heart_disease_dataset;

Count the number of patients with reversible thalassemia detected by thallium stress testing.
SELECT 
    COUNT(*) AS patients_with_reversible_thalassemia
FROM 
    heart_disease_dataset
WHERE 
    thal = 7;

Calculate the average age of patients who experienced chest pain during diagnosis.
SELECT 
    AVG(age) AS average_age_with_chest_pain
FROM 
    heart_disease_dataset
WHERE 
    cp != 0;

Investigate the distribution of patients based on the number of major vessels colored by fluoroscopy (0-3).
SELECT 
    ca, 
    COUNT(*) AS patient_count
FROM 
    heart_disease_dataset
GROUP BY 
    ca
ORDER BY 
    ca;
