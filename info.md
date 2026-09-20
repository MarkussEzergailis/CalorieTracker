19/09/2026
This is the first day of the project. Here's the discoveries about the project today. 
    - There is a good API that I can use " https://world.openfoodfacts.org/api/v2/product/{BARCODE} "
        Essentially, if i find a way that uses camera available on your phone/laptop to capture the barcode,
        It would accept it as input and return back all the product details, example is here: "https://world.openfoodfacts.org/api/v2/product/4000177026717 " -> This a barcode for a caprisun. 
    - So far the identified most useful information:
        Product Name, Brand, Service Size, Product quantitiy, Cateogry, Calories, Protein, Carbohydrates, Sugar, Fat, Saturated Fat, Fiber, Salt.

20/09/2026
    - Managed to get the proper prints working, now it does actually display all of the nutrition information outright in the print statements. So far this has been tested on only 2 products. Caprisun Jungle Safari("4000177026717") and Driend Mango Slices("7090046314103")
    - Soon need to start making a front end, the goal is to host it on varcel to have some sort of accessability from the mobile device, but the logic is not completed today...
    - Self note: Much like in university, I NEED to start making a plan before I actually start implomenting. Otherwise the scope creep will overtake this entire project.