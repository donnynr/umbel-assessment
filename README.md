# Engineer Candidate Take-Home Assessment

## Purpose

The purpose of this assessment is to validate that the candidate can:

* Contribute to an existing web application
* Write clear, comprehensible, and extensible code
* Work with multiple data sources
* Demonstrate an understanding of Python and Django
* Communicate clearly about design and architecture decisions

## Project Prompt

One of the capabilities of the Umbel platform is to help clients engage with their 
fans with digital Activations, while collecting data about those Activations. An 
Activation is a single digital campaign to present users with the opportunity to 
Submit a form response. For any Submission, we create a user Profile and _may_ 
collect a set of Brands that the user likes. So there are possibly many Brands 
associate to a Profile. For our purposes, Brands are defined by a brand id. 

Upon completion, the Submission, Profile, and associated Brands are stored in 
the database. This data is provided and can be treated as given.

We have an existing web application that is used to view a list of Activations.
However listing just the Activations doesn't fulfill the clients' needs. We 
would like to add  two new features to this application to make it more useful 
to our clients.

### Feature 
1 - Submissions per Activation
For each Activation in the activation list we would like to know how many
Submissions were completed. 

Please update the existing activation list API to return the total number 
of Submissions along with the existing fields.

### Feature 
2 - Submissions with Brand Data
For each Activation in the activation list we would like to know how many
Submissions have Brand data. You should be able to determine if a Profile
has brand data by checking to see if the Profile has associated brand ids. 

Please update the existing activation list API to return the total number 
of Submissions with Brand data along with the existing fields.

## Project Deliverables

Please send us back the project repository with the following:

* Code changes you made to implement the two above features.
* A file explaining any decisions you had to make or challenges you overcame.
* Brief API documentation describing how to use the APIs you've created.

## Bonus Points

We would love to see:

* Project history (We sent you a git repository, so you can commit your work as you see fit)
* Production-quality code
