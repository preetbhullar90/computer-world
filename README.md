# Computer World

![Computer World Images](assets/testing-file/am-i-responsive.PNG)

[View the live project here](https://preet-computer-world.herokuapp.com/)

## Contents
1. [**Introduction**](#Introduction)

2. [**User Experience**](#User-Experience)

   - [**Strategy**](#strategy)
   - [**Scope**](#Scope)
   - [**Structure**](#Structure)

3. [**Database**](#Database)

4. [**Design**](#Design)

5. [Features](#Features)

6. [Bugs](#Bugs)

7. [Other Features](#Other-Features)

8. [Features Left to Implement](#Feature-Left-to-Implement)

9. [Technologies Used](#Technologies-Used)

10. [Frameworks Libraries and Programs Used](#Frameworks-Libraries-and-Programs-Used)

11. [Testing](#Testing)

    - [Testings.md](assets/testing-file/testing.md)

12. [Deployment](#Deployment)

13. [Make a clone](#Make-a-clone)

14. [Credit](#Credit)

15. [Acknowledgements](#Acknowledgements)

## **Introduction**

This is my 5th and final portfolio project at code institute. This project is designed to be an Online Computer Retailer, which allows the customer to buy computer products and components. This project is a computer shop website designed to advertise the shop and to allow the customer to buy products and components. On the website, customers can buy any product as a guest as they don’t need to register to buy any product. But if they want to save their information then they must register. This website has been deployed on Heroku.

[View the live project here](https://preet-computer-world.herokuapp.com/)

[Go Top](#Computer-World)

## **User Experience**

### **Strategy**
I will start with the Strategy - thinking about the target audience for this gallery & the features they would benefit from.

The target audience for 'Computer World' are:

- Computer Enthusiasts.
- IT Professionals.

These users will be looking for:

- Any product on the website, easy to check detail and purchase.
- All the products price, description, and new product up to date every day.
- User account functionality to view past orders and store billing information.
- Sign up newsletter for see deals, new products everyday.

### **User Stories**

Please find all my defined user stories & their acceptance criteria [here](https://github.com/preetbhullar90/computer-world/issues)

### **1. Sort and Searching products:**

- As a **shopper** I can sort the list of all the products so that I can easily find the best price, high rate and sorted by product category.
- As a **shopper** I can sort product by specific categories so that I can sort product by specific category and find best price and best rates.
- As a **shopper** I can search a product by name or description so that I can easily find a specific product by name which I’d like to purchase.
- As a **shopper** I can see what I’ve searched for and the number of results so that I can easily decide whether the product I want is available.

### **2. Viewing and Navigation Functionality:**

- As a shopper I can view all the products so that I can select some products to purchase.
- As a shopper I can see individual product details so that I can see product description, price, image, and sizes.
- As a shopper I can identify deals and special offers so that I can take advantage of special savings some money on a product.
- As a shopper I can see grand total of money and all product which I selected so that I can save lot of time.

### **3. Purchase and checkout products:**

- As a shopper I can easily select a size and quantity of product so that I can select right size and quantity of a product when I buy it.
- As a shopper I can easily view items in my bag so that I can identify the total cost of purchase.
- As a shopper I can adjust the quantity of my bag so that I can make any changes before buy.
- As a shopper I can add my personal payment information safe and secure so that I can confidently provide the information to make a purchase.
- As a shopper I can view my order confirmation after checkout so that I can easily see that I didn't make any mistake.
- As a shopper I can receive confirmation email after checkout so that I can keep that email as a proof what I have brought from store.

### **4. Admin and Store management:**

- As a shop owner I want to add new products so that I can add new items to my store.
- As a shop owner I want to easily Edit and Update a product so that I can update images prices and other criteria.
- As a shop owner I want to easily delete a discontinued product so that I can remove items from store site.

### **5. User Authentication:**

- As a user I want to create a personal user profile so that I can view my personal order and save my payment information.
- As a user I want to receive a confirmation email after registering an account so that I can verify that my account registration was successful.
- As a user I want to recover my password in case I forget it so that I can recover access to my account.
- As a user I want to login or logout of my account so that I can access my personal account information.
- As a user, I want to create a personal account so that I can view my profile.

### **Scope**

To achieve the desired user & business goals, the following features will be included in this website:
- A Responsive website to open on any devices like desktop, tablet and mobile.
- Home page with three different backgrounds banners and shopping buttons and with all the information to be found on the website.
- Logged in users can see their name on the navbar.
- Register/login feature using Django All AUTH so that users can create an account.
- 404 error page added to go home page if there is an error.

### **Structure**

In this website I have used seven apps:
1.	About us – location
2.	Bag – All products basket
3.	Checkout – cards details
4.	Contact – user feedback
5.	Home – Information about all the pages
6.	Products- All products
7.	Profiles- users information

## **Databases**

The about us, checkout, products, and profile apps require databases to store information, so I have built 6 custom models. I connected this website to the Heroku Postgres database which is provided by Heroku as an add-on.

These models are following this flow diagram:

![](/assets/readme-file/diagram.PNG)

### **About us**
In the about us app, I created one model named ‘Newsletter Users’. This model that provides email to display subscribe and unsubscribe newsletter of the computer world.

### **Checkout**
There are two models in the checkout app, ‘Order’ and ‘OrderLineItem’. These 3 models allow for the customer details, products size and quantity to be stored.

For each checkout, there will be a customer detail, delivery cost, and grand total form which comes from Order models. The customer must fill in this form to make a payment but if the customer logged in and saved their information beforehand, then the form will already be filled so they would only need to add their card details.

With the ‘OrderLineItem’, the customer will be able to retrieve all the information about the product, such as their name, size, and quantity.


### **Products**
In the products app, I created two models named Products & Category. This app controls the products that are displayed in the online shop.

Products enables individual products to be added to the database for the customer to be buy through online shop. Only admin users can add, edit, and delete products from the front end and the admin page, but the normal user can see and buy the products. The ‘Category’ model connects to the products through the foreign key.

Category stores various types of categories like monitors, graphics card, components, laptops etc. This category allows to users to find a specific product from the website.

### **Profiles**
The Profile app allows users to save their information, so that when they are logged in and they want to purchase any product, they will get a prefilled form to save their time. The `UserProfile` model has a one-to-one field that is linked to the Django All AUTH user account, and upon logging in the model method `create_or_update_user_profile` creates the profile if it isn't already present in the model.

## **Design**

### **Colour Schema**

- I used three colours for the background and content, which are white, black, and blue. I have also used a small amount of green in the add to basket button.

- I used blue from the theme waGon website, Black and white from the code institute project ‘Boutique ado’, and Green I checked add to basket button colour online.

### **Typography**

- I selected the font I used from the Google font website and linked it with my CSS file.

- I used three font styles: Poppins-Regular, Poppins-Light, Poppins-ExtraLight, Poppins-Medium, Poppins-Italic, Poppins-Italic, Poppins-SemiBold, sans-serif.

-  I have used the font Sans-serif as a backup in instances where if the correct link is not provided to the css3 file.If this occurs and the Google font does not work the backup font sans-serif will always work.

### **Imagery**

- The background images used in this website plays a vital role in the user’s experience of the website.
- The images shown on the website has been selected to convince the customer purchase the products.
- The Images are downloaded for free from the [Ebuyer](https://www.ebuyer.com/) [razer](https://www.razer.com/gb-en) [corsair](https://www.corsair.com/uk/en/) website.

### **Skeleton**

- I used [Figma](https://www.figma.com/file/xGZ1gadhIzf7MHrQTEKplK/Computer-world?node-id=0%3A1 "Link to Figma homepage") Wireframe for the website.


