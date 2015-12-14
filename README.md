## Modelling User Preferences to provide Location Based Recommendations 

##### Project for CS 5100: Foundations of AI.


## Packages Used

`pymongo >= 3.1.1`

`plotly`

To install all packages `cd` to the working directory and run, 

`pip install -e .`

## How to run

1. Clone this repo to your local machine using `git clone <repo link>`

2. `cd` to the root of the directory

3. Download all the required packages using the command `pip install -e`

4. Run `app.py`. That's it!

## File Structure

- `lib:` 
    Main files.
    
- `helpers:`
    Contains all the helper files.

- `util:`
    This folder contains all the utility functions.
    File Operations
    Dictionary Operations
    
- `static:`
    - csv
    - json
    
- `algorithm:`
    This folder will contain the actual KNN algo.

- `docs:`
    Contains all the docs related to the project
    
- `models:`
    Contains the model data classes

## Future Scope:

This application can be extended by adding Natural Language Processing. In future, we aim to apply Natural Language Processing to a user's review and try to understand that if they do or don't like a business then what is the real reasoning behind that? Is it because of some specific thing like a lack of parking? If it is, should we stop recommending businesses which doesn't have parking space? Is it because the business doesn't have free Wi-fi?

All these factors we believe would help us in improving our recommendations and giving even better results.
