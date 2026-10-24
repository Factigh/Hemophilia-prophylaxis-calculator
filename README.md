# Hemophilia Prophylaxis Calculator

A console-based Python program that processes hemophilia patients one by one. It classifies disease severity, decides whether prophylaxis should be applied, calculates the medication dose, works out the vial combination, estimates the cost, and prints a summary report for the whole patient group.

> **Note:** This was my first project in the Algorithms and Programming course. The scenario and rules come from the course assignment. It is an educational program and is **not** meant for real clinical use.

## What it does

For every patient entered, the program:

1. Collects the data: ID, name/surname, deficient factor (8 or 9), factor level (%), antibody amount (BU), and, when needed, bleeding episodes in the past year, weight and medication type.
2. Validates the input (factor must be 8 or 9, factor level between 0 and 50, no negative values, medication type must be P/R).
3. Classifies the disease:
   - Factor 8 deficiency → **Hemophilia A**, Factor 9 deficiency → **Hemophilia B**
   - Factor level < 1% → **Severe**, 1–5% → **Moderate**, above 5% → **Mild**
   - Antibody amount ≥ 5 BU → **inhibitor present**
4. Decides on prophylaxis:
   - Severe and no inhibitor → prophylaxis
   - Moderate, no inhibitor, and at least 3 bleeding episodes per month on average → prophylaxis
   - Everyone else → no prophylaxis
5. For prophylaxis patients, calculates:
   - **Dose per administration**
     - Factor 8: `(40 - factor level) / 2 × weight` IU, 3 times a week
     - Factor 9: `(40 - factor level) × weight` IU, 2 times a week
   - **Vial combination** using 2000, 1500, 1000, 500 and 250 IU vials, rounding the dose up to the nearest suitable vial
   - **4-week requirement** in IU and vials (12 doses for Factor 8, 8 doses for Factor 9)
   - **4-week cost**: $0.30 per IU for plasma-derived, $0.40 per IU for recombinant medication

## Summary report

After the last patient, the program prints:

- Number of Hemophilia A / B patients and total patients
- Number and percentage of severe, moderate and mild patients
- Inhibitor percentage for Hemophilia A and B
- Number and percentage of patients receiving prophylaxis (A and B), and the share of moderate patients among them
- Plasma-derived vs. recombinant usage percentages for A and B
- Total IU and vial counts for plasma-derived / recombinant Factor 8 and Factor 9 (4 weeks)
- Total medication cost for 4 weeks and for 1 year (13 four-week periods)
- Average annual medication amount and cost per prophylaxis patient
- The Hemophilia A patient and the Hemophilia B patient with the highest 4-week medication amount
- The patient with the highest 4-week medication cost

## How to run

Requires Python 3.6 or newer (uses f-strings). No external libraries.

```bash
python hemophilia_calculator.py
```

The program keeps asking for new patients until you answer `n` / `N` to "Is there any more patient?".

## Example (single patient)

Input:

```
Enter ID 1
Enter name and surname Ali Yilmaz
Enter deficient factor protein(8/9) 8
Enter factor level (%) 0.5
Enter antibody amount 2
Enter weight 70
Enter medication type (Plasma-derived/Recombinant): (P/p/R/r) P
```

Resulting values:

```
Severity of disease: Severe
Prophylaxis will be applied
Factor-8 will be used
Will be taken 3 times a week
Minimum required dose of medication at one time: 1382.50 IU
Amount of medication to be used at one time: 1500 IU
Number of 1500s vial needed: 1
Total amount of medication for 4 weeks: 18000 IU
Total medication cost for 4 weeks: $5400.00
```

## Known limitations

- The final report divides by group sizes, so it needs enough data to run. To get the full report, enter at least one Hemophilia A and one Hemophilia B patient, at least one moderate patient, and at least one prophylaxis patient of each type. Otherwise the program ends with a `ZeroDivisionError`.
- The code is written as one long script with many repeated blocks (especially the vial counting and totals). A natural next step is refactoring it into functions and using dictionaries/lists for the vial sizes.
- All data is entered by hand; nothing is saved to a file or database.

## Concepts practiced

Loops and input validation, conditional logic with many rules, counters and accumulators, formatted output, running totals and finding maximums.
