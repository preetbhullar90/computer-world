# **Computer World - Testing**

[**README.md file**](/README.md)

[**View live project**](https://preet-computer-world.herokuapp.com/)

## **Table of contents**
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


