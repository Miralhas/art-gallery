# Gallery 2 You

This project is a Django-based web application designed to provide a digital platform for artists to exhibit their creative works. It employs a robust user authentication system, allowing artists to establish unique profiles using their email addresses. This feature enhances the user experience by personalizing their interactions with the platform.

In addition to creating profiles, artists can create their own virtual galleries. This feature provides a dedicated space for each artist to display their artworks, fostering a sense of ownership and pride in their work. Artists can further enhance their galleries by uploading high-quality images of their artworks, providing a tangible connection between the artists and their audience.

Artists also have the opportunity to engage with their peers and the wider community. They can rate and comment on other artists' work, fostering a vibrant and interactive community. This feature encourages constructive feedback and discussion, promoting continuous improvement and innovation.

The project also incorporates a sophisticated analytics system powered by Chart.js. This feature generates insightful data on the most viewed galleries, most rated artworks, and most viewed user profiles. This information is presented in an intuitive and visually appealing manner, providing valuable insights for both artists and administrators.

Finally, the project includes an admin interface that allows for effective management of user accounts and artworks. This feature provides a centralized control panel, streamlining administrative tasks and ensuring optimal performance of the platform.

## Project Structure

This project is structured into four main directories:

- `accounts`: Contains the user authentication views and models.
- `gallery`: Manages the creation, deletion, and viewing of galleries and artworks.
- `analytics`: Provides analytics on the most viewed galleries, most rated artworks, and most viewed user profiles.

## File Contents

Here's a breakdown of the major files in the project:

### User Authentication Views: Handles user registration, login, profile viewing, and logout.

- `UserLoginView`: Handles user login. It uses the `AuthForm` for form validation and redirects the user to the gallery index page upon successful login.
- `UserProfileView`: Displays a user's profile. It retrieves the user's galleries, updates the views count, and paginates the galleries.
- `UserLogoutView`: Handles user logout. It logs out the user and redirects them to the home page.
- `UserSignUpView`: Handles user sign up. It uses the `RegisterForm` for form validation and creates a new user upon successful registration.

### Gallery Views: Manages the creation, deletion, and viewing of galleries and artworks.

- `IndexView`: Displays the index page. It retrieves the top three most viewed galleries.
- `CreateGalleryView`: Handles the creation of a new gallery. It saves the new gallery and redirects the user to the gallery page.
- `DeleteGalleryView`: Handles the deletion of a gallery.
- `CreateArtworkView`: Handles the creation of a new artwork. It checks if the user is the owner of the gallery before saving the new artwork.
- `DeleteArtworkView`: Handles the deletion of an artwork.
- `UserGallerieView`: Displays a user's gallery. It retrieves the user's galleries, updates the views count, and paginates the galleries.
- `ArtworkPageView`: Displays an artwork page. It retrieves the artwork's comments and updates the views count.
- `GalleriesListView`: Displays a list of galleries. It paginates the galleries.
- `ArtworkListView`: Displays a list of artworks. It paginates the artworks.
- `SearchView`: Handles search queries. It filters galleries, artworks, and users based on the query.
- `edit_artwork_view`: Handles the editing of an artwork. It checks if the user is the owner of the artwork before updating the artwork.
- `edit_gallery_view`: Handles the editing of a gallery. It checks if the user is the owner of the gallery before updating the gallery.

### Analytics Views: Provides views for generating analytics data on the most viewed galleries, most rated artworks, and most viewed user profiles.

- `IndexView`: Displays the analytics index page.
- `get_most_viewed_galleries`: Returns the most viewed galleries.
- `get_most_rated_artworks`: Returns the most rated artworks.
- `get_most_viewed_user_profiles`: Returns the most viewed user profiles.
- `get_gallery_analytics`: Returns analytics data for a specific gallery.
- `get_artwork_analytics_vs_all`: Returns analytics data comparing a specific artwork against all artworks.

## Distinctiveness and Complexity

This project stands out due to its focus on providing a platform for artists to share their work and receive feedback from the community. It incorporates advanced features such as user authentication, image uploading, and user profiling. Notably, the project uses the Python Pillow library for handling user-uploaded images, which allows for efficient image processing and manipulation \[Source 1\]

Moreover, the project uses Chart.js for generating analytics data. Chart.js is a popular JavaScript library that simplifies the process of creating beautiful charts and graphs. This makes the project stand out for its ability to provide visual representation of data, making it easier for users to understand trends and patterns.

Furthermore, the project uses Django's built-in views and forms for user registration and login, enhancing its complexity. This allows for a seamless user experience, as users can easily register, log in, and navigate through the site.

## Features

- User Authentication
    
    - The project utilizes Django's built-in user authentication system. Users can register, log in, view their profiles, and log out. This feature ensures that only registered users can create galleries and artworks, providing a secure environment for artists.
- Gallery Creation and Management
    
    - Users can create their own galleries, which serve as personal spaces to showcase their artworks. They can also delete their galleries when they no longer want them to be publicly accessible.
- Artwork Upload and Management
    
    - Within their galleries, users can upload their artworks, complete with titles, descriptions, and images. Users can also delete their artworks when they no longer wish to display them.
- User Profiles
    
    - Each user has a profile that displays their uploaded artworks and the galleries they've created. The views count for each user's profile increases every time someone visits it, providing a measure of popularity among other users.
- Community Interaction
    
    - Users can rate and comment on each other's artworks, fostering a community of artists and art enthusiasts.
- Analytics
    
    - Admins can generate analytics data on the most viewed galleries, most rated artworks, and most viewed user profiles. This provides valuable insights into user behavior and engagement levels.
- Search Functionality
    
    - Users can search for galleries, artworks, and other users based on keywords. This enhances navigation and discovery within the platform.
- Editing Features
    
    - Users can edit their artworks and galleries, allowing them to update their content as needed. This is done via a PUT request, ensuring data integrity.
- Pagination
    
    - Pagination is implemented across various views to handle large amounts of data efficiently. This includes the listing of galleries, artworks, and user profiles.

## Running the Application

To install and run this project locally, follow these steps:

1. Clone the repository to your local machine.

2. Navigate into the project directory.

3. Install the project.
	```bash
	pip install -e .
	```

4. Start the Django development server.
	```python
	python manage.py runserver
	```

## Additional Information

This project uses a custom user authentication system, which allows users to register using their email addresses. This is achieved by extending Django's built-in `AbstractBaseUser` and `PermissionsMixin` to create a custom `User` model. This model includes fields for email, username, profile picture, and views count. The `login_required` decorator is used to restrict access to certain views to only authenticated users. The `UserManager` class in `accounts/models.py` is used to create and save user instances

## Python Packages

The project uses several Python packages, including Django, django_extensions, pillow, and django_widget_tweaks. These are included in the `setup.py` file.

## License

This project is licensed under the MIT License.