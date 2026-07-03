# Test Cases — Automation Exercise

---

## UI Test Cases

### Login / Logout

| ID | Description | Preconditions | Expected Result |
|----|-------------|---------------|-----------------|
| UI_LO01 | Do a successful login | Registered user in the DB | User should be redirected to HomePage. "Logged in as *username*" text should be displayed in BasePage header. "Signup/Login" link should be replaced with "Logout" and "Delete Account" |
| UI_LO02 | Attempt to login with no email / password (parametrized) | Registered user in the DB | A browser validation tooltip prompting the user to complete the field should be displayed |
| UI_LO03 | Attempt to login with wrong credentials | Registered user in the DB | "Your email or password is incorrect!" message should be displayed |
| UI_LO04 | Do a successful logout | User is logged in | User should be redirected to LoginPage. "Logged in as *username*" text should not be displayed. "Logout" and "Delete Account" links should be replaced with "Signup/Login" |

### Register

| ID | Description | Preconditions | Expected Result |
|----|-------------|---------------|-----------------|
| UI_RE01 | Register a new user | — | /account_created page is displayed |
| UI_RE02 | Attempt to register with an existing email | Registered email in the DB | "Email Address already exist!" text is displayed |

### Delete Account

| ID | Description | Preconditions | Expected Result |
|----|-------------|---------------|-----------------|
| UI_DE01 | Delete the user | User is logged in | User should be redirected to /delete_account page. "Account Deleted!" text is displayed with a "Continue" button |

### Navigation

