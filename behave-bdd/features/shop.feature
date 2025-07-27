Feature: Shop
    Scenario: Add to cart from Shop page
        Given user is on product page
        When they click "Add to cart"
        Then item should appear in cart 