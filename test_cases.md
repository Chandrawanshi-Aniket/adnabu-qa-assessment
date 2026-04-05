Task 1:
Product Search Test Cases


| Test ID | Scenario | Steps | Expected Result | Type |
|---------|----------|-------|-----------------|------|
| PS_001 | Search with valid exact product name | Enter valid product name and search | Matching product should appear | Positive |
| PS_002 | Search with partial keyword | Enter partial product keyword and search | Relevant products should appear | Positive |
| PS_003 | Search with non-existing product | Enter invalid product name and search | No results / proper message shown | Negative |
| PS_004 | Search with empty input | Leave search blank and trigger search | App handles gracefully without crash | Negative |
| PS_005 | Search with special characters | Enter special characters and search | No invalid/broken results shown | Negative |
| PS_006 | Search with very long string | Enter very long search input and search | App should remain stable and handle input | Edge |

---

Add to Cart Test Cases

| Test ID | Scenario | Steps | Expected Result | Type |
|---------|----------|-------|-----------------|------|
| AC_001 | Add in-stock product from listing page | Select available product and add to cart | Product should be added successfully | Positive |
| AC_002 | Add in-stock product from product page | Open product page and add to cart | Product should appear in cart | Positive |
| AC_003 | Add multiple quantity of same product | Increase quantity and add to cart | Correct quantity should be shown in cart | Positive |
| AC_004 | Add out-of-stock product | Attempt to add unavailable product | Product should not be added | Negative |
| AC_005 | Cart quantity for product should not be negative or zero | Attempt to manually type "0" or "-1" in the quantity field | Validation should be shown | Negative |
| AC_006 | Rapid multiple clicks on Add to Cart | Click Add to Cart repeatedly | App should handle cart consistently with correct amount | Edge |
