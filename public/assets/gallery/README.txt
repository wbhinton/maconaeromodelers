=== HOW TO UPDATE THE GALLERY ===

This website automatically builds the gallery pages based on the folders found here.
You do NOT need to write any code to add new photos.

STEP 1: ADDING A NEW EVENT
--------------------------
1. Open the folder for the current year (e.g., "2025").
   If it's a new year, create a new folder named "2026".
2. Create a folder for your event (e.g., "spring-fly-in").
   Note: Use dashes, not spaces (bad: "Spring Fly In", good: "spring-fly-in").
3. Drag your photos into that folder.
   Supported formats: .jpg, .jpeg, .png, .webp

STEP 2: ADDING DETAILS (OPTIONAL)
---------------------------------
If you want a nice title and description, create a file named "info.json" 
inside your event folder and paste this text:

{
  "title": "Spring Fly-In",
  "date": "May 15, 2025",
  "description": "We had 30 pilots and great weather.",
  "cover": "image-01.jpg"
}

* "cover" is the filename of the picture you want on the main gallery card.
* If you don't create this file, the website will just use the folder name.

STEP 3: PUBLISH
---------------
Commit these changes to GitHub, and the site will update automatically.