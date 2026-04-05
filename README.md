# AdNabu QA Assessment

This repository contains:

1. Test cases for:
   - Product Search
   - Add to Cart

2. Selenium automation for one scenario:
   - Search for a product and add it to cart successfully

---

## Tech Stack

- Python
- Selenium
- WebDriver Manager
- Eclipse (PyDev)

---

## Scenario Automated

The following happy-path scenario is automated:

1. Open the store
2. Enter the store password
3. Search for a product
4. Open product details page
5. Add product to cart
6. Verify product is added successfully

---

## Project Files

- `test_search_add_to_cart.py` → Automation script
- `test_cases.md` → Manual test cases
- `requirement.txt` → Required Python dependencies

---

## Setup Instructions

### 1. Clone the repository

git clone https://github.com/Chandrawanshi-Aniket/adnabu-qa-assessment.git  

cd adnabu-qa-assessment

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Run the script

python Assessment/test_search_add_to_cart.py
