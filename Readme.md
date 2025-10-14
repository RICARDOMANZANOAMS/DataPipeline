# Data Pipeline with Software Patterns

## Description

This repository contains a general-purpose program designed to **train and test classification models**.  
It can be easily extended to support **regression problems**.  
The system is **modular and extensible**, following software design patterns such as **Strategy**, **Factory**, and **singleton**.

The **data pipeline** is capable of reading multiple input formats, such as **CSV** and **JSON**, and can be easily extended to handle additional formats.

The pipeline includes **data preprocessing** stages such as:
- Removing duplicates  
- Data imputation (mean, median, or a fixed value)

The **imputation mechanism** is modular, allowing new strategies to be added effortlessly.

The **Trainer class** was implemented to support different **algorithms and data-splitting methods**, including:
- Simple split  
- K-Fold cross-validation  
- Leave-One-Out Cross-Validation (LOOCV)

The program uses a **configuration file** that enables easy customization of experimental parameters.
The program implements logging as singleton.
---

## Workflow Overview

1. The application starts by **reading a configuration file**, which specifies the input source and parameters.  
2. Then, one or more **preprocessing steps** (e.g., duplicate removal, imputation) are applied.  
3. Finally, the system **trains and tests** a classifier.  
4. Inside the classifier, the **type of data split** (split, KFold, LOOCV) can be defined through configuration.

---

## Code Structure


- **Config** – Contains `config.json`, where all experiment parameters are defined.  
- **Data** – Includes the datasets required to train the models.  
- **Exploration** – Contains a Jupyter notebook for exploratory data analysis.  
- **src** – Implements all pipeline classes (readers, preprocessors, trainer, etc.).

---

## Key Features

- Modular and extensible design  
- Built with **Strategy** and **Factory** patterns  
- Supports multiple input formats (CSV, JSON, etc.)  
- Flexible preprocessing pipeline  
- Configurable training and testing workflow  
- Easily extendable for regression tasks  

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/RICARDOMANZANOAMS/DataPipeline.git
   cd datapipeline-patterns
