# **Testing**

## **Code Validation**

[Jigsaw CSS validator](https://jigsaw.w3.org/css-validator/) was used to validate CSS code

<details>
<summary>CSS</summary>
<img src="">
<summary>CSS warnings</summary>
<img src="">
</details>
CSS code passes the validator without errors, however, there are some warnings, please see details in the screenshot. I looked into them, and don’t really know how to fix them at the moment, so I just left them there.

[Nu Html checker](https://validator.nu/) for validate HTML code

<details><summary>HTML</summary>
<summary>index.html</summary>
<img src="">
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

- add post page: I had to remove the summernotewidget on the content field, because although it was working fine, but it does error during the code validation, so I decided to remove it after all.

this is with summernotewidget
<img src="">

this is without summernotewidget

<img src="">

### **Unfixed bugs:**

Post.object – put it under unfixed bugs Pylint is pythons error message, and unfortunately python can’t see what Django is doing, so as an example, objects are there, python just can’t see that Django is handling the objects.
