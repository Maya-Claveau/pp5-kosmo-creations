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
No errors were found in the final verion. There was no report could be generated.

---

## **Manual Testing**

Testing was done throughout the development, for each feature and on different sized devices, to ensure responsiveness.

Features were tested with different users to ensure testing from different devices, sizes and browsers, to keep an eye for any potetial bugs while in developing stage.

The site is built with responsive design in mind, therefore it can be viewed from different size devices, supporting smart phone, tablet and desktop.

### _Bugs_

Shopping Cart page

- The position of Update link was not aligned properly, I manage to fix it, but between 576px - 767px, and 1200px - 1256px the buttons for Update and Delete are not aligned correctly.
<details><summary>example is here</summary>
<img src="static/readme/bug-shopping-cart.jpg" width="800">
</details>

- Update button didn't work for some reason, and with the help of amazing tutor from CI, we found out that was the extra div I had between the form and a tag was causing the issue. Removed that div and it worked like a charm.

- The error message was displaying on the checkout page below the payment section, this was also solved with the help from CI's tutor.

- On the jewelry detail page, I have the logic in place for if there is inventory, it shows options for choosing the quantity the add to cart button, otherwise it only show "Sold out" and the continue shopping button. However, everything was showing sold out even there is inventory. After talking to Ci's Tutor - Josh, the problem didn't get fixed, but he helped me to find where the problem was. And I managed to fix it myself. Then after deployment, everything were showing sold out again, after long hours of investigation, I realised that inventory wasn't in the admin, therefore django couldn't find it, it was doing what my code told it to do. So I added the inventory to admin.py, increased the inventory and now the logic works. What I learnt is how to determine where to look for when there is an error. Josh showed me just that. I am really grateful.

- Above just few examples, I can't remember how many things went wrong and some I tried and fixed successfully, a quick search on slack is always helpful. Some I needed help from the tutors.
