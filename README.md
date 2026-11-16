# GitHub Activity CLI 🚀

A lightweight, easy-to-use command-line interface (CLI) tool built in Python to quickly inspect a GitHub user's public repositories or recent activity without needing to open a browser.

---

## Features

* **View Public Repositories:** Lists a user's public projects along with their descriptions and formatted names.
* **View Recent Activity:** Displays recent GitHub events (such as pushes, issues, etc.) tied to a user.
* **Customizable Limits:** Easily control how many items you want to display using the limit flag.
* **Robust Error Handling:** Gracefully handles non-existent usernames (404) and connection issues.

---

## Prerequisites

Make sure you have **Python 3.x** installed on your machine. You will also need the `requests` library.

---

## Installation

1. Clone or download this repository to your local machine.
2. Install the required dependency (`requests`):
   ```
   pip install requests

<h3>Usage</h3>
Run the script from your terminal using the following command structure:

 ```python githubCLI.py <username> [options]```




<h3>Available Arguments & Flags:</h3>
<ol>
<li>username (Required): The GitHub username you want to look up.</li>
<li>-c, --commands (Optional): Choose what to show. Options are repo (default) or event.</li>
<li>-l, --limits (Optional): Limit the number of items displayed.</li>
</ol>


