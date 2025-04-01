# Zillow Property Scraper & Form Submitter

This project automatically scrapes property listings from a Zillow clone website and submits each listing's data to a Google Form. This README provides a complete step-by-step guide to set up and run the project.

## Project Overview

This script performs the following tasks:
1. Scrapes property listings (addresses, prices, and links) from a Zillow clone website
2. Cleans the data to ensure proper formatting
3. Opens a Google Form for each listing
4. Automatically fills in the form with the listing data
5. Submits the form

## Prerequisites

Before starting, make sure you have the following installed:

- Python 3.6 or higher
- pip (Python package installer)
- Chrome browser

## Step 1: Set Up Your Environment

### Install Required Packages

Open your terminal/command prompt and run:

```bash
pip install requests beautifulsoup4 selenium
```

### Install Chrome WebDriver

1. Check your Chrome browser version:
   - Open Chrome
   - Click the three dots in the top-right corner
   - Go to Help > About Google Chrome
   - Note your version number

2. Download the matching ChromeDriver:
   - Go to [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)
   - Select the version that matches your Chrome version
   - Download the appropriate file for your operating system

3. Extract the downloaded file and note the path to the chromedriver executable

## Step 2: Create Your Google Form

1. Go to [Google Forms](https://docs.google.com/forms)
2. Create a new form with three short answer questions:
   - Property Address
   - Property Price
   - Property Link
3. After creating the form, click "Send" and copy the form link

## Step 3: Create the Python Script

Create a new file named `zillow_scraper.py` and copy the following code into it:

## Step 4: Customize the Script

Before running the script, make the following changes:

1. Replace the Google Form link:
   - Find this line: `GOOGLE_FORM_LINK = 'https://docs.google.com/forms/d/e/1FAIpQLScnAHPNrOdv_V-UvSwtaCEVLjSlXzzJMI54hWnbIOwKipaW6g/viewform'`
   - Replace it with your own Google Form link

2. If needed, adjust the CSS selectors:
   - Google occasionally updates the CSS classes for form elements
   - If the script doesn't work, you may need to update these selectors:
     - Input fields: `input.whsOnd.zHQkBf`
     - Submit button: `div.uArJ5e.UQuaGc.Y5sE8d.VkkpIf`

## Step 5: Run the Script

1. Open a terminal/command prompt
2. Navigate to the directory containing your script
3. Run the script:

```bash
python zillow_scraper.py
```

4. Watch as the script automatically:
   - Opens Chrome
   - Scrapes the property data
   - Fills out the form for each listing
   - Submits each form

## Troubleshooting

### Form Fields Not Being Found

If the input fields or submit button aren't being found:

1. Open your Google Form in Chrome
2. Right-click on the first input field
3. Select "Inspect"
4. Look for the class names of the input element
5. Update the CSS selector in the script

Same process for the submit button - inspect it and update the CSS selector.

### Timing Issues

If the script is moving too fast for your internet connection:

1. Increase the waiting times by changing the `time.sleep(2)` values to a higher number, like `time.sleep(4)`

### Chrome WebDriver Path

If the script can't find ChromeDriver:

1. Specify the path to the ChromeDriver executable in the script:
```python
driver = webdriver.Chrome(executable_path='/path/to/chromedriver', options=chrome_options)
```