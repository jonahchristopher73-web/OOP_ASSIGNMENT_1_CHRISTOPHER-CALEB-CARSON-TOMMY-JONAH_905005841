# Vaccination Tracker System

A simple Object-Oriented Programming project built in Python for tracking vaccinations while following Digital Public Goods (DPG) standards.

## Description

This program helps manage basic vaccination records using OOP concepts. It allows creating vaccine types, registering patients with only non-sensitive information (ID and age group), recording vaccines received, and viewing all records. The system is designed to be modular, privacy-respecting, and easy to understand.

Domain: Health (Vaccination Tracker)

## Features

- Create and manage Vaccine objects
- Create and manage Patient objects
- Store multiple patients using a dictionary
- Add vaccines to patients
- Display individual and all patient records
- Track total number of vaccines created

## OOP Concepts Used

- Classes and Objects
- Attributes and Methods
- Instance Methods
- Class Methods (`@classmethod`)
- Static Methods (`@staticmethod`)
- Object interaction (Patient objects receive Vaccine objects)
- Dictionary as the main data structure to store patients

## Digital Public Goods (DPG) Alignment

- **Open Source**: Full source code is publicly available on GitHub
- **Inclusive and Accessible**: Uses simple age groups instead of exact ages and avoids complex interfaces
- **Privacy-Respecting**: No real names, addresses, phone numbers, or sensitive medical history is stored. Only patient IDs and age groups are used
- **Modular and Reusable**: Code is divided into clear classes (Vaccine, Patient, VaccinationTracker) that can be extended or reused in other projects

## How to Run

1. Make sure you have Python 3 installed
2. Download or clone this repository
3. Open a terminal in the project folder
4. Run the command:

```bash
python vaccination_tracker.py
