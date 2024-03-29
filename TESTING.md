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
<summary>Contact us Page</summary>
<img src="static/testing/html-contact-pg.jpg">
<summary>Newsletter Page</summary>
<img src="static/testing/html-newsletter-pg.jpg">
<summary>Wishlist Page</summary>
<img src="static/testing/html-wishlist-pg.jpg">

</details>

<br>

[CI Python Linter](https://pep8ci.herokuapp.com/) was used for validate python code
No errors were found in the final verion. There was no report could be generated.

---

## **Manual Testing**

Testing was done throughout the development, for each feature and on different sized devices, to ensure responsiveness.

Features were tested with different users to ensure testing from different devices, sizes and browsers, to keep an eye for any potetial bugs while in developing stage.

The site is built with responsive design in mind, therefore it can be viewed from different size devices, supporting smart phone, tablet and desktop.

<details><summary>Mobile view as Admin</summary>
<img src="static/testing/mob-view-1.gif" width="600">
<img src="static/testing/mob-view-3.gif" width="600">
<img src="static/testing/mob-view-2.gif" width="600">
<img src="static/testing/mob-view-4.gif" width="600">
<img src="static/testing/mob-view-5.gif" width="600">
</details>

<br>

### **Lighthouse Scores**

Home page

Accessibility score on desktop is 88 due to render-blocking resources

<details><summary>Desktop</summary>
<img src="static/testing/lh-desktop-home.jpg" width="800">
</details>

<br>

Performance score on mobile is 69 due to render-blocking resources

<details><summary>Mobile</summary>
<img src="static/testing/lh-mob-home.jpg" width="800">
</details>

<br>

All Jewelries page

Initial performance score on all jewelries page was 39! Because the images I used were 2MB, my mentor suggested to use something less than 10KB for improvement. I used [iloveimg.come](https://www.iloveimg.com/) to first compress and then resize to make them 90%+ smaller, not the performance score is at 69. Still room for improvement obviously, so I tried to convert them into avif format, bad news I couldn't make it render on the page, given the time pressure I had to move on. But 69 is much better than 39, I will take that.

<details><summary>Desktop</summary>
<img src="static/testing/lh-desktop-jewelries.jpg" width="800">
</details>

On Mobile the performance score is 57, definetely need to figure out how to make avif work next time.

<details><summary>Mobile</summary>
<img src="static/testing/lh-mob-jewelries.jpg" width="800">
</details>

<br>

Register Page

<details><summary>Desktop</summary>
<img src="static/testing/lh-desktop-register.jpg" width="800">
</details>

<details><summary>Mobile</summary>
<img src="static/testing/lh-mob-register.jpg" width="800">
</details>

<br>

Login Page

<details><summary>Desktop</summary>
<img src="static/testing/lh-desktop-login.jpg" width="800">
</details>

<details><summary>Mobile</summary>
<img src="static/testing/lh-mob-login.jpg" width="800">
</details>

<br>

My Profile Page

<details><summary>Desktop</summary>
<img src="static/testing/lh-desktop-profile.jpg" width="800">
</details>

<details><summary>Mobile</summary>
<img src="static/testing/lh-mob-profile.jpg" width="800">
</details>

<br>

Product Management Page

<details><summary>Desktop</summary>
<img src="static/testing/lh-desktop-prod-mgt.jpg" width="800">
</details>

<details><summary>Mobile</summary>
<img src="static/testing/lh-mob-prod-mgt.jpg" width="800">
</details>

<br>

Shopping Cart Page

<details><summary>Desktop</summary>
<img src="static/testing/lh-desktop-shopping-cart.jpg" width="800">
</details>

<details><summary>Mobile</summary>
<img src="static/testing/lh-mob-shopping-cart.jpg" width="800">
</details>

<br>

Checkout Page

<details><summary>Desktop</summary>
<img src="static/testing/lh-desktop-checkout.jpg" width="800">
</details>

<details><summary>Mobile</summary>
<img src="static/testing/lh-mob-checkout.jpg" width="800">
</details>

<br>

Checkout Success Page

<details><summary>Desktop</summary>
<img src="static/testing/lh-desktop-checkout-success.jpg" width="800">
</details>

<details><summary>Mobile</summary>
<img src="static/testing/lh-mob-checkout-success.jpg" width="800">
</details>

<br>

Contact Us Page

<details><summary>Desktop</summary>
<img src="static/testing/lh-contact-desktop.jpg" width="800">
</details>

<details><summary>Mobile</summary>
<img src="static/testing/lh-contact-mob.jpg" width="800">
</details>

<br>

Newsletter Page

<details><summary>Desktop</summary>
<img src="static/testing/lh-newsletter-desktop.jpg" width="800">
</details>

<details><summary>Mobile</summary>
<img src="static/testing/lh-newsletter-mob.jpg" width="800">
</details>

<br>

Wishlist Page

<details><summary>Desktop</summary>
<img src="static/testing/lh-wishlist-desktop.jpg" width="800">
</details>

<details><summary>Mobile</summary>
<img src="static/testing/lh-wishlist-mob.jpg" width="800">
</details>

<br>

### _Bugs_ _Bugs_ _Bugs_

**Shopping Cart page**

- The position of Update link was not aligned properly, I manage to fix it, but between 576px - 767px, and 1200px - 1256px the buttons for Update and Delete are not aligned correctly.
<details><summary>example is here</summary>
<img src="static/readme/bug-shopping-cart.jpg" width="800">
</details>

- Update button didn't work for some reason, and with the help of amazing tutor from CI, we found out that was the extra div I had between the form and a tag was causing the issue. Removed that div and it worked like a charm.

- On desktop view, when there is only on item, the image is squshed on the deployed version, but look good on the dev version, which is very confusing. After hours of trying different things, I went to CI's tutor support for help. And Ed manage to find a solution which worked on the first try, that's amazing.
<details><summary>example is here</summary>
<img src="static/testing/bug-shopping-cart-one-item.jpg" width="800">
</details>

<br>

**Checkout Page**

- The error message was not displaying below the payment section, this was also solved with the help from CI's tutor.

Jewelry Detail Page

- I have the logic in place for if there is inventory, it shows options for choosing the quantity the add to cart button, otherwise it only show "Sold out" and the continue shopping button. However, everything was showing sold out even there is inventory. After talking to Ci's Tutor - Josh, the problem didn't get fixed, but he helped me to find where the problem was. And I managed to fix it myself. Then after deployment, everything were showing sold out again, after long hours of investigation, I realised that inventory wasn't in the admin, therefore django couldn't find it, it was doing what my code told it to do. So I added the inventory to admin.py, increased the inventory and now the logic works. What I learnt is how to determine where to look for when there is an error. Josh showed me just that. I am really grateful.

**Footer**

- Footer was floating on logout page, login page, register page and my profile page. I manage to find the problem and fixed it.
<details><summary>example</summary>
<img src="static/testing/bug-footer-floating.jpg" width="800">
</details>

- After fixed the issue with floating footer, I discovered the another issue, the footer is covering the buttons on product management page. After search on stackoverflow, I found the solution by adding to the css code clear: both; and increase the margin-bottom to the div above footer, now it is sitting at its designated place.
<details><summary>example</summary>
<img src="static/testing/bug-prod-mgt-btn-hidden.jpg" width="800">
</details>

<br>

**Wishlist and Contact Page**
Both were working fine in the development site, but not in deployed site for some reason. I did do migration after create these two apps, but I couldn't figure out what's causing the issue. After few hours of not going anywhere. I turned to Tutor support for rescue. Josh took my tickets, and get it solved in no time. Turns out that I am missing the link to ElephantSQL database. And thanks to Josh who helped me link my code directly to ElephantSQL for both development and deployed site.

<br>

### Unsolved Bugs

On the checkout page, when the logged in user check the box of save their information, the info doesn't get saved to their profile for some reason. But if the user update info in their profile, the change is reflected on the checkout page. Due to the time pressure, I didn't manage to find the cause, therefore I removed that bit, so it is not visible to the user, but the backend code are still in the project as I intend to fix it in the future.

On the Newsletter page, the two buttons at the bottom of Subcribe and Unsubcribe doesn't work yet, given the time I couldn't attend to this, but this is definitely something I would like to make it work.

<br>

Above just few examples, I can't remember how many things went wrong and some I tried and fixed successfully, a quick search on slack is always helpful. Some I needed help from the tutors. I am so grateful for CI's Tutor's support!!!!
