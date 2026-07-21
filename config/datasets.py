# datasets.py
dataset_columns = {
    "automated_manufacturing_part_lengths.csv": {
        "name": "Automated Manufacturing Part Lengths", 
        "data": "Value (mm)", 
        "label": "Sample", 
        "stage": None, 
        "tick_interval": 2,
        "description": "This dataset contains 60 part length measurements from an automated manufacturing line."
        },
    "manufacturing_PMI.csv": {
        "name": "Manufacturing PMI (Purchase Manager's Index)", 
        "data": "Manufacturing PMI", 
        "label": "Month", 
        "stage": None, 
        "tick_interval": 1,
        "description": "This dataset contains monthly manufacturing PMIs (Purchase Manager's Index) from February 2025 to January 2026."
        },
    "millikans_electron_charge_observations.csv": {
        "name": "Millikan's Electron Charge Observations", 
        "data": "Value", 
        "label": "Sample", 
        "stage": None, 
        "tick_interval": 5,
        "description": "This dataset contains 58 electron charge measurements (in coloumbs) made by Millikan."
        },
    "monthly_united_states_trade_deficits_2024.csv": {
        "name": "Monthly United States Trade Deficits 2024", 
        "data": "Value ($ billions)", 
        "label": "Month", 
        "stage": None, 
        "tick_interval": 1,
        "description": "This dataset contains the monthly tade deficits for the united states in 2024."
        },
    "OP200_weekly_first_pass_yield.csv": {
        "name": "OP200 Weekly First Pass Yield", 
        "data": "First-Pass Yield (%)", 
        "label": "Week", 
        "stage": None, 
        "tick_interval": 1,
        "description": "This dataset contains the first-pass yield for operation 200 (OP200) for a period of 24 weeks."
        },
    "quarterly_sales_by_region.csv": {
        "name": "Quarterly Sales by Region", 
        "data": "Sales", 
        "label": "Quarter", 
        "stage": "Stage", 
        "tick_interval": 5,
        "description": "This dataset contains the quarterly sales for 6 sales regions for 20 consecuitve quarters."
        },
    "shewharts_resistance_measurements.csv": {
        "name": "Shewhart's Resistance Measurements", 
        "data": "Resistance", 
        "label": "Value", 
        "stage": "Stage", 
        "tick_interval": 11,
        "description": "This dataset contains two sets of electrical resistance measurements collected by Walter A. Shewhart at Bell Telephone Laboratories."
        "The first set of measurements, called the 'Initial' stage, were collected before process improvements. The second set of measurements, called the 'Additional' "
        "stage, were collected after process improvements."
        },
    "vienna_general_death_to_birth_rates.csv": {
        "name": "Vienna General Death-to-Birth Rates", 
        "data": "Rate", 
        "label": "MonthYear", 
        "stage": "Stage", 
        "tick_interval": 6,
        "description": "This dataset contains the death-to-birth rates at Vienna General Hospital from January 1841 to March 1849. By dividing the dataset according to "
        "the implementation of Ignaz Semmelweis's handwashing policy, the impact of the policy is qualitatively and quantitaively visualized. "
        "To learn more about this dataset and the work of Ignaz Semmelweis read [The Virus of Variation: Making Sense of Death and Data using Process Behavior Charts](https://www.brokenquality.com/book)."
        },
    "wafer_assembly_part_placement.csv": {
        "name": "Wafer Assembly Part Placement",
        "data": "X position", 
        "label": "Sample", 
        "stage": "Stage", 
        "tick_interval": 10,
        "description": "This dataset contains part placement measurements from an automated pick-and-place manufacturing line. The values provided "
        "are the x-coordinates for wafer placement relative to a welded plate assembly."
        },
}