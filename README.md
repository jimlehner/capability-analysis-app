# XmR Chart-It

A web application for generating XmR charts, the most useful type of process behavior. Built as part of [The Broken Quality Initiative](https://www.brokenquality.com/).

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
  - [Requirements](#requirements)
  - [Running the App](#running-the-app)
- [File Structure](#file-structure)
- [How to Use](#how-to-use)
  - [Selecting a Sample Dataset](#selecting-a-sample-dataset)
  - [Uploading Your Own Data](#uploading-your-own-data)
  - [XmR Chart Display Controls](#xmr-chart-display-controls)
  - [Stage View](#stage-view)
- [Process Limit Formulas](#process-limit-formulas)
- [Sample Datasets](#sample-datasets)
- [About](#about)

---

## Overview

Try the live app at [xmr-chart-it.streamlit.app](https://xmrit.streamlit.app).

When a dataset is composed of logically comparable individual values that retain their time-ordered sequence, the only tool capable of characterizing process behavior is the XmR chart. XmR charts characterize process behavior as either predictable or unpredictable by comparing individual values and moving ranges with three calculated process limits: the Upper Process Limit (UPL), the Lower Process Limit (LPL), and the Upper Range Limit (URL). When one or more values fall outside the process limits, the underlying causal system is characterized as unpredictable. Here, both common causes of routine variation and assignable causes of exceptional variation influence process behavior. Although few in number, assignable causes are dominant in their effect. They cause a process to bounce and shift in unpredictable ways. When all of the values fall inside the process limits, the process is characterized as predictable. Here, only common causes of routine variation influence process behavior. As a result, future process behavior can be predicted within the calculated process limits.

The app allows users to:
- Explore nine sample datasets spanning manufacturing, economics, and science
- Upload their own CSV files
- Visualize data as an XmR chart with calculated process limits
- Analyze multi-stage processes
- Test their understanding with interactive questions

---

## Features

- **Sample datasets** — nine preloaded datasets with default column configurations and descriptions
- **CSV upload** — upload your own data with selectable data, label, and stage columns
- **XmR chart** — interactive Plotly chart with Upper Process Limit (UPL), Lower Process Limit (LPL), and Upper Range Limit (URL)
- **Stage view** — divide data into stages for direct visual comparison of process behavior across periods
- **Display controls** — adjust tick interval, decimal places, tick angle, and toggle process limits, annotations, and connecting lines
- **Interactive questions** — multiple choice questions with instant feedback for each sample dataset
- **Bound LPL/UPL** — options to prevent limits from going below zero or above 100%

---

## Installation

### Requirements

```
streamlit
pandas
plotly
Pillow
```

Install dependencies:

```bash
pip install streamlit pandas plotly Pillow
```

### Running the App

```bash
streamlit run xmr_chart_app.py
```

---

## File Structure
```
│   .gitignore
│   LICENSE
│   README.md
│   requirements.txt
│   styles.css
│   xmr_app.py
│
├───calculations
│   │   xmr_limits.py
│   │   xmr_rules.py
│   │
│   └───__pycache__
│           xmr_limits.cpython-39.pyc
│           xmr_rules.cpython-39.pyc
│
├───components
│   │   additional_resources.py
│   │   charts.py
│   │   chart_annotations.py
│   │   chart_stages.py
│   │   chart_styles.py
│   │   dataset_selector.py
│   │   limit_formulas.py
│   │   sidebar.py
│   │   xmr_chart_tab1.py
│   │   xmr_intro.py
│   └───__init__.py
│
├───config
│       datasets.py
│       questions.py
│
├───content
│       characterization_flowchart.md
│       instructions.md
│       limit_formulas.md
│       sidebar_author.md
│       sidebar_contact.md
│       sidebar_project.md
│       sidebar_socials.md
│       sidebar_website.md
│       taguchi_loss.md
│       understanding_process_cap.md
│       virus_of_variation.md
│       xmr_intro.md
│
├───data
│   │   loader.py
│   │
│   ├───examples
│   │       automated_manufacturing_part_lengths.csv
│   │       manufacturing_PMI.csv
│   │       millikans_electron_charge_observations.csv
│   │       monthly_united_states_trade_deficits_2024.csv
│   │       OP200_weekly_first_pass_yield.csv
│   │       quarterly_sales_by_region.csv
│   │       shewharts_resistance_measurements.csv
│   │       vienna_general_death_to_birth_rates.csv
│   │       wafer_assembly_part_placement.csv
│   │
│   └───__pycache__
│           loader.cpython-39.pyc
│
└───figures
        Broken_quality_logo.png
        characterization_flowchart.png
        EQ_UPL_LPL.png
        EQ_URL.png
        Fig_is_all_the_data_within_limits.png
        Fig_xmr_chart_app_figure_1.png
        Fig_xmr_chart_example.png
        taguchi_loss_distribution.png
        taguchi_loss_one.png
        understand_process_cap.png
        virus_of_variation_book_cover.png
        virus_of_variation_cover.png
```

---

## How to Use

### Selecting a Sample Dataset
Use the **Select a sample dataset** dropdown to choose from nine preloaded datasets. Each dataset includes a description, default column selections, and a set of interactive questions.

### Uploading Your Own Data
Use the **Or upload a CSV file** file uploader to upload a CSV. You will be prompted to select:
- **Data column** — the column containing the values to be plotted
- **Label column** — the column used for x-axis labels (or use the default 1 to n)
- **Stage column** — optional column used to divide the data into stages

### XmR Chart Display Controls
Expand the **XmR Chart Display Controls** section to adjust:
- Tick interval and label angle
- Number of decimal places displayed
- Show/hide process limits, annotations, and connecting lines
- Bound UPL at 100% or LPL at 0%

### Stage View
If a stage column is selected, expand the **Stage View & Customization** section to enable stage-based process limits. Each stage is calculated independently, allowing direct comparison of process behavior across different periods or conditions.

---

## Process Limit Formulas

The XmR chart process limits are calculated as follows:

```
UPL = X̄ + 2.660 × mR̄
LPL = X̄ - 2.660 × mR̄
URL = 3.268 × mR̄
```

Where X̄ is the mean of the data and mR̄ is the average moving range. The scaling factors 2.660 (E2) and 3.268 (D4) correspond to a subgroup size of n = 2.

---

## Sample Datasets

| Dataset | Description |
|---|---|
| Automated Manufacturing Part Lengths | 60 part length measurements from an automated manufacturing line |
| Manufacturing PMI | Monthly Purchase Manager's Index values from Feb 2025 to Jan 2026 |
| Millikan's Electron Charge Observations | 58 electron charge measurements by Millikan |
| Monthly United States Trade Deficits 2024 | Monthly US trade deficits for 2024 |
| OP200 Weekly First Pass Yield | 24 weeks of first-pass yield data for operation 200 |
| Quarterly Sales by Region | Quarterly sales for 6 regions over 20 consecutive quarters |
| Shewhart's Resistance Measurements | Electrical resistance measurements before and after process improvements |
| Vienna General Death-to-Birth Rates | Death-to-birth rates at Vienna General Hospital, 1841–1849 |
| Wafer Assembly Part Placement | X-coordinate placement measurements from a pick-and-place line |

---

## About

This app was created by [The Broken Quality Initiative](https://www.brokenquality.com/). We teach engineers how to reduce costs and improve the quality of 
manufactured product by understanding variation.

To learn more, visit [BrokenQuality.com](https://www.brokenquality.com/) or read [The Virus of Variation: Making Sense of Death and Data using Process Behavior Charts](https://www.brokenquality.com/store).

**Author:** [Jim Lehner](https://www.linkedin.com/in/jim-lehner/)

**Contact:** James.Lehner@gmail.com | QualityIsBroken@gmail.com
