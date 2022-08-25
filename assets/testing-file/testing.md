# **Computer World - Testing**

[**README.md file**](/README.md)

[**View live project**](https://preet-computer-world.herokuapp.com/)

## Table of contents
1. [**Testing User Stories**](#Testing-User-Stories)
2. [**Manual File Test**](#Manual-File-Test)
3. [**Automated Testing**](#Automated-Testing)
     - [**Code Validation**](#Code-Validation)
     - [**Browser Validation**](#Browser-Validation)
     - [**Lighthouse**](#Lighthouse)

## **Testing User Stories**

### **1. Sort and Searching products:**
1. As a **shopper** I can **sort the list of all the products** so that **I can easily find the best price, high rate and sorted by product category.**
2. As a **shopper** I can **sort product by specific categories** so that **I can sort product by specific category and find best price and best rates.**


- On the right side of the product page, there is a filter button where users can find all the products sorted by category, price, and rating with one click. This filter function works with help of the jQuery. Users also can sort products by clicking on the top nav bar and then clicking on the ALL PRODUCTS link.

![](/assets/testing-file/search-image.PNG)

3. As a **shopper** I can **search a product by name or description** so that **I can easily find a specific product by name which I’d like to purchase.**
4. As a **shopper** I can **see what I’ve searched for and the number of results** so that **I can easily decide whether the product I want is available.**
- In the products view, I used the Django prebuild Query set to find any specific product by writing one word in the search bar. Query set is linked with products name and description so that when users type any word which relates to the product they will see it on the page.

![](/assets/testing-file/search-bar-image.PNG)

![](/assets/testing-file/search-bar-product-image.PNG)

[Go Top](#Table-of-contents)

### **2. Viewing and Navigation Functionality:**

1. As a **shopper** I can **view all the products** so that **I can select some products to purchase.**
- On the products page, users can see all the products on one page including the  product name, image, and price. If users like something on product page, then they can add the product straight to the basket from the product page because this function saves users times.

![](/assets/testing-file/all-products-image.PNG)

2. As a **shopper** I can **see individual product details** so that **I can see product description, price, image, and sizes.**
- By clicking on the “more details“ button in products page, users will be redirected to product’s detail page where users can see the product’s name, description, and price. In the product’s details page, users can choose the product’s size and also view more images for the product. Users can also see product dimensions and weight at the bottom of the page.

![](/assets/testing-file/product-detail-image.PNG)

3. As a **shopper** I can **identify deals and special offers** so that **I can take advantage of special savings some money on a product.**
- On the top of navbar, there is a deals button. By clicking on this button users can see all the deals of the products. It is very useful for users because some customers  just want to see products that are only on offer. They don’t need to scroll down to all products to find the deals.

![](/assets/testing-file/deal-image.PNG)

3. As a **shopper** I can **see grand total of money and all product which I selected** so that **I can save lot of time.**
- When users add products to the basket from the “All products” page or a select product’s details page, they will receive an alert message on top right-hand corner of the website noting the product name, image, price and grand total so that users can easily see the total number of the products. They can also see the grand total of the products by clicking on the basket logo.

![](/assets/testing-file/grand-total-image.PNG)
![](/assets/testing-file/grand-total-image2.PNG)

[Go Top](#Table-of-contents)

### **3. Purchase and checkout products:**

1. As a **shopper** I can **easily select a size and quantity of product** so that **I can select right size and quantity of a product when I buy it.**
- In the basket page and product details page, users can select the product size and quantity before buying any product. These functions are very useful for the users, because if users want more than one product, they can simply change the quantity of the product by one click. Otherwise, they would have to go onto the product page, find the product again, and add it to the basket. It is very complicated and waste of time, so that’s why I added this functionality to these pages.

![](/assets/testing-file/product-size-image.PNG)

2. As a **shopper** I can **easily view items in my bag** so that **I can identify the total cost of purchase.**
- Users can see the items in the bag by clicking on basket logo, or they can see an alert message with total amount of the products on top of the right-hand corner of the website. So that they can easily identify the total cost of the products before buying.

![](/assets/testing-file/shopping-bag-image.PNG)

3. As a **shopper** I can **adjust the quantity of my bag** so that **I can make any changes before buy.**
- Users can adjust the quantity of the products in the individual product’s details page and adjust in the bag. By default they will get quantity of one in the basket but if they change the quantity by clicking the plus or minus buttons, they can add or remove items from the basket before purchasing.

![](/assets/testing-file/bag-quantity-adjust-image.PNG)

4. As a **shopper** I can **add my personal payment information safe and secure** so that **I can confidently provide the information to make a purchase.**
- Users can add personal payment information on the checkout page, where they would fill a form containing details such as card details, address, and phone number. They can go through secure payment by clicking the secure payment button at the bottom of the basket page or they can go by clicking secure payment under of the alert message while they are adding a product to the basket.

![](/assets/testing-file/payment-image.PNG)

5. As a **shopper** I can **view my order confirmation after checkout** so that **I can easily see that I didn't make any mistake.**
- After the checkout, users will get an email confirmation that your payment is successful so that users can be satisfied that they have not made any mistakes during checkout.

![](/assets/testing-file/order-confirmation-image.PNG)

6. As a **shopper** I can **receive confirmation email after checkout**a so that **I can keep that email as a proof what I have brought from store.**
- When users finish checking out, they will get an email as a proof that they brought something from the website so that if something happens while delivery or there is any manufacturer fault in the item then they can show that email that contains the order number of the item as a proof.

![](/assets/testing-file/email-order-confirmation-image.PNG)

### **4. Admin and Store management:**

1. As a **shop owner** I can **add new product** so that I can **add new items to my store.**
- Once logged in as an admin superuser, the navbar displays products management. Clicking this shows the below menu:

![](/assets/testing-file/admin-image.PNG)

From here, if the user clicks `product management`, they are taken to the product management page. This page shows a form of add product with all the categories, where they can add new products.

![](/assets/testing-file/add-product-image.PNG)

2. As a **shop owner** I can **easily Edit and Update a product** so that **I can update images prices and other criteria.**
- If the admin superuser is logged in, they can edit products from the products page. At the bottom of the products, there is an edit button which can take them straight to the edit product form where they can update details for the product.

![](/assets/testing-file/edit-product-image.PNG)

![](/assets/testing-file/edit-product-image2.PNG)

3. As a **shop owner** I can **easily delete a discontinued product** so that **I can Remove items from store site.**
- When the admin superuser logged in, they can delete any product by clicking the `delete` button under every product image.

![](/assets/testing-file/edit-product-image.PNG)

[Go Top](#Table-of-contents)

### **5. User Authentication:**

1. As a **user** I can **create a personal user profile** so that **I can view my personal order and save my payment information.**
- If users are logged in, they can view their profile by clicking on their name and clicking the `profile` button on the dropdown menu.  This will redirect to the `my profile` page, where they can add their default information and can see their purchase history as well.

![](/assets/testing-file/new-account-image.PNG)
![](/assets/testing-file/new-profile-image.PNG)

2. As a **user** I can **receive a confirmation email after registering an account** so that **I can verify that my account registration was successfully.**
- When new users register on the website, they will get a confirmation email, and when they click on the verification link in the mail, they will be directed to a confirmation button. After clicking confirm, they will redirected again to the login page where they can login.

![](/assets/testing-file/account-confirm-image.PNG)

![](/assets/testing-file/account-confirmation-image.PNG)

3. As a **user** I can **recover my password in case I forget it** so that **I can recover access to my account.**
- If users forget their password, there is a password forgot button found on the login page. By clicking this button, users will be taken to the email form where they can enter their correct email to recover the password. After entering the correct email and pressing the “reset my password” button, the user will get an email. In this email they will get a link that will redirect the user to the new password page where they can reset the password.

![](/assets/testing-file/forget-password-image.PNG)

4. As a **user** I can **login or logout my account** so that **I can access my personal account information.**
- Once users are registered on the website, they can logout at any time. They can also login at any time, when they want to access their personal account information.

![](/assets/testing-file/login-image.PNG)
![](/assets/testing-file/logout-image.PNG)

5. As a **user** I can **create a personal account** so that **I can view my profile.**
- Users can buy anything as a guest, but if they create a personal account, they can see their personal details and their order history. They can also update their profile at any time.

![](/assets/testing-file/my-profile-image.PNG)

[Go Top](#Table-of-contents)