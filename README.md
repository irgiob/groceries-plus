# Groceries+
Groceries+ is a desktop app built with python designed to keep track of your grocery list. 

I created it because I typically buy the same groceries week-to-week, and prefer to bring the exact amount of cash I require to buy everything so I'm not tempted to buy things I don't really need. 

I also created it to experiment with PyQt5 and the Qt Designer for GUI construction, as it seems to be more intuitive and easier to use compared to Tkinter. More updates to come.

<p align="center"><img src=images/app_gui.png alt="Application User Interfact" width=500></p>

### features
* Add & delete items from the grocery list
* Add info to each item such as description, quantity, and price
* Uses item info to create a shopping list with the exact budget required to buy everythibng
* Gives the option to exclude items from next shopping list
* automatically saves new items from shopping list & automatically opens up shopping list from when the app was last opened

### to-do list
* Allow input of expiration date or typical time a product lasts so the app can decide whether to add or exclude a product from the shopping list automatically
* Add web-scraping capabilities so the app can automatically find prices for certain items at supermarkets instead of having the user type the price manually
