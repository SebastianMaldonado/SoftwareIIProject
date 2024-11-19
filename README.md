# SoftwareIIProject

SuperUser Data
user: admin
password: 12345

REQUEST for auth/user endpoint:

- POST /user/: Create a new user
- GET /user/: List all users (requires authentication).
- GET /user/{id}/: Retrieve the details of a user (requires authentication).
- PUT/PATCH /user/{id}/: Update user data (requires authentication).
- DELETE /user/{id}/: Delete the user (requires authentication, but only the user themselves can delete their account).

To access to Token by authentication:

- POST /token/: Send a json with (for generic [User] username is the same email)
    {
        'username': USERNAME,
        'password': PASSWORD
    }
- POST /token/refresh: Send a json with previous refresh token
    {
        'refresh': REFRESH_TOKEN
    }


eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMzMzNTMzMSwiaWF0IjoxNzMyMDM5MzMxLCJqdGkiOiIxZjExMDc0NTlhNGY0ZWUwODM0M2IzMDYwM2NkZGRmNSIsInVzZXJfaWQiOjl9.1oHes-h1gOwIWqLBFL3419NhmP6ULwB0jvL3Ksi7V5A