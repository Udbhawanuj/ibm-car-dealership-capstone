# Exact screenshots to capture

Run the application with `RUN_PROJECT_WINDOWS.bat` or `RUN_PROJECT_LINUX_MAC.sh`.

Demo users:

- Reviewer: `reviewer` / `Reviewer@123`
- Root admin: `root` / `Root@123`

Keep the browser address bar visible whenever the rubric asks for an endpoint.

1. `admin_login.png`: open `/admin/`, sign in as root, capture the admin dashboard with the root username visible.
2. `admin_logout.png`: click **Log out**, capture Django's logged-out confirmation page.
3. `get_dealers.png`: open `/` before user login; capture multiple dealership cards.
4. `get_dealers_loggedin.png`: log in as reviewer; capture username and **Review Dealer** buttons.
5. `dealersbystate.png`: select Kansas; capture `/dealers/KS/` and filtered dealer cards.
6. `dealer_id_reviews.png`: open `/dealer/1/`; capture dealer details and reviews.
7. `dealership_review_submission.png`: open `/dealer/1/review/`, fill the review fields, and capture before submitting.
8. `added_review.png`: submit the review and capture it at the top of `/dealer/1/`.

After deployment, repeat the relevant pages using the public deployment URL and save:

- `deployed_landingpage.png`
- `deployed_loggedin.png`
- `deployed_dealer_detail.png`
- `deployed_add_review.png`
