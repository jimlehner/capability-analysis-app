# datasets.py
dataset_columns = {
    "automated_manufacturing_part_lengths.csv": {
        "name": "Automated Manufacturing Part Lengths", 
        "data": "Value (mm)", 
        "label": "Sample", 
        "stage": None, 
        "USL": 1.3,
        "LSL": 0.7,
        "Target": 1.0,
        "tick_interval": 1,
        "description": "This dataset contains 60 part length measurements from an automated manufacturing line."
        },
    "shewharts_initial_resistance_measurements.csv": {
        "name": "Shewhart's Initial Resistance Measurements", 
        "data": "Resistance", 
        "label": "Value", 
        "stage": "Stage", 
        "USL": 5295,
        "LSL": 3395,
        "Target": 4345,
        "tick_interval": 11,
        "description": "This dataset contains two sets of electrical resistance measurements collected by Walter A. Shewhart at Bell Telephone Laboratories."
        "The first set of measurements, called the 'Initial' stage, were collected before process improvements. The second set of measurements, called the 'Additional' "
        "stage, were collected after process improvements."
        },
    "shewharts_additional_resistance_measurements.csv": {
            "name": "Shewhart's Additional Resistance Measurements", 
            "data": "Resistance", 
            "label": "Value", 
            "stage": "Stage", 
            "USL": 5295,
            "LSL": 3395,
            "Target": 4345,
            "tick_interval": 11,
            "description": "This dataset contains two sets of electrical resistance measurements collected by Walter A. Shewhart at Bell Telephone Laboratories."
            "The first set of measurements, called the 'Initial' stage, were collected before process improvements. The second set of measurements, called the 'Additional' "
            "stage, were collected after process improvements."
            },
    "wafer_assembly_part_placement.csv": {
        "name": "Wafer Assembly Part Placement",
        "data": "X position", 
        "label": "Sample", 
        "stage": "Stage", 
        "USL": 1.2,
        "LSL": 0.4,
        "Target": 0.8,
        "tick_interval": 10,
        "description": "This dataset contains part placement measurements from an automated pick-and-place manufacturing line. The values provided "
        "are the x-coordinates for wafer placement relative to a welded plate assembly."
        },
}