| ID | Description | Preconditions | Expected Result |
|----|-------------|---------------|-----------------|
| UI_NA01 | Navigate to Women > Dress category (parametrized for all 7 categories) | — | Category page should be displayed. Only products matching the selected category should be displayed |
| UI_NA02 | Navigate to a brand section (parametrized) | — | /brand_products/*brand* page should be displayed. Only products for the selected brand should be displayed |
| UI_NA03 | Navigate to a product detail | — | Product detail page is displayed |

### Subscription

| ID | Description | Preconditions | Expected Result |
|----|-------------|---------------|-----------------|
| UI_SU01 | Verify subscription in Home / Cart pages (parametrized) | — | "You have been successfully subscribed!" message is displayed |

### Product Detail

| ID | Description | Preconditions | Expected Result |
|----|-------------|---------------|-----------------|
| UI_PD01 | Write a review on a product detail page | — | "Thank you for your review." text is displayed |

### Products

| ID | Description | Preconditions | Expected Result |
|----|-------------|---------------|-----------------|
| UI_PR01 | Search for an existing product | — | Only products matching the search terms should be displayed |
| UI_PR02 | Search for a non-existing product | — | No products should be displayed in the results |

### Cart

| ID | Description | Preconditions | Expected Result |
|----|-------------|---------------|-----------------|
| UI_CA01 | Add a product to cart from HomePage / ProductsPage, then login (parametrized) | Registered user in the DB | Product should be added to the cart and remain in the cart after login |
| UI_CA02 | Add to cart from Recommended items | — | Product is added to the cart |
| UI_CA03 | Add the same product to cart multiple times | — | Product count in cart should reflect the amount added |
| UI_CA04 | Add multiple products to cart from product detail page | — | Products should be added to the cart |
| UI_CA05 | Remove a product from cart | At least one product in cart | Product should be removed from cart |
| UI_CA06 | Verify empty cart | — | "Cart is empty! Click here to buy products." message is displayed. "Here" links to ProductsPage |

### Checkout

| ID | Description | Preconditions | Expected Result |
|----|-------------|---------------|-----------------|
| UI_CH01 | Attempt to checkout without being signed in | At least one product in cart | A pop-up prompting the user to login to complete the purchase should be displayed |
| UI_CH02 | Verify the address details in checkout | User is logged in, at least one product in cart | The details should match the account details |
| UI_CH03 | Verify the total amount in checkout | User is logged in, at least one product in cart | The total amount should match the sum of (price × quantity) for all items in cart |

### Payment

| ID | Description | Preconditions | Expected Result |
|----|-------------|---------------|-----------------|
| UI_PY01 | Complete an order | User is logged in, at least one product in cart | /payment_done page should be displayed |
| UI_PY02 | Download order invoice after successful order | User is logged in, order completed | A .txt invoice with the message "Hi *username*, Your total purchase amount is *totalamount*. Thank you" is downloaded |
| UI_PY03 | Attempt to complete payment with an empty field in card details | User is logged in, at least one product in cart | A browser validation tooltip prompting the user to complete the field should be displayed |

### Contact Us

| ID | Description | Preconditions | Expected Result |
|----|-------------|---------------|-----------------|
| UI_CT01 | Submit a contact message | — | "Success! Your details have been submitted successfully." message is displayed |
| UI_CT02 | Attempt to submit a contact message with blank email | — | A browser validation tooltip prompting the user to complete the field should be displayed |

### End to End

| ID | Description | Preconditions | Expected Result |
|----|-------------|---------------|-----------------|
| UI_E2E01 | Login → Search product → Add to cart → Checkout → Payment → Download invoice | Registered user in the DB | A .txt invoice with the message "Hi *username*, Your total purchase amount is *totalamount*. Thank you" is downloaded |
| UI_E2E02 | Browse product → Add to cart → Attempt checkout (not logged in) → Register → Checkout → Payment → Delete Account | — | User should be redirected to /delete_account page. "Account Deleted!" text is displayed with a "Continue" button |

---

## API Test Cases

### Products List

| ID | Description | URL | Method | Parameters | Expected Status | Expected Response |
|----|-------------|-----|--------|------------|-----------------|-------------------|
| API_PL01 | Get all products list | /api/productsList | GET | — | 200 | All products list |
| API_PL02 | POST to all products list (method not supported) | /api/productsList | POST | — | 405 | "This request method is not supported." |

### Brands List

| ID | Description | URL | Method | Parameters | Expected Status | Expected Response |
|----|-------------|-----|--------|------------|-----------------|-------------------|
| API_BR01 | Get all brands list | /api/brandsList | GET | — | 200 | All brands list |
| API_BR02 | PUT to all brands list (method not supported) | /api/brandsList | PUT | — | 405 | "This request method is not supported." |

### Search

| ID | Description | URL | Method | Parameters | Expected Status | Expected Response |
|----|-------------|-----|--------|------------|-----------------|-------------------|
| API_SR01 | Search for an existing product | /api/searchProduct | POST | search_product | 200 | Matching products list |
| API_SR02 | Search without search_product parameter | /api/searchProduct | POST | — | 400 | "Bad request, search_product parameter is missing in POST request." |

### Auth / Login

| ID | Description | URL | Method | Parameters | Expected Status | Expected Response |
|----|-------------|-----|--------|------------|-----------------|-------------------|
| API_AU01 | Verify login with valid credentials | /api/verifyLogin | POST | email, password | 200 | "User exists!" |
| API_AU02 | Verify login without email parameter | /api/verifyLogin | POST | password | 400 | "Bad request, email or password parameter is missing in POST request." |
| API_AU03 | DELETE to verify login (method not supported) | /api/verifyLogin | DELETE | — | 405 | "This request method is not supported." |
| API_AU04 | Verify login with invalid credentials | /api/verifyLogin | POST | email, password (invalid) | 404 | "User not found!" |

### User Account

| ID | Description | URL | Method | Parameters | Expected Status | Expected Response |
|----|-------------|-----|--------|------------|-----------------|-------------------|
| API_US01 | Create / register user account | /api/createAccount | POST | name, email, password, title, birth_date, birth_month, birth_year, firstname, lastname, company, address1, address2, country, zipcode, state, city, mobile_number | 201 | "User created!" |
| API_US02 | Delete user account | /api/deleteAccount | DELETE | email, password | 200 | "Account deleted!" |
| API_US03 | Update user account | /api/updateAccount | PUT | name, email, password, title, birth_date, birth_month, birth_year, firstname, lastname, company, address1, address2, country, zipcode, state, city, mobile_number | 200 | "User updated!" |
| API_US04 | Get user account detail by email | /api/getUserDetailByEmail | GET | email | 200 | User detail |

---

> **Notes**
>
> **UI**
> - UI_LO02, UI_PY03, UI_CT02: browser-level validation (native tooltip). Low priority — does not test application logic.
> - UI_NA01: parametrized to cover all 7 categories (Women: Dress, Tops, Saree / Men: Tshirts, Jeans / Kids: Dress, Tops & Shirts).
> - UI_NA02, UI_SU01, UI_CA01: parametrized as noted in description.
> - Cart quantity field appears editable in the UI but does not respond to interaction. Not covered in this suite.
> - Payment tests use test card data accepted by the site's sandbox environment.
> - User creation and deletion for test setup/teardown will be handled via API (API_US01, API_US02) where possible.
>
> **API**
> - No endpoint available to add products to cart. Cart state for UI tests must be prepared through UI navigation or fixtures.
> - API_US01 and API_US02 are candidates for use in UI test fixtures (setup/teardown) to avoid dependency on UI registration flow.
