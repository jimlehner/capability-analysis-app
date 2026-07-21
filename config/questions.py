# questions.py
dataset_questions = {
    # Automated Manufacturing Line Part Lengths
    "automated_manufacturing_part_lengths.csv": [
        {
            "question": "Based on the XmR chart of part lengths, how would you characterize the behavior of this process?",
            "options": ["Predictable, all points are within the process limits", 
                        "Unpredictable, multiple values fall outside the process limits", 
                        "Based on the information provided I can't say"],
            "answer": "Unpredictable, multiple values fall outside the process limits",
            "explanation": "With several values falling outside the process limits the process is characterized as unpredictable.",
            "key": "auto_mfg_q1"
        },
        {
            "question": "Based on the XmR chart of part lengths, how many values are equal to the Lower Process Limit (LPL)?",
            "options": ["There is 1 value equal to the LPL",
                        "There is 1 value greater than the UPL", 
                        "There are 5 values equal to the LPL", 
                        "There are 4 values equal to the LPL"],
            "answer": "There are 4 values equal to the LPL",
            "explanation": "There are 4 values equal to the LPL of zero.",
            "key": "auto_mfg_q1a"
        },
        {
            "question": "Based on the XmR chart of part lengths, how many moving ranges are greater than the Upper Range Limit (URL)?",
            "options": ["There is 1 moving range greater than the URL",
                        "There is 1 moving range greater than the UPL", 
                        "There are 5 moving ranges greater than the URL", 
                        "There are 4 moving ranges equal to the URL"],
            "answer": "There is 1 moving range greater than the URL",
            "explanation": "There is 1 moving range greater than the URL.",
            "key": "auto_mfg_q1b"
        },
        {
            "question": "What does a value outside of the limits indicate?",
            "options": ["Only common causes of routine variation influence process behavior", 
                        "Only assignable causes of exceptional variation influence process behavior", 
                        "Both common causes of routine variation and assignable causes of exceptional variation influence process behavior", 
                        "It doesn't indicate anything"],
            "answer": "Both common causes of routine variation and assignable causes of exceptional variation influence process behavior",
            "explanation": "When one or more values fall outside the process limits it indicates that both common causes of routine variation and assignable causes of exceptional"
            "variation influence process behavior.",
            "key": "auto_mfg_q2"
        },
        {
            "question": "How is the X chart different from the mR chart?",
            "options": ["The X chart plots moving ranges, while the mR chart plots the individual values (actual observations)", 
                        "The X chart plots the individual values (actual observations), while the mR chart plots the moving ranges", 
                        "There is no difference—they plot the same thing", 
                        "They both plot the same thing"],
            "answer": "The X chart plots the individual values (actual observations), while the mR chart plots the moving ranges",
            "explanation": "The X chart plots the individual values, which are the actual observations or measurements, while the mR chart plots "
            "the absolute value of the difference between individual values called the moving ranges.",
            "key": "auto_mfg_q2a"
        },
        {
            "question": "What actions should be taken to improve this process?",
            "options": ["Mitigate the influence of common causes of routine variation", 
                        "Eliminate the influence of assignable causes of exceptional variation", 
                        "Nothing, this process is fine", "Based on the information provided I can't say"],
            "answer": "Eliminate the influence of assignable causes of exceptional variation",
            "explanation": "Although assignable causes are few in number they are dominant in their effect. Thus, improvement of this process requires the "
            "elimination of assignable causes."
            "variation influence process behavior.",
            "key": "auto_mfg_q3"
        },
    ],

    # Manufacturing PMI
    "manufacturing_PMI.csv": [
        {
            "question": "Based on the XmR chart of monthly manufacturing PMIs, how would you characterize the behavior of this process?",
            "options": ["Unpredictable, multiple values fall outside the process limits", 
                        "Predictable, all points are within the process limits", 
                        "Based on the information provided I can't say"],
            "answer": "Unpredictable, multiple values fall outside the process limits",
            "explanation": "With 1 value greater than the UPL, the process is characterized as unpredictable.",
            "key": "auto_mfg_q4"
        },
        {
            "question": "Based on the XmR chart of monthly manufacturing PMIs, how many moving ranges are greater than the Upper Range Limit (URL)?",
            "options": ["There is 1 moving range greater than the URL", 
                        "0, none of the moving ranges is greater than the URL",
                        "There are 4 values greater than the URL",
                        "Based on the information provided I can't say"],
            "answer": "0, none of the moving ranges is greater than the URL",
            "explanation": "Although one of the individual values on the X chart is greater than the UPL, none of the moving ranges on the mR chart "
            "are greater than the URL.",
            "key": "auto_mfg_q4a"
        },
        {
            "question": "What does the XmR chart of manufacturing PMIs indicate about process behavior?",
            "options": ["It indicates that only common causes of routine variation influence process behavior", 
                        "It indicates that only assignable causes of exceptional variation influence process behavior", 
                        "It doesn't indicate anything", 
                        "It indicates that both common causes of routine variation and assignable causes of exceptional variation influence process behavior"],
            "answer": "It indicates that both common causes of routine variation and assignable causes of exceptional variation influence process behavior",
            "explanation": "With one value greater than the UPL this process is influenced by both common and assignable causes.",
            "key": "auto_mfg_q5"
        },
        {
            "question": "What actions should be taken to improve this process, if any?",
            "options": ["Mitigate the influence of common causes of routine variation", 
                        "Eliminate the influence of assignable causes of exceptional variation", 
                        "Understand what caused the increase in manufacturing PMI",
                        "Based on the information provided I can't say"],
            "answer": "Understand what caused the increase in manufacturing PMI",
            "explanation": "An increase in manufacturing PMI is an indicator that the manufacturing sector is expanding. Thus, efforts should "
            "be made to understand the underlying "
            "cause of the expansion so that they can be reinforced.",
            "key": "auto_mfg_q6"
        },
    ],

    # Millikan's electron charge observations
    "millikans_electron_charge_observations.csv": [
        {
            "question": "Based on the XmR chart of Millikan's electron charge observations, how would you characterize the behavior of this process?",
            "options": ["Predictable, all points are within the process limits", 
                        "Unpredictable, multiple values fall outside the process limits", 
                        "Based on the information provided I can't say"],
            "answer": "Predictable, all points are within the process limits",
            "explanation": "With all values falling inside the process limits, the process is characterized as predictable.",
            "key": "auto_mfg_q7"
        },
        {
            "question": "What is the Upper Process Limit of Millikan's electron charge observations (to 4 decimal places)? "
            "Hint: Under the 'XmR Chart Display Controls' dropdown menu you can change the number of decmial places that are displayed with the 'Number of Decimal Places'"
            " input.",
            "options": ["The UPL is 0.0187 coulombs",
                        "The UPL is 4.8301 coulombs", 
                        "The UPL is 4.7308 coulombs", 
                        "The UPL is 0.0610 coulombs"],
            "answer": "The UPL is 4.8301 coulombs",
            "explanation": "The UPL is 4.8301 coulombs.",
            "key": "auto_mfg_q7a"
        },
        {
            "question": "What is the Upper Range Limit for the moving ranges associated with Millikan's electron charge observations (to 5 decimal places)? "
            "Hint: Under the 'XmR Chart Display Controls' dropdown menu you can change the number of decmial places that are displayed with the 'Number of Decimal Places'"
            " input.",
            "options": ["The URL is 0.01867 coulombs",
                        "The URL is 4.83012 coulombs", 
                        "The URL is 4.73081 coulombs", 
                        "The URL is 0.06100 coulombs"],
            "answer": "The URL is 0.06100 coulombs",
            "explanation": "The URL is 0.06100 coulombs.",
            "key": "auto_mfg_q7b"
        },
        {
            "question": "When all of the values fall within the process limits, what does this indicate about future process behavior?",
            "options": ["It indicates that assignable causes must be eliminated",
                        "It indicates that future behavior cannot be predicted within limits", 
                        "It doesn't indicate anything", 
                        "It indicates that future behavior can be predicted within the process limits"],
            "answer": "It indicates that future behavior can be predicted within the process limits",
            "explanation": "When all of the values on an XmR chart fall within the process limits, it indicates that future behavior can be predicted within those limits.",
            "key": "auto_mfg_q8"
        },
        {
            "question": "What actions (if any) should be taken to improve this process?",
            "options": ["Mitigate the influence of common causes of routine variation", 
                        "Eliminate the influence of assignable causes of exceptional variation", 
                        "Nothing, this process cannot be improved because it is observations (measurements) of a naturally occuring phenomenon", 
                        "Based on the information provided I can't say"],
            "answer": "Nothing, this process cannot be improved because it is observations (measurements) of a naturally occuring phenomenon",
            "explanation": "When a mechanical (or man made) process is influenced by only common causes of routine variation, improvement is only possible through reengineering "
            "(i.e., new technology, new techniques, "
            "new methods, and new materials). However, in this case, further improvement is not possible because Millikan was measuring a naturally occuring phenomenon. While improvements"
            " in the measurement system may increase the precision of the observations there is nothing we can do that will change the charge of electrons."
            "variation influence process behavior.",
            "key": "auto_mfg_q9"
        },
    ],

    # Monthly United States trade deficits in 2024
    "monthly_united_states_trade_deficits_2024.csv": [
        {
            "question": "Based on the XmR chart of monthly United States trade deficits in 2024, how would you characterize the behavior of this process?",
            "options": ["Predictable, all points are within the process limits", 
                        "Based on the information provided I can't say",
                        "Unpredictable, a value falls outside the process limits",
                        ],
            "answer": "Unpredictable, a value falls outside the process limits",
            "explanation": "With one value greater than the UPL the process is characterized as unpredictable.",
            "key": "auto_mfg_q10"
        },
        {
            "question": "When one or more values fall outside the process limits, what does this indicate about future process behavior?",
            "options": ["It indicates that only common causes of routine variation influence process behavior", 
                        "It indicates that only assignable causes of exceptional variation influence process behavior", 
                        "It doesn't indicate anything", 
                        "It indicates that future behavior cannot be predicted within the process limits"],
            "answer": "It indicates that future behavior cannot be predicted within the process limits",
            "explanation": "When one or more values fall outside the process limits the influence of assignable causes makes it impossible to predict "
            "future process behavior within the process limits.",
            "key": "auto_mfg_q11"
        },
        {
            "question": "Based on the XmR chart of trade deficits, what was the average monthly deficit for the observed period?",
            "options": ["The average deficit was 95.1", 
                        "The average deficit was 76.5", 
                        "The average deficit was 57.8", 
                        "The average deficit was 22.9"],
            "answer": "The average deficit was 76.5",
            "explanation": "The average deficit for the observed period was 76.5.",
            "key": "auto_mfg_q12"
        },
        {
            "question": "For the XmR chart of trade deficits, how many values are greater than the Upper Range Limit (URL)?",
            "options": ["There is 1 value greater than the UPL", 
                        "There is 1 value greater than the URL", 
                        "There are 0 values greater than the URL", 
                        "Based on the information provided I can't say"],
            "answer": "There are 0 values greater than the URL",
            "explanation": "While there is one value greater than the Upper Process Limit (UPL) on the X chart, none of the values (0) are greater than"
            "the Upper Range Limit (URL) on the mR chart.",
            "key": "auto_mfg_q12a"
        },
    ],

    # OP200 Weekly First-Pass Yield
    "OP200_weekly_first_pass_yield.csv": [
        {
            "question": "Based on the XmR chart of weekly first-pass yields, how would you characterize the behavior of this process?",
            "options": ["Predictable, all points are within the process limits", 
                        "Based on the information provided I can't say",
                        "Unpredictable, several values falls outside the process limits",
                        ],
            "answer": "Unpredictable, several values falls outside the process limits",
            "explanation": "Several values fall outside the process limits that characterize the process as unpredictable.",
            "key": "auto_mfg_q10a"
        },
        {
            "question": "When one or more values fall outside the process limits, what does this indicate about future process behavior?",
            "options": ["It indicates that only common causes of routine variation influence process behavior", 
                        "It indicates that only assignable causes of exceptional variation influence process behavior", 
                        "It doesn't indicate anything", 
                        "It indicates that future behavior cannot be predicted within the process limits"],
            "answer": "It indicates that future behavior cannot be predicted within the process limits",
            "explanation": "When one or more values fall outside the process limits the influence of assignable causes makes it impossible to predict "
            "future process behavior within the process limits.",
            "key": "auto_mfg_q11b"
        },
        {
            "question": "What was the average weekly first-pass yield for the observed period (to 2 decimal places)? Hint: You can change the number of "
            "decimals that are displayed in the 'XmR Chart Display Controls' dropdown menu.",
            "options": ["The average weekly first-pass yield was 91.02%", 
                        "The average weekly first-pass yield was 81.4%", 
                        "The average weekly first-pass yield was 81.42%", 
                        "The average weekly first-pass yield was 71.82"],
            "answer": "The average weekly first-pass yield was 81.42%",
            "explanation": "The average first-pass yield was 81.42%. However, because the process is characterized as unpredictable, this average is an "
            "inaccurate representation of what the process has done in the past and cannot be used to anticipate what it will do in the future. "
            "Only when a process is characterized as predictable does the calculated mean accurately represent past and future behavior.",
            "key": "auto_mfg_q12c"
        },
        {
            "question": "How many weekly first-pass yields are less than the Lower Process Limit (LPL)?",
            "options": ["There are 10 weekly first-pass yields that are less than the LPL", 
                        "There is 1 weekly first-pass yields that are less than the LPL", 
                        "There are 5 weekly first-pass yields that are less than the LPL", 
                        "None of the weekly first-pass yields (0) that are less than the LPL"],
            "answer": "There are 5 weekly first-pass yields that are less than the LPL",
            "explanation": "There are 5 weekly first-pass yields that are less than the LPL and 5 weekly first-pass yields that are greater than the UPL."
            "the Upper Range Limit (URL) on the mR chart.",
            "key": "auto_mfg_q12d"
        },
    ],

    # Quarterly Sales by Region
    "quarterly_sales_by_region.csv": [
        {
            "question": "Based on the XmR chart of the sales regions, how would you characterize the behavior of the sales process?",
            "options": ["Predictable, all points are within the process limits", 
                        "Based on the information provided I can't say",
                        "Unpredictable, there are many values that fall outside the process limits",
                        ],
            "answer": "Unpredictable, there are many values that fall outside the process limits",
            "explanation": "With many values falling outside the process limits, the sales process is characterized as unpredictable. With this said, "
            "evaluating all of the sales regions in a single XmR chart doesn't make much sense. It is better to evaluate each sales region on its own and with respect "
            "to the others using 'Stages'.",
            "key": "auto_mfg_q13"
        },
        {
            "question": "Click the 'Stage View & Customization' dropdown menu and select the 'Show Stages' check mark. This will divide the sales data into unique sales regions. "
            "What sales regions are predictable and what sales regions are unpredictable?",
            "options": ["All of the sales regions are characterized as unpredictable", 
                        "All of the sales regions are characterized as predictable", 
                        "Sales regions A, C, and E are predictable, while regions B, D, and F are unpredictable.", 
                        "Sales regions A, C, and E are unpredictable, while regions B, D, and F are predictable."],
            "answer": "Sales regions A, C, and E are predictable, while regions B, D, and F are unpredictable.",
            "explanation": "Sales regions A, C, and E are predictable while regions B, D, and F are unpredictable. Using a stage-based view of multiple processes that use the "
            "same quality or performance metric allows the stages to be compared directly. This makes differenes in variation between the stages more clear.",
            "key": "auto_mfg_q14"
        },
        {
            "question": "Assume you are the director managing these sales regions. Based on the stage view, what sales region needs the most attention?",
            "options": ["Region B, the sales in this region appear to be declining rapidly",
                        "Region E, the sales in this region are slow and will continue to be slow if something isn't done", 
                        "Region F, the sales in this region are unpredictable although they have grown recently", 
                        "Region A, even though the sales in this region are predictable they display a lot of variation"],
            "answer": "Region B, the sales in this region appear to be declining rapidly",
            "explanation": "The downward slope and unpredictable characterization of region B indicates that questions need to be asked.",
            "key": "auto_mfg_q15"
        },
        {
            "question": "Of the three regions that are characterized as predictable (A, C and E), which region had the highest average sales for the observed period?",
            "options": ["Region A had the highest average sales", 
                        "Region C had the highest average sales", 
                        "Region E had the highest average sales", 
                        "Based on this chart I can't tell"],
            "answer": "Region C had the highest average sales",
            "explanation": "On an XmR chart, the solid black line is the average (mean) of the process data. Since the mean line for Region C is greater than the mean line "
            "for Regions A and E it had the highest average sales for the observed period.",
            "key": "auto_mfg_q16"
        },
    ],

    # Shewhart's resistance measurements
    "shewharts_resistance_measurements.csv": [
        {
            "question": "Based on the XmR chart of resistance measurements (without 'Show Stages' selected), how would you characterize the behavior of this process?",
            "options": ["Predictable, all points are within the process limits",
                        "Unpredictable, there are many values that fall outside the process limits", 
                        "Based on the information provided I can't say",
                        ],
            "answer": "Unpredictable, there are many values that fall outside the process limits",
            "explanation": "With many values falling outside the process limits, the process is characterized as unpredictable.",
            "key": "auto_mfg_q17"
        },
        {
            "question": "Click the 'Stage View & Customization' dropdown menu and select the 'Show Stages' check mark. This will divide the resistance measurements into two stages (Initial and Additional). "
            "What is the characterization of the two stages?",
            "options": ["Both stages are characterized as unpredictable", 
                        "Both stages are characterized as predictable", 
                        "The 'Initial' stage is characterized as predictable, while the 'Additional' stage is characterized as unpredictable", 
                        "The 'Initial' stage is characterized as unpredictable, while the 'Additional' stage is characterized as predictable"],
            "answer": "The 'Initial' stage is characterized as unpredictable, while the 'Additional' stage is characterized as predictable",
            "explanation": "The 'Initial' stage is characterized as unpredictable, while the 'Additional' stage is characterized as predictable."
            " fall inside the process limits characterizing it as predictable.",
            "key": "auto_mfg_q18"
        },
        {
            "question": "What can be said about the 'Additional' resistance measurements?",
            "options": ["Because the 'Additional' resistance measurements are characterized as predictable, future process behavior can be predicted within limits",
                        "Because the 'Additional' resistance measurements are characterized as unpredictable, future process behavior cannot be predicted within limits", 
                        "Based on the information provided I can't make any statements", 
                        "Only assignable causes of exceptional variation influence process behavior"],
            "answer": "Because the 'Additional' resistance measurements are characterized as predictable, future process behavior can be predicted within limits",
            "explanation": "When a process is characterized as predictable future process behavior can be predicted within the respective process limits.",
            "key": "auto_mfg_q19"
        },
        {
            "question": "What is the Lower Process Limit (LPL) for the 'Additional' resistance measurements?",
            "options": ["The LPL is 4922.8", 
                        "The LPL is 4417.8", 
                        "The LPL is 3912.8", 
                        "Based on this chart I can't tell"],
            "answer": "The LPL is 3912.8",
            "explanation": "The LPL is 3912.8. megaohms",
            "key": "auto_mfg_q20"
        },
    ],

        # Vienna General Death-to-Birth Rates
        "vienna_general_death_to_birth_rates.csv": [
        {
            "question": "Based on the XmR chart of death-to-birth rates (without 'Show Stages' selected), how would you characterize the behavior of this process?",
            "options": ["Predictable, all points are within the process limits",
                        "Unpredictable, there are many values that fall outside the process limits", 
                        "Based on the information provided I can't say",
                        ],
            "answer": "Unpredictable, there are many values that fall outside the process limits",
            "explanation": "With many values falling outside the process limits, the process is characterized as unpredictable.",
            "key": "auto_mfg_q21"
        },
        {
            "question": "Click the 'Stage Customization' dropdown menu and select the 'Show Stages' check mark. This will divide the death-to-birth rates into stages "
            "(Before Handwashing and After handwashing). What is the characterization of the two stages?",
            "options": ["Both stages are characterized as unpredictable", 
                        "Both stages are characterized as predictable", 
                        "The 'Before' stage is characterized as predictable, while the 'After' stage is characterized as unpredictable", 
                        "The 'Before' stage is characterized as unpredictable, while the 'After' stage is characterized as predictable"],
            "answer": "Both stages are characterized as unpredictable",
            "explanation": "With multiple values falling outside the process limits for both stages, they are characterized as unpredictable.",
            "key": "auto_mfg_q22"
        },
        {
            "question": "How did the variation change between the before handwashing stage and the after handwashing stage?",
            "options": ["The variation decreased",
                        "The variation increased", 
                        "Based on the information provided I can't say", 
                        "The variation stayed the same"],
            "answer": "The variation decreased",
            "explanation": "By comparing the width of the process limits from the the two stages it is obvious that the variation "
            "decreased after handwashing was introduced.",
            "key": "auto_mfg_q23"
        },
        {
            "question": "What is the Upper Process Limit (UPL) for the 'After handwashing' stage?",
            "options": ["The UPL is 2.1%", 
                        "The UPL is 4.8%", 
                        "The UPL is 0.0%", 
                        "Based on this chart I can't tell"],
            "answer": "The UPL is 4.8%",
            "explanation": "The UPL is 4.8\% for the 'After handwashing' stage.",
            "key": "auto_mfg_q24"
        },
        {
            "question": "How many values are equal to the Lower Process Limit (LPL) for the 'After handwashing' stage?",
            "options": ["3 values are equal to the LPL for the 'After handwashing' stage", 
                        "2 values are equal to the LPL for the 'After handwashing' stage", 
                        "5 values are equal to the LPL for the 'After handwashing' stage", 
                        "None of the values (0) are equal to the LPL for the 'After handwashing' stage"],
            "answer": "2 values are equal to the LPL for the 'After handwashing' stage",
            "explanation": "2 of the values are equal to the LPL in the 'After handwashing' stage.",
            "key": "auto_mfg_q24a"
        },
    ],

    # Wafer assembly part placement
    "wafer_assembly_part_placement.csv": [
        {
            "question": "Based on the XmR chart of wafer assembly part placements (without 'Show Stages' selected), how would you characterize the behavior of this process?",
            "options": ["Predictable, all points are within the process limits",
                        "Unpredictable, there are many values that fall outside the process limits", 
                        "Based on the information provided I can't say",
                        ],
            "answer": "Unpredictable, there are many values that fall outside the process limits",
            "explanation": "With many values falling outside the process limits, the process is characterized as unpredictable.",
            "key": "auto_mfg_q25"
        },
        {
            "question": "Click the 'Stage Customization' dropdown menu and select the 'Show Stages' check mark. This will divide the wafer assembly placement data into three stages "
            "(Baseline, Initial change, Secondary change). What is the characterization of the three stages?",
            "options": ["All stages are characterized as unpredictable", 
                        "All stages are characterized as predictable", 
                        "The 'Baseline' stage and 'Initial change' stage are characterized as predictable, while the 'After' stage is characterized as unpredictable", 
                        "The 'Baseline' stage and 'Initial change' stage are characterized as unpredictable, while the 'After' stage is characterized as predictable"],
            "answer": "All stages are characterized as unpredictable",
            "explanation": "The characterization of a process is a function of both the X chart and mR chart. Thus, while the X chart of the 'Secondary change' shows"
            " all values fall within the process limits there are two values on the asssociated mR chart that are greater than the URL.",
            "key": "auto_mfg_q26"
        },
        {
            "question": "What is the Upper Process Limit (UPL) for the stage labeled 'Secondary change' (to 2 decimal places)? Hint: You can change the number of decimal places in the "
            "'XmR Chart Display Controls' dropdown menu.",
            "options": ["The UPL is 1.00",
                        "The UPL is 0.77", 
                        "The UPL is 0.48", 
                        "The UPL is 1.06"],
            "answer": "The UPL is 1.06",
            "explanation": "The UPL is 1.06 units.",
            "key": "auto_mfg_q27"
        },
        {
            "question": "What is the Upper Range Limit (URL) for the stage labeled 'Secondary change' (to 2 decimal places)?",
            "options": ["The URL is 1.06",
                        "The URL is 0.11", 
                        "The URL is 0.36", 
                        "The URL is 0.40"],
            "answer": "The URL is 0.36",
            "explanation": "The URL is 0.36 units",
            "key": "auto_mfg_q28"
        },
    ],
}