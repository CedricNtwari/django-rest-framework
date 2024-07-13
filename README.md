## Django Rest Framework API Project

### Project Description

This project is a backend API developed using Django and Django REST Framework (DRF). It provides a platform for users to create and interact with posts, comments, likes, followers, and profiles. The API supports CRUD operations and ensures proper permissions and ownership checks.

## Features

- **User Authentication:** Secure user registration and login.
- **Profiles:** Each user has a profile with additional information.
- **Posts:** Users can create, update, delete, and view posts.
- **Comments:** Users can comment on posts.
- **Likes:** Users can like posts.
- **Followers:** Users can follow and unfollow other users.

## Technologies Used

- **Django:** High-level Python web framework.
- **Django REST Framework (DRF):** Powerful and flexible toolkit for building Web APIs.
- **Cloudinary:** Media management and optimization.

### Access the API:

### API Endpoints:

### Authentication:

- **POST** /admin/: Login a superuser.
- **POST /api-auth/login/:** Login a user.
- **POST /api-auth/logout/:** Logout a user.

### Profiles

- **GET /profiles/:** List all profiles.
- **GET /profiles/<int:id>/:** Retrieve, update, or delete a specific profile.

### Posts

- **GET /posts/:** List all posts.
- **POST /posts/:** Create a new post.
- **GET /posts/<int:id>/:** Retrieve, update, or delete a specific post.

### Comments

- **GET /comments/:** List all comments.
- **POST /comments/:** Create a new comment.
- **GET /comments/<int:id>/:** Retrieve, update, or delete a specific comment.

### Likes

- **GET /likes/:** List all likes.
- **POST /likes/:** Like a post.
- **GET /likes/<int:id>/:** Retrieve or delete a like.

### Followers

- **GET /followers/:** List all followers.
- **POST /followers/:** Follow a user.
- **GET /followers/<int:id>/:** Retrieve or unfollow a user.

### Permissions

- Only authenticated users can create, update, or delete content.
  Users can only modify their own content.
  All users can view public content.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

### Connecting your Mongo database

- **Connect to Mongo CLI on a IDE**
- navigate to your MongoDB Clusters Sandbox
- click **"Connect"** button
- select **"Connect with the MongoDB shell"**
- select **"I have the mongo shell installed"**
- choose **mongosh (2.0 or later)** for : **"Select your mongo shell version"**
- choose option: **"Run your connection string in your command line"**
- in the terminal, paste the copied code `mongo "mongodb+srv://<CLUSTER-NAME>.mongodb.net/<DBname>" --apiVersion 1 --username <USERNAME>`
  - replace all `<angle-bracket>` keys with your own data
- enter password _(will not echo **\*\*\*\*** on screen)_

---

Happy coding!
