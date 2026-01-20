import pandas as pd
import json
import os
from datetime import datetime

def excel_to_timeline(excel_file):
    """
    Convert Excel file with medication studies to HTML timeline pages
    """
    
    # Read Excel file
    print(f"Reading {excel_file}...")
    df = pd.read_excel(excel_file)
    
    # Get medication name from first row
    medication_name = df['medication_name'].iloc[0]
    medication_slug = medication_name.lower().replace(' ', '_')
    
    print(f"Processing {medication_name}...")
    
    # Create output directories if they don't exist
    os.makedirs('medications', exist_ok=True)
    os.makedirs('studies', exist_ok=True)
    os.makedirs('data', exist_ok=True)
    
    # Generate timeline data JSON
    timeline_data = generate_timeline_json(df, medication_name)
    json_file = f'data/{medication_slug}_timeline.json'
    with open(json_file, 'w') as f:
        json.dump(timeline_data, f, indent=2)
    print(f"Created {json_file}")
    
    # Generate medication timeline page
    timeline_html = generate_timeline_page(df, medication_name, medication_slug)
    timeline_file = f'medications/{medication_slug}.html'
    with open(timeline_file, 'w') as f:
        f.write(timeline_html)
    print(f"Created {timeline_file}")
    
    # Generate individual study pages
    for idx, row in df.iterrows():
        study_html = generate_study_page(row, medication_name)
        study_file = f"studies/study_{row['study_id']}.html"
        with open(study_file, 'w') as f:
            f.write(study_html)
    print(f"Created {len(df)} study pages")
    
    print(f"\n✓ Successfully generated timeline for {medication_name}!")
    print(f"  - Timeline page: {timeline_file}")
    print(f"  - Data file: {json_file}")
    print(f"  - Study pages: {len(df)} files in studies/ folder")

def generate_timeline_json(df, medication_name):
    """
    Convert DataFrame to TimelineJS compatible JSON format
    """
    events = []
    
    for idx, row in df.iterrows():
        event = {
            "start_date": {
                "year": str(row['year']),
                "month": str(row.get('month', '')),
                "day": str(row.get('day', ''))
            },
            "text": {
                "headline": row['study_name'],
                "text": f"<p>{row['brief_description']}</p><p><a href='../studies/study_{row['study_id']}.html'>View full details →</a></p>"
            },
            "group": row.get('study_type', 'Clinical Trial')
        }
        events.append(event)
    
    timeline_json = {
        "title": {
            "text": {
                "headline": f"{medication_name} Evidence Timeline",
                "text": "<p>Clinical trial evidence and key milestones</p>"
            }
        },
        "events": events
    }
    
    return timeline_json

def generate_timeline_page(df, medication_name, medication_slug):
    """
    Generate the main timeline HTML page for a medication
    """
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{medication_name} Timeline - Gerimedcrit</title>
    <link rel="stylesheet" href="../css/style.css">
    <link title="timeline-styles" rel="stylesheet" href="https://cdn.knightlab.com/libs/timeline3/latest/css/timeline.css">
    <script src="https://cdn.knightlab.com/libs/timeline3/latest/js/timeline.js"></script>
</head>
<body>
    <header>
        <h1>Gerimedcrit</h1>
        <nav>
            <ul>
                <li><a href="../index.html">Home</a></li>
                <li><a href="../timelines.html">Medication Timelines</a></li>
                <li><a href="../about.html">About</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section>
            <h2>{medication_name} Evidence Timeline</h2>
            <p>Interactive timeline of clinical trials and key evidence for {medication_name}.</p>
            <p><strong>Total studies tracked:</strong> {len(df)}</p>
        </section>

        <section>
            <div id='timeline-embed' style="width: 100%; height: 600px"></div>
        </section>

        <section>
            <h3>All Studies</h3>
            <ul>
"""
    
    # Add list of all studies
    for idx, row in df.iterrows():
        html += f"""                <li>
                    <strong>{row['year']} - {row['study_name']}</strong><br>
                    {row['brief_description']}<br>
                    <a href="../studies/study_{row['study_id']}.html">View details →</a>
                </li>
"""
    
    html += f"""            </ul>
        </section>
    </main>

    <footer>
        <p>&copy; 2026 Gerimedcrit</p>
    </footer>

    <script type="text/javascript">
        // Load timeline data
        fetch('../data/{medication_slug}_timeline.json')
            .then(response => response.json())
            .then(data => {{
                window.timeline = new TL.Timeline('timeline-embed', data);
            }})
            .catch(error => console.error('Error loading timeline:', error));
    </script>
</body>
</html>
"""
    return html

def generate_study_page(row, medication_name):
    """
    Generate individual study detail page
    """
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{row['study_name']} - Gerimedcrit</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <header>
        <h1>Gerimedcrit</h1>
        <nav>
            <ul>
                <li><a href="../index.html">Home</a></li>
                <li><a href="../timelines.html">Medication Timelines</a></li>
                <li><a href="../about.html">About</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section>
            <p><a href="../medications/{medication_name.lower().replace(' ', '_')}.html">← Back to {medication_name} Timeline</a></p>
            <h2>{row['study_name']}</h2>
            <p><strong>Year:</strong> {row['year']}</p>
            <p><strong>Study Type:</strong> {row.get('study_type', 'N/A')}</p>
        </section>

        <section>
            <h3>Study Overview</h3>
            <p>{row['brief_description']}</p>
        </section>

        <section>
            <h3>Key Details</h3>
            <ul>
                <li><strong>Authors:</strong> {row.get('authors', 'N/A')}</li>
                <li><strong>Journal/Source:</strong> {row.get('journal', 'N/A')}</li>
                <li><strong>Sample Size:</strong> {row.get('sample_size', 'N/A')}</li>
                <li><strong>Primary Outcome:</strong> {row.get('primary_outcome', 'N/A')}</li>
            </ul>
        </section>

        <section>
            <h3>Results</h3>
            <p>{row.get('results_summary', 'Details to be added.')}</p>
        </section>

        <section>
            <h3>Citation</h3>
            <p>{row.get('citation', 'Citation to be added.')}</p>
        </section>
    </main>

    <footer>
        <p>&copy; 2026 Gerimedcrit</p>
    </footer>
</body>
</html>
"""
    return html

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python excel_to_html_timeline.py <excel_file.xlsx>")
        print("\nExample: python excel_to_html_timeline.py midodrine_studies.xlsx")
        sys.exit(1)
    
    excel_file = sys.argv[1]
    
    if not os.path.exists(excel_file):
        print(f"Error: File '{excel_file}' not found!")
        sys.exit(1)
    
    excel_to_timeline(excel_file)
