## Introduction

**Modelling User Preferences to provide Location Based Recommendations**

This application uses KNN to create an artificial agent that can recommend eating places to a user. Our agent will parse through the user's information with an aim to understand different characteristics about the user. Then based on that we will provide different recommendations to the user. Additionally, through user’s feedback, the agent will evolve its preference model and recommendation function. 

This project is our submission for CS 5100 (Northeastern University).

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

- `algorithm` 
    Main files including knn.
    
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

- `plots`
    Contains the code for the graphs

- `tests`
    Testing

- `app.py` main file to run the program

- `settings.py` contains all the predefined settings

- `setup.py` to setup the project

## Future Scope

This application can be extended by adding Natural Language Processing. In future, we aim to apply Natural Language Processing to a user's review and try to understand that if they do or don't like a business then what is the real reasoning behind that? Is it because of some specific thing like a lack of parking? If it is, should we stop recommending businesses which doesn't have parking space? Is it because the business doesn't have free Wi-fi?

All these factors we believe would help us in improving our recommendations and giving even better results.

## Team

* [Bhanu Pratap Jain](http://github.com/bhanupratapjain)
* [Rohit Begani](https://github.com/rohitbegani)
* [Ronny Mathew](http://github.com/ronnygeo)

## License

The MIT License (MIT)

Copyright (c) 2015-2017 Rohit Begani

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
