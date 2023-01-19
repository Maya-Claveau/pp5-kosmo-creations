# **Testing**

## **Code Validation**

[Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/) was used to validate CSS code. It passes the validator without errors, however, there are some warnings, you can find the details in the screenshot. I looked into them, and don’t think is critical issue, so I just left them there.

<details>
<summary>CSS and warnings</summary>
<img src="static/testing/validation-css.jpg">
<img src="static/testing/validation-css-warnings.jpg">
</details>

<br>

[W3C Markup Validation Service](https://validator.w3.org/) was used for validate HTML code. Errors and warnings were taken care of until the code satisfy the requirements.

<details><summary>HTML validation reports</summary>
<summary>Home Page</summary>
<img src="static/testing/html-index-pg.jpg">
<summary>All Jewelries Page</summary>
<img src="static/testing/html-jewelries-pg.jpg">
<summary>Jewelry Details Page</summary>
<img src="static/testing/html-jewelries-detail-pg.jpg">
<summary>Shopping Cart Page</summary>
<img src="static/testing/html-shopping-cart-pg.jpg">
<summary>Login Page</summary>
<img src="static/testing/html-login-pg.jpg">
<summary>My Profile Page</summary>
<img src="static/testing/html-my-profile-pg.jpg">
<summary>Checkout Page</summary>
There is a warning here, since the empty heading element was left empty on purpose, I just left it there.
<img src="static/testing/html-checkout-pg.jpg">
<summary>Checkout Success Page</summary>
<img src="static/testing/html-checkout-success-pg.jpg">
<summary>Logout Page</summary>
<img src="static/testing/html-logout-pg.jpg">
<summary>Register Page</summary>
<img src="static/testing/html-register-pg.jpg">
<summary>Product Management Page</summary>
There are two errors on this page, however after investigation, both errors are coming from imported django file, due to the time pressure, I decided not to fix it. Details can be seen from below screenshot.
<img src="static/testing/html-prod-mgt-pg.jpg">
<img src="static/testing/html-prod-mgt-pg-error.jpg">

</details>

<br>

[CI Python Linter](https://pep8ci.herokuapp.com/) was used for validate python code
No errors were found in the final verion. There was no report generated.

## **Manual Testing**

Testing was done throughout the development, for each feature and on different sized devices, to ensure responsiveness.

Features were tested with different users to ensure testing from different devices, sizes and browsers, to keep an eye for any potetial bugs while in developing stage.

Shopping Cart page

- The position of Update link was not aligned properly, I manage to fix it, but between 576px - 767px, the button for Update and Delete are not aligned correctly.
<details><summary>Shopping Cart</summary>
<img src="static/readme/bug-shopping-cart.jpg" width="800">
</details>

## Below are example of list of things I struggled with:

-
-
-
-
-
-

### **Unfixed bugs:**

Post.object – put it under unfixed bugs Pylint is pythons error message, and unfortunately python can’t see what Django is doing, so as an example, objects are there, python just can’t see that Django is handling the objects.
