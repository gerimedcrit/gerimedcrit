import pandas as pd
from datetime import datetime

# Sample data for Midodrine studies
data = {
    'medication_name': [
        'Midodrine', 'Midodrine', 'Midodrine', 'Midodrine', 'Midodrine'
    ],
    'study_id': ['001', '002', '003', '004', '005'],
    'study_name': [
        'Efficacy and Safety of Midodrine in Patients with Orthostatic Hypotension',
        'Randomized Double-Blind Placebo-Controlled Trial of Midodrine in NOH',
        'Long-Term Safety of Midodrine in Neurogenic Orthostatic Hypotension',
        'Midodrine vs Placebo in Autonomic Failure: A Comparative Study',
        'Effects of Midodrine on Cognitive Function in Orthostatic Hypotension'
    ],
    'year': [2015, 2017, 2019, 2021, 2023],
    'month': [3, 6, 9, 2, 11],
    'day': [15, 10, 22, 14, 5],
    'study_type': [
        'RCT', 'RCT', 'Open-label Follow-up', 'RCT', 'RCT'
    ],
    'brief_description': [
        'Phase 3 randomized controlled trial demonstrating efficacy of midodrine for orthostatic hypotension symptoms.',
        'Placebo-controlled study showing significant improvement in standing systolic blood pressure.',
        'Extended follow-up data on safety and tolerability over 24 months of treatment.',
        'Head-to-head comparison of midodrine dosing strategies in autonomic failure patients.',
        'Novel assessment of cognitive outcomes in patients with orthostatic hypotension treated with midodrine.'
    ],
    'authors': [
        'Low PA, et al.',
        'Kaufmann H, et al.',
        'Biaggioni I, et al.',
        'Freeman R, et al.',
        'Grubb BP, et al.'
    ],
    'journal': [
        'American Journal of Medicine',
        'Journal of Autonomic Nervous System',
        'Clinical Autonomic Research',
        'Hypertension',
        'Neurology'
    ],
    'sample_size': [120, 95, 85, 110, 75],
    'primary_outcome': [
        'Change in standing systolic blood pressure',
        'Symptom relief as measured by OHSA scale',
        'Adverse event rate and blood pressure stability',
        'Blood pressure response by dose cohort',
        'Cognitive function measured by MMSE'
    ],
    'results_summary': [
        'Midodrine significantly improved standing systolic BP (p<0.001). Mean increase of 15 mmHg vs 2 mmHg placebo. Adverse events were mild and transient.',
        'Primary endpoint met with 70% symptom improvement in midodrine group vs 25% in placebo (p<0.0001). Well tolerated across all doses.',
        'Safety confirmed with consistent BP improvements maintained over 24-month period. No serious adverse events reported.',
        'Dose-response relationship demonstrated with optimal benefit at 10mg TID. No plateau effect observed.',
        'Cognitive function stable or improved in midodrine group. Orthostatic intolerance improvements correlated with symptom relief.'
    ],
    'citation': [
        'Low PA, Gilden JL, Freeman R, et al. Efficacy of midodrine vs placebo in neurogenic orthostatic hypotension. JAMA. 2015;277(13):1046-1051.',
        'Kaufmann H, Freeman R, Biaggioni I, et al. Efficacy and safety of midodrine in neurogenic orthostatic hypotension. American Journal of Medicine. 2017;130(5):547-555.',
        'Biaggioni I, Freeman R, Kaufmann H, et al. Long-term efficacy and safety of midodrine in neurogenic orthostatic hypotension. Clinical Autonomic Research. 2019;29(2):119-127.',
        'Freeman R, Wieling W, Axelrod FB, et al. Consensus statement on the definition of orthostatic hypotension. Hypertension. 2021;77(2):e30-e42.',
        'Grubb BP, Karabin B, Koceja D, et al. The effects of midodrine on cognitive function in orthostatic hypotension. Neurology. 2023;100(11):e1234-e1242.'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
output_file = 'midodrine_studies.xlsx'
df.to_excel(output_file, index=False)

print(f"✓ Sample data file created: {output_file}")
print(f"✓ Contains {len(df)} studies for Midodrine")
print(f"\nYou can now run:")
print(f"  python excel_to_html_timeline.py {output_file}")
