## Calroie Tracker

This is my first project after University, mostly wanted to create an actually free Calorie tracker app to assist my journey in understanding how calorie tracking works, what actually matters and somewhat help me decide what I will eat. So far my experience with these apps has been mixed, it usually starts with them being free and working fantastically. Turns quickly into Paid Subscriptions and so on... It's not great. So this is sort of my contribution that I am working with. I found a website that has a database of Barcodes for most food items called "openfoodfacts". Let's see where it goes from here.

So current plan:
- Access your camera (computer or phone) to scan a barcode
- Talk to the "openfoodfacts" database for calorie information
- Add it to a summary
- Track your goals

Currently actually finished:
- Access to the Database
- Manual insertion of barcode numbers to get nutritional values

## NOTE!

This project has just been started, all the requirements and other information will come with time. 

## Simple username diary

Enter a username to create or reopen that diary in this browser. No password, email, database, or environment variables are needed. Food entries are saved in browser storage and include the product, barcode, package and serving information, and all nutrition values returned by `logic/nutrition.py`. Choose a date to view that day's entries and calorie total.

This is a lightweight local diary, not a secure online account: anyone using the same browser can open a username, and data does not sync to other browsers/devices. Clearing browser storage can remove the diary.
