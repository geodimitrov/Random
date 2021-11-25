def potatoes(initial_perc, initial_weight, outcome_perc):
    # Get the non-water weight (in kg) which is static and won't change
    dry_matter_weight = initial_weight * ((100 - initial_perc) / 100)

    # Calc the weight after drying by applying the outcome percentage
    outcome_weight = dry_matter_weight / ((100 - outcome_perc) / 100)
