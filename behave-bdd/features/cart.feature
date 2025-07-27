Feature: cart
    Scenario: Cart items are removed successfully
        Given User is on cart page with non empty items
        When User removes all items from cart
        Then Cart quantity should be empty

        
