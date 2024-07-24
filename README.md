# Web Scraper

## Overview

This script scrapes job postings from a specific webpage (in this case, a thread from Y Combinator) and counts the occurrences of certain keywords (programming languages and technologies). The results are then displayed in a bar graph.

## Requirements

- Python 3.x
- Libraries (`requests`, `beautifulsoup4`, `matplotlib`)

## Installation

1. Clone the repository or download the script.
2. Install the required libraries using pip:
    ```sh
    pip install requests beautifulsoup4 matplotlib
    ```

## Usage

1. Open the script file.
2. Change the `url` variable to the desired webpage (it is recommended to stick to one of the threads from Y Combinator; see the Notes section for further details). Make sure to update the `class_` parameter in the `soup.find_all` method accordingly if necessary.
3. Run the script:
    ```sh
    python script_name.py
    ```

## Notes

- Currently, changing the `url` to another website like Indeed or LinkedIn results in a 403 error (requested resource is forbidden). These websites are more complex and have stricter security protocols for retrieving information. Consider looking into Selenium to overcome these roadblocks.
- This project was inspired by pixegami.
