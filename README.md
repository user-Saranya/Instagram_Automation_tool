# INSTAGRAM AUTOMATION TOOL

## Part 1: Vehicle Management System

### Project Overview
The Vehicle Management System is the first part of this project and is designed to create and manage two types of vehicles: "Bus" and "Car," both inheriting properties from the "Vehicle" class. The system allows users to create instances of these classes, control passenger counts, and respond to specific user inputs. This part was created to learn Python fundamentals.

### Vehicle Classes
Two classes are implemented as part of this project: "Car" and "Bus." They inherit properties from the base "Vehicle" class defined in the provided `vehicle.py`.

### Car and Bus Class Properties
- **Bus**: Seating capacity of 25 people and standing capacity of 15 people.
- **Car**: Seating capacity of 5 people, and it has an ID as a member variable.

### Tasks
1. Create two instances of the "Car" class, each with a unique car ID, and one instance of the "Bus" class.
2. Initially, all three vehicles have 0 passengers, and the program keeps track of passenger counts.
3. The program responds to user input as follows:

- "A": The user requests a seat in a car. If allotted, return "Allotted seat in car" and provide the ID.
- "B": The user requests a seat on the bus. If allotted, specify whether it's a sitting or standing space. Sitting space must be filled before any standing seats are allotted.
- "C": Randomly remove one passenger (60% chance from the bus, 20% from each car). If a passenger is removed, specify the vehicle and ID.
- Any other command: Exit the program.

## Implementation Notes
- Passenger counts are tracked using member variables and functions within the classes.
- This project was designed to learn Python fundamentals and basic object-oriented programming.

## Part 2: Instagram Automation Tool

### Project Overview
The Instagram Automation Tool is the second part of this project and is designed to automate various interactions on Instagram, including login, liking, commenting, following, and saving posts based on specific hashtags. It allows you to explore and automate actions on Instagram while respecting Instagram's server limits to prevent throttling.

### Task 1: Setting Up and Login Automation
- In this initial task, the project focuses on setting up the environment, installing dependencies, and implementing a proof of concept for the login process.
- You can choose your preferred browser for automation (Firefox was used in the example).
- It's important to consider profiles and options, which can be explored in the documentation for further customization.

### Task 2: Automating Post Crawling and Interactions
- In the second task, the tool automates interactions with posts on the explore page.
- It involves clicking on the first post, liking it, moving to the next post, and storing metadata such as URLs, profile names, likes, and comments in a CSV.
- Additionally, you can simulate user comments by using predefined messages stored in a JSON file.
- The tool includes random sleep intervals to prevent overloading Instagram's servers.
- Besides crawling the explore page, it also allows you to crawl posts with specific tags.

### Expected Outcome
- The main goal of this project is to understand web page interaction and automate actions like clicking and typing using Selenium.

## Implementation Notes
- The Instagram Automation Tool builds on Python knowledge gained from the Vehicle Management System and focuses on web automation using Selenium.

## How to Run
1. Clone this repository to your local machine.
2. Make sure you have Python and any required dependencies installed for each part.
3. Run the respective main script for the Instagram Automation Tool(instagram.py) or the Vehicle Management System(main.py), depending on your interest.
4. Follow the on-screen prompts to interact with the system.

Feel free to explore, test, and extend the functionalities of both parts of this project. Enjoy learning Python fundamentals, managing passengers in buses and cars, and automating Instagram interactions!



