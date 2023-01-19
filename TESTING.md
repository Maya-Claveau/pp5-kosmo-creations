# **Testing**

## **Code Validation**

[Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/) was used to validate CSS code. It passes the validator without errors, however, there are some warnings, you can find the details in the screenshot. I looked into them, and don’t think is critical issue, so I just left them there.

<details>
<summary>CSS and warnings</summary>
<img src="static/testing/validation-css.jpg">
<img src="static/testing/validation-css-warnings.jpg">
</details>

<br>

[W3C Markup Validation Service](https://validator.w3.org/) was used for validate HTML code

<details><summary>HTML validation reports</summary>
<summary>index.html</summary>
<img src="static/testing/html-index-pg.jpg">
<summary>contact.html</summary>
<img src="">
<summary>all_posts.html</summary>
<img src="">
<summary>signup.html</summary>
<img src="">
<summary>login.html</summary>
<img src="">
<summary>logout.html</summary>
<img src="">
<summary>shared_posts.html</summary>
<img src="">
<summary>add_post.html</summary>
<img src="">
<summary>update_post.html</summary>
<img src="">
<summary>delete_post.html</summary>
<img src="">
</details>

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
